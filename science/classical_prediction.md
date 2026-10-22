# Classical prediction under hidden refreshes

The [model](model.md) emits one native quantum specimen per round. The hidden pure state is retained with probability $`q=1-r`$ and independently redrawn from the Haar distribution with probability $`r`$, where $`d\ge2`$ and $`0<r<1`$. Independently, the current fair label selects either that pure state or $`I/d`$. Conditioned on the hidden path and labels, the emitted specimens form a product state. Learners observe neither labels nor refresh flags.

A classical-memory policy may process each current specimen by arbitrary quantum operations, adapt those operations to its entire classical record, and retain unlimited classical information. It carries no quantum information from one arrival to the next. This page proves both a universal upper bound for that class and an explicit matching strategy.

## Result

For a policy $`\mathcal A`$, let

```math
\beta_{\mathcal A,T}
=\frac1T\sum_{t=1}^T
\left[\Pr_{\mathcal A}(\widehat Y_t=Y_t)-\frac12\right],
\qquad
\beta_C(d,r)
=\sup_{\mathcal A\in\mathsf C}
\limsup_{T\to\infty}\beta_{\mathcal A,T}.
```

**Theorem.** Uniformly for $`d\ge2`$ and $`0<r<1`$,

```math
\boxed{
\frac{q}{128e^3(1+rd)}
\le\beta_C(d,r)
\le\frac{q}{1+rd}.
}
```

The upper bound allows unlimited classical storage and computation. The lower bound uses a fixed-basis measurement and a cache of $`L=\lfloor\min(d,1/r)\rfloor`$ classical outcomes. The parameters $`d,r`$ and the source law are known; their realizations are hidden.

## The per-round comparison experiment

Let $`A_t`$ be the number of preceding arrivals in the current hidden-state epoch. Thus $`A_t=0`$ immediately after a refresh, and $`A_1=0`$.

Fix one prediction round $`t`$. For an upper bound, strengthen the learner by providing the refresh boundaries and a bundle of $`A_t`$ pure copies of the current hidden state $`P_t`$. It can perform any collective measurement on that bundle, but must convert the bundle completely into classical information before receiving the current test specimen.

This comparison experiment dominates every actual classical-memory policy at round $`t`$. To verify the claim, condition on the refresh pattern and on the classical record from before the current epoch. The latter record is independent of the current Haar state: the epoch began with an independent draw, and the refresh process is independent of the data. Conditional on that record, simulate the original policy's earlier steps in the current epoch. For each of the supplied pure copies, flip an independent fair coin and either retain it or replace it by $`I/d`$. This exactly produces the earlier unlabeled input ensemble. Apply the original policy's measurements in their original adaptive order. All intermediate predictions, measurement outcomes, and private random bits can be included in the resulting classical record.

Since the original policy retains no quantum information between inputs, this whole simulation is a measurement of the supplied bundle with a classical outcome. An arbitrary collective POVM on the bundle is at least as powerful. Operations and randomness originating in older epochs only choose an independent mixture of such POVMs. The current label remains an independent fair bit throughout this construction.

The comparison bundle is supplied separately for this fixed round. It is not asserted that these strengthened resources can be realized simultaneously for every round of one physical experiment. A separate domination argument for each summand is sufficient for an upper bound on the expected average success.

Apply the [Haar posterior classification proposition](haar_posterior.md) with $`m=A_t`$. Its consequence is

```math
\Pr_{\mathcal A}(\widehat Y_t=Y_t)-\frac12
\le
\frac{1-1/d}{2}
\mathbb E\!\left[\frac{A_t}{d+A_t}\right]
```

for every classical-memory policy. No reset information or pure-copy oracle is assumed for the actual learner; these are extra resources used to prove its limitation.

## Age distribution and the upper bound

For the process started with a fresh Haar state at round one,

```math
\Pr(A_t=a)=
\begin{cases}
r q^a,&0\le a\le t-2,\\
q^{t-1},&a=t-1.
\end{cases}
```

At $`t=1`$ only the second line applies. Equivalently, $`A_t`$ has the distribution of $`\min(A,t-1)`$ for a geometric age $`A`$ with

```math
\Pr(A=a)=r q^a,\quad a\ge0,
\qquad
\mathbb E A_t
=\sum_{k=1}^{t-1}q^k
=\frac{q(1-q^{t-1})}{r}
\le\frac qr.
```

In particular, a sharper upper bound than the stated theorem, valid also for every finite-horizon average, is

```math
\beta_{\mathcal A,T}
\le U_C(d,r)
:=\frac{1-1/d}{2}
\sum_{a=0}^{\infty} r q^a\frac{a}{d+a}.
```

The function $`a\mapsto a/(d+a)`$ is increasing and concave on the nonnegative real line. Jensen's inequality gives

```math
U_C(d,r)
\le\frac{1-1/d}{2}
\frac{q/r}{d+q/r}
=\frac{(1-1/d)q}{2(rd+q)}
\le\frac{q}{1+rd}.
```

For the last inequality it suffices that $`1-1/d\le1`$ and $`2(rd+q)\ge1+rd`$. These bounds are uniform in the policy and horizon, so taking a limsup and then a supremum gives the claimed upper bound on $`\beta_C`$.

## An explicit cache classifier

Fix one computational basis and a positive integer $`L`$. On every arrival, perform that basis measurement and call the outcome $`J_t\in\{1,\ldots,d\}`$. After the first $`L`$ rounds, predict signal exactly when $`J_t`$ appears among the preceding $`L`$ outcomes. Compare against the old cache before appending $`J_t`$ and removing the oldest cached outcome.

During the first $`L`$ rounds, make independent fair guesses while still collecting the basis outcomes. The algorithm uses $`O(L\log d)`$ bits for its cache and can maintain membership counts by ordinary classical bookkeeping. When $`d=2^n`$, its quantum operation is just a computational-basis measurement of the $`n`$ input qubits.

For a current hidden state $`P`$, write

```math
p_j=\langle j|P|j\rangle,
\qquad
z_j=\frac{p_j+1/d}{2}.
```

Here $`z_j`$ is the probability of seeing basis symbol $`j`$ on an earlier unlabeled specimen in the same epoch. The Haar basis probabilities have the Dirichlet distribution with all parameters equal to one. In particular, any one coordinate $`p`$ has density

```math
w_d(p)=(d-1)(1-p)^{d-2},\qquad 0\le p\le1,
```

and mean $`1/d`$. This marginal also follows by representing a Haar vector as independent complex Gaussian coordinates divided by their Euclidean norm: their squared magnitudes are independent exponential variables before normalization.

## Every refresh history contributes nonnegative advantage

Consider a round with a full cache. Condition on the renewal partition of its preceding $`L`$ specimens and the current specimen. Let $`a\in\{0,\ldots,L\}`$ count the most recent cached specimens that share the current epoch. For each older epoch segment of length $`\ell`$, averaging over its independent hidden Haar state gives the avoidance probability

```math
h_\ell
=\mathbb E\!\left[
\left(1-\frac{p+1/d}{2}\right)^\ell
\right].
```

This probability is the same for every symbol $`j`$. Let $`C`$ be the product of these factors over the older segments, with the empty product equal to one. Then $`C\ge0`$. Conditional on the current state and the partition, and averaged over all older hidden states, the probability that symbol $`j`$ is absent from the cache is

```math
C(1-z_j)^a.
```

It follows that the difference between the probabilities of predicting signal under the signal and background hypotheses, averaged over the current Haar state, is $`C\Delta_a`$, where

```math
\Delta_a
=-d\,\mathbb E\!\left[
\left(p-\frac1d\right)
\left(1-\frac{p+1/d}{2}\right)^a
\right].
```

To obtain this expression, subtract the two current outcome distributions $`p_j`$ and $`1/d`$ and sum over $`j`$. The part independent of cache avoidance cancels because $`\sum_j(p_j-1/d)=0`$; permutation symmetry then makes all remaining expectations equal.

For every $`a`$, the function multiplying $`p-1/d`$ is decreasing in $`p`$. Its covariance with $`p`$ is therefore nonpositive. Explicitly, for independent copies $`p,p'`$ and a decreasing function $`f`$,

```math
2\operatorname{Cov}(p,f(p))
=\mathbb E[(p-p')(f(p)-f(p'))]\le0.
```

Hence $`\Delta_a\ge0`$, including $`\Delta_0=0`$. Every refresh partition contributes nonnegative predictive advantage. This positivity justifies retaining only one favorable partition in a lower bound; other histories cannot cancel its contribution.

With probability $`q^L`$, no refresh occurs between any of the cached specimens and the current specimen. On this event $`a=L`$ and $`C=1`$. Because the current label is fair, half the difference in signal-output probabilities is the accuracy excess. Thus

```math
\beta_{\mathrm{cache}}(L)
\ge\frac{q^L\Delta_L}{2}.
```

Here $`\beta_{\mathrm{cache}}(L)`$ denotes the expected excess at a full-cache round, which is independent of the round index.

## The Beta identity and an explicit constant

For a continuously differentiable $`f`$, integration by parts against $`w_d`$ gives

```math
\mathbb E\!\left[\left(p-\frac1d\right)f(p)\right]
=\frac1d\mathbb E[p(1-p)f'(p)].
```

Indeed, $`[p(1-p)w_d(p)]'=(1-dp)w_d(p)`$, and the boundary term vanishes at both endpoints for $`d\ge2`$. Apply the identity to $`f(p)=(1-(p+1/d)/2)^L`$ to obtain

```math
\Delta_L
=\frac L2\mathbb E\!\left[
p(1-p)
\left(1-\frac{p+1/d}{2}\right)^{L-1}
\right].
```

Suppose $`1\le L\le d`$. Restrict the expectation to the interval $`1/(2d)\le p\le1/d`$. Its probability obeys

```math
\Pr\!\left(\frac1{2d}\le p\le\frac1d\right)
\ge\frac{d-1}{2d}\left(1-\frac1d\right)^{d-2}
\ge\frac1{4e}.
```

On this interval,

```math
p\ge\frac1{2d},\qquad
1-p\ge\frac12,\qquad
\left(1-\frac{p+1/d}{2}\right)^{L-1}
\ge\left(1-\frac1d\right)^{d-1}
\ge e^{-1}.
```

Consequently,

```math
\Delta_L\ge\frac{L}{32e^2d},
\qquad
\beta_{\mathrm{cache}}(L)
\ge\frac{q^L L}{64e^2d}.
```

Choose

```math
L=\left\lfloor\min\!\left(d,\frac1r\right)\right\rfloor.
```

Then $`L\ge1`$, $`L\ge\tfrac12\min(d,1/r)`$, and $`L-1\le q/r`$. The elementary inequality $`q\log q\ge q-1=-r`$ gives

```math
q^L=q\exp[(L-1)\log q]
\ge q\exp\!\left(\frac qr\log q\right)
\ge\frac qe.
```

Therefore

```math
\beta_{\mathrm{cache}}(L)
\ge\frac{q}{128e^3}
\min\!\left(1,\frac1{rd}\right)
\ge\frac{q}{128e^3(1+rd)}.
```

This proves the matching lower bound. The constants are explicit but are not optimized.

## Finite horizons

The hidden process starts with its invariant Haar marginal. Every length-$`L+1`$ window beginning at or after round one therefore has the same joint distribution. A full-cache round has exactly the expected excess $`\beta_{\mathrm{cache}}(L)`$, while each initial fair guess has zero excess. Hence, for every positive integer $`T`$,

```math
\beta_{\mathrm{cache},T}^{(L)}
=\frac{(T-L)_+}{T}\,\beta_{\mathrm{cache}}(L)
\ge
\left(1-\frac LT\right)_+
\frac{q}{128e^3(1+rd)},
```

where $`x_+=\max(x,0)`$. The startup loss is $`O(L/T)`$ relative to a full-cache stream. In particular, $`T\ge2L`$ suffices to retain the same scaling with a universal constant. The upper bound derived earlier applies for every $`T`$ without a startup correction.

## Exact cache recurrence

The lower-bound proof discards positive terms. The full stationary accuracy of a fixed window length can also be evaluated exactly.

Let $`z=(p+1/d)/2`$, set $`h_k=\mathbb E[(1-z)^k]`$, and define $`G_m`$ to be the probability that a chosen basis symbol is absent from a length-$`m`$ window of earlier unlabeled outcomes. Let $`G_0=1`$. Conditioning on the length of the first epoch segment in that window gives, for $`m\ge1`$,

```math
G_m=q^{m-1}h_m
+r\sum_{k=1}^{m-1}q^{k-1}h_kG_{m-k}.
```

The first term is the case with no internal refresh. In a summand, the first refresh follows $`k`$ specimens; after it, the remaining window is independent and has avoidance probability $`G_{m-k}`$.

For the current prediction, either all $`L`$ cached specimens share the current epoch, or the last refresh is $`a`$ arrivals back with $`0\le a<L`$. The latter event has probability $`r q^a`$, the older part of the cache contributes $`G_{L-a}`$, and the current-epoch part contributes $`\Delta_a`$. Since $`\Delta_0=0`$,

```math
\boxed{
\beta_{\mathrm{cache}}(L)
=\frac12\left[
q^L\Delta_L
+r\sum_{a=1}^{L-1}q^aG_{L-a}\Delta_a
\right].
}
```

These quantities have finite moment formulas. With $`b=1-1/(2d)`$ and the rising factorial $`(d)_j=d(d+1)\cdots(d+j-1)`$, with $`(d)_0=1`$,

```math
h_k
=\sum_{j=0}^k
\binom kj b^{k-j}\left(-\frac12\right)^j
\frac{j!}{(d)_j},
```

```math
\Delta_k
=h_k-d\sum_{j=0}^k
\binom kj b^{k-j}\left(-\frac12\right)^j
\frac{(j+1)!}{(d)_{j+1}}.
```

They follow by expanding the polynomial and using $`\mathbb E[p^j]=j!/(d)_j`$. For rational $`r`$, every expression is rational and can be checked without sampling error. For example, the exact advantages are $`1/32`$ at $`(d,L,r)=(2,1,1/4)`$, $`593/38880`$ at $`(2,3,1/3)`$, and $`149/7200`$ at $`(3,3,2/5)`$.

## Range of the result

The uniform theorem covers $`0<r<1`$. At $`r=1`$, each signal is independently redrawn and averages to the same state as background, so every learner's advantage is zero. At $`r=0`$, a single hidden state persists and the stationary geometric-age argument is inapplicable; an unlimited classical-memory learner can accumulate information about that state indefinitely.

The matching cache theorem is for the Haar source specified in the model. The [efficient-source construction](efficient_sources.md) separately quantifies which conclusions survive a finite-order approximate-design replacement. The [quantum prediction theorem](quantum_prediction.md) establishes $`\beta_Q=\Theta(q)`$, so the ratio of optimal predictive advantages in the Haar model is $`\Theta(1+rd)`$.
