# Model and exact results

The central resource is information retained between successive quantum inputs. A classical record can describe earlier measurement outcomes with unlimited precision. A coherent register can preserve a physical state for comparison with a later specimen. A changing latent source makes the age of that information matter.

This page fixes the common experiment and the quantifiers of the results. The [Haar posterior](haar_posterior.md), [classical prediction](classical_prediction.md), and [quantum prediction](quantum_prediction.md) pages contain the proofs. [Efficient sources](efficient_sources.md) and [implementation and noise](implementation_and_noise.md) state the extensions under their own assumptions.

## 1. Source and timing

Fix a dimension $`d\ge2`$ and a refresh probability $`0<r<1`$; write $`q=1-r`$. Both parameters and the source law are known to the learner. A hidden rank-one projector $`P_1`$ is drawn from the unitarily invariant Haar distribution. At each transition,

```math
P_{t+1}=
\begin{cases}
P_t,&\text{with probability }q,\\
P'_{t+1},&\text{with probability }r,
\end{cases}
```

where each $`P'_{t+1}`$ is a fresh independent Haar draw. Refresh choices are independent of all labels and of the learner. They partition the stream into epochs of mean length $`1/r`$.

At round $`t`$, an independent fair bit $`Y_t`$ selects the incoming density operator

```math
\rho_{Y_t}(P_t)=
\begin{cases}
P_t,&Y_t=1\quad\text{(signal)},\\
I/d,&Y_t=0\quad\text{(background)}.
\end{cases}
```

Conditioned on the complete hidden state path and labels, the emitted systems have product state $`\bigotimes_t\rho_{Y_t}(P_t)`$. The learner's operations cannot change the source's latent process or future emissions. The unlabeled state within an epoch is $`(P_t+I/d)/2`$.

Each round has the following causal order:

1. The learner receives exactly one physical specimen.
2. It processes that specimen and its permitted memory, outputs $`\widehat Y_t`$, and updates its memory.
3. The next specimen arrives. Earlier predictions are final.

The learner receives neither true labels nor refresh flags. It has no preparation circuit description, inverse circuit, extra-copy oracle, or reference copy of the hidden state. For both learner classes, all initial memory and internal randomness are independent of the complete source process. The physical source supplies quantum data directly. There is no classical-data loading promise or QRAM assumption.

An epoch records a refresh event, rather than a test that successive hidden states are unequal. This distinction matters for the finite ensembles in the [source corollary](efficient_sources.md), where independent draws can coincide.

## 2. Learner classes

### Classical records

A classical-record learner has unlimited classical memory, numerical precision and computation. It may choose an arbitrary quantum instrument on each current specimen, with fresh ancillas and controls determined by its entire classical history. It may reprepare any state described by that history. Before the next arrival, all information it retains is classical.

Thus the restriction is on coherent retention across arrival times, not on the complexity of an individual measurement or the size of a classical computer. Arbitrary adaptive POVMs and randomized policies are included. A current measurement may produce both the prediction and additional classical outcomes used later.

### Quantum memory

A quantum learner may retain quantum systems between arrivals and combine them coherently with the next specimen. Its initial memory and internal randomness are independent of the hidden source. The optimal quantum comparison permits arbitrary quantum memory and processing.

The constructive lower bound uses only one $`d`$-dimensional retained register. When $`d=2^n`$, it needs $`n`$ persistent logical qubits, $`n`$ current-input qubits, and one measured ancilla during each global SWAP test. [Implementation](implementation_and_noise.md) specifies the instrument and gate costs.

Both classes receive the same specimens and obey the same prediction deadline. The stronger pure-copy experiment used in the classical proof is a mathematical upper-bound device, not a resource granted to the actual quantum algorithm.

## 3. Accuracy and optimality

For a policy $`\mathcal A`$ and horizon $`T`$, define its expected average advantage over a fair guess by

```math
\beta_{\mathcal A,T}(d,r)
=\frac1T\sum_{t=1}^{T}
\Pr_{\mathcal A}(\widehat Y_t=Y_t)-\frac12.
```

The probability averages source draws, refresh events, labels, measurement outcomes and any policy randomness. Define

```math
\beta_{\mathrm C}(d,r)
=\sup_{\mathcal A\in\mathrm C}\limsup_{T\to\infty}\beta_{\mathcal A,T}(d,r),
\qquad
\beta_{\mathrm Q}(d,r)
=\sup_{\mathcal A\in\mathrm Q}\limsup_{T\to\infty}\beta_{\mathcal A,T}(d,r).
```

Policies may depend on $`d,r`$ and time; the upper bounds do not assume stationary, finite-memory or computationally efficient policies. The statements concern expected accuracy, not a high-probability bound for each realized trajectory. The optimal quantities are nonnegative because random guessing is allowed.

## 4. Matching prediction law

**Theorem 1 — uniform correlation-lifetime frontier.** For every $`d\ge2`$ and $`0<r<1`$,

```math
\frac{q}{128e^3(1+rd)}
\le\beta_{\mathrm C}(d,r)
\le\frac{(1-1/d)q}{2(rd+q)}
\le\frac{q}{1+rd},
```

and

```math
\frac{(1-1/d)q}{8(1+r)}
\le\beta_{\mathrm Q}(d,r)
\le\frac{(1-1/d)q}{2}.
```

In particular,

```math
\beta_{\mathrm C}(d,r)=\Theta\!\left(\frac{q}{1+rd}\right),
\qquad
\beta_{\mathrm Q}(d,r)=\Theta(q),
\qquad
\frac{\beta_{\mathrm Q}(d,r)}{\beta_{\mathrm C}(d,r)}=\Theta(1+rd),
```

with universal constants. This is constant-factor optimal scaling, not an exact formula for either optimal accuracy.

The classical lower bound is attained in order by measuring in a fixed basis and testing whether the current outcome appears in a cache of length $`L=\lfloor\min(d,1/r)\rfloor`$. The classical upper bound follows from a stronger per-round learning experiment and the [inherited Haar posterior identity](haar_posterior.md). A nondestructive SWAP measurement with one retained register gives the displayed quantum lower bound. On a fresh redraw, no learner has prior information about the current hidden state; this supplies the quantum upper bound.

### Finite horizons

The classical upper bound in Theorem 1 holds for every $`T`$. The cache strategy, making random predictions while initially filling its cache, obeys

```math
\beta_{\mathrm{cache},T}
\ge\left(1-\frac LT\right)_+
\frac{q}{128e^3(1+rd)}.
```

Here $`x_+=\max(x,0)`$. For the SWAP learner initialized in $`I/d`$, set

```math
B_{\mathrm{swap}}=\frac{(1-1/d)q}{8(1+r)}.
```

Its exact expected average advantage is

```math
\beta_{\mathrm{swap},T}
=B_{\mathrm{swap}}
\left[1-\frac{1-(q/2)^T}{T(1-q/2)}\right].
```

Consequently the matching classical scaling is attained after a horizon comparable to $`L`$, and the SWAP learner has a dimension-independent startup time. These are startup statements for the displayed policies, with no claim of exact finite-horizon optimality.

## 5. Source-construction corollary

The exact theorem above concerns Haar-distributed hidden states. Generic exact Haar preparation need not have polynomial cost in $`n`$. A separate result uses a known ensemble of pure states with exact first moment $`I/d`$ and sufficiently accurate higher moments.

**Theorem 2 — efficiently generated separation.** For each fixed $`0<r<1`$ and $`d=2^n`$, there are finite-gate, polynomial-size hidden-state preparation circuits for which every classical-record learner has long-run advantage $`O(2^{-n})`$, while the same retained-register SWAP learner has constant advantage. The ensemble is known, but the newly sampled circuit and seed for each epoch are hidden. Preparation costs are charged equally to the two learners.

The [full source theorem](efficient_sources.md) gives the trace/diamond-norm approximation convention, the geometric age-tail bound, and the extension to inverse-polynomial refresh rates. It does not silently replace the complete Haar crossover by an efficiently prepared family in every parameter regime.

## 6. Endpoints and interpretation

At $`r=1`$, every incoming signal is a fresh independent draw with mean $`I/d`$. Both classes have zero advantage. Their ratio is undefined.

At $`r=0`$, the hidden state is fixed forever. For fixed $`d`$, perform a fixed informationally complete measurement at rounds $`t=k^2`$ and use all other rounds for prediction. There are infinitely many estimation samples, but their fraction tends to zero. Conditional on $`P`$, these samples are independent copies of $`(P+I/d)/2`$, so their empirical outcome frequencies consistently determine this state. Its largest eigenvalue has gap $`1/2`$; therefore the leading eigenprojector of the estimate converges to $`P`$. Testing the remaining specimens against that estimated projector approaches the known-state Helstrom accuracy $`1-1/(2d)`$. Bounded convergence and averaging over rounds give the same long-run expected accuracy. No learner can exceed the known-state optimum, so both classes attain it at this endpoint. The stationary geometric-age proof is not used here.

The initialized latent process, and hence the observed input process, is stationary in distribution for all $`r`$. Refreshing its latent concept gives it a finite correlation lifetime. The [interpretation page](interpretation.md) explains why that lifetime, rather than total archive length, controls the prediction law.
