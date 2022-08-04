# Continuous Random Variables


## PDFs and CDFs

The probability of landing on any single point is zero, but the integral from negative to positive infinity is unity.

### Features

- **Median**: The value $m$ such that $F(m) = 1/2$; It splits the distribution evenly.
- **Mode**: The value where the PDF attains its maximum value.

### Expectation and Variance

$$
\mu_x = E[X] = \int_{-\infty}^\infty xf(x) dx
$$

$$
Var[X] = \int_{-\infty}^{\infty} (x-\mu_x)^2 f(x) \dd{x}
$$

A useful identity is 
$$
Var[X] = E[X^2] - \mu_x^2.
$$

You can remember the order as "E-mu", or by verifying the variance is positive.



## Common PDFs

### Uniform Random Variable

**Mean:** $(\beta +\alpha)/2$

**Variance:** $(\beta -\alpha)^2/12$

**Domain:** $(\alpha, \beta)$

$$
f(x) = 1/(\beta - \alpha)
$$

On $(\beta-\alpha)$.

$$
F(x) = \frac{x-\alpha}{\beta - \alpha}
$$

For $x > \beta$, $F(x) = 1$.

### Exponential Random Variable

If $X ~ Po(\lambda)$, then $T$ is the time until the first event occurs. This distribution is derived from $F(t) =  1 - P(X=0;\lambda = \lambda_t)$, then differentiating. Like the Poisson distribution, it has the memoryless property.

**Mean:** $1/\lambda$
**Variance:** $1/\lambda^2$
**Domain:** $[0,\infty)$

$$
f(x) = \lambda e^{-\lambda t}
$$
$$
F(x) = 1-e^{-\lambda t}
$$

For $x > \beta$, $F(x) = 1$.

### Normal Distribution

$X ~ N(\mu,\sigma^2)$. 

**Mean/Mode/Median:** $\mu$
**Variance:** $\sigma^2$
**Domain:** $[0,\infty)$
**Special values**: 68%,95%,99.7% fall within 1,2,3 standard deviations of the mean.

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

#### Standard Nomral Distrbiution

Since all normal distribution are the same up to scaling and translation, we may define one standard normal distribution with zero mean and unit variance. Sums of gaussian distributions are also gaussian distributions.

Define the z-score as
$$
z = \frac{x-\mu}{\sigma}.
$$

Calculating $P(X = x; \sigma, \mu)$ is then equivalent to finding $P(Z = (x-\mu)/\sigma)$. Using GC, it is also possible to find the $z$ for which $F(Z \leq z)$ attains some value.

Note $F(-z) = 1-F(z)$.





