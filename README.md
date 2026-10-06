# Dropout implementation — 24CS2032

## Goal
Implement Bernoulli dropout manually inside an MLP and study generalization
across drop rates 0.0–0.7. This is a reduced-scale educational reproduction.

Paper: Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov —
"Dropout: A Simple Way to Prevent Neural Networks from Overfitting", JMLR 2014.

## Setup
```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run
```bash
python run.py --self-test --device cpu
python run.py --datasets mnist --device cpu --out results_mnist
python make_notebook.py
```

## Experiment
- 10,000 training / 5,000 validation / 10,000 official test examples
- Split seed 2026; model seeds 42, 43, 44; 20 epochs; batch 128
- MLP 784-256-256-256-10; Adam lr=0.001; no weight decay
- Inverted dropout after hidden ReLUs. Validation selects the rate.
- Test curves are descriptive and never used for model selection.

## Results
*Paste the actual table from results_mnist/RESULTS.md here after running.*
*Include selected rate, baseline comparison and any negative result.*

## Reproduction limits
Figure 9(a)-inspired fixed-width sweep, with reduced model/data/training.
Our result is not an exact reproduction of original-paper accuracy.
Record the actual device and package versions from config.json.

## Colab
Upload `24CS2032_Dropout.ipynb` to https://colab.research.google.com/
It embeds run.py and runs without cloning this repository.

## References and assistance
- Paper: https://jmlr.org/papers/v15/srivastava14a.html
- Author resources: https://www.cs.toronto.edu/~nitish/dropout/
- Historical repo consulted: https://github.com/nitishsrivastava/deepnet
- PyTorch: https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html
- Dataset: https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html
- Document any assistance or reused code in accordance with course policy.
