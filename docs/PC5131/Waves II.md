# Waves II

This topic deals with the superposition of moving waves. Consider two propagating moves as shown below:

$$\begin{align*}\psi_1(x,t) &= A_1 \sin(k_1x - \omega_1 t)\\\psi_2(x,t) &= A_2 \sin(k_2x - \omega_2 t)\end{align*}$$

If we consider the summation of these waves, $\psi_3(x,t)$,

$$
\begin{align*}
\psi_3(x,t) &= \psi_1(x,t) + \psi_2(x,t) \\
&= A\sin(k_1x - \omega_1t) + A\sin(k_2x-\omega_2 t) \\
&= A\left(2\sin\left(\frac{k_1x-\omega_1t + k_2x-\omega_2t}{2} \right)\cos\left(\frac{k_1x-\omega_1t - k_2x+\omega_2t}{2} \right) \right) \\
\psi_3(x,t) &= 2A\left(2\sin\left(\frac{k_1+k_2}{2}x - \frac{\omega_1+\omega_2}{2}t\right)\cos\left(\frac{k_1-k_2}{2}x - \frac{\omega_1-\omega_2}{2}t\right) \right) \\
\end{align*}
$$

The result?

<div align="center"><iframe src="https://www.desmos.com/calculator/vjwqguzt7t?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe></div>

(To experience the non-excruciating dark mode, go to [here](https://www.desmos.com/calculator/vjwqguzt7t) and turn on Dark Reader.)

