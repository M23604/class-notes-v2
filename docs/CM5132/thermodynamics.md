# Chemical Thermodynamics

## Entropy, $S$
Entropy is a measure of **disorderliness**. At absolute zero, the value for entropy is zero. It increases:
- change in states (gas is highest)
- increase in $V$ or $T$
- increase in molecular complexity

### Entropy Change of System, $\Delta S_\text{sys}$
Also a state function, and operates similarly as with enthalpy change.

$$\Delta S_\text{sys} = \sum n_\text{product} S_\text{ product} - \sum n_\text{ reactant} S_\text{reactant}$$

### Entropy Change of Surroundings, $\Delta S_\text{surr}$
Change in entropy in the surrounding, which is essentially just the following:

$$\Delta S_\text{surr} = \frac{-\Delta H_\text{sys}}{T}$$

### Entropy of Universe, $\Delta S_\text{univ}$

Combined entropy of system and surrounding, the entropy of the universe is supposed to be positive for any spontaneous process, that is to say that the entropy of the universe increaes as time goes by. (**Second Law of Thermodynamics**)

$$
\begin{align*}
\Delta S_\text{univ} &= \Delta S_\text{sys}+\Delta S_\text{surr} \\ 
&= \Delta S_\text{sys}-\frac{\Delta H_\text{sys}}{T}
\end{align*}
$$


## Gibbs Free Energy, $G$

Basically just the Entropy of the Universe, but with a fancier name.

|Situation|Entropy of Universe, $\Delta S_\text{univ}$|Gibbs Free Energy, $\Delta G$|Reaction Quotient, $Q$|
|---|---|---|---|
|Spontaneous|$+$|$-$|$Q<K$|
|Equilibrium|$0$|$0$|$Q=K$|
|Spontaneous in Reverse Direction|$-$|$+$|$Q > K$|

### Gibbs Free Energy at Standard State Conditions, $\Delta G^\circ$

$$
\begin{align*}
\Delta G^\circ &= -T\Delta S^\circ_\text{univ} \\
&= \Delta H^\circ_\text{sys} - T\Delta S^\circ_\text{sys}
\end{align*}
$$

As you can see, it's basically the same thing.

### Gibbs Free Energy under Non-Standard State Conditions, $\Delta G$

Under Non-Standard State Conditions, we have to adjust the Gibbs Free Energy to match said conditions. This is done by the following expression:

$$\Delta G = \Delta G^\circ{} + RT \ln Q$$

Where Q is the reaction quotient. For aqueous conditions, this is $Q_c$ (i.e. concentration is in focus), while in gaseous conditions, this is $Q_p$ (i.e. pressure is in focus).

One thing of note is that at equilibrium, $\Delta G$ is equivalent to 0. Thus, we have the following expression:

$$\Delta G^\circ{} = - RT \ln K$$

This can be used to compute standard state Gibbs Free Energy or the Equilibrium Constant.


```kt
// TODO('diagrams')
```