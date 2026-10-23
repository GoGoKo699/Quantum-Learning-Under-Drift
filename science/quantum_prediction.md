# Quantum prediction with one retained register

In the [drifting-state model](model.md), a single retained $`d`$-dimensional register suffices for an expected predictive advantage proportional to the persistence probability $`q=1-r`$. This page gives the physical measurement instrument, its exact finite-horizon accuracy, and a converse that permits arbitrary quantum memory.

The SWAP test is an established primitive, including in [quantum fingerprinting](../references/RELATED_WORK.md#buhrman2001). Retaining registers after symmetry measurements is also part of prior work on [streaming purification](../references/RELATED_WORK.md#childs2025) and [quantum online learning](../references/RELATED_WORK.md#zheng2026). The claim proved here is the resulting accuracy under hidden refreshes and its comparison with the [classical-memory frontier](classical_prediction.md).

## Result

Let $`\mathsf Q`$ contain all causal policies with arbitrary quantum and classical memory, initialized independently of the source. Define

```math
\beta_Q(d,r)
=\sup_{\mathcal A\in\mathsf Q}
\limsup_{T\to\infty}
\frac1T\sum_{t=1}^T
\left[\Pr_{\mathcal A}(\widehat Y_t=Y_t)-\frac12\right].
```

For $`d\ge2`$, $`0<r<1`$, and $`q=1-r`$,

```math
\frac{(1-1/d)q}{8(2-q)}
\le\beta_Q(d,r)
\le\frac{q(1-1/d)}{2}.
```

In particular,

```math
\boxed{\frac q{32}\le\beta_Q(d,r)\le\frac q2.}
```

The lower bound is achieved with one retained register of dimension $`d`$. The upper bound allows unlimited quantum memory. Exact optimality of the proposed protocol is not needed for this constant-factor characterization.

## A physical retained-register SWAP instrument

Prepare a memory register $`M`$ in $`I/d`$. On each arrival, let $`B`$ denote the current input and perform the projective measurement

```math
\Pi_+=\frac{I+S}{2},\qquad
\Pi_-=\frac{I-S}{2}
```

on $`M\otimes B`$, where $`S`$ swaps the two registers. Predict signal on $`+`$ and background on $`-`$. Retain register $`M`$ after the measurement and discard $`B`$.

The instrument can be implemented by an ancilla initially in $`|0\rangle`$, a Hadamard gate, a controlled SWAP of the two data registers, another Hadamard, and computational-basis measurement of the ancilla. The induced Kraus operators on the data are exactly $`\Pi_+`$ and $`\Pi_-`$. Thus the data registers remain available after the ancilla is read. They are generally disturbed; no assumption of preserving either individual input state is made. A destructive implementation that measures both data registers would not implement the retained-memory protocol.

For $`d=2^n`$, a register SWAP is the product of $`n`$ pairwise swaps, so the controlled operation uses $`O(n)`$ elementary controlled-swap gates, each with a constant-size standard gate decomposition. The protocol retains $`n`$ qubits between arrivals and uses, while processing an input, another $`n`$ input qubits and one ancilla. Its memory must remain coherent over an arrival interval. The [implementation discussion](implementation_and_noise.md) specifies the ideal or protected logical-access assumptions and source costs.

## Exact averaged memory update

Condition on the hidden path and on the learner's previous measurement record. Let $`\sigma`$ be the memory state before the current arrival and $`\rho`$ the fresh input state. The model's conditional product-state assumption ensures that the joint input is $`\sigma\otimes\rho`$. The nonselective postmeasurement joint state is

```math
\begin{aligned}
\sum_{s\in\{+,-\}}\Pi_s(\sigma\otimes\rho)\Pi_s
&=\frac12\left[
\sigma\otimes\rho+S(\sigma\otimes\rho)S
\right]\\
&=\frac12(\sigma\otimes\rho+\rho\otimes\sigma).
\end{aligned}
```

Tracing out the current input therefore gives the averaged update

```math
\overline\sigma^{\,+}=\frac{\sigma+\rho}{2}.
```

This equation averages over the newly observed SWAP outcome. The conditional retained state in an individual branch need not equal this average. The recurrence below uses linear observables of the memory, so the nonselective update gives their exact expectations without neglecting outcome-dependent backaction.

For a fixed current hidden state $`P_t`$ and memory state $`\sigma_t`$, the SWAP probabilities satisfy

```math
\Pr(+\mid Y_t=1)=\frac{1+\mathrm{Tr}(\sigma_tP_t)}2,
\qquad
\Pr(+\mid Y_t=0)=\frac{1+1/d}{2}.
```

The fair-label success probability is consequently

```math
\Pr(\widehat Y_t=Y_t\mid \sigma_t,P_t)
=\frac12+
\frac{\mathrm{Tr}(\sigma_tP_t)-1/d}{4}.
```

## Correlation recursion and stationary accuracy

Define the averaged overlap and its excess over an independent reference by

```math
x_t=\mathbb E\mathrm{Tr}(\sigma_tP_t),
\qquad y_t=x_t-\frac1d.
```

The initial memory gives $`y_1=0`$. Averaged over the current fair label, the input state is $`(P_t+I/d)/2`$. After the memory update, its overlap with the same hidden state has expectation

```math
\mathbb E\mathrm{Tr}(\sigma_t^+P_t)
=\frac{x_t}{2}+\frac{1+1/d}{4}.
```

With probability $`q`$, the next hidden state is the same state. With probability $`r`$, it is an independent Haar draw and its expected overlap with any retained memory state is $`1/d`$. Thus

```math
x_{t+1}
=q\left(\frac{x_t}{2}+\frac{1+1/d}{4}\right)+\frac rd,
```

or equivalently

```math
y_{t+1}=\frac q2 y_t+\frac{q(1-1/d)}4,
\qquad y_1=0.
```

Solving this scalar recurrence yields

```math
y_t=\frac{q(1-1/d)}{2(2-q)}
\left[1-\left(\frac q2\right)^{t-1}\right].
```

The per-round predictive advantage is $`y_t/4`$, so the limiting advantage is

```math
\boxed{
\beta_{\mathrm{swap}}(d,r)
=\frac{(1-1/d)q}{8(2-q)}
=\frac{(1-1/d)(1-r)}{8(1+r)}.
}
```

Because $`1-1/d\ge1/2`$ and $`2-q\le2`$, this is at least $`q/32`$.

The derivation uses only purity of each hidden state and an independent-refresh ensemble with mean $`I/d`$. It does not assume that a conditional memory state is Haar covariant. In particular, the formula remains exact for every pure-state refresh ensemble whose first moment is exactly $`I/d`$. This is the property used by the [efficient-source construction](efficient_sources.md).

## Finite-horizon accuracy

Summing the geometric transient gives, for every integer $`T\ge1`$,

```math
\boxed{
\beta_{\mathrm{swap},T}
=\beta_{\mathrm{swap}}
\left[
1-\frac{1-(q/2)^T}{T(1-q/2)}
\right].
}
```

The first-round advantage is zero, as required by the lack of prior information. Since $`1-q/2\ge1/2`$,

```math
0\le\beta_{\mathrm{swap}}-\beta_{\mathrm{swap},T}
\le\frac{2\beta_{\mathrm{swap}}}{T}.
```

This is an exact expectation calculation. It does not assert a concentration or high-probability guarantee for the realized fraction of correct labels.

## Converse for arbitrary quantum memory

Consider any causal policy and a round $`t\ge2`$. On the event of a fresh redraw, $`P_t`$ is independent of the learner's entire previous quantum and classical memory. Averaging the signal input over that redraw gives $`I/d`$, exactly the background state. The two current labels therefore induce the same joint state of prior memory and current input. Every decision rule has success probability $`1/2`$ conditional on this event.

On the complementary event, grant the learner a classical description of the exact hidden state $`P_t`$ and knowledge that no redraw occurred. This additional information cannot reduce its success. Conditioned on $`P_t`$, its previous memory does not depend on the current independent label, and the fresh input has no entanglement with that memory. The best possible discrimination is consequently between $`P_t`$ and $`I/d`$ themselves. Their trace distance is

```math
\left\|P_t-\frac Id\right\|_1
=2\left(1-\frac1d\right),
```

so their equal-prior discrimination success is $`1-1/(2d)`$. Combining the two refresh events gives

```math
\Pr_{\mathcal A}(\widehat Y_t=Y_t)-\frac12
\le\frac{q(1-1/d)}2.
```

At round one the averaged input hypotheses are identical and the advantage is zero. Therefore the finite-horizon upper bound is

```math
\beta_{\mathcal A,T}
\le\left(1-\frac1T\right)
\frac{q(1-1/d)}2.
```

It holds for arbitrary quantum memory, computation, and measurement adaptation. Taking the limsup and the supremum proves the theorem. The SWAP learner is within a factor $`4(2-q)\le8`$ of this universal upper bound in predictive advantage.

## Disjoint pairs already achieve the quantum scaling

A simpler protocol groups consecutive specimens into disjoint pairs. On the first specimen in each pair, make a fair guess and store the specimen unchanged. On the second, perform the SWAP measurement, predict signal on $`+`$ and background on $`-`$, then discard both data registers.

If the hidden state persists between the two arrivals, the first unlabeled specimen has mean $`(P+I/d)/2`$ and hence overlap $`(1+1/d)/2`$ with the current pure state. If a refresh occurs, the expected overlap is $`1/d`$. Thus the second round of each pair has advantage $`q(1-1/d)/8`$, while the first has zero. The exact finite-horizon and limiting advantages are

```math
\beta_{\mathrm{pair},T}
=\frac{\lfloor T/2\rfloor}{T}
\frac{q(1-1/d)}8,
\qquad
\beta_{\mathrm{pair}}
=\frac{q(1-1/d)}{16}.
```

The rolling protocol improves the limiting constant by

```math
\frac{\beta_{\mathrm{swap}}}{\beta_{\mathrm{pair}}}
=\frac{2}{2-q}
=\frac{2}{1+r},
```

which is between one and two. Persistent recycling is therefore not necessary for the $`\Theta(q)`$ quantum advantage. Coherent comparison of consecutive native specimens already suffices. The main separation comes from combining this quantum scaling with the universal classical result $`\beta_C=\Theta(q/(1+rd))`$, giving the optimal-advantage ratio $`\Theta(1+rd)`$.
