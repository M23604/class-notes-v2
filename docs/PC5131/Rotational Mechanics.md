# Rotational Mechanics

(yeet.)

Chapter 1 of PC5131 is Rotational Mechanics, which is problematic. The topic is just a scam, since it is just all of Mechanics but with **Angular** (not the *painful* JS Framework). Surmised below is a list of equations which can probably help one understand Rotational Mechanics in the context of normal Mechanical concepts. Good Luck.

## Translational and Rotational Counterparts

It's just everything we have already learnt, but they added angular in front of it. So let's just walk through a list of equations, and their rotational counterparts.

|Translational|Rotational|
|---|---|
|$v_f = v_i + at$|$\omega_f = \omega_i + \alpha t$|
|$\Delta x = v_i t + \frac{1}{2} at^2 = \frac{v_f+v_i}{2}t$|$\Delta\theta=\omega_it+\frac{1}{2}\alpha t^2 = \frac{\omega_i+\omega_f}{2}t$|
|$v_f^2 = v_i^2 + 2a\Delta x$|$\omega_f^2 = \omega_i^2 + 2\alpha\Delta\theta$|
|$F_{net} = ma$|$\tau_{net} = I\alpha$|
|$p = mv$|$L = I\omega$|
|$J = F\Delta t$|$\Delta L = \tau\Delta t$|
|$W = F_\parallel \cdot s$|$W = \tau \cdot \Delta\theta$|
|$E_K = \frac{1}{2}mv^2$|$E_L = \frac{1}{2}I\omega^2$|
|$P = \frac{W}{t} = F \cdot v$|$P = \tau \cdot \omega$|

## Moment of Inertia, $I$

Do note that $I$ is slightly more cursed, and the following table demonstrates the definition of $I$:

|Situation|$I$|$\beta$|
|---|---|---|
|Moment of Inertia off from $I_{cm}$|$I = I_{cm} + Md^2$|-|
|Moment of Inertia of Multiple Parts|$I = \sum I_{part}$|-|
|Hoop (from the centre)|$I = MR^2$|$1$|
|Circular Disc (from the centre)|$I = \frac{1}{2}MR^2$|$\frac{1}{2}$|
|Circular Disc (through diameter)|$I = \frac{1}{4}MR^2$|$\frac{1}{4}$|
|Long Rod (from the centre)|$I = \frac{1}{12}ML^2$|$\frac{1}{12}$|
|Long Rod (from end)|$I = \frac{1}{3}ML^2$|$\frac{1}{3}$|
|Solid Sphere|$I = \frac{2}{5}MR^2$|$\frac{2}5$|
|Hollow Sphere|$I = \frac{2}{3} MR^2$|$\frac{2}3$|

## Shifting from Translational to Rotational

We also note that we can relate all the quantities to each other via the variable $r$, as shown below:

|Translational|Rotational|
|---|---|
|$\Delta x$|$r\Delta\theta$|
|$v$|$r\omega$|
|$a$|$r\alpha$|
|$I$|$\beta mr^2$|
|$\vec F \times \vec{r}$|$\vec \tau$|
|$\vec r \times \vec p$|$\vec L$|

## Conservation Cases

Cases to be considered for collisions:

|Situation|Translational|Rotational|
|---|---|---|
|Elastic Collision|COE, COM applies|COE, COAM applies|
|Inelastic Collison|COM applies, COE does not|COAM applies, COE does not|
|Completely Inelastic Collision (objects stick together)|COM applies, COE does not|COAM applies, COE does not|
|Some force acting throughout the motion (e.g. Gravity)|COE applies, COM does not|COE applies, COAM does not|

## Ramp

| Name                                           | Quantity                                                     |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Rotational Kinetic Energy                      | $K_{rot} = \frac{\beta}{1+\beta}mgh$                         |
| Translational Kinetic Energy                   | $K_{trans} = \frac{1}{1+\beta}mgh$                           |
| Velocity of Centre of Mass                     | $v_{cm} = \sqrt{\frac{2gh}{1 + \beta}}$                      |
| Acceleration of Centre of Mass                 | $a_{cm} = \frac{v_{cm}^2}{2\Delta x} = \frac{g\sin\theta}{1+\beta}$ |
| Velocity at Top of Loop-_de_-Loop (Radius $R$) | $v_{loop} = \sqrt{g(R-r)}$                                   |
| Minimum height, $h$ for Loop-_de_-Loop         | $h = \frac{5+\beta}{2}(R-r)$                                 |

## Loop-_de_-Loop

Loop-_de_-Loop for normal circular motion:

$$\begin{align*}N &= \frac{mv^2}R - mg =  0 \\ v^2 &= Rg \\ \frac{1}{2}mv^2 &= mg(h-2R) \\ v^2 &= 2g(h-2R) = Rg \\ 2h - 4R &= R \\ h &= 2.5 R\end{align*}$$

For rigid body of radius $r$:

$$\begin{align*}N &= \frac{mv^2}{R-r} - mg =  0 \\ v^2 &= g(R-r) \\ \frac{1}{2}(1+\beta)mv^2 &= mg(h+2r-2R) \\ (1+\beta)g(R-r) &= 2g (h+2r-2R) \\ (1+\beta)(R-r) &= 2h - 4(R-r) \\ 2h &= (5+\beta)(R - r) \\ h &= \frac{5+\beta}{2}(R-r) \end{align*}$$






