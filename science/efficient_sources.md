# Efficient pure-state sources

The [Haar-source prediction bounds](classical_prediction.md) describe every refresh rate $`0<r<1`$. This page gives a separate source-replacement theorem. It preserves those bounds for an ensemble of pure states prepared by finite circuits, with preparation polynomial in the number of qubits when the refresh rate is fixed or inverse polynomial. The source distribution is known to the learner; its independently sampled seed in the current epoch is private.

Write $`d=2^n`$, $`q=1-r`$, and let $`\mu`$ be the distribution from which a new pure state $`P`$ is drawn at each refresh. The same sampled state is prepared again for each signal arrival in that epoch. Define its normalized moments by

```math
M_k(\mu)=\mathbb E_{P\sim\mu}P^{\otimes k},
\qquad M_0(\mu)=1.
```

The assumptions are

```math
M_1(\mu)=I/d,
\qquad
\|M_k(\mu)-M_k(\mathrm H)\|_1\le\epsilon
\quad (1\le k\le K),
```

where $`\mathrm H`$ denotes Haar-distributed pure states and $`\|\cdot\|_1`$ is the unnormalized trace norm. Thus the trace distance is one half of the displayed norm. These are statements about density operators of trace one; there is no division by their Hilbert-space dimension.

## A dimension-safe source construction

For a distribution $`\nu`$ of unitaries, write

```math
\mathcal T_{\nu,K}(X)
=\mathbb E_{U\sim\nu}U^{\otimes K}X(U^\dagger)^{\otimes K}.
```

Suppose $`\|\mathcal T_{\nu,K}-\mathcal T_{\mathrm H,K}\|_\diamond\le\epsilon`$. Applying these channels to $`(|0\rangle\langle0|)^{\otimes K}`$ gives the required order-$`K`$ moment bound for $`P=U|0\rangle\langle0|U^\dagger`$. Partial trace gives every lower-order moment bound with the same error. Neither step introduces a factor depending on $`d`$ or $`K`$.

Brandão, Harrow, and Horodecki use a relative completely-positive-order definition of an approximate unitary design. Their Definition 2 and Lemma 3 imply that relative error $`\epsilon/2`$ suffices for the diamond error $`\epsilon`$ used here. Corollary 6 supplies polynomial-length local random circuits; Corollary 7 supplies the corresponding result for a fixed finite universal gate set with inverses and algebraic matrix entries. The resulting circuit size is polynomial in $`n`$, $`K`$, and $`\log(1/\epsilon)`$. See [BHH, Definition 2, Lemma 3, and Corollaries 6–7](../references/RELATED_WORK.md#brandao2016).

To enforce the first moment exactly, independently sample a uniform $`n`$-qubit Pauli $`W`$ and replace $`P`$ by $`WPW^\dagger`$. The Pauli average of any density operator is $`I/d`$. At order $`k`$, this operation is a completely positive trace-preserving map on $`M_k`$; it leaves the Haar moment invariant and contracts the trace norm of the difference. The Pauli is sampled once per epoch and retained with that epoch's circuit, so successive signal inputs still contain copies of the same pure state.

An unspecified approximate-design norm cannot be substituted into this argument. For example, converting an additive operator-norm bound on a moment to a trace-norm bound can cost the dimension of its support. Starting from the channel diamond norm, or the cited relative CP-order guarantee, avoids that conversion.

## Classical transfer at one prediction time

Let $`A=m`$ be the number of preceding arrivals since the most recent refresh. Use the strengthened comparator from the [classical prediction proof](classical_prediction.md): reveal the refresh boundaries and give the learner $`m`$ pure training copies of the current hidden state. Require it to convert those copies into a classical record before the test arrives.

This comparator dominates the actual classical-record learner. It can reproduce an earlier mixed input by replacing a pure copy by $`I/d`$ with probability one half. All adaptive measurements and classical processing during the epoch form one collective training POVM. Records from earlier epochs are independent of the current draw and only randomize that POVM. This remains true when the ensemble has finite support and is fully known: repeated independent draws do not create an unknown shared source parameter.

Before any learner operations, include the true current label in a classical register. The training-plus-test state is

```math
\Omega_m(\mu)
=\frac12|1\rangle\langle1|\otimes M_{m+1}(\mu)
+\frac12|0\rangle\langle0|\otimes
   \bigl(M_m(\mu)\otimes I/d\bigr).
```

For $`1\le m<K`$, the block structure gives

```math
\|\Omega_m(\mu)-\Omega_m(\mathrm H)\|_1
\le \frac12\epsilon+\frac12\epsilon=\epsilon.
```

Every training-and-prediction strategy is a channel followed by a success effect on this joint state. Its success probability therefore changes by at most $`\epsilon/2`$. The comparison applies to a strategy chosen with full knowledge of $`\mu`$: the same strategy is a valid POVM in the Haar comparison experiment. It does not compare normalized posteriors conditioned on rare measurement outcomes, which could amplify approximation error.

At $`m=0`$, both hypotheses average to $`I/d`$, so every learner has success exactly one half. There is no design error at age zero.

The stationary age distribution is $`\Pr(A=m)=rq^m`$. Let $`b_C(\mu)`$ denote the optimal long-run expected classical prediction advantage above one half. Combining the Haar fixed-age bound with the age-zero observation and the tail $`\Pr(A\ge K)=q^K`$ gives

```math
\begin{aligned}
b_C(\mu)
&\le \frac{1-1/d}{2}\,
      \mathbb E\!\left[\frac{A}{d+A}\right]
   +\frac{q-q^K}{2}\epsilon+\frac{q^K}{2}\\
&\le \frac{(1-1/d)q}{2(rd+q)}
   +\frac{q\epsilon}{2}+\frac{q^K}{2}.
\end{aligned}
```

The factor $`q`$ on the approximation error matters when $`r`$ approaches one. There is no accumulation proportional to the stream length: the comparison is made at each current epoch, and previous independent epochs contain no information about its fresh seed. The same stationary upper bound applies to a stream started with an empty record, whose age is bounded by the stationary geometric age.

## Transfer of the explicit cache lower bound

The fixed-basis cache classifier stores the preceding $`L`$ measurement outcomes and predicts signal when the current outcome appears in that cache. Choose

```math
L=\left\lfloor\min(d,1/r)\right\rfloor.
```

The [Haar cache proof](classical_prediction.md) obtains conditional advantage at least $`L/(64e^2d)`$ on the event of no refresh across the $`L`$ preceding transitions. That event has probability $`q^L`$.

If $`K\ge L+1`$, the joint labeled experiment on this event is within trace norm $`\epsilon`$ of its Haar counterpart. Previous signal/background labels can be averaged before this comparison: each resulting branch contains at most $`L+1`$ copies and the branch weights sum to one. Thus the conditional cache advantage decreases by at most $`\epsilon/2`$.

The other refresh partitions still have nonnegative advantage for any ensemble with exact first moment. To see this, fix a coordinate $`j`$, put $`p_j=\langle j|P|j\rangle`$, and let $`a`$ be the number of cached samples in the current epoch. The older epochs contribute an avoidance probability $`C_j\ge0`$. Their distributions may depend on $`j`$; coordinate permutation symmetry is unnecessary. The signal-minus-background prediction difference is

```math
-\sum_j C_j\,
\mathbb E\!\left[
\left(p_j-\frac1d\right)
\left(1-\frac{p_j+1/d}{2}\right)^a
\right]\ge0.
```

Each term has the required sign because $`\mathbb E p_j=1/d`$ and the second factor decreases with $`p_j`$. Consequently

```math
b_{\mathrm{cache}}(\mu)
\ge q^L\left(\frac{L}{64e^2d}-\frac\epsilon2\right).
```

This lower-bound transfer uses moments through $`L+1`$. An approximate design sufficient for a truncated classical upper bound is not automatically sufficient for this particular lower bound.

## A sufficient parameter choice and its cost

One convenient choice preserving both sides is

```math
\epsilon\le\frac{1}{128e^2(1+rd)},
\qquad
K\ge \max\!\left\{
L+1,
1+\left\lceil\frac{\log(1+rd)}{-\log q}\right\rceil
\right\}.
```

Indeed, $`L/d\ge1/[2(1+rd)]`$, so the cache loses at most half its stated Haar lower bound. Also $`q^K\le q/(1+rd)`$. The resulting source family therefore satisfies

```math
b_C(\mu)=\Theta\!\left(\frac{q}{1+rd}\right),
\qquad
b_Q(\mu)=\Theta(q),
```

with absolute constants. The quantum statement follows without a design-approximation loss: the [rolling-SWAP overlap recursion](quantum_prediction.md) requires only pure draws and the exact first moment $`I/d`$.

Since $`-\log q\ge r`$, taking the largest allowed $`\epsilon`$ and the smallest sufficient $`K`$ gives $`K=O(1+n/r)`$ and $`\log(1/\epsilon)=O(n)`$. Thus the source circuit is polynomial in $`n`$ for fixed $`r`$ and for $`r\ge n^{-c}`$ with fixed $`c`$. This construction does not establish preparation polynomial in $`n`$ uniformly over exponentially small refresh rates. The full Haar frontier and this preparation-efficient regime are distinct statements.

The source samples a new circuit and Pauli at a refresh, stores their descriptions privately, and executes that circuit for every signal arrival. Background states can be produced by uniformly sampling a computational-basis state and withholding the source's random choices. Circuit sampling, storage, and execution are source resources, charged identically for both learner classes. The learner receives one state per arrival and no circuit description, inverse operation, or additional state-preparation access. The polynomial preparation guarantee is an existence bound, not an estimate of practical gate counts.
