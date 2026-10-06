# Speaker Notes — Manual Dropout Presentation (24CS2032)

**Presenter:** Satyam Gupta (Roll No. 24CS2032)  
**Total Target Speaking Time:** ~9 minutes (+ 1 minute for live saved-model demo & questions)  
**Tone:** Natural academic student presentation, methodical, and evidence-grounded.

---

### Slide 1: Title & Overview
- **Allocated Time:** ~35–40 seconds
- **Talking Points:**
  1. Good morning everyone. I am Satyam Gupta, roll number 24CS2032, and today I will present our project on implementing and evaluating manual inverted dropout in neural networks.
  2. This work is an educational, reduced-scale reproduction and ablation study inspired by Figure 9(a) of the landmark 2014 paper by Srivastava et al. in JMLR.
  3. Our core objective was twofold: first, to build dropout completely from mathematical first principles in PyTorch without using any built-in library primitives; and second, to systematically measure how eight uniform drop rates impact generalization across three independent random seeds.
  4. We evaluated this on the primary MNIST digit dataset and extended the exact same protocol to Fashion-MNIST.
  5. Let's begin by looking at why dropout is such an essential regularization technique.

---

### Slide 2: Why Dropout?
- **Allocated Time:** ~55–60 seconds
- **Talking Points:**
  1. Deep feedforward networks have immense representational capacity, which allows them to easily memorize small training datasets.
  2. In unregularized training, individual hidden units tend to develop complex co-adaptations—meaning one neuron learns to fix the specific errors of another, rather than learning robust, standalone features.
  3. This causes training error to drop near zero while test error plateaus, resulting in a large generalization gap.
  4. Dropout solves this by stochastically deactivating hidden units during each training iteration with drop probability $d$, or keep probability $q = 1 - d$.
  5. By temporarily removing units, each neuron must learn useful features in random contexts alongside diverse thinned subnetworks.
  6. At test time, all neurons remain active deterministically, effectively forming an implicit geometric ensemble that generalizes significantly better.
  7. However, dropout is not magic—if the drop rate is too high, it starves network capacity and leads to underfitting.

---

### Slide 3: Manual Dropout Implementation
- **Allocated Time:** ~90–100 seconds
- **Talking Points:**
  1. For this assignment, using PyTorch's built-in `torch.nn.Dropout` or `F.dropout` was strictly prohibited, so we implemented `ManualDropout` from scratch as an `nn.Module`.
  2. During training, we sample a binary mask $m$ where each element is drawn independently from a Bernoulli distribution with parameter $q = 1 - d$.
  3. Rather than using classical test-time scaling, we adopt modern inverted dropout, dividing the unmasked activations by $q$ directly during training: $\tilde{h}_i = m_i h_i / q$.
  4. The mathematical elegance here is that the conditional expectation during training, $\mathbb{E}[\tilde{h}_i \mid h_i]$, equals $(h_i / q) \cdot q$, which exactly equals $h_i$.
  5. Because the expected signal magnitude is preserved during training, the evaluation pass is simply the identity function: $\tilde{h}_i = h_i$.
  6. This means inference is completely deterministic and requires zero extra floating-point operations or memory allocations at test time.
  7. In our architecture, dropout is applied strictly after hidden ReLU activations—never on raw inputs or final classification logits.

---

### Slide 4: Controlled Experimental Setup
- **Allocated Time:** ~65–75 seconds
- **Talking Points:**
  1. To ensure fair and reproducible comparisons, we locked a strict protocol named `dropout-24cs2032-v1`.
  2. We used a 3-hidden-layer MLP: 784 inputs, three hidden layers of 256 units with ReLU, and 10 outputs, totalling 335,114 trainable parameters.
  3. Our datasets were partitioned into 10,000 training, 5,000 validation, and 10,000 official test examples using fixed split seed 2026.
  4. We evaluated eight uniform drop rates from $0.0$ to $0.7$ across three random seeds: 42, 43, and 44.
  5. Crucially, each seed was initialized with bitwise-identical starting weights across all eight drop rates, ensuring completely fair initial conditions.
  6. Models were trained for 20 epochs using the Adam optimizer with learning rate 0.001 and batch size 128 on CPU, which benchmarked 5.5 times faster than MPS on this tensor scale.
  7. Most importantly, model selection was governed strictly by lowest mean validation error—the test set was never used for selecting rates or epochs.

---

### Slide 5: MNIST Empirical Results
- **Allocated Time:** ~100 seconds
- **Talking Points:**
  1. Slide 5 presents our measured results on MNIST across 24 completed training runs.
  2. Looking at the keep-probability curve on the left, we observe a distinct U-shaped trajectory mirroring Figure 9(a) of the Srivastava paper.
  3. The unregularized baseline ($d=0.0$) reached $0.203\%$ training error but suffered a test error of $4.320 \pm 0.295\%$, exhibiting a wide 4.12 percentage point generalization gap.
  4. As dropout is introduced, test error decreases steadily. Validation error selected $d=0.4$ as the optimal rate, achieving a validation error of $3.747 \pm 0.130\%$.
  5. On the unseen test set, this selected model achieved $3.843 \pm 0.282\%$ error, representing an absolute improvement of 0.48 percentage points and an 11.03% relative error reduction over the baseline.
  6. Now, there is an important methodological nuance: descriptively, the lowest average test error occurred at $d=0.3$ with $3.820\%$. But because test data must never guide selection, $d=0.4$ is our sole authorized model. The 0.02% difference is negligible and well within experimental noise.
  7. Notice also the negative finding: when drop rate exceeds 0.5, test error degrades sharply to $5.110\%$ at $d=0.7$, performing markedly worse than having no dropout at all.

---

### Slide 6: Historical Comparison & Fashion-MNIST Extension
- **Allocated Time:** ~90 seconds
- **Talking Points:**
  1. On the left side of this slide, we contextualize our findings against Table 2 of the original 2014 paper.
  2. Srivastava et al. reported a test error of approximately $1.25\%$ using a 3-layer ReLU network with dropout.
  3. We explicitly emphasize that our result of $3.843\%$ is not an apples-to-apples numerical comparison: the original paper trained networks with over 1,024 to 8,192 hidden units on the full 60,000 dataset for hundreds of epochs with momentum SGD and max-norm constraints.
  4. Our study successfully replicates the core scientific phenomenon—the qualitative U-shaped curve and regularization benefit—under a constrained 20-epoch educational budget.
  5. On the right side, we extended the identical protocol to Fashion-MNIST.
  6. Here, validation selected a lower drop rate, $d=0.2$, which lowered test error from $14.663\%$ to $14.347\%$, a 2.16% relative improvement.
  7. Strikingly, the canonical rate of $d=0.5$ produced $15.133\%$ test error—worse than the no-dropout baseline.
  8. This proves that optimal regularizer strength is sensitive to dataset complexity: Fashion-MNIST requires preserving more feature capacity than simple stroke digits.

---

### Slide 7: Failure Analysis & Limitations
- **Allocated Time:** ~65–75 seconds
- **Talking Points:**
  1. To understand where our best models still fail, Slide 7 examines misclassified test samples from the validation-selected checkpoints.
  2. On MNIST with $d=0.4$, errors typically stem from ambiguous handwriting—for instance, an open digit 2 visually resembling a 3, or a compressed digit 9 with a curved stem resembling an 8.
  3. On Fashion-MNIST with $d=0.2$, failures concentrate along semantically adjacent apparel silhouettes—such as misclassifying an open coat as a pullover, or a low-cut ankle boot as a sneaker.
  4. Fully connected MLPs lack the translation invariance of convolutional networks, making subtle $28 \times 28$ grayscale textures challenging to disentangle.
  5. We must also acknowledge key experimental limitations: our sample size of three seeds cannot support formal significance testing, our 20-epoch training horizon is deliberately constrained, and Fashion-MNIST was evaluated purely as an exploratory extension.
  6. High dropout rates might recover performance if given hundreds of epochs, but under fixed budgets, aggressive dropout underfits.

---

### Slide 8: Conclusion & Saved-Model Demo
- **Allocated Time:** ~45–50 seconds
- **Talking Points:**
  1. In conclusion, we successfully built and verified inverted dropout from mathematical first principles without external library abstractions.
  2. Moderate validation-tuned dropout reliably reduced generalization error on both datasets—achieving an 11.03% relative improvement on MNIST and 2.16% on Fashion-MNIST.
  3. Our negative results demonstrate that canonical dropout rates like $d=0.5$ cannot be applied blindly: regularizer strength must be tuned against validation data.
  4. The complete codebase, audited metrics, and verified IEEE report are available in our private GitHub repository.
  5. Finally, we have prepared a quick Python demo script that loads our saved validation-selected checkpoint and performs instant CPU inference on test examples without any retraining.
  6. Thank you, and I would now be happy to demonstrate the model and answer any questions.
