# Physical Optics
Chapter 3 of PC5131 is Physical Optics. It is essentially just the behaviour of light when it passes through physical objects. These objects are double slits, diffraction grating, single slit and thin films. The behaviour when passing through objects can be quantified using Optical Path Length.
## Optical Path Length
Optical Path Length $= nd$
$n =$ refractive index of medium
$d =$ physical distance

<u>Example</u>
![Figure of glass with thickness l](https://www.sarthaks.com/?qa=blob&qa_blobid=10286458292504049266)

Optical path length between $A\&B = x + y + l\mu$
Number of cycles between $A\&B=\frac {\text{Optical Path length}}\lambda$

## Double Slit + Diffraction Grating
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6wdgqtSBHX1nIYgixe1m-uSGBQYK3P-Xg-A&usqp=CAU)

<u>Dark Spots (Destructive Interference)</u>
$\Delta \phi = (2n + 1)\pi$, Offset of $\pi$ or $\frac 12$ cycle
$d\sin\theta = (m - \frac 12)\lambda$ where $m\in\mathbb{Z}^+$
$x\tan\theta = y_m$

<u>Light Spots (Constructive Interference)</u>
$\Delta \phi = (2n)\pi$, Offset of $2\pi$ or $1$ cycle
$d\sin\theta = m\lambda$ where $m\in\mathbb{Z}^+ \cup {0}$
$x\tan\theta = y_m$

Sometimes $d << L$, And we can use the following $\sin\theta \approx \tan\theta \approx \theta \text{(radians)}$ 
### Intensity Graph
![](https://s3-us-west-2.amazonaws.com/courses-images-archive-read-only/wp-content/uploads/sites/222/2014/12/20111413/Figure_28_04_03a.jpg)

## Single Slit
Split single slit into 2 equal width slits
Distance between slits $= \frac {\text{width of slit}}2$
$\implies d = \frac a2$

### Intensity Graph
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIIMYaYje8FTsNHVhYv3YFI8YfFbJtLbQC1w&usqp=CAU)

## Thin Film
An incident ray lands on a thin film. Recall from Waves I that a wave undergoes a half-wavelength phase shift when it goes from a less optical dense material (smaller refractive index) to a more optically dense material (bigger refractive index). 

![](https://cdn1.byjus.com/wp-content/uploads/2021/04/Thin-Film-Interference-1.png)

In the above diagram, ray 1 gets phase-shifted once. Ray 2 gets phase shifted twice, (once at air-to-film interface, second time at film-to-Surface B interface). Ray 2 also travels an extra $2t$ units of distance (this is approximation because the film is thin) than ray 1. But the shift in wavelength is not actually $2t$, because the wavelength becomes shorter when it enters the film (WHY?). It is instead $2t n_{film}$. 

Adding all the phase shifts, the total phase shift is $d = 2n_{film}t + \frac12 \lambda$. When d is an integer multiple, it is constructive interference. When d is an integer multiple plus half, it is destructive.
