# Dropout implementation — 24CS2032

## Goal
Implement Bernoulli dropout manually inside a multilayer perceptron (MLP) and perform a controlled fixed-rate ablation across dropout probabilities $d \in [0.0, 0.7]$. This project is an educational, reduced-scale reproduction inspired by Figure 9(a) of the seminal dropout paper.

## Assignment
- **Paper:** Srivastava, Nitish, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. *"Dropout: A Simple Way to Prevent Neural Networks from Overfitting."* Journal of Machine Learning Research 15.56 (2014): 1929-1958.
- **Main comparison:** Impact of dropout rate $d$ on training error, test error, and generalization gap in a feedforward network.
- **Scope:** Educational reduced-scale reproduction using a 784–256–256–256–10 architecture on 10,000 training examples for 20 epochs.

## Manual Dropout
This implementation uses a custom inverted `ManualDropout` layer applied strictly after hidden ReLU activations:
- **Drop probability:** $d \in [0, 1)$
- **Retention probability:** $q = 1 - d$
- **Training pass:**
  $$y = \frac{x \odot m}{q}, \quad m \sim \text{Bernoulli}(q)$$
- **Evaluation pass:**
  $$y = x$$

No built-in PyTorch dropout (`nn.Dropout`, `F.dropout`, or `functional.dropout`) is used anywhere in the model. Model parameter count with width 256 is exactly **335,114**.

## Setup

Create an isolated virtual environment and install portable dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

*Note: All code runs entirely on CPU (or Apple Silicon). No CUDA or GPU drivers are required.*

## Reproduce

1. **Run correctness self-test:**
   ```bash
   python run.py --self-test --device cpu
   ```
2. **Execute final MNIST sweep (Main Reproduction):**
   ```bash
   python run.py --datasets mnist --device cpu --out results_mnist
   ```
3. **Execute final Fashion-MNIST sweep (Extension):**
   ```bash
   python run.py --datasets fashion --device cpu --out results_fashion
   ```
4. **Generate self-contained notebook:**
   ```bash
   python make_notebook.py
   ```

*Compute choice:* CPU was benchmarked at 0.785 seconds per 2-epoch run versus 4.398 seconds on MPS (>5.5x faster on CPU due to small tensor dimensions and zero GPU kernel launch overhead). CPU is the locked, deterministic backend.

## Frozen Experiment
- **Protocol ID:** `dropout-24cs2032-v1`
- **Data split:** 10,000 train / 5,000 validation / 10,000 official test (`split_seed = 2026`)
- **Network:** `784 → 256 → 256 → 256 → 10` MLP, ReLU activations
- **Dropout:** Manual hidden-layer inverted dropout only (no input/output dropout)
- **Rates evaluated:** $d \in \{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7\}$
- **Seeds:** 42, 43, 44 (same seed generates identical initial weights across all rates)
- **Training:** 20 fixed epochs, batch size 128, Adam optimizer (`lr = 0.001`, `weight_decay = 0`)
- **Model selection:** Lowest mean validation error across seeds at fixed epoch 20 (ties broken by lower $d$).
- **Test evaluation:** Descriptive evaluation only; test performance is strictly never used for model selection or tuning.

## Verified Results

All numbers below reflect independent recomputations from verified final runs across seeds 42, 43, 44 (sample standard deviation with $ddof=1$).

### MNIST (Main Reproduction)
- **Baseline ($d=0.0$):**
  - Test error: $4.320 \pm 0.295\%$ (Accuracy: $95.680\%$)
  - Generalization gap: $4.117 \pm 0.101$ pp
- **Validation-selected model ($d=0.4$):**
  - Validation error: $3.747 \pm 0.130\%$ (selected by minimum validation error)
  - Test error: $3.843 \pm 0.282\%$ (Accuracy: $96.157\%$)
  - Generalization gap: $3.520 \pm 0.295$ pp
  - **Test-error change vs baseline:** $+0.477$ percentage points lower test error ($11.03\%$ relative error reduction)
- **Reference rate ($d=0.5$):**
  - Test error: $3.883 \pm 0.087\%$
- **Descriptive test-error-best:**
  - $d=0.3$ had lowest mean test error ($3.820 \pm 0.118\%$), but $d=0.4$ is the true chosen model governed by validation error.
- **Negative findings:**
  - High dropout rates noticeably degraded performance ($d=0.6$: $4.380\%$, $d=0.7$: $5.110\%$) below the no-dropout baseline ($4.320\%$).

### Fashion-MNIST (Extension Benchmark)
- **Baseline ($d=0.0$):**
  - Test error: $14.663 \pm 0.175\%$ (Accuracy: $85.337\%$)
  - Generalization gap: $7.533 \pm 0.351$ pp
- **Validation-selected model ($d=0.2$):**
  - Validation error: $13.087 \pm 0.408\%$ (selected by minimum validation error)
  - Test error: $14.347 \pm 0.253\%$ (Accuracy: $85.653\%$)
  - Generalization gap: $5.763 \pm 0.165$ pp
  - **Test-error change vs baseline:** $+0.317$ percentage points lower test error ($2.16\%$ relative error reduction)
- **Reference rate ($d=0.5$):**
  - Test error: $15.133 \pm 0.325\%$ ($+0.470$ pp *worse* than baseline)
- **Descriptive test-error-best:**
  - $d=0.1$ had lowest mean test error ($14.220 \pm 0.105\%$), but $d=0.2$ is the chosen model based on validation error.
- **Negative findings:**
  - Standard paper rate $d=0.5$ underperformed the baseline; higher rates ($d=0.7$: $17.453\%$) severely degraded test accuracy.

*Complete 8-rate audit tables and detailed statistical breakdowns are documented in [RESULTS_AUDIT.md](RESULTS_AUDIT.md), [results_mnist/RESULTS.md](results_mnist/RESULTS.md), and [results_fashion/RESULTS.md](results_fashion/RESULTS.md).*

## Output Files
Each experiment run produces the following artifacts in its output directory:
- `config.json`: Complete execution metadata, hyperparameters, environment info, and `run.py` source hash.
- `history.csv`: Per-epoch metrics across all 480 runs (24 runs × 20 epochs).
- `final_results.csv`: Final epoch 20 metrics for all 24 rate-seed runs.
- `summary.csv`: Aggregated means and sample standard deviations across seeds.
- `selected_rates.json`: Drop rate selected strictly by lowest mean validation error.
- `RESULTS.md`: Markdown summary table.
- Plots:
  - `*_overfitting.png`: Training/test error and validation loss curves ($d=0$ vs $d=0.5$).
  - `*_drop_rates.png`: Error vs drop probability $d$.
  - `*_keep_probability.png`: Error vs retention probability $q = 1 - d$ (Figure 9(a) convention).
  - `*_failure_cases.png`: Grid of first 12 misclassified test images with predictions and confidences.
- Checkpoints: `*_d*_s*.pt` local PyTorch model state dicts (ignored by Git).

## Colab
The generated notebook `24CS2032_Dropout.ipynb` is fully self-contained and embeds the complete `run.py` script.
- Default execution runs the full MNIST sweep (`results_mnist_colab`).
- An optional, clearly labeled cell provides the Fashion-MNIST extension sweep (`results_fashion_colab`).
- **Hosted Colab status:** Hosted Colab execution has not yet been verified.

## Reproduction Limits
This study is an educational reduced-scale ablation inspired by Srivastava et al. (2014) and does not claim exact numerical replication:
- **Architecture:** 784–256–256–256–10 MLP (original used 784–1024–1024–1024–10 or larger).
- **Scale:** 10,000 training examples and 20 epochs with Adam (original used 50,000+ examples, hundreds of epochs, SGD with momentum and max-norm weight clipping).
- **Dropout formulation:** Standard inverted dropout during training ($x \cdot m / q$) vs test-time weight scaling ($x \cdot q$).
- **Fashion-MNIST:** Serves as a modern extension benchmark under the identical protocol; it was not evaluated in the original 2014 paper.

## References
1. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). *"Dropout: A Simple Way to Prevent Neural Networks from Overfitting."* Journal of Machine Learning Research, 15(56), 1929-1958. https://jmlr.org/papers/v15/srivastava14a.html
2. Author dropout project page: https://www.cs.toronto.edu/~nitish/dropout/
3. Historical Deepnet repository (consulted for historical context; not a dependency): https://github.com/nitishsrivastava/deepnet
4. PyTorch Dropout reference: https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html
5. Torchvision MNIST documentation: https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html

## Assistance and Provenance
ChatGPT and Antigravity were used for implementation guidance, code review, local execution automation, verification, and documentation support. All reported experiment results come from the recorded real-data runs in this repository; no synthetic result data were used. External assistance should be disclosed according to the course policy.
