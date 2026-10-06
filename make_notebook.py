import json
from pathlib import Path


def markdown(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': text.splitlines(True)}


def code(text):
    return {'cell_type': 'code', 'execution_count': None, 'metadata': {},
            'outputs': [], 'source': text.splitlines(True)}


source = Path('run.py').read_text()
cells = [
    markdown(
        '# Dropout implementation — 24CS2032\n\n'
        '**Paper:** Srivastava, Nitish, et al. "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." '
        '*Journal of Machine Learning Research* 15.56 (2014): 1929-1958.\n\n'
        '**Context & Scope:** This notebook implements an educational, reduced-scale reproduction '
        'of the fixed-width dropout ablation inspired by Figure 9(a) of the original paper. '
        'Architecture: `784 → 256 → 256 → 256 → 10` MLP with ReLU activations, Adam optimizer (`lr=0.001`), '
        '10,000 training examples, 5,000 validation examples, and 20 fixed epochs.\n\n'
        '**Dropout Formulation:** Custom inverted `ManualDropout` after hidden ReLUs only:\n'
        '- Drop probability: $d \\in [0, 1)$\n'
        '- Retention / keep probability: $q = 1 - d$\n'
        '- Training mode: $y = x \\odot \\text{mask} / q$\n'
        '- Evaluation mode: $y = x$\n'
        '- Model contains NO built-in PyTorch dropout (`nn.Dropout` / `F.dropout`).\n\n'
        '**Protocol & Model Selection Policy:**\n'
        '- Model selection is strictly governed by lowest mean validation error across seeds at fixed epoch 20 (ties broken by lower $d$).\n'
        '- Official test set (10,000 examples) is evaluated strictly for descriptive comparison; test curves are NEVER used as tuning signals.\n'
        '- Self-contained notebook embedding the complete project `run.py`; no GitHub clone is required.\n'
        '- No results are pre-filled as fake execution output; run cells sequentially.'
    ),
    code('%pip install torch torchvision numpy pandas matplotlib\n'),
    code(
        'from pathlib import Path\n'
        '# Write exact project run.py locally\n'
        'Path("run.py").write_text(' + repr(source) + ')\n'
    ),
    code(
        'import subprocess, sys\n'
        '# Run ManualDropout mathematical self-test on CPU\n'
        'subprocess.run([sys.executable, "run.py", "--self-test", "--device", "cpu"], check=True)\n'
    ),
    markdown(
        '## Main experiment — MNIST (Default Reproduction)\n\n'
        'Executes the full 20-epoch × 8-rate × 3-seed sweep on real MNIST on CPU.\n'
        '- Rates: `0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7`\n'
        '- Seeds: `42, 43, 44`\n'
        '- Epochs: `20`\n'
        '- Output directory: `results_mnist_colab`'
    ),
    code(
        'import subprocess, sys\n'
        'from pathlib import Path\n\n'
        'DATASETS = ["mnist"]\n'
        'OUT = "results_mnist_colab"\n'
        'DEVICE = "cpu"\n'
        'command = [\n'
        '    sys.executable, "run.py",\n'
        '    "--datasets", *DATASETS,\n'
        '    "--device", DEVICE,\n'
        '    "--epochs", "20",\n'
        '    "--seeds", "42", "43", "44",\n'
        '    "--out", OUT\n'
        ']\n'
        'subprocess.run(command, check=True)\n'
    ),
    code(
        'import pandas as pd\n'
        'from pathlib import Path\n'
        'from IPython.display import display, Image, Markdown\n\n'
        'out_path = Path(OUT)\n'
        'if (out_path / "summary.csv").exists():\n'
        '    display(Markdown("### MNIST Summary Table"))\n'
        '    display(pd.read_csv(out_path / "summary.csv"))\n'
        '    display(Markdown((out_path / "RESULTS.md").read_text()))\n'
        '    for suffix in ["overfitting", "drop_rates", "keep_probability", "failure_cases"]:\n'
        '        img_p = out_path / f"mnist_{suffix}.png"\n'
        '        if img_p.exists():\n'
        '            display(Image(filename=str(img_p)))\n'
    ),
    code(
        'import shutil\n'
        'from pathlib import Path\n'
        'if Path(OUT).exists():\n'
        '    archive = shutil.make_archive(OUT, "zip", OUT)\n'
        '    try:\n'
        '        from google.colab import files\n'
        '        files.download(archive)\n'
        '    except ImportError:\n'
        '        print("Saved local archive:", archive)\n'
    ),
    markdown(
        '## Optional extension — Fashion-MNIST\n\n'
        'Executes the identical frozen protocol (`dropout-24cs2032-v1`) on Fashion-MNIST as an extension benchmark.\n'
        'To execute, uncomment the `subprocess.run(...)` call in the cell below.'
    ),
    code(
        'import subprocess, sys\n'
        'from pathlib import Path\n\n'
        'DATASETS_FASHION = ["fashion"]\n'
        'OUT_FASHION = "results_fashion_colab"\n'
        'command_fashion = [\n'
        '    sys.executable, "run.py",\n'
        '    "--datasets", *DATASETS_FASHION,\n'
        '    "--device", DEVICE,\n'
        '    "--epochs", "20",\n'
        '    "--seeds", "42", "43", "44",\n'
        '    "--out", OUT_FASHION\n'
        ']\n'
        '# Uncomment to execute Fashion-MNIST extension sweep:\n'
        '# subprocess.run(command_fashion, check=True)\n'
    ),
    markdown(
        '## Verified local reference results\n\n'
        '*Note: The values below are documented reference results obtained from the verified final Mac CPU experiments '
        '(`protocol: dropout-24cs2032-v1`). They are provided as reference text for comparison and are NOT fabricated cell execution outputs.*\n\n'
        'Model selection used mean validation error only across seeds at fixed epoch 20. Test error was not used to choose the dropout rate.\n\n'
        '### MNIST (Main Reproduction)\n'
        '- **No-dropout baseline ($d=0.0$):** Test error $4.320 \\pm 0.295\\%$, Gap $4.117$ pp\n'
        '- **Validation-selected rate ($d=0.4$):** Validation error $3.747 \\pm 0.130\\%$\n'
        '- **Selected model test error:** $3.843 \\pm 0.282\\%$ (Test accuracy $96.157\\%$)\n'
        '- **Selected model generalization gap:** $3.520 \\pm 0.295$ pp\n'
        '- **Test-error change vs baseline:** $+0.477$ percentage points lower test error ($11.03\\%$ relative error reduction)\n'
        '- **Paper reference rate ($d=0.5$):** Test error $3.883 \\pm 0.087\\%$\n'
        '- **Descriptive test-error-best rate:** $d=0.3$ ($3.820 \\pm 0.118\\%$; not used for selection)\n'
        '- **Negative finding:** High dropout rates noticeably degraded performance ($d=0.6$: $4.380\\%$, $d=0.7$: $5.110\\%$ vs $4.320\\%$ baseline).\n\n'
        '### Fashion-MNIST (Extension Benchmark)\n'
        '- **No-dropout baseline ($d=0.0$):** Test error $14.663 \\pm 0.175\\%$, Gap $7.533$ pp\n'
        '- **Validation-selected rate ($d=0.2$):** Validation error $13.087 \\pm 0.408\\%$\n'
        '- **Selected model test error:** $14.347 \\pm 0.253\\%$ (Test accuracy $85.653\\%$)\n'
        '- **Selected model generalization gap:** $5.763 \\pm 0.165$ pp\n'
        '- **Test-error change vs baseline:** $+0.317$ percentage points lower test error ($2.16\\%$ relative error reduction)\n'
        '- **Paper reference rate ($d=0.5$):** Test error $15.133 \\pm 0.325\\%$ ($0.470$ pp *worse* than baseline)\n'
        '- **Descriptive test-error-best rate:** $d=0.1$ ($14.220 \\pm 0.105\\%$; not used for selection)\n'
        '- **Negative finding:** Reference $d=0.5$ underperformed no-dropout baseline; severe degradation occurred at higher rates ($d=0.7$: $17.453\\%$).\n\n'
        '### Comparison with Figure 9(a) of Srivastava et al. (2014)\n'
        'Plotting test error against keep probability $q = 1 - d$ reproduces the qualitative U-shaped curve observed in Figure 9(a): '
        'performance improves with moderate retention rates and deteriorates as $q$ falls below $0.5$ (high drop rates).'
    ),
    markdown(
        '## References & Assistance\n\n'
        '1. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). '
        '"Dropout: A Simple Way to Prevent Neural Networks from Overfitting." *Journal of Machine Learning Research*, 15(56), 1929-1958. '
        'https://jmlr.org/papers/v15/srivastava14a.html\n'
        '2. Author dropout project page: https://www.cs.toronto.edu/~nitish/dropout/\n'
        '3. Historical Deepnet repository (consulted for historical context; not a dependency): https://github.com/nitishsrivastava/deepnet\n'
        '4. PyTorch Dropout reference (scaling formula comparison only): https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html\n'
        '5. Torchvision MNIST/FashionMNIST documentation: https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html\n\n'
        '**Assistance and Provenance Statement:**\n'
        'ChatGPT and Antigravity were used for implementation guidance, code review, local execution automation, verification, and documentation support. '
        'All reported experiment results come from the recorded real-data runs in this repository; no synthetic result data were used. '
        'External assistance is disclosed according to the course policy.'
    ),
]
nb = {
    'cells': cells,
    'metadata': {
        'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
        'language_info': {'name': 'python'}
    },
    'nbformat': 4,
    'nbformat_minor': 5
}
for i, cell in enumerate(cells):
    cell['id'] = f'cell-{i:02d}'
Path('24CS2032_Dropout.ipynb').write_text(json.dumps(nb, indent=2))
print('Created 24CS2032_Dropout.ipynb')
