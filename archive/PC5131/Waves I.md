# Waves I

(yeet.)

Chapter 2 of PC5131 is Waves... I. This is effectively singular waves, rather than interfering waves. This includes normal wave properties and equations, wave intensity, string waves, polarisation, sound waves (longitudinal waves) and the Doppler Effect. This is relatively easier than the next topic (Waves II) so uh yay thank god only this much is tested in the Common Test on Monday. Anyways yeah good luck, and let's see what comes out of this, right? Aight. See yah.

## Basics

### Wave Quantities
$$\begin{align*}\omega &=2\pi f = \frac{2\pi}{T}\\k &= \frac{2\pi}{\lambda}\\v &= f\lambda = \frac{f}{T} = \frac{\omega}{k}\end{align*}$$
### Wave Equation

$$\begin{align*}\psi(x, t)&=A\sin(\phi_x -\phi_t + \phi_0)\\&=A\sin(kx-\omega t+\phi_0)\end{align*}$$

For wave moving backwards:

$$\psi(x, t) = A\sin(kx+\omega t+\phi_0)$$

### Phase Difference
$$\begin{align*}\Delta\phi &= \phi_2 - \phi_1 \\ &= (kx_2 - \omega t + \phi_0) - (kx_1-\omega t+\phi_0) \\ &= k(x_2 - x_1) \\ &= k\Delta x \\ &= 2\pi \frac{\Delta x}\lambda \\ &= -\omega \Delta t \\ &=-2\pi \frac{\Delta t}{T} \end{align*}$$

This applies to both $\Delta t$ and $\Delta x$, which is great. If the wave is moving backwards, the phase difference in terms of $\Delta t$ is positive, not negative.

## Intensity of Wave

$$\begin{align*} I &= \frac{P}{A}\\&=\frac{P}{4\pi r^2} \\ I &\propto \frac{1}{r^2} \\ \frac{I_1}{I_2} &= \left(\frac{r_2}{r_1}\right)^2 \end{align*}$$

## String Wave

$$v = \sqrt{\frac{T}{\mu}}$$

## Polarisation

### Polarising Filter

$$\begin{align*}I_1 &= \frac{I_0}{2}\\A_{n+1} &= A_n \cos\phi_{n+1,n}\\I_{n+1} &= I_n \cos^2\phi_{n+1,n}\end{align*}$$

### Brewster's Angle

$$\begin{align*}n_a \sin\theta_i &= n_a \sin\theta_{reflect} \\ n_a \sin\theta_i &= n_b \sin\theta_{refract} \\ n_a \sin\theta_{reflect} &= n_b \sin\theta_{refract}\end{align*}$$

From here, we note the following for **Brewster's Angle**, which is defined as $\theta_b$.

$$\begin{align*}\theta_{reflect} &= \theta_{brewster} = \theta_b \\ \theta_{refract} &= \theta_{polarised} = \theta_p \\ \theta_{b} + \theta_{p} &= \frac{\pi}2 \\ \sin\theta_p &= \cos\theta_b \\ n_a \sin\theta_{b} &= n_b \sin\theta_{p} = n_b\cos\theta_b \\ \frac{\sin\theta_b}{\cos\theta_b} &= \frac{n_b}{n_a} \\ \tan\theta_b &= \frac{n_b}{n_a} \\ 
\theta_b &= tan^{-1}\left(\frac{n_b}{n_a} \right)\end{align*}$$


## Sound

### Speeds of Sound

|Condition|Speed|
|---|---|
|0°C (Standard Temperature and Pressure)|330 m/s|
|30°C (Room Temperature and Pressure)|343 m/s|
|T°C (Any Temperature)|$331.5 \times \sqrt{1 + \frac{T}{273.15}}$|


### Doppler Effect

$$f' = f \frac{c \pm v_o}{c \mp v_s}$$

|Source|Observer|Numerator|Denominator|Remarks|
|---|---|---|---|--|
|stationary|stationary|c|c|-|
|approaching|stationary|$c$|$c-v_s$|-|
|moving away|stationary|$c$|$c+v_s$|-|
|stationary|approaching|$c+v_o$|$c$|-|
|stationary,|moving away|$c-v_o$|$c$|-|
|approaching|approaching|$c+v_o$|$c-v_s$|maximum|
|moving away|approaching|$c+v_o$|$c+v_s$|-|
|approaching|moving away|$c-v_o$|$c-v_s$|-|
|moving away|moving away|$c-v_o$|$c+v_s$|minimum|

***Just draw a damn diagram, for god's sake.***
