# Viva Examination Preparation — Manual Dropout (24CS2032)

**Candidate:** Satyam Gupta (Roll No. 24CS2032)  
**Topic:** Manual Inverted Dropout Implementation & Empirical Ablation Study  
**Protocol:** `dropout-24cs2032-v1`

---

### 1. Why divide by keep probability $q$?
**Answer:** In inverted dropout, dividing unmasked activations by $q = 1 - d$ during training preserves the expected signal magnitude across layers ($\mathbb{E}[\tilde{h}_i \mid h_i] = \frac{h_i}{q} \cdot q = h_i$). This eliminates the need to scale network weights or activations at test time, keeping inference deterministic and computationally identical to a standard forward pass.

---

### 2. Why is there no dropout during inference?
**Answer:** During inference (evaluation), we want deterministic, lowest-variance predictions rather than noisy stochastic outputs. By keeping all units active without masking, the full network acts as an implicit geometric mean ensemble over the exponentially many thinned subnetworks sampled during training.

---

### 3. Why not use `torch.nn.Dropout`?
**Answer:** The educational goal of this project was to implement dropout from fundamental mathematical principles. Using built-in library primitives (`torch.nn.Dropout` or `F.dropout`) would obscure mask generation, scaling arithmetic, and train/eval mode branching, defeating the implementation objective.

---

### 4. What does $d=0$ mean?
**Answer:** $d=0$ corresponds to a keep probability $q=1.0$, meaning no activations are dropped. It represents the unregularized baseline model where the mask is an all-ones vector and activations pass through unaltered.

---

### 5. Why is $d=1$ invalid?
**Answer:** A drop rate of $d=1.0$ implies a keep probability $q=0.0$. This causes a division by zero in the inverted scaling factor ($1/q = 1/0$) and zeroes out all layer activations, completely severing forward information flow and gradient propagation.

---

### 6. Why use three random seeds (42, 43, 44)?
**Answer:** Neural network training is stochastic due to random weight initialization, mini-batch shuffling, and Bernoulli mask sampling. Evaluating across three seeds measures performance stability, provides sample standard deviations, and protects against selecting a rate that succeeded purely by random chance.

---

### 7. Why use validation error instead of test error for rate selection?
**Answer:** Using the test set to select hyperparameters (such as drop rate) causes data leakage, where the model indirectly overfits the evaluation benchmark and inflates reported performance. The test set must remain strictly quarantined for unbiased descriptive assessment of generalization.

---

### 8. Why recompute training error in evaluation mode?
**Answer:** During training, forward passes include random dropout masks and unscaled noise. To fairly compare training error against validation and test error, training error must be evaluated with dropout deactivated (deterministic mode), reflecting the true representational fit of the full ensemble.

---

### 9. Does dropout reduce the number of trainable model parameters?
**Answer:** No. Dropout only temporarily zeroes out neuron *activations* during individual forward/backward passes. The underlying weight matrices and bias vectors remain fully intact and allocated in memory. All 335,114 parameters persist throughout training and inference.

---

### 10. Does dropout always improve model accuracy?
**Answer:** No. Dropout acts as a regularizer. Under a fixed training horizon, if the drop rate is set too high (e.g., $d \ge 0.5$ on Fashion-MNIST), the network exhibits underfitting and achieves higher test error than the unregularized baseline.

---

### 11. Why was CPU selected instead of Apple Silicon MPS?
**Answer:** On our 3-layer MLP architecture (335,114 parameters and batch size 128), tensor operations are relatively small. Benchmarks revealed that CPU execution took 0.785 seconds per 2-epoch run, while MPS took 4.398 seconds (>5.5× slower) due to Metal GPU kernel launch, dispatch, and synchronization overhead on small tensor batches.

---

### 12. Why was $d=0.4$ selected for MNIST even though $d=0.3$ had slightly lower observed test error?
**Answer:** Because our scientific protocol strictly forbids test-set snooping. Model selection was governed exclusively by minimum mean validation error, where $d=0.4$ achieved $3.747 \pm 0.130\%$ compared to $3.753 \pm 0.061\%$ for $d=0.3$. The observed mean test-error difference between $d=0.3$ and $d=0.4$ is only 0.023 percentage points. Test set data remained strictly quarantined and was never used for model selection.

---

### 13. Why did $d=0.5$ perform poorly on Fashion-MNIST?
**Answer:** Under this fixed protocol, $d=0.5$ produced higher mean test error ($15.133 \pm 0.325\%$) than the no-dropout baseline ($14.663 \pm 0.175\%$). If asked why, possible factors include stronger regularization and a fixed 20-epoch optimization budget, but the experiment does not isolate a causal mechanism. We do not present speculation as measured fact.

---

### 14. What is the difference between drop probability and keep probability?
**Answer:** Drop probability $d$ is the likelihood that an individual unit's activation is set to zero ($d \in [0, 1)$). Keep probability $q = 1 - d$ is the probability that the activation is retained ($q \in (0, 1]$). In Bernoulli sampling, $\mathbb{P}(m_i = 1) = q$ and $\mathbb{P}(m_i = 0) = d$.

---

### 15. What are the key differences between your experiment and the original Srivastava et al. (2014) paper?
**Answer:** 
1. **Network width:** Srivastava et al. used wide networks (1,024 to 8,192 hidden units); we used 256 units.
2. **Data scale:** Original paper used all 60,000 MNIST training examples; we used a 10,000-example subset.
3. **Training horizon:** Original paper trained for hundreds of epochs with momentum SGD and max-norm constraints; we used 20 epochs with Adam.
4. **Formulation:** We used inverted dropout ($x \cdot m / q$ at train time); the original paper used test-time scaling ($x \cdot q$).

---

### 16. Why is Fashion-MNIST referred to as an "extension"?
**Answer:** Fashion-MNIST was released in 2017 (by Xiao et al.), three years after the 2014 dropout paper. It was not part of the original study. We evaluated it as an independent extension to test whether our dropout findings generalize to more complex visual benchmarks under the identical protocol.

---

### 17. What does sample standard deviation ($ddof=1$) represent in our tables?
**Answer:** It quantifies the run-to-run variability across our three independent random seeds (42, 43, 44). Using Bessel's correction ($ddof=1$, dividing by $N-1 = 2$) provides an unbiased estimator of population variance from a small sample.

---

### 18. Why do we not claim formal statistical significance?
**Answer:** A sample size of $N=3$ random seeds possesses very low statistical power ($df=2$). While adequate for estimating variance and checking stability, it is mathematically insufficient to support rigorous paired $t$-tests or non-parametric significance testing.

---

### 19. What is an ablation study?
**Answer:** An ablation study systematically varies or removes individual components of an algorithm or model while holding all other variables strictly constant, isolating the specific causal contribution of the varied parameter (in our case, the dropout probability $d \in [0.0, 0.7]$).

---

### 20. What happens if dropout rate is set too high ($d \ge 0.6$)?
**Answer:** Under our fixed 20-epoch training budget, high dropout rates ($d \ge 0.6$) produced higher training and test error on both benchmarks, consistent with stronger underfitting. Higher dropout rates may require more optimization, but our experimental protocol intentionally kept the same 20-epoch budget across all rates.
