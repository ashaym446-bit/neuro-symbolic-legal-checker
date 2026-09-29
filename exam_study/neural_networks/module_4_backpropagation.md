# Neural Networks — Module 4: Backpropagation & Optimization 🧠

## Syllabus Breakdown (RAIT / University Pattern)
1. **Topic 1**: Backpropagation & Differentiation (Chain Rule, Forward & Backward Pass)
2. **Topic 2**: Hessian Matrix (Second-Order Derivatives & Curvature of Error Surface)
3. **Topic 3**: Generalization & Cross-Validation (Overfitting vs Underfitting)
4. **Topic 4**: Network Pruning Techniques (Optimal Brain Damage / Surgeon)
5. **Topic 5**: Virtues and Limitations of Backpropagation
6. **Topic 6**: Accelerated Convergence (Momentum & Adaptive Learning Rates)
7. **Topic 7**: Supervised Learning Framework

---

## 📖 Jargon Buster (Difficult Words Decoded)

| Term | What it Means in Plain English | Real-World Analogy |
| :--- | :--- | :--- |
| **Backpropagation** | Sending the error backwards from the output to adjust connection weights. | A manager giving feedback down the corporate ladder to fix mistakes. |
| **Differentiation ($\frac{\partial E}{\partial w}$)** | Finding how much the total error changes when one weight is slightly nudged. | Turning a knob and seeing if the volume goes up or down. |
| **Chain Rule** | Multiplying rates of change step-by-step across layers. | Gear system: Gear A turns Gear B, which turns Gear C. |
| **Hessian Matrix** | A table of second derivatives showing how curved the error bowl is. | Checking if you're in a steep canyon or a flat valley. |
| **Generalization** | How well the network performs on brand new, unseen test data. | Passing an exam without having seen the exact questions beforehand. |

---

## 📌 Topic 1: Backpropagation & Differentiation

### 1. Key Concept
- **Forward Pass:** Input is passed forward through layers to compute predictions. Error is calculated ($E = \frac{1}{2}\sum (Target - Output)^2$).
- **Backward Pass:** Using the **Chain Rule of Calculus**, the error gradient is propagated backward to compute $\frac{\partial E}{\partial w}$.
- **Weight Update Formula:**
  $$\Delta w_{ij} = -\eta \cdot \frac{\partial E}{\partial w_{ij}}$$
  *(where $\eta$ is the learning rate)*.

### 2. 5–10 Mark Exam Algorithm Steps
1. **Initialize Weights:** Set small random weights.
2. **Forward Propagation:** Compute activations layer by layer ($y = f(W \cdot x + b)$).
3. **Compute Error:** Calculate error at output layer.
4. **Backward Propagation:** Compute local gradients ($\delta$) using the chain rule.
5. **Weight Adjustment:** Update weights using gradient descent formula.
6. **Repeat:** Continue until error falls below a threshold or max epochs reached.
