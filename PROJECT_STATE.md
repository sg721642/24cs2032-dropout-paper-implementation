# 24CS2032 project state
Last updated: 2026-10-07 01:46 IST
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
Verified remote URL / branch / last pushed SHA: https://github.com/sg721642/24cs2032-dropout-paper-implementation / main / 421968ac997b96ea38b11041319b07d1c5f3b69e

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
CPU test: PENDING (G2–G4)
Chosen final backend: PENDING (G4 — device/protocol lock)
Timing observations/estimated duration: PENDING (G2–G4)

## Gate status
G0 context: PASS — roll 24CS2032 identified; master read to END marker (line 1829); workspace and pre-existing state inspected; no unrelated repository overwritten
G1 setup: PASS — arm64 native Python 3.13.9; isolated .venv created; all dependencies installed; run.py/make_notebook.py/verify_results.py compile; ManualDropout present, no built-in dropout; parameter count 335114 verified; PROJECT_STATE.md updated from real observations
G2 core tests: PENDING
G3 smoke pipeline: PENDING
G4 protocol/device lock: PENDING
G5 full experiments: PENDING
G6 results audit: PENDING
G7 notebook/README: PENDING
G8 report: PENDING
G9 presentation: PENDING
G10 clean package: PENDING
G11 repository/course submission: PENDING

## Commands executed in G0–G1 stage
```
pwd && uname -m && sw_vers && ls -la
find /Users/satyamgupta/Documents -maxdepth 3 -type f -print | sort | head -60
find /Users/satyamgupta -maxdepth 4 -name "*24CS2032*Dropout*" -o -name "*Dropout*MASTER*"
wc -l /Users/satyamgupta/Downloads/24CS2032_Dropout_FINAL_MASTER.md
# [read entire master in 4 chunks, lines 1–400, 400–800, 800–1200, 1200–1830]
git rev-parse --show-toplevel 2>/dev/null || true  # NOT_A_GIT_REPO
git status --short --branch 2>/dev/null || true
command -v python3 && python3 --version
python3 -c "import platform,sys; print(sys.executable); print(platform.machine())"
command -v python3.13 && python3.13 --version
python3.13 -m venv /Users/satyamgupta/Documents/24CS2032_Dropout/.venv
source .venv/bin/activate && python --version && python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"
python -m py_compile run.py make_notebook.py verify_results.py
grep -nE 'ManualDropout|nn\.Dropout|functional\.dropout|F\.dropout' run.py
python -c "import run; print(sum(p.numel() for p in run.MLP(0.0, 256).parameters()))"
gh --version && gh auth status && gh api user --jq .login
gh repo view sg721642/24cs2032-dropout-paper-implementation ...
git init -b main
git add .gitignore requirements.txt run.py make_notebook.py verify_results.py README.md 24CS2032_Dropout_FINAL_MASTER.md PROJECT_STATE.md
git commit -m "Initialize manual dropout project and reproducible setup"
gh repo create sg721642/24cs2032-dropout-paper-implementation --private --source=. --remote=origin --push
```

## Pre-existing state found
- Workspace /Users/satyamgupta/Documents/untitled\ folder was empty (fresh folder)
- Master file found at /Users/satyamgupta/Downloads/24CS2032_Dropout_FINAL_MASTER.md (1830 lines)
- No PROJECT_STATE.md pre-existed
- No other project files pre-existed
- /Users/satyamgupta/Documents/24CS2032_Dropout/ created fresh
- No unrelated repository in project folder

## Errors/blockers
NONE encountered in G0–G1.

## Source files created
- /Users/satyamgupta/Documents/24CS2032_Dropout/run.py (extracted from master Section 8, verbatim)
- /Users/satyamgupta/Documents/24CS2032_Dropout/make_notebook.py (extracted from master Section 9, verbatim)
- /Users/satyamgupta/Documents/24CS2032_Dropout/verify_results.py (extracted from master Part III Section K, verbatim)
- /Users/satyamgupta/Documents/24CS2032_Dropout/requirements.txt (from master Section 7.3)
- /Users/satyamgupta/Documents/24CS2032_Dropout/.gitignore (from master Section 7.3, plus .env)
- /Users/satyamgupta/Documents/24CS2032_Dropout/README.md (from master Section 17 template)
- /Users/satyamgupta/Documents/24CS2032_Dropout/24CS2032_Dropout_FINAL_MASTER.md (copied from ~/Downloads/)
No backups or diffs needed — no pre-existing source to compare against.

## Static validation results (G1)
- run.py py_compile: PASS
- make_notebook.py py_compile: PASS
- verify_results.py py_compile: PASS
- ManualDropout found: YES (lines 25, 48, 49, 50, 82, 95, 96, 103 in run.py)
- nn.Dropout found: NO
- functional.dropout / F.dropout found: NO
- Default parameter count: 335114 VERIFIED

## Experiments
MNIST final output folder: NONE
MNIST completed runs: 0/24
Fashion final output folder: NONE
Fashion completed runs: 0/24
Separate exploratory/smoke folders: NONE
Protocol deviations and reason: NONE
Source changes and reason: NONE

## Actual results
Do not fill until CSVs are complete and checked.
Baseline/selected rate/mean error/sample SD: PENDING
Selection based on: mean validation error, fixed final epoch
Negative findings/failure examples: PENDING

## Artifacts and evidence
Source/requirements/notebook paths: /Users/satyamgupta/Documents/24CS2032_Dropout/{run.py,make_notebook.py,verify_results.py,requirements.txt,.gitignore,README.md}
Notebook local execution: NOT VERIFIED
Hosted Colab execution: NOT VERIFIED
Report source/PDF/page count/render check: PENDING
Slides/source/render check: PENDING
Submission ZIP/integrity: PENDING
GitHub URL: PENDING (push in progress)
Course submission receipt: PENDING

## GitHub status
gh version: 2.100.0
Authenticated account: sg721642 (verified via gh api user --jq .login)
Repository: sg721642/24cs2032-dropout-paper-implementation
Visibility: PRIVATE (confirmed via gh repo view)
Push status: VERIFIED
Remote URL: https://github.com/sg721642/24cs2032-dropout-paper-implementation
Branch: main
Local HEAD SHA: 421968ac997b96ea38b11041319b07d1c5f3b69e
Upstream SHA: 421968ac997b96ea38b11041319b07d1c5f3b69e
HEAD == upstream: YES
Commit message: "Initialize manual dropout project and reproducible setup"

## Commands and active process
Exact currently running/last command: gh repo create sg721642/24cs2032-dropout-paper-implementation --private --source=. --remote=origin --push
Active process or terminal session: NONE
Log path: NONE
Last observed progress/time: 2026-10-07 01:46 IST

## Immediate next step
First incomplete gate: G2–G4 (correctness/smoke/device choice)
Exact command: python run.py --self-test --device cpu (then MPS timing and smoke pipeline)
Expected evidence: PASS line from self_test(); smoke CSV/PNG/checkpoint files; device timing; v1 protocol locked.

## Blockers requiring user interaction
None currently. If GitHub 2FA or SSH confirmation is needed for push, user must approve in Terminal.

## Session handoff
What was completed: G0 (workspace inspection, master read to END marker) + G1 (venv, dependencies, file extraction, static validation, GitHub setup initiated)
What changed: Created /Users/satyamgupta/Documents/24CS2032_Dropout/ with all project files; created .venv with torch 2.14.1 / torchvision 0.29.1 / numpy 2.5.3 / pandas 3.0.6 / matplotlib 3.11.2; initialized git; created remote repo sg721642/24cs2032-dropout-paper-implementation (private); pushed initial commit.
What failed and full error/log location: NONE
What remains: G2 (run.py --self-test on CPU and MPS); G3 (smoke pipelines); G4 (device/protocol lock); G5–G11 (experiments through submission)
