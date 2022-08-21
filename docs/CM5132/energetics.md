# Chemical Energetics


## Summary (for those in a hurry)
- $U = q_\text{in system} - w_\text{by system} = n \Delta H - p \Delta V = -(mc+C)\Delta T-p\Delta V$
- Standard State ($H^{\circ}$) is 1M for aqueous, 1 atm for gaseous and pure otherwise

|Name|Symbol|Definition|
|---|---|--------------|
|Formation Enthalpy|$\Delta H_f$|Enthalpy change to form one mole of molecule|
|Combustion Enthalpy|$\Delta H_c$|Enthalpy change to combust one mole of molecule (always exothermic)|
|Neutralisation Enthalpy|$\Delta H_n$|Enthalpy change to form one mole of water in neutralisation|
|Atomization Enthalpy|$\Delta H_a$|Enthalpy change to form one mole of element for uni-elemental or to react one mole of molecule for multi-elemental molecules (always endothermic)|
|Bond Energy|$BE$|Energy required to break one mole of said bond (always endothermic)|
|Lattice Energy|$\Delta H_\text{LE}$|Energy required to dissociated a solid ionic lattice into gaseous ions (always endothermic)|
|$n$th Ionization Energy|$\Delta H_{n\text{th IE}}$|Energy required for element to release $n$th electron|
|$n$th Electron Affinity|$\Delta H_{n\text{th EA}}$|Energy required for element to accept $n$th electron|
|Hydration Enthalpy|$\Delta H_{hyd}$|Energy required to dissolve gaseous ions into water (always exothermic)|
|Solution Enthalpy|$\Delta H_\text{solution}$|Energy required to dissolve anything into water|

## First Law of Thermodynamics
$$
\begin{align*}
\Delta U &= q - w  \\
&= n \Delta H - p \Delta V
\end{align*}
$$

Where $\Delta U$ is the change in internal energy of the system, $q$ is the heat absorbed by the system and $w$ is the work done by the system. $\Delta H$ is the enthalpy change of a given reaction within the system, $p$ is the pressure exerted, $\Delta V$ is the change in volume of the system.


## Enthalpy, $\Delta H$
Essentially change in heat of system caused by any particular reaction taking place within said system.

It is a **state function**, which means every path to get from one set of reactants to one set of products requires the same enthalpy change. This also means that the reverse reaction has the opposite polarity and same magnitude of enthalpy change. This is known as **Hess's Law**.

### Standard State Enthalpy, $\Delta H ^{\circ}$

Enthalpy change is not the same at every point. Different variables like temperature, pressure and concentration and more can influence the enthalpy change. Standard State is defined to be the following:

|State|Condition for Standard State Enthalpy|
|----|--------------|
|Liquid, Solid|Pure|
|Gaseous|1 atm|
|Aqueous|1 M|

### Computing $\Delta H$ experimentally

In most reactions, we often conduct it in water, or on a surface not participating in the reaction (or both, like in a Calorimeter). In this case, we must know the following values:

- Specific Heat Capacity of the **Solution**: $c$
- Mass of the **Solution**: $m$
- Heat Capacity of Surface: $C$
- Change in Temperature: $\Delta T$

From here, we can compute the energy absorbed/supplied by the surroundings via the formula $q = mc\Delta T + C\Delta T$. This is the energy released for the given moles of reactants, so we need to divide it by said number of moles reacted to get the actual Enthalpy Change. Thus:

$$\Delta H = -\frac{mc\Delta T + C\Delta T}{n_\text{limit}}$$

### Enthalpy of Formation, $\Delta H_f$

Formation Enthalpy is the enthalpy of the reaction that forms the compound from its constituent elements. Note that these elements should be in their most stable allotropic state, which essentially means the state they are most likely to be found in. For a compound $\text{ABC}$, where $\text{A}$ exists in the form of gaseous $\text{A}_2$ for stability, $\text{B}$ remains in solid state and $C$ is Carbon, we have the following expression:

$$\frac{1}{2}\text{ A}_2\text{ (g) } + \text{ B (s) } + \text{ C (graphite)} \rightarrow \text{ABC}\quad\quad\Delta H_f$$

For elements in their most stable allotropic state, their $\Delta H_f$ is 0. This is why the Formation Enthalpies of Graphite and Oxygen gas are 0, while those of Diamond or Ozone are not.

#### Using $\Delta H_f$ meaningfully
An extension of this is seen when we are required to compute the enthalpy change of any given reaction. Since we can simplify all reactants to the their allotropic elements via the reverse reaction, and produce the products from said allotropes, we can essentially represent the the reaction enthalpy as follows:

$$\Delta H_{rxn} = \sum n_\text{product} \Delta H_{f, \text{ product}} - \sum n_\text{ reactant} \Delta H_{f, \text{reactant}}$$

This makes it easier for us to retrieve the enthalpy change of a reaction.

### Enthalpy of Combustion, $\Delta H_c$

Combustion is **ALWAYS** an exothermic reaction, so this enthalpy is always negative. The general reaction is as follows:

$$\text{C}_x\text{H}_y\text{O}_z+\frac{4x+y-2z}{4}\text{ O}_2\text{ (g) } \rightarrow x \text{ CO}_2 + \frac{y}{2}\text{ H}_2\text{O}\quad\Delta H_c$$

### Enthalpy of Neutralisation, $\Delta H_n$

This is the enthalpy change of any given neutralisation reaction to form one mole of water.

$$\text{H}^+\text{ (aq)}+\text{OH}^-\text{ (aq)}\rightarrow \text{H}_2\text{O (l)} \quad\quad\Delta H_n$$

**Note:** The above reaction is simply the ionic reaction, this is actually still the enthalpy change of the actual reaction.

### Enthalpy of Atomization, $\Delta H_a$

Atomization has two cases, as follows:

#### $\Delta H_a$ for uni-elemental molecules

This pertain to the atomization enthalpy of any given molecule, and the reaction is such that one mole of the **elemental gas** is formed:

$$\frac{1}{n}\text{ X}_n \rightarrow \text{X (g)}\quad\quad\Delta H_a$$

#### $\Delta H_a$ for multi-elemental molecules

If any given molecule is made of more that a single elemnt, the reaction is such that one mole of the **molecule** is formed.

$$\text{X}_m\text{Y}_n \rightarrow m\text{ X (g) }+n\text{ Y (g)}\quad\quad\Delta H_a$$

#### Using $\Delta H_a$ meaningfully
Same thing as with $\Delta H_f$.

$$\Delta H_{rxn} = \sum n_\text{reactant} \Delta H_{a, \text{ reactant}} - \sum n_\text{product} \Delta H_{a, \text{ product}}$$


### Bond Energy, $BE$

This is technically a side-tour. Bond Energy is the energy required to overcome a bond (i.e it is endothermic, positive). The reaction for an example is as follows:

$$\text{Cl}-\text{Cl} \rightarrow 2\text{ Cl}\quad \quad BE_{\text{Cl}-\text{Cl}}$$

This is similar to the formation enthalpy (of course it's the reverse reaction), and it's only for one bond. But we can also use this meaningfully!
#### Using $BE$ meaningfully
Same thing as with $\Delta H_a$ honestly.

$$\Delta H_{rxn} = \sum BE_\text{bonds broken} - \sum BE_\text{bonds formed}$$

### Lattice Energy, $\Delta H_\text{LE}$
This is the energy required to dissociate a solid ionic lattice into gaseous ions, for instance as follows:

$$\text{X}_m\text{Y}_n\text{ (s)}\rightarrow m\text{ X}^{n+}\text{ (g) }+n\text{ Y}^{m-}\text{ (g) }\quad \Delta H_{LE}$$

This is proportional to the charges and inversely proportional to the ionic radii.

### Ionization Energy, $\Delta H_{n\text{th IE}}$
Basically the energy required for a gaseous atom/ ion to release an electron.

$$
\begin{align*}
\text{X (g) }&\rightarrow\text{X}^+\text{ (g) }+ e^- \quad\quad \Delta H_\text{1st IE} \\
\text{X}^+\text{ (g) }&\rightarrow\text{X}^{2+}\text{ (g) }+ e^- \quad\quad \Delta H_\text{2nd IE} \\
\text{X}^{2+}\text{ (g) }&\rightarrow\text{X}^{3+}\text{ (g) }+ e^- \quad\quad \Delta H_\text{3rd IE}
\end{align*}
$$

### Electron Affinity, $\Delta H_{n\text{th EA}}$
Basically the energy required for a gaseous atom/ ion to absorb an electron.

$$
\begin{align*}
\text{X (g) }+e^-&\rightarrow\text{X}^-\text{ (g)}\quad\quad \Delta H_\text{1st EA} \\
\text{X}^-\text{ (g) }+e^-&\rightarrow\text{X}^{2-}\text{ (g)}\quad\quad \Delta H_\text{2nd EA} \\
\text{X}^{2-}\text{ (g) }+e^-&\rightarrow\text{X}^{3-}\text{ (g)}\quad\quad \Delta H_\text{3rd EA}
\end{align*}
$$

### Enthalpy of Hydration, $\Delta H_{hyd}$
This is an always exothermic reaction to dissolve gaseous ions into water. It is proportional to the charge density ($|Q|/r$).

$$
\begin{align*}
\text{X}^{m+}\text{ (g) }&\rightarrow\text{ X}^{m+}\text{ (aq)}\quad\quad\Delta H_{hyd, \text{ cation}}\\
\text{Y}^{n-}\text{ (g) }&\rightarrow\text{ Y}^{n-}\text{ (aq)}\quad\quad\Delta H_{hyd, \text{ anion}}
\end{align*}
$$

### Enthalpy of Solution, $\Delta H_\text{solution}$
This is the enthalpy change to dissolve any ionic lattice into water. Thus it is simply as follows:

$$\Delta H_\text{solution} = \Delta H_\text{LE} + \Delta H_{hyd}$$


## Representation

### Energy Cycle Diagram
![Example of Energy Cycle Diagram](https://chemistryguru.com.sg/images/energy_cycle_using_enthalpy_change_of_formation_-_formation_of_CO2.png)

### Energy Level Diagram
![Example of Energy Level Diagram](https://chemistryguru.com.sg/images/Born_Haber_Cycle-atomisation.png)


#### Born-Haber Cycle
Very similar, except it's only used when doing IE and EA computations.
![Example of Born-Haber Cycle](https://chemistryguru.com.sg/images/Born_Haber_Cycle-lattice_energy.png)

