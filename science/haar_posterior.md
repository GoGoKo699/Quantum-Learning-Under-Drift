# Predicting a Haar state from a classical training record

This page proves the measure-training-first bound used in the [classical online converse](classical_prediction.md). A learner receives several copies of an unknown pure state, converts them into a classical record, and then classifies one fresh specimen. The restriction concerns what survives between training and prediction: training measurements can be collective, and classical storage is unlimited.

The arbitrary-effect posterior identity below is established in [Hayashi, Dasgupta, and Warsi](../references/RELATED_WORK.md#hayashi2026). We give its derivation and the binary classification consequence needed here. The Haar moment machinery is also standard in the [quantum-design literature](../references/RELATED_WORK.md#brandao2016).

## Experiment and exact optimum

Let $`P=|\psi\rangle\langle\psi|`$ be Haar distributed on the pure states of $`\mathbb C^d`$, with $`d\ge2`$. A learner first receives $`m`$ copies, $`P^{\otimes m}`$. It performs an arbitrary POVM and keeps only its classical outcome $`Z`$. A fresh test specimen is then supplied in one of the states

```math
\rho_Y(P)=
\begin{cases}
P,&Y=1,\\
I/d,&Y=0,
\end{cases}
\qquad \Pr(Y=0)=\Pr(Y=1)=\frac12,
```

where $`Y`$ is independent of the training experiment. The learner may choose any test measurement as a function of its classical record. There is no surviving quantum training register.

**Proposition.** The optimal success probability in this experiment is

```math
p_m^{\mathrm{cl}}
=\frac12+\frac{m(d-1)}{2d(d+m)}.
```

In particular, the optimum is $`1/2`$ at $`m=0`$. Independent side information, auxiliary randomness, and ancillary states independent of $`P`$ do not change the bound: they can be absorbed into the training POVM or a mixture of such POVMs.

## Posterior mean for an arbitrary training effect

Write $`\Pi_m`$ for the projector onto the symmetric subspace of $`(\mathbb C^d)^{\otimes m}`$, and

```math
D_m=\operatorname{Tr}\Pi_m=\binom{d+m-1}{m}.
```

For $`m\ge1`$, let $`M_z`$ be a training POVM effect with nonzero outcome probability. The formulas apply equally to an effect density for a continuous outcome. Define

```math
A_z=\Pi_m M_z\Pi_m,\qquad
a_z=\operatorname{Tr}A_z,\qquad
B_z=\frac{A_z}{a_z},\qquad
\tau_z=\operatorname{Tr}_{2,\ldots,m}B_z.
```

The state $`B_z`$ is supported on the symmetric subspace, so all of its one-particle reductions equal the density matrix $`\tau_z`$.

The normalized Haar moments are

```math
\int P^{\otimes k}\,dP=\frac{\Pi_k}{D_k}.
```

Indeed, the integral is invariant under every $`U^{\otimes k}`$, has support in the symmetric subspace, and has trace one. Irreducibility of the symmetric representation gives the stated normalization. It follows that

```math
\Pr(Z=z)=\int\operatorname{Tr}(M_zP^{\otimes m})\,dP
=\frac{a_z}{D_m}.
```

Let $`R_z=\mathbb E[P\mid Z=z]`$ be the posterior predictive state. Its unnormalized numerator is

```math
N_z
=\int P\,\operatorname{Tr}(M_zP^{\otimes m})\,dP
=\frac{1}{D_{m+1}}
\operatorname{Tr}_{1,\ldots,m}
\bigl[(A_z\otimes I)\Pi_{m+1}\bigr].
```

To evaluate the partial trace, use the permutation identity

```math
\Pi_{m+1}
=\frac{1}{m+1}
\left(I+\sum_{i=1}^{m}S_{i,m+1}\right)
(\Pi_m\otimes I).
```

Here $`S_{i,m+1}`$ exchanges training register $`i`$ with the test register. The identity follows by partitioning the permutations of $`m+1`$ objects according to the image of the last object. Because $`A_z=\Pi_m A_z\Pi_m`$, the identity term contributes $`a_zI`$ to the partial trace, while each swap term contributes the corresponding one-particle reduction, $`a_z\tau_z`$. Therefore

```math
N_z=\frac{a_z}{(m+1)D_{m+1}}(I+m\tau_z).
```

Since $`(m+1)D_{m+1}=(d+m)D_m`$, normalization gives the exact identity

```math
\boxed{R_z=\frac{I+m\tau_z}{d+m}.}
```

No rank-one assumption on $`M_z`$ is used. This is why the identity applies to arbitrary collective training measurements, including measurements that simulate an adaptive sequence of individual operations.

## From the posterior to a classification bound

Conditioned on $`Z=z`$, the two test hypotheses are $`R_z`$ and $`I/d`$, with the same equal prior probabilities. For any two states $`R,S`$, a two-outcome effect $`0\le E\le I`$ has equal-prior success probability

```math
\frac12\operatorname{Tr}(ER)
+\frac12\operatorname{Tr}[(I-E)S]
=\frac12+\frac12\operatorname{Tr}[E(R-S)].
```

The largest value is obtained by projecting onto the positive eigenspace of $`R-S`$. As $`\operatorname{Tr}(R-S)=0`$, the sum of its positive eigenvalues is $`\|R-S\|_1/2`$. Thus the optimal success probability is $`1/2+\|R-S\|_1/4`$.

For the posterior above,

```math
R_z-\frac Id
=\frac{m}{d+m}\left(\tau_z-\frac Id\right).
```

Every density matrix $`\tau`$ satisfies

```math
\left\|\tau-\frac Id\right\|_1
\le 2\left(1-\frac1d\right).
```

One way to see this is to decompose $`\tau`$ into pure states and use convexity of the trace norm; each pure state has exactly the displayed distance from $`I/d`$. Consequently, for every nonzero-probability training record,

```math
\Pr(\widehat Y=Y\mid Z=z)
\le\frac12+\frac{m(d-1)}{2d(d+m)}.
```

Averaging over $`z`$ proves the upper bound. When $`m=0`$, the averaged signal state is already $`I/d`$, so the success probability is exactly $`1/2`$.

## Attainment by a covariant training measurement

For $`m\ge1`$, use the covariant POVM with effect density

```math
dM(\phi)=D_m
\bigl(|\phi\rangle\langle\phi|\bigr)^{\otimes m}\,d\phi.
```

It integrates to $`\Pi_m`$; adding the outcome $`I-\Pi_m`$ completes a POVM on the full training Hilbert space, and this extra outcome never occurs on $`P^{\otimes m}`$. For an observed $`\phi`$, the one-particle reduction is pure:

```math
\tau_\phi=|\phi\rangle\langle\phi|,
\qquad
R_\phi=\frac{I+m|\phi\rangle\langle\phi|}{d+m}.
```

The positive eigenspace of $`R_\phi-I/d`$ is precisely the span of $`\phi`$. Measure the test using

```math
\left\{|\phi\rangle\langle\phi|,
I-|\phi\rangle\langle\phi|\right\},
```

and predict signal on the first outcome. This saturates the trace-distance bound for every training record and proves the exact optimum.

The attainment statement is information theoretic. The online converse only needs the upper bound and grants arbitrary measurements, without assuming that this continuous covariant POVM has an efficient gate implementation.
