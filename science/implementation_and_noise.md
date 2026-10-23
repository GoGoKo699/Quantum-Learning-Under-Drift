# Physical implementation and noise

The prediction separation concerns access to a persistent quantum register. Its implementation requires the global SWAP measurement with the specified state update, together with enough coherence to retain an $`n`$-qubit register between arrivals. The bounds below separate errors of that complete logical operation from noise on individual physical gates or qubits.

## The retained-memory instrument

Let $`M`$ be the memory, $`X`$ the current input, and $`S`$ the unitary that swaps these two $`d`$-dimensional registers. The ideal measurement has projectors

```math
P_\pm=\frac{I\pm S}{2}.
```

Predict signal on the plus outcome and background on the minus outcome. Discard $`X`$ after the measurement and retain $`M`$. The full channel, including the classical output, is

```math
\mathcal J(\omega_{MX})
=\sum_{y\in\{+,-\}} |y\rangle\langle y|
  \otimes\mathrm{Tr}_X(P_y\omega_{MX}P_y).
```

For a product input $`\sigma\otimes\rho`$, tracing out the outcome gives

```math
\mathrm{Tr}_{Y}\mathcal J(\sigma\otimes\rho)
=\frac{\sigma+\rho}{2}.
```

The conditional retained states generally depend on the outcome. The displayed nonselective identity is sufficient because subsequent ideal operations do not depend on previous predictions. The [quantum prediction proof](quantum_prediction.md) uses this instrument and the conditional independence of a freshly supplied input from the learner's memory, given the source history.

For $`d=2^n`$, the usual SWAP-test circuit prepares an ancilla in $`|0\rangle`$, applies a Hadamard, a controlled global SWAP, another Hadamard, and a computational-basis measurement of the ancilla. Its two Kraus operators on $`MX`$ are exactly $`P_+`$ and $`P_-`$. See [Buhrman et al.](../references/RELATED_WORK.md#buhrman2001) for the underlying SWAP test.

The controlled global SWAP decomposes into $`n`$ controlled-SWAP gates, all sharing that ancilla, between corresponding memory and input qubits. This uses $`O(n)`$ logical gates, $`n`$ persistent memory qubits, $`n`$ incoming qubits, and one ancilla. The straightforward implementation has sequential depth $`O(n)`$; physical connectivity and fault tolerance may add costs. The memory must survive the interval between source arrivals, including preparation time. The input register and ancilla are consumed; the retained register remains available for the next arrival.

## Outcome statistics do not specify the memory update

Measuring a SWAP observable separately on every corresponding qubit pair and multiplying the signs has the same two-outcome probabilities as the global SWAP observable. It refines the measurement, however, and generally implements a different retained-memory channel. A destructive test also leaves no quantum register to retain.

For a concrete distinction, take two-qubit registers with memory $`|00\rangle`$ and input $`|11\rangle`$. The global Lüders instrument above leaves the nonselective memory state

```math
\frac12|00\rangle\langle00|+\frac12|11\rangle\langle11|.
```

Independently measuring the two local SWAP observables leaves $`I_4/4`$ after discarding the input and all outcomes. The trace distance between these retained states is $`1/2`$. Therefore an implementation that merely reproduces the parity outcome probabilities cannot be substituted into the rolling-memory proof. This finite example is included in the [verification suite](../verification/README.md).

## Uniform error of the complete instrument

Use the half-diamond convention

```math
\delta=\frac12\|\widetilde{\mathcal J}_t-\mathcal J\|_\diamond.
```

Assume this bound holds uniformly at each step for the full map from the two input registers to the retained memory and the classical prediction. Any inter-arrival storage error is included in that step's map. Time-varying instruments are allowed; dependence on previous classical outputs is also allowed if the same bound holds for every such history. This assumption is about channels on the stated registers, without an uncontrolled environment carrying an additional correlated quantum memory between steps.

Couple the ideal and perturbed learners to the same source realization. Average over their internal measurement outcomes, and let $`e_t`$ be the source-averaged trace distance between their memory states immediately before arrival $`t`$. For fixed incoming $`\rho`$, the ideal memory channel contracts differences by exactly one half:

```math
\frac12\left\|
\frac{\sigma+\rho}{2}-\frac{\tau+\rho}{2}
\right\|_1
=\frac12\left(\frac12\|\sigma-\tau\|_1\right).
```

Trace-distance contractivity and the instrument error consequently imply

```math
e_{t+1}\le\frac12e_t+\delta.
```

With identical initial memories, $`e_1=0`$, this yields

```math
e_t\le2\delta\bigl(1-2^{-(t-1)}\bigr).
```

For the ideal instrument and a fixed current hidden pure state $`P`$, the balanced-label accuracy is

```math
A(\sigma,P)=\frac12+
\frac{\mathrm{Tr}(\sigma P)-1/d}{4}.
```

Changing the memory changes this accuracy by at most one quarter of the memory trace distance. Changing the complete instrument at fixed memory changes any success probability by at most $`\delta`$. Therefore

```math
|\widetilde A_t-A_t|
\le\delta+\frac14e_t
\le\delta\left(\frac32-2^{-t}\right)
\le\frac32\delta.
```

This controls the expected accuracy uniformly in time, rather than allowing a sum growing with the number of arrivals. If the full diamond norm is instead denoted by $`\varepsilon`$, the final bound is $`3\varepsilon/4`$. In particular, the noisy learner's liminf per-round expected advantage, and its liminf expected average advantage, are at least $`b_{\mathrm{SWAP}}-3\delta/2`$. This is a nonzero advantage guarantee when that quantity is positive; it requires no stationary noise process.

## An exactly solvable global-noise model

For illustration, let signal inputs be

```math
\rho_{\mathrm{sig}}=\eta P+(1-\eta)I/d,
\qquad 0\le\eta\le1,
```

while backgrounds remain $`I/d`$. Between arrivals, apply the global memory channel $`\sigma\mapsto\lambda\sigma+(1-\lambda)I/d`$, with $`0\le\lambda\le1`$, and otherwise perform the ideal instrument.

Define the normalized memory alignment with the current hidden state by

```math
a_t=\frac{\mathbb E\mathrm{Tr}(\sigma_tP_t)-1/d}{1-1/d}.
```

Its recursion and stationary value are

```math
a_{t+1}=\lambda q\left(\frac{a_t}{2}+\frac\eta4\right),
\qquad
a_\infty=\frac{\lambda q\eta}{2(2-\lambda q)}.
```

The exact stationary prediction advantage is

```math
b_{\mathrm{SWAP}}^{\lambda,\eta}
=\frac{(1-1/d)\lambda q\eta^2}{8(2-\lambda q)}.
```

This formula describes global depolarization of the logical register and a specified global signal visibility. It is not a model of independent constant-strength noise on every physical qubit.

## Relation to local physical noise

A constant bound on the error of each constituent gate does not imply a dimension-independent bound on the total instrument error. Composing $`O(n)`$ noisy operations gives, by the direct diamond-norm triangle bound, a total error at most the sum of their individual half-diamond errors. That sum can grow with $`n`$. Physical memory noise also depends on how long a state must be stored while the next input is prepared.

This distinction is consequential for high-dimensional quantum data. The local-noise purity-testing obstruction in [Noisy quantum learning theory](../references/RELATED_WORK.md#noisy2026) shows why ideal multi-copy or memory-assisted access should not be equated with resilience to constant local noise. The present prediction theorem assumes coherent logical access to its input and memory registers. The uniform instrument bound gives a sufficient accuracy condition for a concrete implementation; it does not supply an error-correction construction or a local-noise threshold.
