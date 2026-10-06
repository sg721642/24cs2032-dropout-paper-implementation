import json
from pathlib import Path


def markdown(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': text.splitlines(True)}


def code(text):
    return {'cell_type': 'code', 'execution_count': None, 'metadata': {},
            'outputs': [], 'source': text.splitlines(True)}


source = Path('run.py').read_text()
cells = [
    markdown('# Dropout implementation — 24CS2032\n'
             'Paper: Srivastava et al., JMLR 2014.\n'
             'Reduced-scale fixed-width MLP experiment. No results are pre-filled.\n'
             'Run cells in order. The code is embedded; no GitHub clone is required.\n'
             'The final run uses a fixed protocol; test curves are descriptive, not tuning signals.'),
    code('%pip install torch torchvision numpy pandas matplotlib\n'),
    code('from pathlib import Path\nPath("run.py").write_text(' + repr(source) + ')\n'),
    code('import subprocess, sys\n'
         'subprocess.run([sys.executable, "run.py", "--self-test", "--device", "cpu"], check=True)\n'),
    markdown('## Experiment\nCPU is sufficient. The default cell runs the full MNIST rate sweep. '
             'Use a separate output folder if you change the configuration. '
             'Add fashion to DATASETS if you also want the second suggested dataset.'),
    code('DATASETS = ["mnist"]\n'
         'OUT = "results_mnist_colab"\n'
         'DEVICE = "cpu"\n'
         'command = [sys.executable, "run.py", "--datasets", *DATASETS, "--device", DEVICE,\n'
         '           "--epochs", "20", "--seeds", "42", "43", "44", "--out", OUT]\n'
         'subprocess.run(command, check=True)\n'),
    code('import pandas as pd\nfrom IPython.display import display, Image, Markdown\n'
         'display(pd.read_csv(Path(OUT) / "summary.csv"))\n'
         'display(Markdown((Path(OUT) / "RESULTS.md").read_text()))\n'
         'for name in DATASETS:\n'
         '    for suffix in ["overfitting", "drop_rates", "keep_probability", "failure_cases"]:\n'
         '        display(Image(filename=str(Path(OUT) / f"{name}_{suffix}.png")))\n'),
    markdown('## My observations\nReplace this paragraph after running: validation-selected rate; '
             'baseline and selected test error; change in percentage points; seed variation; '
             'whether dropout helped; two failure cases. '
             'Compare the reduced-scale rate plot with Figure 9(a), not as an exact numerical replication.'),
    code('import shutil\narchive = shutil.make_archive(OUT, "zip", OUT)\n'
         'try:\n    from google.colab import files\n    files.download(archive)\n'
         'except ImportError:\n    print("Saved:", archive)\n'),
    markdown('## References\n'
             '- https://jmlr.org/papers/v15/srivastava14a.html\n'
             '- https://www.cs.toronto.edu/~nitish/dropout/\n'
             '- https://github.com/nitishsrivastava/deepnet (consulted for historical context; not a dependency)\n'
             '- https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html\n'
             '- https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html\n'
             'Record assistance and reused resources according to course policy.'),
]
nb = {'cells': cells, 'metadata': {'kernelspec': {'display_name': 'Python 3',
      'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}},
      'nbformat': 4, 'nbformat_minor': 5}
for i, cell in enumerate(cells):
    cell['id'] = f'cell-{i:02d}'
Path('24CS2032_Dropout.ipynb').write_text(json.dumps(nb, indent=2))
print('Created 24CS2032_Dropout.ipynb')
