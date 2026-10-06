# 24CS2032 project state
Last updated: 2026-10-07 03:47 IST
Master version: 3, 5 October 2026
Protocol: dropout-24cs2032-v1

## Identity and administrative details
Roll: 24CS2032
Name: NOT PROVIDED (STUDENT_NAME_PENDING used in report)
Presentation start date in workbook: 15 October 2026
Individual slot: UNKNOWN
Exact submission portal/cutoff: UNKNOWN
Repository owner: sg721642
Preferred repository: 24cs2032-dropout-paper-implementation
Visibility: private by default
Repository creation / ordinary commits / pushes: USER AUTHORIZED
Verified remote URL / branch / last pushed SHA: https://github.com/sg721642/24cs2032-dropout-paper-implementation / main / 1d39d3576ebd9fd95b8661670c7e607e860ff79e

## Local environment
Workspace absolute path: /Users/satyamgupta/Documents/24CS2032_Dropout
OS/architecture: macOS 26.6.2 (Build 25G83) / arm64 (Apple Silicon)
Python executable/version: /Users/satyamgupta/Documents/24CS2032_Dropout/.venv/bin/python / Python 3.13.9
Venv path: /Users/satyamgupta/Documents/24CS2032_Dropout/.venv
torch version: 2.14.1 (macosx_14_0_arm64)
torchvision version: 0.29.1
numpy version: 2.5.3
pandas version: 3.0.6
matplotlib version: 3.11.2
MPS built: True
MPS available: True
CPU test: PASS (self_test PASS: mask, scaling, gradient, fresh masks, eval, p=0, bounds, MLP shape)
MPS test: PASS (self_test PASS: mask, scaling, gradient, fresh masks, eval, p=0, bounds, MLP shape)
Chosen final backend: cpu
Timing observations / measured elapsed:
- CPU 2-epoch benchmark (default width=256, train=10000, val=5000, test=10000): 0.785 seconds
- MPS 2-epoch benchmark (default width=256, train=10000, val=5000, test=10000): 4.398 seconds
- Backend decision: CPU is >5.5x faster than MPS on this workload due to GPU dispatch and synchronization latency on small tensors (MLP parameter count: 335,114). CPU selected as optimal stable backend.
Estimated duration (ESTIMATE ONLY):
- One dataset full sweep (24 runs × 20 epochs): ~0.785s × 240 ≈ 188.4s (~3.14 minutes)
- Two datasets full sweep (48 runs total): ~376.8s (~6.28 minutes)

## Gate status
G0 context: PASS — roll 24CS2032 identified; master read to END marker (line 1829); workspace and pre-existing state inspected; no unrelated repository overwritten
G1 setup: PASS — arm64 native Python 3.13.9; isolated .venv created; all dependencies installed; run.py/make_notebook.py/verify_results.py compile; ManualDropout present, no built-in dropout; parameter count 335114 verified; initial commit and push verified
G2 core tests: PASS — CPU ManualDropout self-test PASS; initialization equality across d=0.0, 0.5, 0.7 for seed 42 PASS; no built-in dropout in model; MPS self-test PASS
G3 smoke pipeline: PASS — real MNIST & Fashion-MNIST smoke pipelines completed (smoke_mnist, smoke_fashion); 6 history rows, 3 final rows, 3 summary rows each; finite metrics verified; train/val split disjoint verified; 3 checkpoints each; checkpoint reload & inference verified. Programmatic PNG checks passed (PNG header signatures, PIL dimension/mode checks, non-empty). Direct visual inspection of all 8 smoke plots completed and confirmed unclipped, readable titles/axes/legends, correct axis designations (drop probability d vs keep probability q = 1 - d), and clean 3x4 failure-case grids. Smoke results are pipeline checks only and are not final experiment results.
G4 protocol/device lock: PASS — CPU selected based on measured timing evidence (0.785s vs 4.398s); dropout-24cs2032-v1 protocol frozen; exact G5 commands recorded; final sweep NOT started
G5 full experiments: PASS — 24/24 MNIST runs complete (480 history rows, 24 checkpoints), 24/24 Fashion-MNIST runs complete (480 history rows, 24 checkpoints); all metrics finite; disjoint train/val splits; frozen configs and source hashes verified; no missing/fabricated runs; CPU backend used throughout
G6 results audit: PASS — read-only verify_results.py passed on both datasets; protocol/configs/splits verified; all aggregates (mean and sample SD, ddof=1) independently recomputed and matched summary.csv within 1e-8; validation selection independently verified (MNIST d=0.4, Fashion d=0.2; test error strictly not used in selection); selected checkpoints reloaded and full-test error matches CSV records; all 8 final plots directly visually inspected; RESULTS_AUDIT.md created
G7 notebook/README: PASS — make_notebook.py embeds project run.py byte-for-byte (SHA: e368902657099fcbf06ea48e91e1552320b881a2646ff3bb36a6a4023090fa5b); 24CS2032_Dropout.ipynb generated (12 cells, clean outputs, unexecuted deliverable); local smoke execution in notebook_smoke/ passed exit code 0; README.md updated with G6 verified metrics, reproduction limits, cautious negative finding discussions, and assistance disclosure; hosted Colab execution recorded as NOT VERIFIED; environment frozen to environment-lock.txt
G8 report: PENDING (IDENTITY ONLY) — report content/compile/visual QA complete; verified student name required before final PASS
G9 presentation: PENDING
G10 clean package: PENDING
G11 repository/course submission: PENDING

## Commands executed in G2–G4 stage
```bash
# G2 CPU self-test
python run.py --self-test --device cpu | tee g2_selftest_cpu.log

# G2 Fair initialization check
python - <<'PY' | tee g2_initialization_check.log
import torch
from run import MLP, set_seed
seed = 42
set_seed(seed); m0 = MLP(0.0, 256)
set_seed(seed); m5 = MLP(0.5, 256)
set_seed(seed); m7 = MLP(0.7, 256)
assert m0.state_dict().keys() == m5.state_dict().keys() == m7.state_dict().keys()
for k in m0.state_dict():
    assert torch.equal(m0.state_dict()[k], m5.state_dict()[k])
    assert torch.equal(m0.state_dict()[k], m7.state_dict()[k])
print("PASS: identical initial model state for seed 42 across d=0.0, 0.5, 0.7")
PY

# G3 Real MNIST smoke pipeline
python run.py --datasets mnist --device cpu --epochs 2 --train-size 200 --val-size 100 --test-size 100 --rates 0 0.5 0.7 --seeds 42 --width 32 --out smoke_mnist 2>&1 | tee g3_smoke_mnist.log

# G3 Real Fashion-MNIST smoke pipeline
python run.py --datasets fashion --device cpu --epochs 2 --train-size 200 --val-size 100 --test-size 100 --rates 0 0.5 0.7 --seeds 42 --width 32 --out smoke_fashion 2>&1 | tee g3_smoke_fashion.log

# G3 Programmatic audit and checkpoint reload
# (Verified 6 history rows, 3 final rows, 3 summary rows, finite values, disjoint splits, checkpoint reload)

# G4 CPU default-width timing (width=256, train=10000, val=5000, test=10000, batch=128)
python run.py --datasets mnist --device cpu --epochs 2 --rates 0.5 --seeds 42 --out timing_cpu 2>&1 | tee g4_timing_cpu.log

# G4 MPS correctness self-test
python run.py --self-test --device mps | tee g2_selftest_mps.log

# G4 MPS default-width timing
python run.py --datasets mnist --device mps --epochs 2 --rates 0.5 --seeds 42 --out timing_mps 2>&1 | tee g4_timing_mps.log
```

## Frozen scientific protocol (dropout-24cs2032-v1)
- Protocol ID: dropout-24cs2032-v1
- Architecture: 784 → 256 → 256 → 256 → 10
- Activation: ReLU
- Dropout: manual hidden-layer inverted dropout only
  - training: x * mask / q (where q = 1 - d)
  - evaluation: x
  - no input dropout, no output dropout
- Drop rates: 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 (8 rates)
- Seeds: 42, 43, 44 (3 seeds)
- Split seed: 2026
- Data: train 10000, validation 5000, official test 10000
- Preprocessing: float32 / 255
- Epochs: 20
- Batch size: 128
- Optimizer: Adam (lr=0.001, weight_decay=0)
- Other regularization: none
- Selection: lowest mean validation error across seeds (tie → lower drop rate)
- Final metrics: fixed final epoch, mean + sample SD
- Test policy: descriptive comparison only; no rate/epoch/hyperparameter tuning from test set
- Datasets: MNIST main reproduction, Fashion-MNIST same-protocol extension
- Chosen final backend: cpu (measured faster than MPS for this architecture)

## Exact recorded G5 final commands (DO NOT EXECUTE UNTIL G5)
```bash
# MNIST final sweep (24 runs: 8 rates × 3 seeds × 20 epochs = 480 epoch rows)
caffeinate -i python run.py --datasets mnist --device cpu --out results_mnist

# Fashion-MNIST final sweep (24 runs: 8 rates × 3 seeds × 20 epochs = 480 epoch rows)
caffeinate -i python run.py --datasets fashion --device cpu --out results_fashion
```

## Experiments inventory
MNIST final output folder: results_mnist (COMPLETE: 24/24 runs, 480 history rows, 24 final_results rows, 8 summary rows, 24 .pt checkpoints)
MNIST completed runs: 24/24
Fashion final output folder: results_fashion (COMPLETE: 24/24 runs, 480 history rows, 24 final_results rows, 8 summary rows, 24 .pt checkpoints)
Fashion completed runs: 24/24
Separate exploratory/smoke/timing folders:
- smoke_mnist (NON-FINAL pipeline test)
- smoke_fashion (NON-FINAL pipeline test)
- timing_cpu (2-epoch benchmark: 0.785s)
- timing_mps (2-epoch benchmark: 4.398s)
Protocol deviations and reason: NONE
Source changes and reason: NONE

## Actual results
All values derived from independent recomputation of `final_results.csv` at fixed epoch 20 across seeds 42, 43, 44 (sample SD with $ddof=1$).
Model selection strictly based on lowest mean validation error across seeds at fixed epoch 20 (ties broken by lower rate). Test set used for descriptive evaluation only.

### MNIST
- Baseline ($d=0.0$): Test error $4.320 \pm 0.295\%$, Generalization gap $4.117 \pm 0.101$ pp
- Validation-selected rate: $d = 0.4$ (selected by minimum validation error $3.747 \pm 0.130\%$)
- Selected model test error: $3.843 \pm 0.282\%$
- Selected model test accuracy: $96.157 \pm 0.282\%$
- Selected model generalization gap: $3.520 \pm 0.295$ pp
- Test-error change vs baseline: $+0.477$ percentage points lower test error (Relative error reduction: $11.03\%$)
- Reference rate ($d=0.5$): Test error $3.883 \pm 0.087\%$, Gap $3.183 \pm 0.083$ pp
- Descriptive test-error-best rate: $d=0.3$ ($3.820 \pm 0.118\%$; not used for model selection)
- Negative findings: Higher rates degrade test error below baseline ($d=0.6$: $4.380\%$, $d=0.7$: $5.110\%$).

### Fashion-MNIST
- Baseline ($d=0.0$): Test error $14.663 \pm 0.175\%$, Generalization gap $7.533 \pm 0.351$ pp
- Validation-selected rate: $d = 0.2$ (selected by minimum validation error $13.087 \pm 0.408\%$)
- Selected model test error: $14.347 \pm 0.253\%$
- Selected model test accuracy: $85.653 \pm 0.253\%$
- Selected model generalization gap: $5.763 \pm 0.165$ pp
- Test-error change vs baseline: $+0.317$ percentage points lower test error (Relative error reduction: $2.16\%$)
- Reference rate ($d=0.5$): Test error $15.133 \pm 0.325\%$ ($+0.470$ pp worse than baseline!)
- Descriptive test-error-best rate: $d=0.1$ ($14.220 \pm 0.105\%$; not used for model selection)
- Negative findings: Reference $d=0.5$ underperforms no-dropout baseline; rates $d \ge 0.5$ degrade performance sharply ($d=0.7$: $17.453\%$).

## Artifacts and evidence
Source/requirements/notebook paths: /Users/satyamgupta/Documents/24CS2032_Dropout/{run.py,make_notebook.py,verify_results.py,requirements.txt,environment-lock.txt,24CS2032_Dropout.ipynb,.gitignore,README.md}
Audit document: /Users/satyamgupta/Documents/24CS2032_Dropout/RESULTS_AUDIT.md
Final experiment folders:
- results_mnist/ (480 history rows, 24 final rows, 8 summary rows, 24 .pt checkpoints, RESULTS.md, selected_rates.json, 4 PNG plots)
- results_fashion/ (480 history rows, 24 final rows, 8 summary rows, 24 .pt checkpoints, RESULTS.md, selected_rates.json, 4 PNG plots)
Smoke folders: /Users/satyamgupta/Documents/24CS2032_Dropout/{smoke_mnist,smoke_fashion}
Note: Smoke results are pipeline checks only and are not final experiment results.
Visual audit of final plots (all 8 directly opened and inspected):
1. results_mnist/mnist_overfitting.png — readable, unclipped, correct train/test error & validation loss
2. results_mnist/mnist_drop_rates.png — readable, unclipped, x-axis = drop probability d
3. results_mnist/mnist_keep_probability.png — readable, unclipped, x-axis = keep probability q = 1 - d
4. results_mnist/mnist_failure_cases.png — readable, unclipped 3x4 grid of real test images with true/pred labels & confidences
5. results_fashion/fashion_overfitting.png — readable, unclipped, correct train/test error & validation loss
6. results_fashion/fashion_drop_rates.png — readable, unclipped, x-axis = drop probability d
7. results_fashion/fashion_keep_probability.png — readable, unclipped, x-axis = keep probability q = 1 - d
8. results_fashion/fashion_failure_cases.png — readable, unclipped 3x4 grid of real test images with true/pred labels & confidences
Timing folders: /Users/satyamgupta/Documents/24CS2032_Dropout/{timing_cpu,timing_mps}
Diagnostic logs:
- g2_selftest_cpu.log
- g2_initialization_check.log
- g2_selftest_mps.log
- g3_smoke_mnist.log
- g3_smoke_fashion.log
- g3_checkpoint_reload.log
- g4_timing_cpu.log
- g4_timing_mps.log
- g5_mnist.log (total runtime: ~151s)
- g5_fashion.log (total runtime: ~148s)
- g6_verify_mnist.log (PASS)
- g6_verify_fashion.log (PASS)
- g6_aggregate_audit.log (PASS: independent recomputation matches summary.csv within 1e-8)
- g6_checkpoint_final.log (PASS: selected model checkpoints reloaded, evaluated on full 10k test set, matched CSV)
- g7_notebook_smoke.log (PASS: local smoke notebook execution via nbclient, exit code 0)
Notebook local execution: PASS (tested on temporary isolated copy notebook_smoke/24CS2032_Dropout_smoke.ipynb via nbclient; exited code 0; final results untouched; deliverable notebook left unexecuted)
Hosted Colab execution: NOT VERIFIED ("Hosted Colab execution has not yet been verified")
Report source/PDF/page count/render check: report/main.tex (complete), report/references.bib (8 references), report/IEEEtran.cls, report/figures/ (5 genuine final figures), report/24CS2032_Dropout_Report.pdf (584 KB, compiled via tectonic 0.17.0, exit 0, exactly 5 pages, 0 LaTeX errors, 0 unresolved citations/references, visual inspection of all 5 rendered pages PASS; author name marked STUDENT_NAME_PENDING per identity rule)
Slides/source/render check: PENDING
Submission ZIP/integrity: PENDING
GitHub URL: https://github.com/sg721642/24cs2032-dropout-paper-implementation
Course submission receipt: PENDING

## GitHub status
gh version: 2.100.0
Authenticated account: sg721642
Repository: sg721642/24cs2032-dropout-paper-implementation
Visibility: PRIVATE (confirmed)
Push status: VERIFIED (prior commit: 1d39d3576ebd9fd95b8661670c7e607e860ff79e)
Remote URL: https://github.com/sg721642/24cs2032-dropout-paper-implementation
Branch: main

## Commands and active process
Exact currently running/last command: tectonic main.tex (exit 0) && python render_pdf.py (exit 0)
Active process or terminal session: NONE
Log path: report/compile.log
Last observed progress/time: 2026-10-07 03:47 IST

## Immediate next step
First incomplete gate: G8 final closure (awaiting verified student name to replace STUDENT_NAME_PENDING in report/main.tex and recompile PDF)
Exact command: Await verified student name, update \author in report/main.tex, recompile with tectonic, and transition G8 to PASS
Expected evidence: Clean compiled report PDF with verified student name and roll number 24CS2032

## Blockers requiring user interaction
Student Name: The actual student name has not been provided in the project authority. Per strict identity rules, STUDENT_NAME_PENDING is used in report/main.tex and report/24CS2032_Dropout_Report.pdf. The user must provide their verified student name to achieve final G8 PASS before proceeding to G9.

## Session handoff
What was completed:
- G8: IEEE conference 5-page report authored, compiled, audited, and visually inspected:
  1. Installed tectonic 0.17.0 via Homebrew and PyMuPDF 1.28.2 in .venv.
  2. Placed official CTAN IEEEtran.cls in report/.
  3. Populated report/figures/ with genuine final experiment figures (mnist_overfitting.png, mnist_keep_probability.png, fashion_keep_probability.png, mnist_failure_cases.png, fashion_failure_cases.png); no smoke figures used.
  4. Authored report/references.bib with 8 complete bibliographic entries (Srivastava et al. JMLR 2014, LeCun et al. 1998, Xiao et al. 2017, author project page, deepnet repo, PyTorch docs, Torchvision MNIST, Torchvision Fashion-MNIST).
  5. Authored report/main.tex adhering strictly to IEEE conference format, structured into VII sections: Introduction, Dropout Mathematical Formulation, Experimental Setup & Methodology, MNIST Empirical Findings, Fashion-MNIST Extension, Discussion & Limitations, Conclusion, and external Assistance Statement.
  6. Incorporated complete 8-rate summary tables for MNIST and Fashion-MNIST with exact mean +/- sample SD numbers matching RESULTS_AUDIT.md and summary CSVs.
  7. Formatted keep-probability ablation curves and failure analysis side-by-side figures.
  8. Compiled clean PDF report/24CS2032_Dropout_Report.pdf (584 KB) via tectonic 0.17.0 with 0 errors, 0 undefined citations, 0 undefined references, and 0 overfull hboxes.
  9. Verified exact page count: 5 pages (target 4–6 pages).
  10. Programmatically rendered each page to high-resolution PNG at 130 DPI and directly visually inspected all 5 pages via image viewer; confirmed clean two-column layout, unclipped figures, sharp typography, and absence of text overlaps.
  11. Audited against identity rules: Author name marked STUDENT_NAME_PENDING with roll 24CS2032.
  12. Gate status set to PENDING (IDENTITY ONLY); G9 remains PENDING until student name is supplied.
What changed: report/main.tex, report/references.bib, report/IEEEtran.cls, report/figures/*, report/24CS2032_Dropout_Report.pdf, PROJECT_STATE.md, .gitignore.
What failed: NONE.
What remains: G8 final closure upon student name input, G9 (presentation slides), G10 (clean packaging), G11 (submission receipt).
