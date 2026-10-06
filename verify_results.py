"""Read-only verification of a completed run.py results directory."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def verify(folder):
    folder = Path(folder)
    cfg = json.loads((folder / 'config.json').read_text())
    hist = pd.read_csv(folder / 'history.csv')
    final = pd.read_csv(folder / 'final_results.csv')
    summary = pd.read_csv(folder / 'summary.csv')
    selected = json.loads((folder / 'selected_rates.json').read_text())
    keys = ['dataset', 'drop_rate', 'seed']
    expected_runs = len(cfg['datasets']) * len(cfg['rates']) * len(cfg['seeds'])
    assert len(hist) == expected_runs * cfg['epochs'], 'Missing/extra epoch rows'
    assert len(final) == expected_runs, 'Missing/extra final rows'
    assert not hist.duplicated(keys + ['epoch']).any(), 'Duplicate epoch rows'
    assert not final.duplicated(keys).any(), 'Duplicate final rows'
    metrics = ['train_error', 'val_error', 'test_error', 'gap_pp', 'seconds']
    assert np.isfinite(hist[metrics].to_numpy()).all(), 'Non-finite metrics'
    for metric in ['train_error', 'val_error', 'test_error']:
        assert hist[metric].between(0, 100).all(), 'Invalid error percentage'
    for metric in ['train_loss', 'val_loss', 'test_loss', 'online_loss']:
        assert np.isfinite(hist[metric]).all() and (hist[metric] >= 0).all()
    assert np.allclose(hist.gap_pp, hist.test_error - hist.train_error)
    assert np.allclose(final.test_accuracy, 100 - final.test_error)
    assert set(hist.dataset) == set(cfg['datasets'])
    for name in cfg['datasets']:
        split = np.load(folder / f'{name}_split.npz')
        train, val, test = split['train'], split['validation'], split['test']
        assert len(train) == cfg['train_size'] and len(val) == cfg['val_size']
        assert len(test) == cfg['test_size']
        assert len(np.intersect1d(train, val)) == 0, 'Train/validation overlap'
        for ids, limit in [(train, 60000), (val, 60000), (test, 10000)]:
            assert len(ids) == len(np.unique(ids))
            assert (ids >= 0).all() and (ids < limit).all()
        # Test indices address a separate official dataset, not the train array.
        assert np.array_equal(test, np.arange(cfg['test_size']))
        for seed in cfg['seeds']:
            for rate in cfg['rates']:
                rows = hist[(hist.dataset == name) & (hist.seed == seed)
                            & np.isclose(hist.drop_rate, rate)].sort_values('epoch')
                assert np.array_equal(rows.epoch, np.arange(1, cfg['epochs'] + 1))
                f = final[(final.dataset == name) & (final.seed == seed)
                          & np.isclose(final.drop_rate, rate)]
                assert len(f) == 1
                assert np.allclose(rows.iloc[-1][metrics].astype(float),
                                   f.iloc[0][metrics].astype(float))
                checkpoint = folder / f'{name}_d{rate:.1f}_s{seed}.pt'
                assert checkpoint.is_file() and checkpoint.stat().st_size > 0
        for suffix in ['overfitting', 'drop_rates', 'keep_probability', 'failure_cases']:
            path = folder / f'{name}_{suffix}.png'
            assert path.read_bytes()[:8] == b'\x89PNG\r\n\x1a\n', f'Invalid PNG: {path}'
        means = final[final.dataset == name].groupby('drop_rate').val_error.mean()
        expected_rate = min(means.index, key=lambda r: (means.loc[r], r))
        assert np.isclose(selected[name], expected_rate), 'Wrong validation selection'
    columns = ['train_error', 'val_error', 'test_error', 'gap_pp', 'test_accuracy', 'seconds']
    grouped = final.groupby(['dataset', 'drop_rate'])[columns]
    reference = pd.concat([grouped.mean().add_suffix('_mean'),
                           grouped.std(ddof=1).add_suffix('_sd')], axis=1).sort_index()
    actual = summary.set_index(['dataset', 'drop_rate']).sort_index()
    assert reference.index.equals(actual.index), 'Summary groups mismatch'
    assert np.allclose(reference.to_numpy(), actual[reference.columns].to_numpy(),
                       rtol=1e-8, atol=1e-8, equal_nan=True), 'Summary mismatch'
    print(f'PASS: {expected_runs} completed runs; {len(hist)} epoch rows; splits, metrics, '
          'checkpoints, PNG signatures and validation selection consistent.')
    print('This validates file consistency, not exact paper replication or hosted Colab execution.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder')
    verify(parser.parse_args().folder)
