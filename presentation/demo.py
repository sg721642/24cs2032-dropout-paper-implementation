#!/usr/bin/env python3
"""
Quick Saved-Model Demo for 24CS2032 Dropout Presentation.
Loads the validation-selected MNIST model checkpoint (d=0.4, seed 42)
and performs instantaneous CPU inference on the first 10 test images.
NO TRAINING IS PERFORMED.
"""

import sys
from pathlib import Path
import torch
import torchvision.datasets as datasets
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Ensure project root is importable
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from run import MLP

def run_demo():
    print("=" * 60)
    print(" 24CS2032 MANUAL DROPOUT — SAVED MODEL INFERENCE DEMO")
    print("=" * 60)
    
    device = torch.device("cpu")
    ckpt_path = PROJECT_ROOT / "results_mnist" / "mnist_d0.4_s42.pt"
    
    if not ckpt_path.exists():
        print(f"Error: Checkpoint not found at {ckpt_path}")
        sys.exit(1)
        
    print(f"[*] Loading model architecture: MLP(784 -> 256 -> 256 -> 256 -> 10)")
    print(f"[*] Checkpoint: {ckpt_path.name} (Validation-selected d=0.4, seed 42)")
    
    model = MLP(drop_rate=0.4, width=256).to(device)
    state_dict = torch.load(ckpt_path, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
    model.eval()
    print("[*] Checkpoint loaded successfully into CPU memory.")
    print("[*] Model set to eval mode (stochastic dropout bypassed, deterministic inference).")
    
    # Load first 10 official MNIST test examples
    data_dir = PROJECT_ROOT / "data"
    test_dataset = datasets.MNIST(str(data_dir), train=False, download=False)
    
    num_samples = 10
    x_raw = test_dataset.data[:num_samples]
    y_true = test_dataset.targets[:num_samples]
    
    # Preprocess: shape (N, 1, 28, 28), float32 in [0, 1]
    x_tensor = x_raw.unsqueeze(1).float().div(255.0).to(device)
    
    print("\n[*] Performing forward pass on first 10 test examples...")
    with torch.no_grad():
        logits = model(x_tensor)
        probs = torch.softmax(logits, dim=1)
        preds = probs.argmax(dim=1)
        confs = probs.max(dim=1).values
        
    print("\n" + "-" * 60)
    print(f"{'Sample':<8}{'True Label':<12}{'Predicted':<12}{'Confidence':<14}{'Status':<8}")
    print("-" * 60)
    
    correct = 0
    for i in range(num_samples):
        t = y_true[i].item()
        p = preds[i].item()
        c = confs[i].item()
        is_match = (t == p)
        if is_match:
            correct += 1
        status = "MATCH" if is_match else "MISMATCH"
        print(f"#{i+1:<7}{t:<12}{p:<12}{c*100:>6.2f}%       {status:<8}")
        
    print("-" * 60)
    print(f"Accuracy on demo batch: {correct}/{num_samples} ({correct/num_samples*100:.1f}%)")
    
    # Save a visual grid image as backup artifact
    fig, axes = plt.subplots(2, 5, figsize=(11, 5.2))
    plt.subplots_adjust(hspace=0.45, wspace=0.25, top=0.88, bottom=0.08)
    axes = axes.flatten()
    for i in range(num_samples):
        ax = axes[i]
        ax.imshow(x_raw[i].numpy(), cmap='gray')
        t = y_true[i].item()
        p = preds[i].item()
        c = confs[i].item()
        color = 'darkgreen' if t == p else 'red'
        ax.set_title(f"True: {t} | Pred: {p}\nConf: {c*100:.1f}%", fontsize=10, color=color, fontweight='bold', pad=4)
        ax.axis('off')
        
    plt.suptitle("24CS2032 Dropout Demo: Validation-Selected MNIST Model (d=0.4, Seed 42)", fontsize=13, fontweight='bold')
    
    out_img = PROJECT_ROOT / "presentation" / "demo_predictions.png"
    plt.savefig(out_img, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[*] Visual backup grid saved to: {out_img.relative_to(PROJECT_ROOT)}")
    print("=" * 60)
    print(" DEMO COMPLETED SUCCESSFULLY (0 RETRAINING PERFORMED)")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()
