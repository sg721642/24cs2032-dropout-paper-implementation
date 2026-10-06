# 24CS2032 project state
Last updated: 2026-10-07 02:18 IST
Master version: 3, 5 October 2026
Protocol: dropout-24cs2032-v1

## Identity and administrative details
Roll: 24CS2032
Name: NOT PROVIDED
Presentation start date in workbook: 15 October 2026
Individual slot: UNKNOWN
Exact submission portal/cutoff: UNKNOWN
Repository owner: sg721642
Preferred repository: 24cs2032-dropout-paper-implementation
Visibility: private by default
Repository creation / ordinary commits / pushes: USER AUTHORIZED
Verified remote URL / branch / last pushed SHA: https://github.com/sg721642/24cs2032-dropout-paper-implementation / main / 1f2749550663c1810c78c899565e60a91fd016f5

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
G5 full experiments: IN PROGRESS (MNIST 24/24 complete, 480 epoch rows, 24 checkpoints; Fashion-MNIST PENDING)
G6 results audit: PENDING
G7 notebook/README: PENDING
G8 report: PENDING
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
Fashion final output folder: NONE (G5 pending)
Fashion completed runs: 0/24
Separate exploratory/smoke/timing folders:
- smoke_mnist (NON-FINAL pipeline test)
- smoke_fashion (NON-FINAL pipeline test)
- timing_cpu (2-epoch benchmark: 0.785s)
- timing_mps (2-epoch benchmark: 4.398s)
Protocol deviations and reason: NONE
Source changes and reason: NONE

## Actual results
Do not fill until CSVs are complete and checked in G5/G6.
Baseline/selected rate/mean error/sample SD: PENDING
Selection based on: mean validation error, fixed final epoch
Negative findings/failure examples: PENDING

## Artifacts and evidence
Source/requirements/notebook paths: /Users/satyamgupta/Documents/24CS2032_Dropout/{run.py,make_notebook.py,verify_results.py,requirements.txt,.gitignore,README.md}
Smoke folders: /Users/satyamgupta/Documents/24CS2032_Dropout/{smoke_mnist,smoke_fashion}
Note: Smoke results are pipeline checks only and are not final experiment results.
Visual audit of smoke plots (all 8 directly opened and inspected):
1. smoke_mnist/mnist_overfitting.png — readable, unclipped, correct train/test error & validation loss
2. smoke_mnist/mnist_drop_rates.png — readable, unclipped, x-axis = drop probability d
3. smoke_mnist/mnist_keep_probability.png — readable, unclipped, x-axis = keep probability q = 1 - d
4. smoke_mnist/mnist_failure_cases.png — readable, unclipped 3x4 grid with true/pred labels & confidences
5. smoke_fashion/fashion_overfitting.png — readable, unclipped, correct train/test error & validation loss
6. smoke_fashion/fashion_drop_rates.png — readable, unclipped, x-axis = drop probability d
7. smoke_fashion/fashion_keep_probability.png — readable, unclipped, x-axis = keep probability q = 1 - d
8. smoke_fashion/fashion_failure_cases.png — readable, unclipped 3x4 grid with true/pred labels & confidences
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
Notebook local execution: NOT VERIFIED
Hosted Colab execution: NOT VERIFIED
Report source/PDF/page count/render check: PENDING
Slides/source/render check: PENDING
Submission ZIP/integrity: PENDING
GitHub URL: https://github.com/sg721642/24cs2032-dropout-paper-implementation
Course submission receipt: PENDING

## GitHub status
gh version: 2.100.0
Authenticated account: sg721642
Repository: sg721642/24cs2032-dropout-paper-implementation
Visibility: PRIVATE (confirmed)
Push status: VERIFIED (prior commit: 1f2749550663c1810c78c899565e60a91fd016f5)
Remote URL: https://github.com/sg721642/24cs2032-dropout-paper-implementation
Branch: main

## Commands and active process
Exact currently running/last command: caffeinate -i python run.py --datasets mnist --device cpu --out results_mnist (COMPLETE, exit code 0)
Active process or terminal session: NONE
Log path: logs/g5_mnist.log
Last observed progress/time: 2026-10-07 03:02 IST

## Immediate next step
First incomplete gate: G5 Fashion-MNIST sweep
Exact command: `caffeinate -i python run.py --datasets fashion --device cpu --out results_fashion 2>&1 | tee logs/g5_fashion.log`
Expected evidence: 24 completed rate/seed runs, 480 epoch rows in history.csv, final_results.csv (24 rows), summary.csv (8 rows), 24 .pt checkpoints.

## Blockers requiring user interaction
None. All local gates G0–G4 passed with verified evidence; MNIST G5 sweep passed.

## Session handoff
What was completed:
- G5 MNIST: Completed full 24-run sweep on CPU (8 rates × 3 seeds × 20 epochs = 480 epoch rows). All metrics finite, split disjointness verified, 24 checkpoints created, artifacts present.
What changed: Updated PROJECT_STATE.md with MNIST completion; Fashion-MNIST PENDING.
What failed: NONE.
What remains: G5 Fashion-MNIST sweep, G6 (audit), G7 (notebook/README), G8 (report), G9 (slides), G10 (clean package), G11 (submission).
