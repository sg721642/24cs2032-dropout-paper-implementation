# Manual Dropout Implementation — 24CS2032

A from-scratch PyTorch implementation of inverted dropout evaluated on feedforward neural networks. This project conducts a controlled drop-rate ablation across eight uniform rates ($d \in [0.0, 0.7]$) over three random seeds on MNIST, with an extension to Fashion-MNIST under the same experimental protocol. The study serves as an educational, reduced-scale investigation inspired by Figure 9(a) of Srivastava et al. (2014).

## Method

During training, activations are randomly dropped and scaled according to inverted dropout:
- Drop probability: $d \in [0, 1)$
- Keep probability: $q = 1 - d$
- Training pass: $\tilde{x} = \frac{x \odot m}{q}$, where $m \sim \text{Bernoulli}(q)$
- Evaluation pass: $\tilde{x} = x$ (identity)

Because $\mathbb{E}[\tilde{x}] = x$, no test-time weight scaling is required. Built-in PyTorch dropout primitives (`torch.nn.Dropout` or `F.dropout`) are not used anywhere in the model.

## Experiment

- **Dataset:** MNIST
- **Extension:** Fashion-MNIST (same experimental protocol)
- **Architecture:** 784–256–256–256–10 MLP with ReLU activations (335,114 parameters)
- **Drop Rates:** 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 (applied to hidden layers only)
- **Seeds:** 42, 43, 44 (identical initial weights across rates for each seed)
- **Epochs:** 20 fixed epochs
- **Optimizer:** Adam ($\text{lr} = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\text{weight decay} = 0$)
- **Data Splits:** 10,000 train / 5,000 validation / 10,000 test (split seed 2026)
- **Backend:** CPU (Apple Silicon native)

## Results

Final results at epoch 20 averaged across seeds 42, 43, 44 (mean $\pm$ sample standard deviation, $ddof = 1$):

| Dataset | Baseline ($d=0.0$) | Selected $d^*$ | Selected Test Error |
| :--- | :---: | :---: | :---: |
| MNIST | $4.320 \pm 0.295\%$ | 0.4 | $3.843 \pm 0.282\%$ |
| Fashion-MNIST | $14.663 \pm 0.175\%$ | 0.2 | $14.347 \pm 0.253\%$ |

Dropout rate was selected using mean validation error only.

High dropout rates degraded performance under the fixed training budget ($d=0.7$ reached $5.110\%$ error on MNIST and $17.453\%$ on Fashion-MNIST).

### Google Colab Portability Note

The reproduction notebook was independently executed on Google Colab CPU. A complete separate 24-run MNIST sweep was finished using the same `run.py` (verified via SHA256) and identical saved split indices. Under the Colab cloud environment, mean validation error selected $d=0.3$, whereas the official Apple Silicon Mac CPU experiment selected $d=0.4$. Official reported project results remain the local Mac CPU experiments; exact cross-platform numerical equivalence is not claimed.

## Run

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Run manual dropout correctness self-test:
```bash
python run.py --self-test --device cpu
```

Execute MNIST experiment sweep:
```bash
python run.py --datasets mnist --device cpu --out results_mnist
```

Execute Fashion-MNIST extension sweep:
```bash
python run.py --datasets fashion --device cpu --out results_fashion
```

Generate self-contained Jupyter notebook:
```bash
python make_notebook.py
```

Run saved-model inference demo:
```bash
python presentation/demo.py
```
> **Note:** `presentation/demo.py` expects the locally generated checkpoint `results_mnist/mnist_d0.4_s42.pt` and a local MNIST dataset cache. The checkpoint file is intentionally not committed to the clean Git repository or submission archive.

## Files

- `run.py`: Core CLI script containing `ManualDropout`, MLP architecture, training loops, evaluation metrics, and plotting routines.
- `make_notebook.py`: Script generating the standalone notebook `24CS2032_Dropout.ipynb`.
- `24CS2032_Dropout.ipynb`: Self-contained reproduction notebook embedding `run.py`.
- `verify_results.py`: Verification utility auditing output CSV files and recomputing summary statistics.
- `requirements.txt`: Minimal runtime dependencies.
- `environment-lock.txt`: Exact pinned local environment package versions.
- `results_mnist/`: Recorded metrics, summaries, configuration, and ablation plots for MNIST.
- `results_fashion/`: Recorded metrics, summaries, configuration, and ablation plots for Fashion-MNIST.
- `report/`: IEEE two-column report source (`main.tex`, `references.bib`, figures) and compiled PDF (`24CS2032_Dropout_Report.pdf`).
- `presentation/`: Presentation deck (`24CS2032_Dropout_Presentation.pptx`), saved-model inference demo (`demo.py`), and sample predictions (`demo_predictions.png`).

## References

1. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). *"Dropout: A Simple Way to Prevent Neural Networks from Overfitting."* Journal of Machine Learning Research, 15(56), 1929–1958.
2. LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). *"Gradient-based learning applied to document recognition."* Proceedings of the IEEE, 86(11), 2278–2324.
3. Xiao, H., Rasul, K., & Vollgraf, R. (2017). *"Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms."* arXiv preprint arXiv:1708.07747.
4. Srivastava, N., et al. (2014). *Deepnet: Implementation of Deep Learning Models in Python and C++ / CUDA.* GitHub repository: https://github.com/nitishsrivastava/deepnet (consulted for historical context on the original dropout implementation; no code was copied).

