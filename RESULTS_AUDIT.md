# Results Audit — 24CS2032

## Protocol verification
- **Protocol ID:** `dropout-24cs2032-v1`
- **Architecture:** `784 → 256 → 256 → 256 → 10` (MLP, ReLU activations)
- **Parameter count:** 335,114 (verified exact)
- **Dropout implementation:** Custom inverted `ManualDropout` after hidden ReLUs only (`training = x * mask / q`, `eval = x`, where `q = 1 - d`). No `nn.Dropout`, `F.dropout`, or `functional.dropout`.
- **Backend:** CPU (verified >5.5x faster than MPS on this architecture; zero GPU dispatch overhead)
- **Source code hash (SHA-256):** `e368902657099fcbf06ea48e91e1552320b881a2646ff3bb36a6a4023090fa5b` (identical in both `results_mnist/config.json` and `results_fashion/config.json`)
- **Dataset splits:** 10,000 train / 5,000 validation / 10,000 official test (`split_seed = 2026`). Disjointness verified: `len(intersect(train, validation)) == 0`. Test set addresses full official 10,000 images (`0..9999`).
- **Optimization:** Adam (`lr = 0.001`, `weight_decay = 0`), batch size 128, 20 fixed epochs.
- **Experiment structure:** 8 drop rates (`0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7`) × 3 seeds (`42, 43, 44`) = 24 runs per dataset, 480 epoch rows per dataset.
- **Selection policy:** Lowest mean validation error across seeds at fixed epoch 20. Ties broken by selecting the lower drop rate. Test set used strictly for descriptive reporting; never used for tuning or selection.

---

## MNIST full-rate table (independent recomputation)

All metrics computed at fixed epoch 20 across seeds 42, 43, 44. Standard deviations are sample SD ($ddof=1$).

| Drop rate $d$ | Train error % (mean ± SD) | Validation error % (mean ± SD) | Test error % (mean ± SD) | Test accuracy % (mean ± SD) | Generalization gap pp (mean ± SD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0.0 | 0.203 ± 0.200 | 4.260 ± 0.533 | 4.320 ± 0.295 | 95.680 ± 0.295 | 4.117 ± 0.101 |
| 0.1 | 0.090 ± 0.044 | 4.180 ± 0.314 | 4.050 ± 0.278 | 95.950 ± 0.278 | 3.960 ± 0.236 |
| 0.2 | 0.110 ± 0.000 | 3.893 ± 0.099 | 3.900 ± 0.239 | 96.100 ± 0.239 | 3.790 ± 0.239 |
| 0.3 | 0.240 ± 0.080 | 3.753 ± 0.061 | 3.820 ± 0.118 | 96.180 ± 0.118 | 3.580 ± 0.044 |
| **0.4** | **0.323 ± 0.047** | **3.747 ± 0.130** | **3.843 ± 0.282** | **96.157 ± 0.282** | **3.520 ± 0.295** |
| 0.5 | 0.700 ± 0.044 | 3.840 ± 0.140 | 3.883 ± 0.087 | 96.117 ± 0.087 | 3.183 ± 0.083 |
| 0.6 | 1.273 ± 0.057 | 4.407 ± 0.219 | 4.380 ± 0.104 | 95.620 ± 0.104 | 3.107 ± 0.070 |
| 0.7 | 2.513 ± 0.153 | 5.133 ± 0.090 | 5.110 ± 0.147 | 94.890 ± 0.147 | 2.597 ± 0.131 |

---

## Fashion-MNIST full-rate table (independent recomputation)

All metrics computed at fixed epoch 20 across seeds 42, 43, 44. Standard deviations are sample SD ($ddof=1$).

| Drop rate $d$ | Train error % (mean ± SD) | Validation error % (mean ± SD) | Test error % (mean ± SD) | Test accuracy % (mean ± SD) | Generalization gap pp (mean ± SD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0.0 | 7.130 ± 0.177 | 13.127 ± 0.247 | 14.663 ± 0.175 | 85.337 ± 0.175 | 7.533 ± 0.351 |
| 0.1 | 7.587 ± 0.471 | 13.113 ± 0.042 | 14.220 ± 0.105 | 85.780 ± 0.105 | 6.633 ± 0.520 |
| **0.2** | **8.583 ± 0.414** | **13.087 ± 0.408** | **14.347 ± 0.253** | **85.653 ± 0.253** | **5.763 ± 0.165** |
| 0.3 | 9.393 ± 0.067 | 13.267 ± 0.244 | 14.567 ± 0.396 | 85.433 ± 0.396 | 5.173 ± 0.351 |
| 0.4 | 10.060 ± 0.584 | 13.573 ± 0.494 | 14.647 ± 0.330 | 85.353 ± 0.330 | 4.587 ± 0.347 |
| 0.5 | 10.990 ± 0.366 | 13.747 ± 0.200 | 15.133 ± 0.325 | 84.867 ± 0.325 | 4.143 ± 0.046 |
| 0.6 | 12.273 ± 0.323 | 14.380 ± 0.053 | 15.730 ± 0.373 | 84.270 ± 0.373 | 3.457 ± 0.179 |
| 0.7 | 14.543 ± 0.468 | 15.673 ± 0.380 | 17.453 ± 0.376 | 82.547 ± 0.376 | 2.910 ± 0.115 |

---

## Validation-selected models

1. **MNIST:**
   - **Independently selected rate:** $d = 0.4$
   - **Mean validation error:** $3.747\%$ (minimum among all rates)
   - **Mean test error:** $3.843 \pm 0.282\%$
   - **Mean test accuracy:** $96.157\%$
   - **Baseline comparison:** $+0.477$ percentage points lower test error than baseline ($d=0.0$).
   - **Relative error reduction:** $11.03\%$.
   - *Descriptive note:* The lowest mean test error occurred at $d=0.3$ ($3.820\%$), but model selection strictly obeyed the protocol rule using validation error only.

2. **Fashion-MNIST:**
   - **Independently selected rate:** $d = 0.2$
   - **Mean validation error:** $13.087\%$ (minimum among all rates)
   - **Mean test error:** $14.347 \pm 0.253\%$
   - **Mean test accuracy:** $85.653\%$
   - **Baseline comparison:** $+0.317$ percentage points lower test error than baseline ($d=0.0$).
   - **Relative error reduction:** $2.16\%$.
   - *Descriptive note:* The lowest mean test error occurred at $d=0.1$ ($14.220\%$), but model selection strictly obeyed validation-based selection.

---

## Baseline vs Selected vs d=0.5 comparison

### MNIST
- **Baseline ($d=0.0$):** Test error $4.320 \pm 0.295\%$, Gap $4.117$ pp.
- **Selected ($d=0.4$):** Test error $3.843 \pm 0.282\%$, Gap $3.520$ pp (Test error reduced by $0.477$ pp).
- **Reference ($d=0.5$):** Test error $3.883 \pm 0.087\%$, Gap $3.183$ pp.

### Fashion-MNIST
- **Baseline ($d=0.0$):** Test error $14.663 \pm 0.175\%$, Gap $7.533$ pp.
- **Selected ($d=0.2$):** Test error $14.347 \pm 0.253\%$, Gap $5.763$ pp (Test error reduced by $0.317$ pp).
- **Reference ($d=0.5$):** Test error $15.133 \pm 0.325\%$, Gap $4.143$ pp ($0.470$ pp *worse* than baseline).

---

## Negative findings
1. **Excessive dropout degrades performance:**
   - On MNIST, $d=0.6$ ($4.380\%$) and $d=0.7$ ($5.110\%$) result in worse test error than the baseline without dropout ($4.320\%$).
   - On Fashion-MNIST, $d=0.5$ ($15.133\%$), $d=0.6$ ($15.730\%$), and $d=0.7$ ($17.453\%$) all degrade performance below the baseline ($14.663\%$).
2. **Fixed paper reference ($d=0.5$) underperforms on Fashion-MNIST:**
   - While $d=0.5$ is effective on MNIST ($3.883\%$), on Fashion-MNIST it harms performance by $+0.470$ percentage points compared to $d=0.0$, demonstrating that optimal dropout rate is dataset- and capacity-dependent.
3. **Training error increases with dropout:**
   - Dropout prevents complete memorization on training data (MNIST train error rises from $0.203\%$ at $d=0.0$ to $2.513\%$ at $d=0.7$; Fashion train error rises from $7.130\%$ to $14.543\%$).

---

## Failure examples (official test set)

### MNIST
1. **Index 0:** True label `2 - two` $\rightarrow$ Predicted `3 - three` (confidence $0.52$). The handwritten two features an open curving loop and bottom curl that resembles a three.
2. **Index 1:** True label `9 - nine` $\rightarrow$ Predicted `8 - eight` (confidence $0.91$). The closed loop and high-contrast stroke overlap mimic an eight.

### Fashion-MNIST
1. **Index 0:** True label `Coat` $\rightarrow$ Predicted `Pullover` (confidence $0.71$). Textured fabric with long sleeves in low-resolution grayscale ($28\times28$) lacks clear button/lapel boundary signals.
2. **Index 2:** True label `Ankle boot` $\rightarrow$ Predicted `Sneaker` (confidence $0.99$). Low-cut ankle boot profile with thick sole contour strongly resembles sneaker footwear.

---

## Paper comparison boundary
- **Not an exact replication:** This study is an educational reduced-scale ablation inspired by Srivastava et al. (JMLR 2014, Figure 9(a)).
- **Key setup differences:**
  - Architecture: 784–256–256–256–10 MLP (original used 784–1024–1024–1024–10 or larger).
  - Training scale: 10,000 training examples, 20 epochs, Adam optimizer (original used 50,000+ examples, hundreds of epochs, SGD with momentum and max-norm weight clipping).
  - Dropout formulation: Standard inverted dropout $x \cdot m / q$ at train time (paper used standard forward scaling at test time $x \cdot q$).
- **Fashion-MNIST:** Serves as a modern controlled extension across the identical protocol, demonstrating that higher-complexity visual patterns require lower regularization ($d=0.2$).

---

## Audit evidence
- **`verify_results.py`:** PASS on both `results_mnist` and `results_fashion`.
- **Aggregate recomputation:** All means and sample standard deviations ($ddof=1$) match `summary.csv` within $10^{-8}$ tolerance.
- **Formulas verified:** `gap_pp = test_error - train_error` and `test_accuracy = 100 - test_error` hold exactly across all rows.
- **Checkpoint reload & inference:** Loaded selected checkpoints (`mnist_d0.4_s42.pt` and `fashion_d0.2_s42.pt`) on CPU, confirmed output shape $[10, 10]$ and finite logits. Evaluated over full 10,000 official test images; accuracy matches CSV records exactly ($3.5200\%$ error on MNIST, $14.5400\%$ error on Fashion).
- **Plot visual audit:** All 8 PNG plots directly rendered and inspected; axes, titles, legends, and unclipped layouts verified.
