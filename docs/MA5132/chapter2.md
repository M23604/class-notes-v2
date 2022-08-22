# Discrete Random Variables

For any discrete random variable (DRV), it is crucial that the following result applies:
$$\sum_{i=0}^n P(X=i)=1$$
## Definitions
### Expected Value (Mean)
$$\mu_x = E(X) = \sum_{i=0}^n i \cdot P(X=i)$$
### Extended Expected Value
$$E(f(X)) = \sum_{i=0}^n f(i) \cdot P(X=i)$$

### Variance
$$\sigma_x^2 = Var(X) = E(X^2)-\left[E(X)\right]^2 = E\left( (X-\mu_x)^2 \right)$$

### Standard Deviation
$$\sigma_x = Std(X) = \sqrt{E(X^2)- [E(X)]^2} = \sqrt{E\left((X-\mu_x)^2\right)}$$

### Crucial Results
$$
\begin{align*}
E(aX\pm bY + c) &= a^2 E(X) + b^2 E(Y) \\
Var(aX+b) &= a^2 Var(X) \\
Var(aX\pm bY) &= Var(aX) + Var(aY) \text{ (Only applies if X and Y are independent.)}
\end{align*}
$$

## Common Distributions
### Binomial
$$
\begin{align*}
P(X=k) &= \binom nk \cdot p^k \cdot (1-p)^{n-k} \\
\sum_{k=0}^n P(X=k) &= \sum_{k=0}^n \binom nk \cdot p^k \cdot (1-p)^{n-k} \\
&= \binom n0 (1-p)^{n} + \binom n1 p(1-p)^{n-1} + \dots + \binom n{n-1}p^{n-1}(1-p) + \binom nn p^n \\
&= (1-p+p)^n = 1^n = \textbf{1} \\
E(X) &= np\\
Var(X) &= np(1-p) \\
P(X < k) &= \sum_{i=0}^{n}
\end{align*}
$$