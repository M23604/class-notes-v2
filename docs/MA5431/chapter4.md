# Eigenvalues and Diagnolisation
## Eigenvalues and Eigenvectors
We note that for some matrix $\mathcal{A}$, the **eigenvalue** $\lambda$ and **eigenvector** $\vec v$ are defined such that

$$\mathcal{A}\vec v = \lambda \vec v$$
 
 From here, we can multiply each side by the Identity Matrix, $I$, to get the following results:
  
$$\begin{align*}\mathcal{A} \vec v &= \lambda I \vec v \\ \left(\mathcal{A} - \lambda I\right)\vec v &= \vec 0\end{align*}$$

We note that the only solutions here are that $\vec v = \vec 0$ or $det(\mathcal{A} - \lambda I) = 0$, which can be taken into account this determinant. Hence, we solve for $\lambda$ such that $det(\mathcal{A} - \lambda I) = 0$. 

We note that we expect a **characteristic polynomial** from this determinant, which can be represented as $\chi(\lambda)$. This gives a set of $\lambda$ values such that $\chi(\lambda) = 0$. These are the eigenvalues.

To determine the eigenvectors, we evaluate a vector space $X$ such that $(\mathcal{A} - \lambda I)\vec X_i = \vec 0$. This is simply the nullspace of $\mathcal{A} - \lambda I$. There you have the eigenvalues, and combining these vector spaces gives you the **eigenspace**, $E_\lambda(\mathcal{A})$.

## Diagnolisation
In diagnolisation, we derive a diagonal matrix $\mathcal{D}$ and invertible matrix $\mathcal{P}$ such that

$$\begin{align*}\mathcal{A} &= \mathcal{P}\mathcal{D}\mathcal{P}^{-1} \\ \mathcal{A}^2 &= \mathcal{P}\mathcal{D}\mathcal{P}^{-1}\mathcal{P}\mathcal{D}\mathcal{P}^{-1} = \mathcal{P}\mathcal{D}^2\mathcal{P}^{-1}\\ \mathcal{A}^n &= \mathcal{P}\mathcal{D}\mathcal{P}^{-1}\times \cdots \times \mathcal{P}\mathcal{D}\mathcal{P}^{-1} = \mathcal{P}\mathcal{D}^n\mathcal{P}^{-1}\end{align*}$$

Here, we consider a matrix $\mathcal{A}$ that has a eigenspace of dimension $n$, i.e. it has $n$ linearly independent basis vectors, $v_1$ to $v_n$. If a matrix does not satisfy this requirement, then it **CANNOT** be diagnolised.

From here we are able to say this:

$$\begin{align*}\mathcal{P} &=\begin{bmatrix}
    \vert & \vert &  &\vert \\
    v_1   & v_2 & \cdots & v_n   \\
    \vert & \vert &  &\vert
\end{bmatrix} \\\\ \mathcal{D} &=\begin{bmatrix}
    \lambda_1 & 0 & \cdots & 0 \\
    0 & \lambda_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \lambda_n
\end{bmatrix}  \end{align*}$$

From here, if you're asked to determine $\mathcal{A}^n$, this should be an ideal way to make your life easier. And that's it.
