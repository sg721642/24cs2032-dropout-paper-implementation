import argparse
import gzip
import hashlib
import json
import math
import platform
import random
import shutil
import time
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets
from torchvision.datasets.utils import check_integrity
import torchvision


class ManualDropout(nn.Module):
    def __init__(self, drop_rate=0.5, inverted=True):
        super().__init__()
        if not 0 <= drop_rate < 1:
            raise ValueError('drop_rate must be in [0, 1).')
        self.drop_rate = float(drop_rate)
        self.inverted = inverted

    def forward(self, x):
        keep = 1.0 - self.drop_rate
        if not self.training:
            return x if self.inverted else x * keep
        if self.drop_rate == 0:
            return x
        mask = (torch.rand_like(x) < keep).to(x.dtype)
        return x * mask / keep if self.inverted else x * mask


class MLP(nn.Module):
    def __init__(self, drop_rate, width=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, width), nn.ReLU(), ManualDropout(drop_rate),
            nn.Linear(width, width), nn.ReLU(), ManualDropout(drop_rate),
            nn.Linear(width, width), nn.ReLU(), ManualDropout(drop_rate),
            nn.Linear(width, 10),
        )

    def forward(self, x):
        return self.net(x)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True


def choose_device(name):
    if name == 'auto':
        name = ('cuda' if torch.cuda.is_available() else
                'mps' if torch.backends.mps.is_available() else 'cpu')
    if name == 'mps' and not torch.backends.mps.is_available():
        raise RuntimeError('MPS unavailable; rerun with --device cpu.')
    if name == 'cuda' and not torch.cuda.is_available():
        raise RuntimeError('CUDA unavailable; use --device cpu or auto.')
    return torch.device(name)


def self_test(device):
    set_seed(123)
    x = torch.ones(200000, device=device, requires_grad=True)
    layer = ManualDropout(0.3).to(device)
    layer.train()
    y = layer(x)
    assert y.shape == x.shape and y.dtype == x.dtype and y.device == x.device
    assert abs((y == 0).float().mean().item() - 0.3) < 0.01
    assert abs(y.mean().item() - 1.0) < 0.02
    assert torch.allclose(y[y != 0], torch.full_like(y[y != 0], 1 / 0.7))
    y.sum().backward()
    assert torch.allclose(x.grad, y.detach())
    assert not torch.equal(y.detach(), layer(x).detach())
    layer.eval()
    assert torch.equal(layer(x), x)
    assert torch.equal(layer(x), layer(x))
    assert torch.equal(ManualDropout(0).to(device)(x), x)
    classic = ManualDropout(0.3, inverted=False).to(device)
    classic.eval()
    assert torch.allclose(classic(x), x * 0.7)
    classic.train()
    assert abs(classic(x).mean().item() - 0.7) < 0.02
    for bad in [-0.1, 1.0, 1.2]:
        try:
            ManualDropout(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid rate accepted')
    model = MLP(0.5).to(device).eval()
    with torch.no_grad():
        assert model(torch.zeros(2, 1, 28, 28, device=device)).shape == (2, 10)
    print('PASS: mask, scaling, gradient, fresh masks, eval, p=0, bounds, MLP shape')


def load_data(name, train_n, val_n, test_n, split_seed, out):
    cls = datasets.MNIST if name == 'mnist' else datasets.FashionMNIST
    def get_dataset(training):
        try:
            return cls('data', train=training, download=True)
        except (ValueError, RuntimeError, OSError, EOFError):
            # Repair an interrupted empty extraction only from checksum-valid data.
            raw = Path('data') / cls.__name__ / 'raw'
            repaired = False
            for filename, md5 in cls.resources:
                archive = raw / filename
                target = archive.with_suffix('')
                if (not target.exists() or target.stat().st_size == 0) and check_integrity(str(archive), md5):
                    temporary = target.with_suffix('.repair')
                    with gzip.open(archive, 'rb') as src, temporary.open('wb') as dst:
                        shutil.copyfileobj(src, dst)
                    temporary.replace(target)
                    repaired = True
            if not repaired:
                raise
            return cls('data', train=training, download=False)
    original_train = get_dataset(True)
    original_test = get_dataset(False)
    if train_n + val_n > len(original_train) or test_n > len(original_test):
        raise ValueError('Requested split exceeds dataset size.')
    gen = torch.Generator().manual_seed(split_seed)
    order = torch.randperm(len(original_train), generator=gen)
    # Validation and training are disjoint; official test is never used for fitting.
    val_ids = order[:val_n]
    train_ids = order[val_n:val_n + train_n]
    test_ids = torch.arange(test_n)
    np.savez(out / f'{name}_split.npz', train=train_ids.numpy(),
             validation=val_ids.numpy(), test=test_ids.numpy())

    def convert(ds, ids):
        x = ds.data[ids].unsqueeze(1).float().div(255.0)
        y = ds.targets[ids].long()
        return TensorDataset(x, y)

    sets = (convert(original_train, train_ids), convert(original_train, val_ids),
            convert(original_test, test_ids))
    counts = {label: torch.bincount(ds.tensors[1], minlength=10).tolist()
              for label, ds in zip(['train', 'validation', 'test'], sets)}
    (out / f'{name}_class_counts.json').write_text(json.dumps(counts, indent=2))
    return sets, original_test.classes


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    loss_sum, correct, count = 0.0, 0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        logits = model(x)
        loss_sum += nn.functional.cross_entropy(logits, y, reduction='sum').item()
        correct += (logits.argmax(1) == y).sum().item()
        count += y.numel()
    return loss_sum / count, 100.0 * (1 - correct / count)


def train_one(name, rate, seed, sets, args, device, out):
    tag = f'{name}_d{rate:.1f}_s{seed}'
    checkpoint = out / f'{tag}.pt'
    history_path = out / f'{tag}.csv'
    if checkpoint.exists() and history_path.exists():
        old = pd.read_csv(history_path)
        if len(old) == args.epochs and int(old.iloc[-1]['epoch']) == args.epochs:
            print('Already complete:', tag)
            return old
    set_seed(seed)
    model = MLP(rate, args.width).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=0)
    # Dedicated generator makes shuffle order identical across drop rates per seed.
    shuffle_gen = torch.Generator().manual_seed(seed + 10000)
    train_loader = DataLoader(sets[0], batch_size=args.batch_size, shuffle=True,
                              generator=shuffle_gen, num_workers=0)
    eval_loaders = [DataLoader(ds, batch_size=512, shuffle=False, num_workers=0)
                    for ds in sets]
    rows = []
    start = time.perf_counter()
    for epoch in range(1, args.epochs + 1):
        model.train()
        online_loss, seen = 0.0, 0
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad(set_to_none=True)
            loss = nn.functional.cross_entropy(model(x), y)
            if not torch.isfinite(loss):
                raise RuntimeError('Non-finite loss. Stop and inspect configuration.')
            loss.backward()
            optimizer.step()
            online_loss += loss.item() * y.numel()
            seen += y.numel()
        row = dict(dataset=name, drop_rate=rate, seed=seed, epoch=epoch,
                   updates=epoch * math.ceil(len(sets[0]) / args.batch_size),
                   online_loss=online_loss / seen)
        for label, loader in zip(['train', 'val', 'test'], eval_loaders):
            row[f'{label}_loss'], row[f'{label}_error'] = evaluate(model, loader, device)
        row['gap_pp'] = row['test_error'] - row['train_error']
        row['seconds'] = time.perf_counter() - start
        rows.append(row)
        pd.DataFrame(rows).to_csv(history_path, index=False)
        print(f"{tag} {epoch:02d}/{args.epochs} "
              f"train={row['train_error']:.2f}% val={row['val_error']:.2f}% "
              f"test={row['test_error']:.2f}% elapsed={row['seconds']:.0f}s", flush=True)
    torch.save({k: v.detach().cpu() for k, v in model.state_dict().items()}, checkpoint)
    return pd.DataFrame(rows)


@torch.no_grad()
def failure_plot(model, ds, class_names, device, path):
    loader = DataLoader(ds, batch_size=512, shuffle=False)
    mistakes = []
    model.eval()
    for x, y in loader:
        probs = model(x.to(device)).softmax(1).cpu()
        preds = probs.argmax(1)
        for i in (preds != y).nonzero(as_tuple=True)[0].tolist():
            mistakes.append((x[i, 0], int(y[i]), int(preds[i]), float(probs[i, preds[i]])))
            if len(mistakes) == 12:
                break
        if len(mistakes) == 12:
            break
    fig, axes = plt.subplots(3, 4, figsize=(12, 8))
    for ax in axes.flat:
        ax.axis('off')
    for ax, (x, truth, pred, confidence) in zip(axes.flat, mistakes):
        ax.imshow(x, cmap='gray')
        ax.set_title(f'True: {class_names[truth]}\nPred: {class_names[pred]} ({confidence:.2f})', fontsize=8)
    fig.suptitle('First misclassified official-test images; not cherry-picked')
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def summarize(hist, args, out):
    hist.to_csv(out / 'history.csv', index=False)
    final = hist[hist.epoch == args.epochs].copy()
    final['test_accuracy'] = 100 - final.test_error
    final.to_csv(out / 'final_results.csv', index=False)
    cols = ['train_error', 'val_error', 'test_error', 'gap_pp', 'test_accuracy', 'seconds']
    grouped = final.groupby(['dataset', 'drop_rate'])[cols]
    avg = grouped.mean().add_suffix('_mean')
    sd = grouped.std(ddof=1).add_suffix('_sd')
    summary = pd.concat([avg, sd], axis=1).reset_index()
    summary.to_csv(out / 'summary.csv', index=False)
    chosen = {}
    lines = ['# Actual measured results', '',
             'Final fixed epoch; rates selected using mean validation error only.',
             'SD is sample standard deviation across seeds; one seed has no SD.', '',
             '| Dataset | Drop rate | Train error % | Val error % | Test error % | Test SD | Gap pp |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for r in summary.itertuples():
        sd_text = f'{r.test_error_sd:.3f}' if pd.notna(r.test_error_sd) else 'N/A'
        lines.append(f'| {r.dataset} | {r.drop_rate:.1f} | {r.train_error_mean:.3f} | '
                     f'{r.val_error_mean:.3f} | {r.test_error_mean:.3f} | {sd_text} | {r.gap_pp_mean:.3f} |')
    for name in args.datasets:
        sub = summary[summary.dataset == name].sort_values('drop_rate')
        best = sub.sort_values(['val_error_mean', 'drop_rate']).iloc[0]
        chosen[name] = float(best.drop_rate)
        lines += ['', f'{name}: validation-selected drop rate = {best.drop_rate:.1f}.']
        if 0.0 in sub.drop_rate.values:
            baseline = sub[sub.drop_rate == 0].iloc[0]
            delta = baseline.test_error_mean - best.test_error_mean
            lines.append(f'Test-error change vs no dropout = {delta:.3f} percentage points '
                         '(positive means lower error with the selected model).')
        curves = hist[hist.dataset == name]
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        reference_rate = 0.5 if 0.5 in sub.drop_rate.values else chosen[name]
        for rate in sorted(set([0.0, reference_rate])):
            d = curves[np.isclose(curves.drop_rate, rate)]
            if d.empty:
                continue
            mean = d.groupby('epoch').mean(numeric_only=True)
            axes[0].plot(mean.index, mean.train_error, '--', label=f'd={rate:g} train (eval)')
            axes[0].plot(mean.index, mean.test_error, label=f'd={rate:g} test')
            axes[1].plot(mean.index, mean.val_loss, label=f'd={rate:g} validation')
        axes[0].set_ylabel('Classification error (%)')
        axes[1].set_ylabel('Cross-entropy loss')
        for ax in axes:
            ax.set_xlabel('Epoch'); ax.legend(); ax.grid(alpha=0.25)
        fig.suptitle(f'{name}: reduced-scale overfitting comparison (means across seeds)')
        fig.tight_layout(); fig.savefig(out / f'{name}_overfitting.png', dpi=200); plt.close(fig)
        for keep_axis in [False, True]:
            plot_data = sub.copy()
            plot_data['x'] = 1 - plot_data.drop_rate if keep_axis else plot_data.drop_rate
            plot_data = plot_data.sort_values('x')
            fig, ax = plt.subplots(figsize=(7, 4))
            for metric, label in [('train_error', 'Train (eval mode)'), ('test_error', 'Test')]:
                errors = plot_data[f'{metric}_sd']
                ax.errorbar(plot_data.x, plot_data[f'{metric}_mean'],
                            yerr=None if errors.isna().all() else errors.fillna(0),
                            marker='o', capsize=3, label=label)
            ax.set_xlabel('Keep probability q = 1 - d' if keep_axis else 'Drop probability d')
            ax.set_ylabel('Classification error (%)')
            ax.set_title(f'{name}: fixed-width dropout ablation')
            ax.legend(); ax.grid(alpha=0.25); fig.tight_layout()
            suffix = 'keep_probability' if keep_axis else 'drop_rates'
            fig.savefig(out / f'{name}_{suffix}.png', dpi=200); plt.close(fig)
    (out / 'RESULTS.md').write_text('\n'.join(lines) + '\n')
    (out / 'selected_rates.json').write_text(json.dumps(chosen, indent=2))
    print('\n'.join(lines))
    return chosen


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--datasets', nargs='+', choices=['mnist', 'fashion'], default=['mnist'])
    p.add_argument('--rates', nargs='+', type=float, default=[i / 10 for i in range(8)])
    p.add_argument('--seeds', nargs='+', type=int, default=[42, 43, 44])
    p.add_argument('--epochs', type=int, default=20)
    p.add_argument('--train-size', type=int, default=10000)
    p.add_argument('--val-size', type=int, default=5000)
    p.add_argument('--test-size', type=int, default=10000)
    p.add_argument('--split-seed', type=int, default=2026)
    p.add_argument('--width', type=int, default=256)
    p.add_argument('--batch-size', type=int, default=128)
    p.add_argument('--lr', type=float, default=0.001)
    p.add_argument('--threads', type=int, default=4)
    p.add_argument('--device', choices=['auto', 'cpu', 'mps', 'cuda'], default='cpu')
    p.add_argument('--out', default='results_mnist')
    p.add_argument('--self-test', action='store_true')
    args = p.parse_args()
    if any(v <= 0 for v in [args.epochs, args.train_size, args.val_size, args.test_size,
                            args.width, args.batch_size, args.threads, args.lr]):
        p.error('Sizes, epochs, threads and learning rate must be positive.')
    if any(not 0 <= r <= 0.7 or abs(r * 10 - round(r * 10)) > 1e-6 for r in args.rates):
        p.error('Use rates 0.0, 0.1, ..., 0.7.')
    if len(set(args.seeds)) != len(args.seeds) or len(set(args.rates)) != len(args.rates):
        p.error('No duplicate seeds or rates.')
    torch.set_num_threads(args.threads)
    device = choose_device(args.device)
    print('Device:', device, '| torch:', torch.__version__)
    self_test(device)
    if args.self_test:
        return
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    config = vars(args).copy()
    config.update(device_used=str(device), python=platform.python_version(),
                  torch=str(torch.__version__), torchvision=str(torchvision.__version__),
                  platform=platform.platform(), numpy=np.__version__, pandas=pd.__version__,
                  matplotlib=matplotlib.__version__,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    config_path = out / 'config.json'
    if config_path.exists() and json.loads(config_path.read_text()) != config:
        raise RuntimeError('Existing output has a different config/code/environment. Use a NEW --out folder.')
    config_path.write_text(json.dumps(config, indent=2))
    print('Parameters:', sum(v.numel() for v in MLP(0, args.width).parameters()))
    histories, loaded = [], {}
    for name in args.datasets:
        sets, classes = load_data(name, args.train_size, args.val_size, args.test_size,
                                  args.split_seed, out)
        loaded[name] = (sets, classes)
        for seed in args.seeds:
            for rate in args.rates:
                histories.append(train_one(name, rate, seed, sets, args, device, out))
    selected = summarize(pd.concat(histories, ignore_index=True), args, out)
    for name, rate in selected.items():
        seed = args.seeds[0]
        model = MLP(rate, args.width).to(device)
        model.load_state_dict(torch.load(out / f'{name}_d{rate:.1f}_s{seed}.pt',
                                         map_location=device, weights_only=True))
        sets, classes = loaded[name]
        failure_plot(model, sets[2], classes, device, out / f'{name}_failure_cases.png')
    print('Finished. Results saved in', out.resolve())


if __name__ == '__main__':
    main()
