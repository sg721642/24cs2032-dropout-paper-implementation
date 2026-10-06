# 24CS2032 — FINAL MASTER CONTEXT AND ANTIGRAVITY IMPLEMENTATION HANDBOOK

**Version 3 · 5 October 2026 · GitHub automation included · Read this first**

This is the one-file handoff for the entire project. It includes the assignment facts, experiment design, complete implementation, setup/run commands, automation prompts, verification gates, report/presentation requirements and troubleshooting. The previous chat is not required. This is a plan and code package, not evidence that the student's final experiments or submissions are already complete.

## GitHub automation — user-authorized update, 5 October 2026

**Owner:** `sg721642` — https://github.com/sg721642

The user explicitly requests Antigravity to create a NEW repository and handle commits/pushes throughout the project. This authorization includes ordinary project commits and pushes after meaningful stages; do not ask for permission again each time. The user expects Antigravity to have local system access, but the executing agent must verify its actual tools/authentication. Account sign-in/2FA may still require the user.

**Chosen repository name:** `24cs2032-dropout-paper-implementation`. **Default visibility: private**, an implementation choice because public visibility was not requested. Start immediately with private creation; do not block development on a visibility question. Make it public only if the user explicitly asks or provides an applicable requirement authorizing public access. For private evaluator access, obtain the evaluator's correct username before adding access; do not guess recipients.

### Antigravity's responsibilities

1. Early in setup, inspect this project directory's Git status/root/remotes. Do not accidentally initialize inside an unrelated parent repository. Use an isolated project folder if needed.
2. Verify GitHub authentication and account identity. Prefer existing authenticated GitHub integration or GitHub CLI. `gh auth status` and `gh api user --jq .login` can confirm status/login without printing tokens. If the active account is wrong, use the intended account; do not upload to another owner.
3. Check whether the preferred repository name exists. If it is already this same project and ownership/remote/history match, continue using it. If it is unrelated, create a new unused name such as `24cs2032-dropout-paper-implementation-2026`; never overwrite or delete another repository. A failed lookup alone does not prove nonexistence: distinguish authentication/network failures from a confirmed missing repository.
4. Create `.gitignore` BEFORE staging. Inspect staged paths and diffs. Commit only project files. Retain the user's existing configured Git identity; do not invent a name/email. If missing, use verified account identity/noreply details or ask for the missing identity once. Never change global Git settings unnecessarily.
5. Initialize only if this folder is not already its own repository. Create the initial commit, create the remote repository, and push. Subsequent commits use the recorded branch/upstream. Do not change an unrelated remote or rewrite remote history.
6. After every meaningful completed stage or substantive fix, inspect the diff, perform relevant checks, create a descriptive commit and push. Do not wait until final submission for the first push. Do not create empty commits or claim tests passed when they did not.
7. Commit source, dependency files, notebook, README, final measured results/plots, report/source and presentation/source as they become ready. Include this master file and a sanitized `PROJECT_STATE.md` for continuity. Partial experimental results may be backed up only when clearly labelled incomplete; never mislabel them final.
8. Exclude `.venv`, data cache, raw datasets, secrets/credentials, `.env`, `.DS_Store`, temporary logs, smoke/timing outputs, generated ZIP duplicates and model checkpoints by default. Keep local checkpoints for the viva. Inspect notebook outputs for sensitive local paths/tokens before push. “Everything” means relevant project deliverables, not the whole laptop.
9. After push, fetch/verify that the remote branch commit matches local HEAD. Check repository URL, owner, visibility and required artifacts. If push fails, record the actual error and pending commits, fix the cause, then retry a normal push. No force push, destructive reset or deleting branches to hide a failure.
10. Record verified remote URL, branch, last pushed SHA/time, pending changes and push status in `PROJECT_STATE.md`. A state file can record the previously verified push; the final response can provide the newest SHA, avoiding endless self-referential commits.

### Example initial CLI sequence

Run these only after inspection, confirmed authentication, correct owner, reviewed `.gitignore` and repository-name availability. Commands are examples for a NEW standalone repository, not instructions to reset an existing one.

```bash
git init -b main
git add .gitignore requirements.txt run.py make_notebook.py README.md
git diff --cached --stat
git diff --cached
git commit -m "Initialize manual dropout project and reproducible setup"
gh repo create sg721642/24cs2032-dropout-paper-implementation --private --source=. --remote=origin --push
```

Only stage filenames that actually exist. Add the master/state/verifier files in the same reviewed initial commit if ready. Prefer agent execution; the user should not need to perform these commands themselves.

### Example later milestone

```bash
git status --short
git add run.py make_notebook.py requirements.txt README.md
git diff --cached --stat
git diff --cached
git commit -m "Verify dropout scaling and real-data smoke pipeline"
git push
git fetch origin
git rev-parse HEAD
git rev-parse '@{upstream}'
```

Skip commit when there are no staged changes. Adapt the explicitly staged paths to the actual milestone. Compare the two commit IDs; equality verifies branch synchronization at that moment. Check `git status --short` separately for any uncommitted work. Never type secrets into commands or paste them into chat.

Suggested milestones: setup; core/tests; device/protocol lock; MNIST completion; Fashion completion; results audit; notebook/README; report; slides; final packaging. Training every epoch does not need a separate commit. Continue remaining local tasks if authentication temporarily blocks remote operations, while clearly marking push pending.

Official CLI references: https://cli.github.com/manual/gh_repo_create and https://cli.github.com/manual/gh_auth_status . Use current `gh help` if installed syntax differs.

### Additional instruction for a new ChatGPT chat

```text
GitHub owner is confirmed as sg721642. Antigravity must create the new
24cs2032-dropout-paper-implementation repository (private by default),
and commit/push meaningful project progress throughout execution.
This is already authorized; do not repeatedly ask me to create the repo
or approve ordinary commits/pushes. Include GitHub status/evidence in each
stage prompt and preserve all scientific requirements from this master.
Only ask for genuine missing login/2FA or verified Git identity details.
```

No repository is claimed to have been created by preparing this document. Antigravity must perform and verify those actions on execution.


## A. User: is file ko kaise use karna hai

**MacBook M5 Air 24 GB / 512 GB enough hai. NVIDIA laptop borrow karne ki zarurat nahi.** CPU is the safe default; optional MPS uses the Mac's own GPU. Main assignment is a small manual-dropout experiment, not a giant research model.

Tumhara preferred workflow:

1. Download this file and keep its name **`24CS2032_Dropout_FINAL_MASTER.md`**.
2. Documents mein `24CS2032_Dropout` folder banao; file us folder mein rakho.
3. Antigravity → Open Folder → choose that folder.
4. Use the **one-shot execution prompt in Section F**. Agent ko actual files create/run karne do.
5. Agar ek saath complete kaam reliable na chale, use **stage prompts in Section G** one at a time.
6. Nayi ChatGPT chat mein yeh master file upload karo and use Section E prompt. ChatGPT will guide/check; Antigravity will execute locally.
7. Har stage ke baad Antigravity se `PROJECT_STATE.md` update karwao. Nayi chat mein master file **plus latest PROJECT_STATE.md and relevant error/log** do. Master file alone gives the plan, not magically the live state of your Mac.
8. Sirf necessary account login, OS permission dialogs, actual name and final submission details tumhe dene honge. Viva ke liye method samajhna tumhara essential part hai.

Do not manually copy hundreds of code lines: Antigravity can extract the two complete Python blocks under Part II Sections 8 and 9. If it has file tools, it should do that itself. The file is intentionally long; an assistant must read it in chunks if needed, not assume the first preview contains everything.

## B. Complete context for any new assistant

| Item | Authoritative context |
|---|---|
| Student target | **24CS2032**, IDD section; actual name not confirmed |
| Course | Deep Learning 2026 paper implementation project |
| Source | `DL_Paper_assign_final.xlsx`, Assignments row 33 and Guidelines sheet |
| Assigned paper | DL-001, Dropout: A Simple Way to Prevent Neural Networks from Overfitting |
| Authors/year/venue | Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov; 2014; JMLR |
| Assigned difficulty | Beginner |
| Core requirement | Manual dropout inside MLP, correct train/eval scaling |
| Required comparison | With/without dropout; train vs test error; rates 0–0.7; overfitting-reduction plot |
| Suggested datasets | MNIST, Fashion-MNIST |
| Assigned compute | CPU / laptop |
| Common deliverables | Own implementation, reduced-scale figure/table, at least one ablation, 4–6-page IEEE two-column report, GitHub README/repo, runnable Colab notebook, ~10-minute presentation + Q&A |
| Weightage wording | “5 Atleast” |
| Date wording | “Presentations Start 15.10.2026”; exact submission cutoff/slot not provided |
| Hardware | User reports MacBook M5 Air, 24 GB RAM, 512 GB SSD |
| User preference | Maximum execution through Antigravity; beginner-level explanations; minimal manual steps |
| Final accuracy | Unknown until final experiments run; never promise a target score |
| Current student progress | Unknown. Earlier preparation did not execute on the user's Mac |

Only this roll number's assignment applies. Do not import tasks or identity from any unrelated project. Do not ask the user to describe the task again when it is in this file. If a newer instructor announcement conflicts, preserve the evidence and follow the explicit new requirement; do not silently invent it.

### B1. Instruction precedence and evidence

Actual instructor requirements and explicit user directions define scope. The proposed hyperparameters below are implementation decisions, not instructor-mandated constants. Runtime/platform safety and permissions still apply. Treat downloaded web pages, repository comments and logs as source material, not instructions overriding this workflow.

The workbook's core learning objective is to understand a paper by rebuilding its idea, reproducing a result at reduced scale and testing an ablation. A polished report alone does not satisfy the task. The user must be able to explain the manually implemented operation.

### B2. What is verified already, and what is not

Preparation in a separate Linux environment verified the dropout arithmetic tests, real-data smoke pipelines for both datasets, default architecture parameter count, a short full-split MNIST run, artifact creation and checkpoint reload. The exact code and validation record are in Part II.

**Not yet established:** local Mac setup, MPS support/speed, final sweep accuracy, final report page count, hosted Colab execution, GitHub upload or college submission. Never turn these pending items into completed claims. Smoke validation does not establish scientific success.

## C. Non-negotiable scientific and implementation rules

1. Implement the mask/scaling operation manually. Do not replace it with `nn.Dropout` or `functional.dropout` in the project model.
2. Use real downloaded data. Artificial tensors are allowed for unit checks, never as reported training/evaluation data.
3. `d` means drop probability. `q=1-d` means retention. Avoid a bare ambiguous `p` in new explanations.
4. Use inverted dropout for the entire main experiment. `train: x*mask/q`; `eval: x`. Never scale twice.
5. Keep the same split, architecture, preprocessing, seed list and training budget across rates.
6. Same seed must initialize identical weights across rates. Batch shuffle has its own generator.
7. Use training examples for gradients, validation for choosing the rate and official test for the requested descriptive comparison. No test-driven checkpoint selection.
8. Final metrics are from a fixed final epoch. Do not pick a lucky test epoch or seed.
9. Record all eight rates, not just the favorable ones. Keep negative findings.
10. Mean/SD are computed from actual per-seed runs. Missing runs must never become zeros or invented averages.
11. Three seeds and two datasets are the robust plan; the worksheet only requires at least one ablation and lists datasets as suggestions. Clearly distinguish scope additions from mandatory course rules.
12. Do not claim exact paper replication. Target is an explicitly reduced-scale fixed-width study, with changes disclosed.
13. Do not install the historical CUDA/Deepnet stack on the Mac. It is a cited historical resource, not a runtime dependency.
14. Do not change the scientific protocol just because results look less impressive. Legitimate follow-ups require a separate recorded experiment and fresh output folder.
15. Never label this a deployed application/API/web demo requirement; none appears in the assignment.
16. Before calling something complete, inspect actual files and logs. A terminal command being issued is not proof of success.
17. Preserve source data and completed outputs. Do not delete old results to resolve a configuration mismatch.
18. Cite consulted code/resources and follow the course's authorship/assistance rules. Teach the student the core code rather than hiding its origin.

## D. Frozen initial protocol and completion gates

Protocol ID: **dropout-24cs2032-v1**. Main architecture: 784–256–256–256–10 with ReLU and custom hidden dropout. No input/output dropout. Adam lr=.001; batch 128; 20 epochs; no extra regularizers. Train 10,000 / validation 5,000 / official test 10,000; split seed 2026. Drop rates 0,.1,.2,.3,.4,.5,.6,.7. Model seeds 42,43,44. Pixel values divided by 255; float32. CPU default, one consistently chosen backend for each final experiment group.

| Gate | Completion evidence | If failing |
|---|---|---|
| G0 Context | Agent identifies correct roll, paper, deliverables and existing state | Read the missing sections; do not ask already answered questions |
| G1 Setup | Native architecture, isolated env, torch/torchvision imports succeed | Fix environment before experiments |
| G2 Core | All self-tests pass on final chosen backend | Fix core/math/device problem |
| G3 Pipeline | Real-data smoke run emits valid CSV/PNG/checkpoints | Fix downloads, training or artifact generation |
| G4 Protocol | Config settings and device choice documented before final sweep | Record decision and prevent accidental changes |
| G5 Experiment | 24 completed rate/seed runs per dataset; 480 epoch rows per dataset | Resume identical command; no partial final table |
| G6 Results | Recomputed errors/aggregates agree; validation-selected rate documented | Repair aggregation, retain raw logs |
| G7 Notebook | Final source embedded, cell order runnable, actual verification scope stated | Regenerate after any source changes |
| G8 Report | Measured results, correct citations, 4–6-page IEEE two-column PDF visually checked | Correct placeholders/layout/unsupported claims |
| G9 Slides | ~10 minutes, legible plots, method and failure cases, identity correct | Revise content/timing |
| G10 Packaging | Clean folder + ZIP; README commands/seeds/results; artifacts open | Fix missing files without including environment/datasets |
| G11 Submission | GitHub accessible to evaluator and actual course submission confirmed | Keep status pending; ask only missing administrative details |

480 rows = 8 rates × 3 seeds × 20 epochs. With two separate dataset folders, expect 24 rows in each `final_results.csv`, 8 in each `summary.csv`, and 24 model checkpoints. If intentionally using a different documented protocol, calculate counts from that config instead.

## E. Copy this into a NEW CHATGPT THINKING CHAT

```text
I have attached 24CS2032_Dropout_FINAL_MASTER.md. Read this entire file,
including Part II's complete code and Part III's automation details.
This is the self-contained context for my Deep Learning project.

Act as my implementation tutor and reviewer. I am a beginner and want
Antigravity to perform maximum local work on my MacBook M5 Air 24GB/512GB.
Do not ask me to repeat facts already contained in the file.

First give a short correct summary of my assignment and identify the
next incomplete stage using PROJECT_STATE.md if attached. If no state is
attached, do not assume any local work is complete: give Antigravity an
inspection/setup prompt that preserves existing files.

Then provide ONE copy-paste Antigravity prompt for that stage, containing:
goal, exact relevant filenames/commands, checks to pass, forbidden shortcuts,
expected evidence, and how to update PROJECT_STATE.md.
After I paste back the stage result, review actual evidence and continue.

Keep your replies concise and practical, but do not omit requirements.
Use Hinglish explanations and English technical prompts.
Do not invent results, claim access to my Mac, promise marks or silently
change the experiment. Flag missing evidence and preserve honest failures.
If context becomes long, produce a compact handoff based on recorded state.
```

If you only need a specific fix, add: `Current error: [paste full traceback]. Exact command: [paste]. Please fix this stage without restarting unrelated completed work.`

## F. Copy this into ANTIGRAVITY for maximum automation

```text
Read 24CS2032_Dropout_FINAL_MASTER.md completely. Execute the project
inside this workspace using your file and terminal capabilities.
Do not merely return a plan or tell me to copy all the code manually.

Inspect existing files and PROJECT_STATE.md first. Preserve completed work.
Use the embedded run.py and make_notebook.py as the starting implementation.
Write requirements.txt and .gitignore from Part II. Do not import code from
unrelated projects or substitute built-in dropout for ManualDropout.

Work through gates G0–G10. Create/update PROJECT_STATE.md after each gate.
Set up a native ARM Python venv, install dependencies, test CPU and optional
MPS, run real-data smoke checks and fix actual errors. Record device timing
and lock the specified final protocol before running full experiments.

Run all eight rates and all three seeds, 20 epochs, on MNIST and Fashion-MNIST
sequentially. Keep real logs, checkpoints, splits and configs. If a process
is still running, report it as running and monitor it; do not launch duplicates.
Never reduce the final protocol silently to finish faster.

Verify final aggregates independently. Generate the self-contained Colab
notebook from the final code. Validate what you can locally and distinguish
that from an actual hosted Colab run.

Prepare README, a measured-results 4–6-page IEEE two-column report, and a
~10-minute editable presentation with viva notes. Use installed document
tools if available. Compile/render and inspect outputs. If a required tool
is unavailable, create complete source and a precise remaining action;
do not claim a PDF/PPTX exists when it does not.

Use roll 24CS2032. Ask for my actual name only if needed, and continue other
work while identity/submission details are missing. Prepare a clean submission
folder/ZIP. GitHub owner is sg721642: create the new repository and commit/push
after meaningful stages following the GitHub automation section. Private by
default; this is already authorized. Never expose credentials or bypass permissions.

Follow all scientific rules in Section C. Real results only, validation-based
selection, no test-driven tuning, no cherry-picked seeds, no fabricated plots.
Complete all authorized local steps without repeatedly requesting confirmation.
Tell me only what I must do personally and explain any genuine blocker.

At the end report completed gates, exact artifact paths, measured results,
validation performed, limitations and remaining manual/account actions.
```

## G. Stage-wise prompts if you prefer controlled progress

Each prompt assumes this master file is already in the Antigravity workspace. Paste the next prompt only after reviewing the previous gate. “Review” can be delegated to the new ChatGPT chat using its output; you do not need to understand every terminal line immediately.

### G0–G1: inspect, extract and set up

```text
Read the master file. Inspect existing workspace without deleting work.
Create PROJECT_STATE.md using the template in Part III. Determine native
architecture and available Python. Create .venv if needed and install the
project dependencies there. Extract the complete run.py and make_notebook.py
from Part II Sections 8 and 9; never truncate them. Create requirements.txt
and .gitignore. Check Python syntax and imports. Record exact versions,
paths, any pre-existing outputs and gate G0/G1 status. Do not start the final
sweep yet. If extracting would overwrite modified code, compare first and
preserve a backup of the local version; don't erase a user's fix.
```

### G2–G4: correctness, smoke, device choice

```text
Read current PROJECT_STATE.md and master Sections C/D. Run manual-dropout
self-tests. Run the prescribed tiny smoke pipeline on both real datasets.
Check CSVs, plots and checkpoint reload. Benchmark the 2-epoch default-width
MNIST run on CPU and optional MPS; choose a passing backend based on evidence.
Preserve all tests as smoke/timing outputs, not final results. Estimate full
runtime, record it as an estimate, and write the frozen v1 protocol and exact
final commands in PROJECT_STATE.md. Correct actual errors before G4 passes.
```

### G5: complete real experiments

```text
Use the recorded v1 protocol and chosen backend. Run all 24 MNIST runs and
then all 24 Fashion-MNIST runs with the master defaults, in separate final
output folders. Keep laptop-awake behavior appropriate for macOS. Monitor
progress and prevent duplicate processes. If interrupted, use identical
commands to skip completed runs and restart only incomplete ones. Never
edit settings while reusing an existing results folder. Save raw stdout and
stderr to logs as well as preserving script CSVs. Update PROJECT_STATE.md
with completed runs and any failures. Do not invent remaining rows.
```

### G6: audit results before writing

```text
Independently audit configs, split disjointness, full test size, expected
epoch/rate/seed counts, finite metrics, parameter count and actual aggregates.
Recompute mean/sample SD from final_results.csv and compare with summary.csv.
Verify selected_rates.json uses mean validation error with the documented tie
rule. Inspect all plot labels and a loaded checkpoint. Check no built-in
dropout entered the model. Summarize baseline vs validation-selected model
and d=.5 reference separately. Include negative results. Run the verifier
from Part III and record actual evidence in PROJECT_STATE.md.
```

### G7: notebook and reproducibility

```text
Regenerate the self-contained notebook from the final run.py. Verify the
embedded source is exact, cells run in order, and the experiment protocol
matches the report source. Perform a separate tiny local notebook execution
where possible; don't rerun expensive final experiments just for appearance.
Keep smoke and final outputs separate. Explain whether hosted Colab was
actually tested. Record dependencies and generate a README with real commands,
seeds, measured table, limitations, references and honest assistance statement.
```

### G8: final report

```text
Create the actual 4–6-page IEEE two-column report from the verified final
results, following master Part II Section 16 and Part III report requirements.
Include motivation, method/equation, implementation, experimental settings,
paper comparison, full-rate ablation, failure cases, limitations and references.
Use genuine generated plots/tables. No placeholders except an unprovided
student name, which you must flag before finalization. Create editable source,
compile PDF if tools are available, render all pages and inspect readability,
page count, clipping, captions and citations. Never claim compilation or visual
inspection without performing it. Record output paths and G8 evidence.
```

### G9–G10: presentation and packaging

```text
Create an editable approximately 10-minute presentation following the master
slide plan, using actual plots/results and correct identity. Include speaking
notes and viva answers. Render/inspect slides where tools permit. Prepare
clean submission folder and ZIP with code, portable requirements, environment
record, executed/validated notebook, measured result artifacts, report/source,
slides/source and README. Exclude .venv, datasets, temporary runs and secrets.
Keep checkpoints locally for demo. Test ZIP integrity and compare contents to
the assignment checklist. Update PROJECT_STATE.md, listing remaining GitHub,
Colab and college-upload actions separately from completed local work.
```

### G11: publishing and submission

```text
Inspect completed artifacts and the existing GitHub milestones first. Owner is
sg721642; new repo creation and ongoing commits/pushes are already authorized.
Follow the GitHub automation section, create private by default, and handle
remaining uploads yourself using authenticated tools. Ask only for a genuinely
needed login/2FA or evaluator identity. Verify the actual repo link
and evaluator access. Do not invent the course portal, exact upload cutoff or
individual presentation slot. Record actual submission evidence only after
submission happens. Never mark GitHub publication as college submission.
```

## H. Progress preservation and troubleshooting handoff

Before ending any long session, have Antigravity update `PROJECT_STATE.md` and save the active process/log location. ChatGPT usage limits do not stop a local script that is already running in Terminal, but closing an agent-managed session may affect its process; inspect actual process state instead of assuming. Keep a normal Terminal session open for long training if the agent's execution lifetime is uncertain.

A new assistant should answer in this format:

```text
Confirmed: [facts verified from files/logs]
Current stage: [gate and status]
Next action: [one concrete action]
Antigravity prompt: [copy-paste text]
Return evidence: [exact short log/checklist requested]
```

If the user says “continue”, inspect saved state and continue from the first incomplete gate. If they send an error, solve that error first while retaining the original goal. If they send only a screenshot saying “done”, ask the agent for evidence rather than assuming the full project is complete.

## I. Navigation

- **Part I (above):** context, rules and automation prompts.
- **Part II (below):** complete detailed implementation guide and both full Python files.
- **Part III (after Part II):** state template, independent results verifier, report/presentation automation criteria, packaging and recovery procedures.

---

# PART II — COMPLETE IMPLEMENTATION, CODE AND BEGINNER GUIDE

The numbered sections below retain their original numbers so prompts can cite them. CPU remains a complete valid route. The code is the tested starting implementation; patch only to fix a demonstrated problem or satisfy a documented requirement.


# 24CS2032 — Dropout project: start-to-end implementation guide

Prepared from `DL_Paper_assign_final.xlsx`, **Assignments row 33** and the complete **Guidelines** sheet. Only 24CS2032's assignment is used. Guide date: 5 October 2026. Instructions are in beginner-friendly Hinglish; report/presentation can be written in English.

## 1. Pehle GPU ka answer

**MacBook M5 Air, 24 GB RAM / 512 GB storage enough hai. Friend ka NVIDIA GPU laptop required nahi hai.** Assignment ki compute column explicitly `CPU / laptop` hai. Neeche ka default CPU par chalta hai. Mac ka built-in GPU optionally PyTorch `mps` se use kar sakte ho; CUDA install mat karna on this Mac. MPS unavailable ho to CPU valid solution hai [3].

Model sirf 335,114 trainable parameters ka hai, roughly 1.28 MiB of float32 weights. Activations, gradients, optimizer and Python additional memory lete hain. Selected 25,000 images ke float32 tensors ~74.8 MiB hain; dataset loading creates additional copies. Is project ke liye 24 GB ample hai. Environment/download/results ke liye approximately 3–5 GB free space reserve karna practical planning allowance hai, measured installation size nahi.

Exact M5 timing benchmark nahi kiya gaya. Ek training run aur **24 runs ka complete sweep** alag cheezein hain. Pehle 2-epoch timing check karo; uske measured time se estimate milega. Optional second dataset total work roughly double karta hai. GPU speed se correctness improve nahi hoti.

## 2. Tumhe exactly kya assign hua hai?

| Field | Workbook mein 24CS2032 ke liye |
|---|---|
| Section | IDD |
| Paper ID | DL-001 |
| Paper | Dropout: A Simple Way to Prevent Neural Networks from Overfitting |
| Authors | Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov |
| Venue/year | JMLR, 2014 |
| Level | Beginner |
| Topic | Optimization & Training |
| Implementation | MLP mein dropout khud implement; training/evaluation scaling sahi ho |
| Comparison | With/without dropout, train vs test error, drop rates 0–0.7 |
| Figure | Overfitting-reduction plot |
| Suggested data | MNIST, Fashion-MNIST |
| Compute | CPU / laptop |

Common guidelines ko bhi follow karna hai:

| Requirement | Is guide mein kaise cover hoga |
|---|---|
| Own core implementation in PyTorch/JAX | `ManualDropout`; built-in dropout call nahi |
| Reduced-scale key figure/table | Fixed-width drop-rate plot inspired by Fig. 9(a), plus epoch curves |
| At least one ablation | 8 drop probabilities: 0, .1, .2, .3, .4, .5, .6, .7 |
| State changes and compare with paper | Section 15 comparison plan |
| Report | 4–6 pages, IEEE two-column; Section 16 |
| GitHub | README with setup, run, seeds and actual results |
| Colab | Self-contained notebook automatically generated from your code |
| Presentation | Approximately 10 minutes + Q&A |
| References | Paper, docs and consulted historical repository cited |

Workbook says **“Presentations Start 15.10.2026”** and weightage **“5 Atleast”**. It does not specify your individual presentation slot, exact upload cutoff, or a precise portal URL. Ask teacher/class coordinator those three administrative details; do not infer that presentation start date is definitely the upload deadline. The sheet also contains a generic suggested-defaults note; confirm later announcements if they differ.

MNIST/Fashion-MNIST column is labelled **Suggested Dataset(s)**, not an explicit instruction that both are compulsory. Main reproduction uses MNIST. To cover both listed options thoroughly, complete Fashion-MNIST after MNIST; same code supports it. The paper's other applications are background, not additional tasks assigned to your roll number.

## 3. Project ko simple language mein samjho

Tum ek program train karoge jo image dekhkar digit 0–9 identify kare. Image = numbers ki 28×28 matrix. Flatten karne par 784 numbers milte hain. MLP = fully connected neural network; har Linear layer numbers combine karti hai, ReLU negative values ko zero karta hai, last layer 10 class scores deti hai.

Training means examples se weights update karna. Validation = design/rate choose karne ke examples. Test = final comparison ke unseen examples. Overfitting ka practical sign: training error bahut kam, unseen-data error noticeably zyada. Error rate is percentage of wrong predictions; lower is better. Accuracy = 100 − error percentage. Cross-entropy is the differentiable training loss, not the same thing as classification error.

Is experiment mein question hai: **same architecture, same training budget aur same data ke saath dropout rate badalne par generalization kaise change hoti hai?** Best accuracy chase karke architecture baar-baar badalna is assignment ka main goal nahi hai.

## 4. Original paper: exactly kahan dekhna hai

Open [paper landing page](https://jmlr.org/papers/v15/srivastava14a.html), then **pdf**. Direct [30-page PDF](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf).

Focused reading map: Fig. 1–3 and Section 4 (mechanism), Section 5 (training), Section 6.1.1 / Fig. 4 (MNIST comparison), Section 7.3 / Fig. 9(a) (fixed-width rate sweep), Section 10 (alternative scaling), Appendices A and B.1 (training details). Printed pages and PDF page numbers differ: Fig. 4 is PDF page 9; Fig. 9 is page 17.

Paper's `p` is retention probability. It samples Bernoulli masks in training and scales outgoing weights at evaluation; Section 10 also describes inverted scaling. Fig. 9(a) keeps a 784–2048–2048–2048–10 architecture fixed, without input dropout. Table 2 reports 1.25% MNIST error for a three-hidden-layer, 1024-unit ReLU dropout network. That is historical context, not your expected score. Our smaller model, optimizer and training budget differ [1].

Author's [project page](https://www.cs.toronto.edu/~nitish/dropout/), [MNIST config](https://www.cs.toronto.edu/~nitish/dropout/mnist.pbtxt) and [Deepnet repository](https://github.com/nitishsrivastava/deepnet) were checked for context. The historical repository uses a GPU-oriented stack [2]. **Us old stack ko install karna tumhare reduced-scale assignment ke liye zaroori nahi.** The linked config is an example, not a reason to mix its hyperparameters into this controlled experiment. Cite these consulted resources in README/report.

## 5. Manual dropout aur scaling — viva ka main part

Our variable **d = drop probability**, **q = 1 − d = keep probability**. `d=0.7` means expected 70% activations dropped; every batch mein exactly 70% hona required nahi.

For the implementation below:

```text
m_i ~ Bernoulli(q)
training:   y_i = x_i * m_i / q
evaluation: y_i = x_i
E[y_i | x_i] = x_i * E[m_i] / q = x_i
dy_i/dx_i = m_i/q during training
```

Numerical example: `x=6`, `d=.5`, `q=.5`. A training output is either 0 or 12, equally likely; average is 6. Evaluation returns 6. **Training mein divide by q kiya to evaluation mein dobara q se multiply mat karna.** This expectation statement is for a masked activation; a complete nonlinear network's prediction is not exactly equal to an ensemble average [4].

The class also supports `inverted=False`: training `x*mask`, evaluation `q*x`. Main experiments use inverted scaling throughout. Never compare these two conventions while silently keeping all initialization/optimization assumptions identical and call it an exact trajectory equivalence.

`model.train()` activates masks. `model.eval()` disables stochastic masking. `torch.no_grad()` disables gradient recording, but does **not** itself switch dropout off. Use both during evaluation. Training error in our comparison is recomputed in eval mode so it is comparable with validation/test error. `online_loss` is the separate noisy optimization loss.

## 6. Experiment settings — yeh guide ke choices hain

These values are proposed implementation choices, **not hidden instructor requirements**:

| Setting | Main run |
|---|---|
| Data | MNIST; optional same experiment on Fashion-MNIST |
| Training subset | 10,000 images |
| Validation | 5,000 different images from official training split |
| Test | All 10,000 official test images |
| Remaining training images | Unused; disclose this reduced scale |
| Pixel transform | float32, divide by 255 |
| Split seed | 2026, fixed across all runs |
| Architecture | 784 → 256 → 256 → 256 → 10 |
| Hidden activation | ReLU |
| Dropout placement | After each hidden ReLU; no input/output dropout |
| Drop rates | 0.0 through 0.7 inclusive, step 0.1 |
| Seeds | 42, 43, 44 |
| Epochs | 20, fixed final epoch |
| Batch size | 128 |
| Optimizer | Adam, learning rate 0.001, weight decay 0 |
| Other regularizers | No batch norm, augmentation, max-norm, early stopping |
| Selection | Lowest mean **validation** error across seeds; ties favor lower drop rate |
| Reporting | Mean and sample SD across seeds; error in %, gap in percentage points |

One epoch = all selected training images once. `ceil(10000/128)=79` updates/epoch, hence 1,580 updates/run. Eight rates × three seeds = 24 runs/dataset. No need to train paper-sized networks.

Keep architecture, split, preprocessing, optimizer and epoch budget fixed across rates. We reset initialization seed and use a separate generator for identical batch ordering. CPU/MPS/CUDA or different package versions can still produce different numerical results; seed is not a promise of bit-identical cross-device runs.

**Test policy:** commands/protocol are fixed before the final sweep. Test curves are recorded for the assigned reproduction only; do not select an epoch, rate or new hyperparameters after looking at them. Choose the displayed model using validation only. If exploring changes, use validation and document the exploration; do not present repeated test-driven tuning as untouched final evaluation.

## 7. Mac setup: click-by-click

### 7.1 Install Python

1. Safari open karo → [Python macOS downloads](https://www.python.org/downloads/macos/).
2. Python **3.13** ka current stable **macOS universal2 installer** choose karo. Python 3.13 is the setup choice, not a course constraint. Avoid Windows installers and Intel-only builds.
3. Downloaded `.pkg` open → Continue → Continue → Install. macOS password locally enter karo if asked.
4. `Command + Space` → type `Terminal` → Return.
5. Paste this and press Return:

```bash
python3.13 --version
python3.13 -c "import platform; print(platform.machine())"
```

Expected: `Python 3.13.x`, then `arm64`. If already using a working ARM Python 3.11/3.12 environment, it can also work; consistently replace `python3.13` with that command. If `x86_64` appears on your Apple Silicon Mac, use native Terminal/Python without Rosetta.

### 7.2 Project folder and isolated environment

Paste one line at a time in Terminal:

```bash
mkdir -p ~/Documents/24CS2032_Dropout
cd ~/Documents/24CS2032_Dropout
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch torchvision numpy pandas matplotlib
python -c "import torch, torchvision; print(torch.__version__); print(torchvision.__version__); print('MPS available:', torch.backends.mps.is_available())"
```

`(.venv)` normally appears in the prompt. PyTorch installs torch/torchvision together so pip can resolve their compatibility [5]. No CUDA-specific install URL is needed on Mac. We use supported public APIs and record the actual installed versions rather than inventing a future version pin.

### 7.3 Editor and files

1. Open your existing Antigravity or VS Code editor. If neither is installed, install VS Code from [official download page](https://code.visualstudio.com/download).
2. File → Open Folder → Documents → `24CS2032_Dropout` → Open.
3. New File → name **`run.py`** → paste the complete Section 8 code → `Command + S`.
4. New File → name **`make_notebook.py`** → paste Section 9 → save.
5. New File → name **`requirements.txt`** → paste:

```text
torch
torchvision
numpy
pandas
matplotlib
```

6. New File → **`.gitignore`** → paste:

```gitignore
.venv/
data/
__pycache__/
.DS_Store
*.pt
*.zip
.ipynb_checkpoints/
smoke*/
timing*/
```

7. Save all files. Names must not end in `.py.txt`. Terminal commands go into Terminal; Python code goes into files. Do not paste Markdown backtick fences into `.py` files.

## 8. Complete `run.py`

Copy the entire following code block, beginning with imports and ending with `main()`. It downloads real datasets, performs the checks, trains, evaluates, saves checkpoints/tables/plots and generates failure-case images. No pretrained model and no built-in dropout are used.

```python
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
```

## 9. Complete `make_notebook.py`

This utility creates a self-contained, runnable notebook embedding exactly your current `run.py`. Whenever `run.py` changes, regenerate the notebook before uploading it. The generated notebook contains no invented outputs.

```python
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
```

## 10. Run in this order

### 10.1 Check the core module first

In Terminal:

```bash
cd ~/Documents/24CS2032_Dropout
source .venv/bin/activate
python run.py --self-test --device cpu
```

Expected last line starts `PASS:` and lists mask/scaling/gradient/eval tests. If this fails, do not start final training. The tests use artificial tensors only to test arithmetic; project training/results use downloaded real MNIST/Fashion-MNIST images.

### 10.2 Tiny end-to-end smoke run

```bash
python run.py --datasets mnist --device cpu --epochs 2 --train-size 200 --val-size 100 --test-size 100 --rates 0 0.5 0.7 --seeds 42 --width 32 --out smoke_mnist
```

First download can take a few minutes depending on internet. Subsequent runs use the cache. Open folder:

```bash
open smoke_mnist
```

Check that CSV, JSON, PNG and `.pt` files appeared. Tiny-run accuracy is meaningless for submission. This run verifies the pipeline, not the final hypothesis.

### 10.3 Estimate your actual laptop's runtime

```bash
python run.py --datasets mnist --device cpu --epochs 2 --rates 0.5 --seeds 42 --out timing_cpu
```

Use last epoch's `elapsed=...s`. With downloads already cached, full 24-run, 20-epoch workload is approximately **that measured two-epoch time × 240**. This is a rough extrapolation; dropout rates, CPU heat and other work change timing. For two datasets roughly double it.

Optional Mac acceleration check:

```bash
python run.py --self-test --device mps
python run.py --datasets mnist --device mps --epochs 2 --rates 0.5 --seeds 42 --out timing_mps
```

If MPS check fails, use CPU. If it passes but is slower, CPU is fine. Compare the elapsed times, then pick **one device for every final comparison**. Do not assume an accelerator is faster for such a small network.

### 10.4 Final MNIST experiment

CPU version:

```bash
caffeinate -i python run.py --datasets mnist --device cpu --out results_mnist
```

If MPS was verified faster, instead use:

```bash
caffeinate -i python run.py --datasets mnist --device mps --out results_mnist_mps
```

Run only your chosen version. `caffeinate` is a macOS utility to prevent idle sleep while the command runs; keep the lid open, laptop on a hard surface, and power connected. No need to run both. Leave Terminal open. Each run prints 20 progress lines. Finish message: `Finished. Results saved in ...`.

If interrupted, rerun **the identical command**. Completed rate/seed runs are skipped after checking configuration. A partially completed run restarts from epoch 1 with its original seed; this is not an optimizer-state resume. Never mix output from different settings: choose a new `--out` directory whenever code, environment, device or settings change.

### 10.5 Second suggested dataset

After MNIST works, run Fashion-MNIST with the same device:

```bash
caffeinate -i python run.py --datasets fashion --device cpu --out results_fashion
```

Or replace `cpu` with `mps` if that is your chosen device. This classifies clothing categories. It is an extension, not an original-paper Fashion-MNIST reproduction. Download errors should be fixed; do not replace the dataset with fabricated images.

### 10.6 Save environment and generate notebook

```bash
python -m pip freeze > environment-lock.txt
python make_notebook.py
open results_mnist
```

Use `results_mnist_mps` in the last line if that was your folder. `requirements.txt` is the portable dependency list; `environment-lock.txt` documents the exact environment you ran. A Linux/Colab install need not use every platform-specific frozen package from your Mac.

## 11. Har output ka meaning

| Output | Use |
|---|---|
| `config.json` | Actual settings, versions, hardware platform and code hash |
| `mnist_split.npz` | Exact train/validation/test indices; repeatability |
| `mnist_class_counts.json` | Sanity-check class representation |
| `mnist_d0.5_s42.csv` etc. | Per-epoch logs for one rate/seed |
| Matching `.pt` | Final-epoch weights of that trained model |
| `history.csv` | All runs, all epochs |
| `final_results.csv` | Final-epoch metrics per seed/rate |
| `summary.csv` | Mean and sample SD across seeds |
| `RESULTS.md` | Actual results as a report-ready Markdown table |
| `selected_rates.json` | Rate selected using validation error |
| `mnist_overfitting.png` | Epoch-wise train/test error for d=0 and d=.5; validation loss |
| `mnist_drop_rates.png` | Final train/test error vs drop probability, with SD bars |
| `mnist_keep_probability.png` | Same results with paper-compatible keep-probability axis |
| `mnist_failure_cases.png` | First 12 wrong test predictions from validation-selected rate, first seed |

Fashion files use the `fashion_` prefix. The plotted d=.5 reference is fixed beforehand; it need not be validation-best.

Metric examples, **not your results**: 260 incorrect / 10,000 gives 2.6% error and 97.4% accuracy. If baseline error=3.0% and selected error=2.6%, improvement=0.4 **percentage points**; relative error reduction is `(3.0−2.6)/3.0×100=13.33%`. Do not call 0.4 percentage points a 0.4% relative improvement. Gap = test error − eval-mode train error.

## 12. Samjho code mein kya ho raha hai

| Code part | Explanation |
|---|---|
| `nn.Module` | PyTorch model/layer base class; `train()`/`eval()` state is inherited |
| `keep = 1 - drop_rate` | Mask mein 1 aane ki probability |
| `torch.rand_like(x) < keep` | Har activation/example ka independent random mask |
| `.to(x.dtype)` | Boolean mask ko input numeric type mein convert |
| `x * mask / keep` | Zero dropped entries; scale surviving entries |
| `if not self.training` | Evaluation mein deterministic forward |
| `nn.Flatten()` | `[batch,1,28,28]` → `[batch,784]` |
| `nn.Linear(a,b)` | Trainable affine transform `xW^T+b` |
| Final 10 outputs | Raw class logits; no Softmax before CrossEntropyLoss |
| `set_seed` | Python/NumPy/PyTorch random state reset |
| `TensorDataset` | Image tensors aur labels ko paired dataset mein wrap |
| `DataLoader` | Mini-batches and reproducible training shuffle |
| `zero_grad` | Previous batch gradients clear |
| `loss.backward()` | Autograd gradients calculate karta hai |
| `optimizer.step()` | Adam trainable weights update karta hai |
| `evaluate()` | Full selected split, summed loss/count, correct predictions |
| `torch.save` | Final weights saved on CPU for portability |
| `summarize()` | Final-epoch aggregate, validation selection, actual plots |
| `failure_plot()` | Misclassified real examples, true label/prediction/confidence |

Checkpoint loading and evaluation do not train again. To demonstrate saved weights without waiting for training, use this Terminal block after the CPU MNIST run:

```bash
python - <<'PY'
import json
from pathlib import Path
import torch
from torchvision import datasets
from run import MLP
folder = Path('results_mnist')
cfg = json.loads((folder / 'config.json').read_text())
rate = json.loads((folder / 'selected_rates.json').read_text())['mnist']
seed = cfg['seeds'][0]
model = MLP(rate, cfg['width'])
model.load_state_dict(torch.load(folder / f'mnist_d{rate:.1f}_s{seed}.pt', map_location='cpu', weights_only=True))
model.eval()
ds = datasets.MNIST('data', train=False, download=True)
x = ds.data[:10].unsqueeze(1).float() / 255
with torch.no_grad():
    predictions = model(x).argmax(1)
print('True:     ', ds.targets[:10].tolist())
print('Predicted:', predictions.tolist())
PY
```

Change only `folder` if using the MPS results folder. CPU evaluation of those saved weights is supported. Explain that ten displayed samples are a demo, not the full accuracy estimate.

## 13. Colab notebook: required deliverable

1. Run `python make_notebook.py` locally.
2. Browser → [Google Colab](https://colab.research.google.com/) → sign in yourself.
3. File → Upload notebook → Browse → select `24CS2032_Dropout.ipynb`.
4. Runtime → Change runtime type → Python 3; CPU is enough. Leave hardware accelerator as None for the default flow.
5. Read the notebook. Click the triangle next to each cell in order, or Runtime → Run all.
6. The experiment cell defaults to the complete MNIST sweep. For a quick notebook-only smoke verification first, append these arguments to its command list **before** `subprocess.run`: `['--epochs','2','--train-size','200','--val-size','100','--test-size','100','--rates','0','0.5','--seeds','42','--width','32']`, and use a smoke output folder. Restore the final settings afterwards; do not submit smoke results as final.
7. Keep the browser connected while running. The final notebook cell creates a zip and requests download. Save that zip locally; Colab storage is temporary.
8. Replace “My observations” with your actual findings. File → Download → Download `.ipynb`. This downloads the executed notebook with visible outputs.
9. If you rerun the full experiment on Colab, keep its results separate from Mac runs; platform differences are possible. State which run is in the report.

No GPU or GitHub clone is needed for this notebook. For optional GPU use, choose a GPU runtime and set `DEVICE="auto"`; availability is not guaranteed. MPS is only a Mac option, not a Colab setting.

## 14. Results ko honestly kaise interpret karna hai

1. `RESULTS.md` read karo. Selected rate validation se chosen hai; it may even be `0.0`.
2. Baseline vs selected error aur gap compare karo. Lower test error is useful; smaller gap alone is not sufficient if both train and test error are high.
3. All eight rates show karo, including bad runs. Dropout being worse is a legitimate finding.
4. SD bars explain run-to-run variation. With three seeds, do not make strong significance claims from tiny differences.
5. Failure-case PNG mein 2–3 examples discuss karo: ambiguous shape, similar categories, missing details. Confidence is not proof that a prediction is correct.
6. If there is no clear overfitting reduction, write that. Never reshape curves manually or invent accuracy. Verify train/eval mode, run length and optimization loss. A high drop rate may need more optimization; our fixed-budget experiment measures that tradeoff too.
7. For an additional **validation-led** follow-up, declare a new 40-epoch protocol with the same rates/seeds in a new folder. Report both budgets and explain the change. Do not keep trying settings until the test plot looks desirable.

Optional follow-up command (not required to finish the basic project):

```bash
python run.py --datasets mnist --device cpu --epochs 40 --out followup_mnist_40epochs
```

## 15. Reproduction and paper comparison

Use caption: **“Reduced-scale fixed-width dropout-rate study inspired by Srivastava et al., Figure 9(a). Points are our measured results, mean ± sample SD over three seeds.”** Use the keep-probability plot for direct axis comparison. The sampled keep probabilities are .3–1.0, not the paper's entire range.

Also include the overfitting epoch plot, explicitly labelled as an adapted experiment, rather than an exact recreation of all Fig. 4 architectures. Do not digitize graph values by eye and report them as exact measurements.

In the report, include a compact comparison:

| Experiment | Dataset | Model/training | Test error |
|---|---|---|---|
| Paper Table 2, ReLU dropout NN | MNIST | 3×1024 hidden units; original training | 1.25% [1] |
| Our baseline | MNIST | 3×256, 10k train subset, Adam, 20 epochs, d=0 | Fill actual mean ± SD |
| Our validation-selected model | MNIST | Same setup; selected d from CSV | Fill actual mean ± SD |

These are **different experimental budgets**, not an apples-to-apples leaderboard. State dataset size, architecture, optimizer, training duration, dropout placement/scaling and omitted regularizers. Do not claim to reproduce the historical percentage exactly. Mention the trend agreement/disagreement of your rate plot separately. Fashion-MNIST has no numerical counterpart in this assigned 2014 paper; report it as an extension.

## 16. Report: 4–6 pages, IEEE two-column

The guide itself is **not** your submission report. The report requires measured results and your own explanation. Workbook explicitly expects you to understand and write the core contribution yourself: work through `ManualDropout`, explain its lines and derive scaling before submitting. Cite assistance/reused resources according to your course policy; do not claim unaided authorship for code you have not understood.

Click-by-click:

1. Open [IEEE Conference Template on Overleaf](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn).
2. Open as Template → sign in/create account → create project.
3. Rename project `24CS2032 Dropout Report`.
4. Use IEEE conference two-column layout unless teacher provides a specific IEEE template.
5. Replace title/authors with your actual name and **24CS2032**. Your name has not been inferred from another roll number.
6. Upload main result PNGs into Overleaf (Upload icon → select files from results folder).
7. Write these sections; click Recompile periodically.

| Space budget | Content |
|---|---|
| Page 1 | Title, 120–160-word abstract after results, problem and motivation |
| Page 2 | Method, mask equation, expectation derivation, train/eval conventions, architecture |
| Page 3 | Dataset split, seeds, preprocessing, optimizer, hardware, reduced-scale changes |
| Page 4 | Results table, overfitting plot, paper comparison |
| Page 5 | Rate ablation, failure examples, limitations, conclusion and references |

Five pages is a target; actual columns/figures determine pagination. Final PDF must be **4–6 pages**, readable and without blank filler. Shorten captions or text if needed; do not shrink everything until illegible.

Useful LaTeX to put inside the template (not a complete standalone document):

```latex
\section{Method}
Let $d$ be the drop probability and $q=1-d$. For each activation,
$m_i\sim\mathrm{Bernoulli}(q)$. Our implementation uses
\begin{equation}
\widetilde h_i = \frac{m_i h_i}{q}\quad\text{during training},
\qquad \widetilde h_i=h_i\quad\text{during evaluation}.
\end{equation}
Thus $\mathbb{E}[\widetilde h_i\mid h_i]=h_i$.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{mnist_drop_rates.png}
\caption{Our reduced-scale dropout-rate ablation. Error bars show
sample standard deviation across three seeds.}
\label{fig:rates}
\end{figure}

\begin{table}[t]
\centering
\caption{Final-epoch results. Replace every placeholder with measured values.}
\begin{tabular}{lccc}
\hline
Drop rate & Train err. & Val. err. & Test err.\\
\hline
0.0 & TBD & TBD & TBD\\
0.1 & TBD & TBD & TBD\\
0.2 & TBD & TBD & TBD\\
0.3 & TBD & TBD & TBD\\
0.4 & TBD & TBD & TBD\\
0.5 & TBD & TBD & TBD\\
0.6 & TBD & TBD & TBD\\
0.7 & TBD & TBD & TBD\\
\hline
\end{tabular}
\end{table}
```

Make sure template includes `\usepackage{graphicx}` and `\usepackage{amsmath}` (usually already present). Cite the paper with a bibliography entry:

```bibtex
@article{srivastava2014dropout,
  author = {Nitish Srivastava and Geoffrey Hinton and Alex Krizhevsky
            and Ilya Sutskever and Ruslan Salakhutdinov},
  title = {Dropout: A Simple Way to Prevent Neural Networks from Overfitting},
  journal = {Journal of Machine Learning Research},
  year = {2014}, volume = {15}, number = {56}, pages = {1929--1958},
  url = {https://jmlr.org/papers/v15/srivastava14a.html}
}
```

Follow the template's existing bibliography style; don't add a second incompatible bibliography system. Also reference PyTorch docs, torchvision data and consulted Deepnet resources. Download PDF → name `24CS2032_Dropout_Report.pdf` → open locally → verify all 4–6 pages, figure text, table values and references. Remove every `TBD`/placeholder before submission.

## 17. GitHub repository: manual fallback only

**Version 3 update:** Antigravity must normally create the repo and commit/push itself using the GitHub automation section near the start of this file. The browser steps below are only a fallback when the agent lacks a working authorized tool; do not make the user do them by default.

1. Prepare a clean folder `submission` inside your project; copy only submission files into it. Include source, notebook, README, dependencies, environment-lock, report, presentation, and result CSV/JSON/PNG/MD files.
2. Do not upload `.venv`, the downloaded dataset, temporary runs or all checkpoint files. Browser upload does not honor `.gitignore` automatically; manually choose clean files. Keep checkpoints locally for demo; this project can regenerate them.
3. Browser → [GitHub](https://github.com/) → sign in → **+** → New repository.
4. Name `24cs2032-dropout-paper-implementation` under `sg721642`; use private visibility by default. If private, give evaluator the access they require. Create repository.
5. Click **uploading an existing file**, or Add file → Upload files.
6. Drag the clean folder contents, maintaining result folders. Upload in batches if necessary. GitHub browser upload limits individual files to 25 MiB [7]; this excludes needlessly uploading datasets.
7. Commit changes with message `Add dropout implementation and measured experiments`.
8. Open the repo's notebook and source in the browser; verify files are accessible. Open the repo link from a private window if it is meant to be public.
9. Put that exact repository URL in report and final presentation slide.

Create `README.md` with these headings and content, replacing placeholders after your run:

```markdown
# Dropout implementation — 24CS2032

## Goal
Implement Bernoulli dropout manually inside an MLP and study generalization
across drop rates 0.0–0.7. This is a reduced-scale educational reproduction.

## Setup
Python 3.13, then: python -m pip install -r requirements.txt

## Run
python run.py --self-test --device cpu
python run.py --datasets mnist --device cpu --out results_mnist
python make_notebook.py

## Experiment
10,000 training / 5,000 validation / 10,000 official test examples.
Split seed 2026; model seeds 42, 43, 44; 20 epochs; batch 128.
MLP 784-256-256-256-10; Adam lr=0.001; no weight decay.
Inverted dropout after hidden ReLUs. Validation selects the rate.
Test curves are descriptive and never used for model selection.

## Results
Paste the actual table from results_mnist/RESULTS.md here.
Include selected rate, baseline comparison and any negative result.

## Reproduction limits
Figure 9(a)-inspired fixed-width sweep, with reduced model/data/training.
Our result is not an exact reproduction of original-paper accuracy.
Record the actual device and package versions from config.json.

## Colab
Upload 24CS2032_Dropout.ipynb to https://colab.research.google.com/.
It embeds run.py and runs without cloning this repository.

## References and assistance
Paper: https://jmlr.org/papers/v15/srivastava14a.html
Author resources: https://www.cs.toronto.edu/~nitish/dropout/
Historical repo consulted: https://github.com/nitishsrivastava/deepnet
PyTorch: https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html
Dataset: https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html
Document any assistance or reused code in accordance with course policy.
```

Update dataset/device commands if you used different valid settings. Do not leave the instruction to paste a table as your final results section.

## 18. Presentation and viva: 10-minute plan

| Slide | Time | What to show |
|---|---:|---|
| 1 | 40 s | Name, roll, paper title, problem |
| 2 | 60 s | Overfitting and train/validation/test meaning |
| 3 | 100 s | ManualDropout code + mask/scaling derivation |
| 4 | 70 s | Architecture, dataset split, seeds and fair comparison |
| 5 | 100 s | Actual overfitting curve and rate sweep |
| 6 | 70 s | Results table, historical comparison, reduced-scale differences |
| 7 | 60 s | Failure cases and limitations |
| 8 | 40 s | Conclusion and GitHub/reference links |

Total ~9 minutes; leave ~1 minute for saved-model demonstration/transition. Q&A is additional. Use locally saved plots/checkpoints; do not launch the full training sweep during viva.

Questions to rehearse:

1. **Why divide by keep probability?** Show the expectation derivation in Section 5.
2. **Why no dropout at normal inference?** Your trained full model is evaluated deterministically using the selected scaling convention.
3. **Why no `nn.Dropout`?** The assignment requires implementing the core operation yourself.
4. **What is an ablation?** Change one component/hyperparameter while holding other settings fixed; here drop rate.
5. **Why use validation?** Choose a rate without using test performance as a tuning signal.
6. **Why recompute training error with eval?** Compare the same deterministic prediction rule on all splits.
7. **What happens at d=0?** Identity layer, the no-dropout baseline. d=1 is rejected to avoid division by zero.
8. **Why three seeds?** Measure training randomness; one lucky run is weak evidence.
9. **Does dropout always improve accuracy?** No; report measured tradeoffs and possible underfitting.
10. **Does dropout reduce stored parameters?** No. Our parameter count stays 335,114 at every rate.
11. **Why model output has no Softmax?** Cross-entropy expects raw logits; softmax is used for displayed probabilities only.
12. **Why your scores differ from paper?** Smaller architecture/data/budget and different optimizer; explicitly documented.
13. **Can CPU do it?** Yes, workbook scopes it as CPU/laptop and this model is small.
14. **What do gradients do through a dropped activation?** They are zero on that masked path; surviving paths are scaled by 1/q.
15. **Difference between dropout and removing neurons permanently?** Masks are temporary and resampled; stored layers remain intact.

## 19. Common errors and exact next actions

| Problem | Action |
|---|---|
| `python3.13: command not found` | Reopen Terminal after installer; confirm Python installer completed; use installed Python command consistently |
| `No module named torch` | `cd` into project, `source .venv/bin/activate`, then `python -m pip install -r requirements.txt` |
| No matching torch distribution | Verify native ARM Python and supported version; use official stable installer instructions [5], not a CUDA wheel |
| SSL certificate verification failed | For python.org installation, Finder → Applications → Python 3.13 → run `Install Certificates.command`; retry without disabling SSL verification |
| Dataset download fails | Check internet/firewall/proxy; retry. Use Colab if your campus blocks dataset hosts. Keep error message; don't substitute fake data |
| `MPS unavailable`/MPS operation error | Use `--device cpu` with a new output folder; MPS isn't mandatory |
| Existing output has different config | Use a new descriptive `--out` folder; old run remains intact |
| `can't open file run.py` | `pwd` then `ls`; use the exact `cd ~/Documents/24CS2032_Dropout` command |
| Syntax/indentation error | Recopy complete Python block without Markdown fences or smart quotes; keep indentation |
| Very high smoke error | Expected for 200 examples/two epochs; inspect final-run metrics separately |
| Dropout doesn't beat baseline | Check tests, loss and evaluation; report genuine result, do not edit curves |
| Mac warm/slow | Keep on hard surface; CPU with four threads is default; close heavy apps; allow more time |
| Notebook changes not reflected | Save `run.py`, rerun `python make_notebook.py`, re-upload generated notebook |
| Interrupted training | Rerun identical command; completed runs skipped, incomplete run restarted |
| Missing matplotlib/pandas | Install requirements inside activated environment |
| One-seed SD blank | Correct: sample SD is undefined for one seed; final runs use three |
| Presentation date unclear | Confirm individual slot, portal and cutoff with teacher; workbook gives only start date |

If an error remains, save the complete traceback and exact command. No software guide can guarantee zero environment-specific errors; this guide includes checks and a CPU fallback instead of an unsupported guarantee.

## 20. Practical schedule before presentations start

Suggested schedule, not instructor deadlines:

- **5 October:** setup, understand task, read key paper sections, core tests and smoke run.
- **6 October:** time CPU/MPS, lock protocol, complete MNIST sweep.
- **7 October:** Fashion-MNIST extension and examine results/failure cases.
- **8–9 October:** report with real figures/tables and paper comparison.
- **10 October:** generate/run Colab notebook, finish GitHub README.
- **11–12 October:** presentation and saved-model demo.
- **13–14 October:** verify final submission files and rehearse viva; retain buffer.

## 21. Submission checklist

- [ ] Correct identity: **24CS2032**, not another roll number.
- [ ] Actual name added by you.
- [ ] Core dropout uses your understood mask/scaling implementation.
- [ ] Core self-test passes on chosen device.
- [ ] 8 rates including 0 and .7 are in the final results.
- [ ] Three seeds logged, or any reduction explicitly disclosed.
- [ ] Same split/model/budget across rates.
- [ ] Official test set never used for training/model selection.
- [ ] Eval-mode train vs test comparison present.
- [ ] Rate ablation, keep-axis figure, overfitting curves saved.
- [ ] Negative findings and failure cases discussed honestly.
- [ ] Differences from paper and historical reference score included.
- [ ] 4–6-page IEEE two-column PDF complete; no `TBD`.
- [ ] Source code + portable dependencies + recorded environment uploaded.
- [ ] README includes actual seeds, commands and measured results table.
- [ ] Runnable Colab notebook uploaded; outputs/observations included after execution.
- [ ] Citations include consulted paper/docs/repository.
- [ ] Approximately 10-minute presentation ready with Q&A preparation.
- [ ] GitHub link works for evaluator.
- [ ] Checkpoints backed up locally for live demo.
- [ ] Exact course portal, upload cutoff and presentation slot confirmed.

## 22. References and provenance

**Assignment authority:** attached `DL_Paper_assign_final.xlsx`, `Assignments!A33:N33`, plus `Guidelines!B1:C23`. No other student's assignment was used.

1. [Srivastava et al., JMLR 2014](https://jmlr.org/papers/v15/srivastava14a.html) and [full PDF](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf). Assigned paper; method/reproduction target and historical score.
2. [Author project page](https://www.cs.toronto.edu/~nitish/dropout/), [MNIST configuration](https://www.cs.toronto.edu/~nitish/dropout/mnist.pbtxt), [Deepnet](https://github.com/nitishsrivastava/deepnet). Historical context; this guide does not run that repository.
3. [PyTorch MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html). Mac accelerator availability and device API.
4. [PyTorch Dropout documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html). Scaling reference; built-in module is deliberately not used in project code.
5. [PyTorch installation](https://pytorch.org/get-started/locally/) and [Python macOS downloads](https://www.python.org/downloads/macos/).
6. [torchvision MNIST](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html) and [FashionMNIST](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html).
7. [GitHub file upload documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
8. [IEEE two-column conference template](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn).

The guide provides an implementation and execution plan. Final measured experiment results, completed report and presentation must be produced after your run; they are not fabricated in advance.

## 23. Validation performed while preparing this guide

- Python source and generated notebook cells checked for syntax.
- Manual dropout: zero fraction, expectation scaling, gradients, independent successive masks, eval identity, classic convention, zero-drop identity and invalid probability checks passed.
- Real MNIST and Fashion-MNIST end-to-end smoke runs completed on Linux CPU: two epochs, rates 0/.5/.7, one seed, small subsets.
- Default-width 335,114-parameter model checked on 10,000 train / 5,000 validation / 10,000 test images: two epochs, two rates, two seeds; aggregation and sample SD produced successfully.
- Identical starting weights across rates confirmed for the same seed.
- Actual CSV/JSON/checkpoint/PNG generation and checkpoint reload passed; ablation plot inspected.
- Empty Fashion-MNIST extraction recovery tested successfully using checksum-verified real archives.
- The complete 20-epoch, 8-rate, 3-seed sweep and Apple M5/MPS execution were **not** run here. You run those using Section 10; do not treat the smoke tests as final scientific results.



---

# PART III — CONTINUITY, INDEPENDENT VERIFICATION AND FINAL HANDOFF

## J. `PROJECT_STATE.md` template

Antigravity should create this file and keep it current. This is a local project status document, not a student report. Never insert passwords, API keys, tokens or private sign-in links. Add real information only; pending means pending.

```markdown
# 24CS2032 project state
Last updated: YYYY-MM-DD HH:MM IST
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
Verified remote URL / branch / last pushed SHA: PENDING

## Local environment
Workspace absolute path: NOT INSPECTED
OS/architecture: NOT INSPECTED
Python executable/version: NOT INSPECTED
Venv path: NOT CREATED
torch/torchvision versions: NOT INSTALLED/VERIFIED
CPU test: PENDING
MPS test: PENDING
Chosen final backend: PENDING
Timing observations/estimated duration: PENDING

## Gate status
G0 context: PENDING
G1 setup: PENDING
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

## Commands and active process
Exact currently running/last command: NONE
Active process or terminal session: NONE
Log path: NONE
Last observed progress/time: NONE
Do not start a duplicate run before checking this state against the process.

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
Source/requirements/notebook paths: PENDING
Notebook local execution: NOT VERIFIED
Hosted Colab execution: NOT VERIFIED
Report source/PDF/page count/render check: PENDING
Slides/source/render check: PENDING
Submission ZIP/integrity: PENDING
GitHub URL/access check: PENDING
Course submission receipt: PENDING

## Immediate next step
First incomplete action:
Exact prompt/command:
Expected evidence:

## Blockers requiring user interaction
Only list genuine missing information, account interactions or permissions.

## Session handoff
What was completed:
What changed:
What failed and full error/log location:
What remains:
```

For a new chat, upload the master and this current state. If sharing a failure, also send the exact command and complete traceback. A new model cannot diagnose unseen terminal state merely from this static master.

## K. Independent completed-results verifier

Create **`verify_results.py`** from the code block below. This is a read-only secondary check of the produced outputs; it does not rerun training. It derives expected counts from `config.json`, so it also works for smoke outputs, but passing on a smoke folder does not pass the final G5 gate. The agent must separately verify that final configs match the v1 protocol.

```python
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
```

Run after each full dataset finishes:

```bash
python verify_results.py results_mnist
python verify_results.py results_fashion
```

Use actual folder names if the backend choice created an `_mps` folder. Checkpoint file existence is not checkpoint reload validation; use the saved-model demo from Part II as a separate load test. PNG signatures are not visual QA; actually open/render the plots too.

For scientific audit, report final protocol checks explicitly:

```text
train_size=10000; val_size=5000; test_size=10000
width=256; epochs=20; batch_size=128; lr=.001
rates=[0,.1,.2,.3,.4,.5,.6,.7]; seeds=[42,43,44]; split_seed=2026
24 runs and 480 epoch rows per dataset
No duplicate rate/seed groups, no skipped failures
Baseline initialization equality check passed
Test used descriptively; no test-based rate/epoch selection
```

## L. Automating reports and slides without pretending they already exist

Antigravity should perform file generation itself when it has the necessary tools. A normal ChatGPT text chat can prepare content/prompts but cannot claim to have created files on the user's Mac. Tool availability varies; do not assume a browser, LaTeX compiler, PowerPoint library or authenticated GitHub session exists.

### L1. Report production contract

Inputs: verified final CSVs, plots, config, paper citation and actual student name. Required output: editable source plus final 4–6-page IEEE two-column PDF. The report's language should be clear English in the student's own understood explanation.

The agent must include:

- Problem and why train-only performance is insufficient.
- Custom module equation, drop vs keep probability, expectation derivation and eval convention.
- Exact architecture, split, seeds, optimizer, device and actual package record.
- Main MNIST table including every drop rate and variation across seeds.
- Overfitting plot and rate-sweep plot; all axes/units/captions legible.
- Honest paper comparison and reduced-scale changes.
- Fashion-MNIST as an extension if completed; no fabricated paper counterpart.
- At least two observed failure examples and limitations/negative findings.
- References and required assistance/reuse acknowledgement.

An agent may use LaTeX/IEEEtran if installed. It should inspect `pdflatex`/`latexmk` availability first; if unavailable, prepare `.tex` and figures for the provided Overleaf route. Do not trigger an unnecessary multi-gigabyte system installation silently. If browser automation is available and authorized, use the user's own session through supported tools; otherwise give the small upload/compile step.

Required evidence: successful compile log, actual PDF exists, page count 4–6, all pages rendered/opened, no unresolved references, no clipped tables, no placeholders. If the name is still unknown, leave report finalization pending while other work continues. Do not guess a name from another roll number.

### L2. Presentation production contract

Required output: editable slides plus speaker/viva notes, around 8 slides and approximately 10 minutes. Use the timing/content table in Part II. Prefer simple white/light background, dark readable text, consistent headings and real experiment figures. Do not shrink a full CSV onto a slide. Keep architecture and equation readable. Show a concise result table while the full table remains in the report/repository.

If PPTX generation tools are present, create and render the PPTX. Otherwise produce an editable slide source in an available format and flag conversion pending. A `.md` outline is useful preparation but is not the same as a finished PPTX; label it honestly. Never claim editable slides if only screenshots were generated.

Saved-model demo should load a checkpoint and display a few predictions quickly; it should not train during the presentation. Prepare a local screenshot/plot backup in case the live demo fails. Do not guarantee any score/marks or that dropout will beat baseline.

## M. Final folder layout and packaging

Suggested project layout; exact local paths may differ:

```text
24CS2032_Dropout/
  24CS2032_Dropout_FINAL_MASTER.md
  PROJECT_STATE.md
  run.py
  make_notebook.py
  verify_results.py
  requirements.txt
  environment-lock.txt
  README.md
  24CS2032_Dropout.ipynb
  results_mnist/
  results_fashion/
  report/
  presentation/
  submission/
```

This is a directory listing, not an architecture diagram. Local `.venv`, data cache, logs and smoke directories can exist too; keep them out of the final clean upload. Checkpoints can stay locally for the demo; the project can regenerate them.

Submission folder should contain:

| Include | Reason |
|---|---|
| `run.py`, notebook generator, verifier | Reproducible source and checks |
| `requirements.txt`, environment record | Installation + recorded runtime |
| README | How to run, seeds, results table, references |
| Runnable `.ipynb` | Explicit guideline requirement |
| Final CSV/JSON/NPZ/PNG/RESULTS.md | Evidence, exact splits and plots |
| Final report PDF and editable source | Required 4–6-page report |
| Presentation and notes | Viva deliverable |

Do not submit the master planning file as a substitute for the report. It may remain in your local folder as a helper. Don't include account secrets, installed environment, raw dataset, every temporary log or unrelated projects.

Antigravity can package with Python's standard `zipfile` or `shutil.make_archive`; no special GUI is required. It must build from the clean `submission` folder, list archive members, verify `ZipFile.testzip()` returns `None`, and check key required files exist inside. Do not package empty placeholder deliverables and call the project complete.

Create the new repository under sg721642 and commit/push throughout execution as authorized in the GitHub automation section. Use the specified name and private default; public visibility needs an explicit user instruction. GitHub success must be verified by the real URL and access requirements. Course submission can require additional fields; never invent a portal or assume that a GitHub push submits the assignment.

## N. Handling interruptions, limits and errors

### N1. ChatGPT context/usage limit

Do not restart the project. Preserve this master and current state. Open a new chat, attach them and the last relevant log; use Section E. If only the master is available, request Antigravity to inspect local files and reconstruct state from configs/checkpoints/logs. Reconstructing state is read-only first; do not retrain blindly.

### N2. Antigravity stops while training

First inspect the actual terminal/process and output CSV modification times. A still-running process is not a failure. If dead, rerun the identical recorded command. Completed runs are skipped; a partial run starts from epoch 1. The current script is deliberately not a batch-level optimizer resume system. If code/environment changed, use a new output folder and keep old evidence.

### N3. Dataset or package failures

Record exact exception, architecture, interpreter path and package versions. Use the troubleshooting table in Part II. Fix the environment/download first. The loader can repair empty extracted files from checksum-valid downloaded gzip archives; it must not silently fabricate data or ignore corruption. If a source remains blocked on the current network, use an authorized official alternative/Colab route and record the change.

### N4. Unexpected metrics

Do not solve an unfavorable result by editing CSVs. Inspect gradients/loss curves, train/eval mode, class labels, split sizes and run completion. A tiny smoke model can have poor accuracy by design. A successful smoke test proves execution, not generalization. If final training underfits, report it and design a clearly labelled validation-led follow-up; do not retroactively call a tuned run the original fixed protocol.

### N5. Missing administrative details

The student's name, actual portal/cutoff, individual slot and evaluator identity/access requirements remain unspecified. GitHub owner and permission to create/commit/push are already provided; private visibility is the documented default. These do not block running the experiments. Ask them together when relevant, and continue independent work. Do not repeatedly request authorization for routine reversible local file creation already requested by the user.

### N6. Version-specific interface differences

Menu labels in Antigravity, Colab, GitHub and Overleaf can change. Match the equivalent action rather than insisting on a nonexistent button. Check official current docs when a version issue arises. Do not invent screenshots or claim to see the user's interface. Ask for a screenshot only when the observed UI is genuinely needed.

## O. Final handoff message template for the executing agent

```text
Project: 24CS2032 / DL-001 Dropout
Completed gates: [actual list]
Remaining gates: [actual list]

Experiments:
- MNIST: [actual run count, final folder, validation-selected rate]
- Fashion: [actual run count, final folder, validation-selected rate]
- Backend/versions: [actual]
- Results: [actual baseline and selected error ± SD, units]

Artifacts:
- Report: [path, page count, compile/render status]
- Notebook: [path, local/hosted validation status]
- Presentation: [path, format/editability/render status]
- Clean ZIP: [path, integrity result]
- GitHub: [verified URL or pending]
- Course submission: [receipt/status or pending]

Limitations/negative findings: [actual]
User action still needed: [only necessary actions]
Latest PROJECT_STATE.md: [path]
```

## P. Preparation audit for this master edition

The embedded primary source is carried forward from the earlier tested implementation without silently changing the experimental protocol. This edition adds the automation/context handoff and a read-only verifier. The verifier is checked against actual existing MNIST/Fashion-MNIST smoke outputs and the short default-width MNIST run. These preparation runs remain separate from the student's final experiments.

No document can guarantee zero errors on an unseen machine. The practical protection here is explicit evidence at each gate, real tests, fixed settings, preserved logs and honest pending statuses. A future assistant should resolve demonstrated failures and carry the project to completion rather than make unsupported promises.

**END OF MASTER FILE. A reader has not read the complete file unless it reaches this line.**
