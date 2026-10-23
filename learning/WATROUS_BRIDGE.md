# From Watrous to prediction under drift

The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018). This bridge connects its mathematical tools to the project's [30 milestones](MILESTONES.md). The first twelve milestones establish the language of states, measurements, retained systems, and random-state averages. The remaining eighteen use that language to explain the prediction experiment and its matching bounds.

The book supplies background results. The changing-source experiment and its proofs are developed in the [science pages](../science/model.md), with research antecedents identified in [Related work](../references/RELATED_WORK.md). The bridge explains how those pieces fit and gives one complete small example; the linked science pages remain the canonical proofs.

<a id="source-map"></a>

## Focused source map

Use the [author-hosted draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) alongside the [publication record](../references/RELATED_WORK.md#watrous2018). The draft is available for personal reading; this repository links to it and does not redistribute the book.

All printed page numbers below refer to that draft. A PDF viewer counts eight preliminary pages: **viewer page = printed Arabic page + 8**. The links open at one-based viewer pages. Section and theorem numbers provide the more portable references across formats.

| Topic | Watrous locator | Printed pages | PDF viewer pages |
| --- | --- | --- | --- |
| Matrix norms | §1.1.3 | 24–34 | [32–42](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=32) |
| Partial trace | §2.1.3 | 67–71 | [75–79](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=75) |
| Channels | §§2.2.1–2.2.2 | 72–90 | [80–98](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=80) |
| POVMs | §2.3.1 | 100–104 | [108–112](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=108) |
| Retained measurement outputs | §2.3.2, equations (2.255)–(2.262) | 111–113 | [119–121](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=119) |
| Binary decisions | §3.1.1; Theorem 3.4, equation (3.11) | 125–131; theorem 128 | [133–139](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=133); [theorem 136](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=136) |
| Diamond norm | §3.3.2; Definition 3.43, equation (3.256) | 166–174; definition 170 | [174–182](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=174); [definition 178](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=178) |
| Symmetric powers | §7.1.1; Corollary 7.3 | 391–399; dimension 395 | [399–407](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=399); [dimension 403](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=403) |
| Haar moments | §7.2.1; Lemma 7.24, equation (7.159) | 408–419; moment 416 | [416–427](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=416); [moment 424](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=424) |
| Optional applications | §7.2.2 | 420–428 | [428–436](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=428) |

The optional applications section is background context. The arbitrary-effect posterior formula used by the project is attributed to [Hayashi, Dasgupta, and Warsi, Lemma 10](../references/RELATED_WORK.md#hayashi2026), and is derived in the repository's [posterior page](../science/haar_posterior.md) from the moment identity.

<a id="notation"></a>

## Notation and normalization

The following translation fixes conventions used throughout [M01–M12](MILESTONES.md#m01). In particular, a matrix representing a state, an effect, and a state-changing operation have different roles even when their dimensions coincide.

| Book notation | Project notation or meaning |
| --- | --- |
| A column vector $`u`$ and its adjoint $`u^*`$ | $`\lvert\psi\rangle`$ and $`\langle\psi\rvert`$ |
| $`uu^*`$ | The pure-state density matrix $`P=\lvert\psi\rangle\langle\psi\rvert`$ |
| $`\mathcal X`$, $`\mathrm L(\mathcal X)`$, $`\mathrm D(\mathcal X)`$ | A Hilbert space, its linear operators, and its density matrices |
| $`1_{\mathcal X}`$ | The identity matrix $`I`$; $`I/d`$ is the maximally mixed state |
| $`1_{\mathrm L(\mathcal X)}`$ | The identity **channel**, denoted $`\mathrm{id}`$ |
| $`\langle A,B\rangle=\operatorname{Tr}(A^*B)`$ | $`\operatorname{Tr}(A^\dagger B)`$ |
| A measurement effect $`\mu(a)`$ | A positive operator $`E_a`$ with $`\sum_a E_a=I`$ |
| An instrument operator $`M_a`$ in §2.3.2 | A Kraus operator $`K_a`$; its outcome effect is $`K_a^\dagger K_a`$ |
| $`\mathcal X^{\vee m}`$ and its projector | $`\operatorname{Sym}^m(\mathbb C^d)`$ and $`\Pi_m`$ |
| $`\lvert\!\lvert\!\lvert\Phi\rvert\!\rvert\!\rvert_1`$ | The full diamond norm $`\lVert\Phi\rVert_\diamond`$ |

The [posterior proof](../science/haar_posterior.md) uses $`M_z`$ for a **POVM effect**, not a Kraus operator. Its meaning is fixed by $`\Pr(z\mid P)=\operatorname{Tr}(M_zP^{\otimes m})`$. Keeping effects and operations distinct becomes essential when a measured register is retained.

The project uses $`d`$ for Hilbert-space dimension, $`n`$ for qubit count when $`d=2^n`$, and $`m`$ for a number of prior specimens. These meanings should replace the locally chosen variables in a book formula. The symmetric-subspace dimension is

```math
D_m=\binom{d+m-1}{m}.
```

The trace norm $`\|A\|_1`$ has no factor of one half. The project uses $`\tfrac12\|\rho-\sigma\|_1`$ for trace distance and $`\tfrac12\|\widetilde{\mathcal J}-\mathcal J\|_\diamond`$ for instrument error. With equal label priors, optimal binary success is consequently

```math
p_{\mathrm{succ}}=\frac12+\frac14\|\rho-\sigma\|_1.
```

This normalization is used in the worked example and both prediction bounds.

<a id="states-and-records"></a>

## From a state description to a prediction experiment

The background chain [M01–M08](MILESTONES.md#m01) is needed because the same physical specimen supports several different mathematical descriptions. A density matrix predicts measurement probabilities. A channel describes a physical transformation. An instrument also records which outcome occurred and what state survives. A classical record specifies an outcome history that may control later measurements. None of those descriptions automatically supplies another specimen or a classical description of its unknown preparation.

For the [model in M13–M15](MILESTONES.md#m13), the learner receives one specimen at each arrival. Conditional on the current hidden projector $`P`$, its unlabeled density matrix is

```math
\frac12 P+\frac12\frac Id.
```

The label still matters: the task scores whether the learner identifies which term was selected. Averaging the label is useful for the memory's evolution, but the accuracy calculation must retain the distinction between signal and background.

A fresh Haar draw satisfies $`\mathbb E P=I/d`$. Therefore a specimen from a newly refreshed epoch has identical averaged signal and background states when the learner has no information about that draw. Prediction becomes possible through information correlated with the current hidden state. The experiment specifies whether such information survives as a classical record or as a quantum register.

For a classical record $`h`$, define the predictive state

```math
R_h=\mathbb E[P\mid h].
```

Because the new label is independent and fair, its two conditional hypotheses are $`R_h`$ and $`I/d`$. Linearity of measurement probabilities makes this posterior mean sufficient for the current decision. It need not describe a pure state, and possessing it mathematically does not imply that a learner has reconstructed the unknown $`P`$. This is the connection from [M12](MILESTONES.md#m12) to the posterior analysis in [M16–M17](MILESTONES.md#m16).

<a id="worked-qubit-example"></a>

## Worked example: one qubit, one training outcome

Consider first the stronger training experiment used in the proof. A hidden qubit projector $`P`$ is Haar distributed, and a learner receives **one pure training copy** before the test. It measures that copy in the basis $`\{|0\rangle,|1\rangle\}`$. Suppose the outcome is zero, whose effect is $`E_0=|0\rangle\langle0|`$.

The first two Haar moments, written in the project notation, are

```math
M_1=\mathbb E P=\frac{I_2}{2},
\qquad
M_2=\mathbb E(P\otimes P)
=\frac{I_4+S}{6},
```

where $`S`$ swaps the two qubits. The denominator follows from $`\Pi_2=(I_4+S)/2`$ and $`D_2=3`$. These are the cases $`m=1,2`$ of the moment formula connected to [M10–M11](MILESTONES.md#m10).

The outcome probability is $`\operatorname{Tr}(E_0M_1)=1/2`$. Before dividing by that probability, the posterior first moment is

```math
\begin{aligned}
N_0
&=\mathbb E\!\left[P\operatorname{Tr}(E_0P)\right]\\
&=\operatorname{Tr}_1\!\left[(E_0\otimes I_2)M_2\right]\\
&=\frac{I_2+E_0}{6}.
\end{aligned}
```

The last line uses $`\operatorname{Tr}E_0=1`$ and $`\operatorname{Tr}_1[(E_0\otimes I_2)S]=E_0`$. Normalizing gives

```math
R_0=\frac{N_0}{1/2}
=\frac{I_2+E_0}{3}
=\begin{pmatrix}2/3&0\\0&1/3\end{pmatrix}.
```

The test hypotheses are $`R_0`$ for signal and $`I_2/2`$ for background. Their difference is

```math
R_0-\frac{I_2}{2}
=\begin{pmatrix}1/6&0\\0&-1/6\end{pmatrix},
\qquad
\left\|R_0-\frac{I_2}{2}\right\|_1=\frac13.
```

The optimal test measures in the same basis and predicts signal on outcome zero. Its success is

```math
p_{\mathrm{succ}}
=\frac12+\frac1{12}=\frac7{12}.
```

Directly, it is right on a signal with probability $`2/3`$ and on a background with probability $`1/2`$, giving $`\tfrac12(2/3+1/2)=7/12`$. Training outcome one exchanges the two coordinates and gives the same accuracy. Thus the complete training-and-test procedure attains $`7/12`$, the [fixed-age optimum](../science/haar_posterior.md) at $`d=2,m=1`$.

### What changes for an actual stream input?

The actual first specimen is unlabeled. Given $`P`$, it is $`(P+I_2/2)/2`$, so the probability of observing zero is

```math
\ell_0(P)=\frac12\operatorname{Tr}(E_0P)+\frac14.
```

Its average is again $`1/2`$, but its evidence about $`P`$ is weaker. The normalized posterior becomes

```math
R_0^{\mathrm{stream}}
=\frac{\tfrac12N_0+\tfrac14M_1}{1/2}
=\begin{pmatrix}7/12&0\\0&5/12\end{pmatrix}.
```

Before the next arrival, the hidden state persists with probability $`q`$ and refreshes independently otherwise. The next signal's predictive state is therefore

```math
qR_0^{\mathrm{stream}}+(1-q)\frac{I_2}{2}
=\begin{pmatrix}1/2+q/12&0\\0&1/2-q/12\end{pmatrix}.
```

Measuring the second specimen in the same basis and predicting signal when its outcome repeats the first gives success $`1/2+q/24`$. The zero and one histories have equal performance. The learner can make a fair first-round prediction while storing the first basis outcome; it needs neither a true label nor a refresh flag.

This is a complete two-arrival instance of the cache mechanism. The earlier $`7/12`$ calculation belongs to the stronger pure-copy comparison experiment. Confusing those experiments would turn an upper-bound resource into an unavailable algorithmic input. [M18](MILESTONES.md#m18) and the [causal reduction](../science/classical_prediction.md#the-per-round-comparison-experiment) make that distinction for every possible classical policy.

<a id="classical-mechanism"></a>

## Why the classical bound depends on dimension and lifetime

The classical argument has two complementary parts. The converse must cover arbitrary adaptive measurements and unlimited classical records. The construction must show that an allowed policy reaches the same scaling. [M16–M23](MILESTONES.md#m16) follow those two parts.

For the converse, fix one prediction time and let $`m`$ count previous arrivals in the current epoch. Reveal the refresh boundaries and replace those inputs by pure copies of the current $`P`$. Before the current test arrives, the strengthened learner must measure and discard those copies, retaining only a classical record. A measurement on the copies can simulate the original mixed inputs by randomly replacing copies with $`I/d`$. It can also absorb adaptive processing and randomness. Older epochs are independent of the current draw. The resulting training record is thus described by an effect on $`P^{\otimes m}`$, even though the original policy may have used a much longer history.

The [arbitrary-effect posterior](../science/haar_posterior.md) has the form

```math
R_h=\frac{I+m\tau_h}{d+m},
```

for a density matrix $`\tau_h`$. Its displacement from the background is reduced by $`m/(d+m)`$. The binary discrimination formula therefore limits the fixed-age advantage to

```math
\frac{m(d-1)}{2d(d+m)}.
```

The book's discrimination and moment tools support this step. The per-round domination argument and the refresh process are additional ingredients of the project. Averaging over a geometric age with mean $`q/r`$ yields the [classical upper bound](../science/classical_prediction.md#age-distribution-and-the-upper-bound). An old archive cannot increase the number of specimens correlated with a fresh independent draw.

For the matching construction, every input is measured in one fixed basis. The learner caches the preceding

```math
L=\left\lfloor\min(d,1/r)\right\rfloor
```

outcomes and predicts signal when the new outcome appears in that cache. Repetition contains predictive information because a shared hidden state gives correlated basis probabilities. The proof must handle the fact that a cache can cross unknown refresh boundaries. Its nonnegative-contribution argument for every refresh partition permits a lower bound using only the event that the whole cache belongs to the current epoch. A Beta-moment identity then gives the required window size and dimension dependence. Those arguments, and the exact finite-horizon recurrence, are provided in the [cache proof](../science/classical_prediction.md#an-explicit-cache-classifier); they are not textbook results quoted from Watrous.

<a id="quantum-mechanism"></a>

## Why a retained register can compare before it reconstructs

The quantum construction in [M24–M26](MILESTONES.md#m24) uses information in a physical register directly. It does not estimate the hidden vector or optimize a parametrized circuit. Given memory $`\sigma`$ and the new input $`\rho`$, the global SWAP measurement has projectors

```math
\Pi_\pm=\frac{I\pm S}{2}.
```

Predict signal on the plus outcome, then retain the memory register and discard the input register. The exact instrument matters: a destructive comparison supplies no register for the next arrival, while a finer measurement can change the retained state even if it reproduces the same coarse outcome probabilities. The distinction between an effect and an instrument from [M05–M06](MILESTONES.md#m05) is operational here.

After averaging over the new measurement outcome, the retained state is

```math
\overline\sigma^{\,+}=\frac{\sigma+\rho}{2}.
```

This is an ensemble update. It does not assert that every conditional branch has that density matrix. Because the protocol's subsequent operations do not depend on previous outcomes and the relevant overlap is linear, the averaged update gives its expected performance exactly. The [quantum proof](../science/quantum_prediction.md#exact-averaged-memory-update) derives it by expanding the two projectors and taking a partial trace.

Write $`y_t=\mathbb E\operatorname{Tr}(\sigma_tP_t)-1/d`$ for the memory's excess alignment with the current hidden state. Its two contributions have a simple meaning: existing alignment is halved by the update and survives a refresh transition only with probability $`q`$; the current signal can create new alignment. Quantitatively,

```math
y_{t+1}=\frac q2 y_t+\frac{q(1-1/d)}4.
```

The prediction advantage is $`y_t/4`$. Solving this recurrence gives the exact long-run advantage

```math
\beta_{\mathrm{swap}}
=\frac{(1-1/d)q}{8(1+r)}.
```

At a fresh redraw, the entire past is independent of the new state, which limits even an unlimited quantum-memory learner. The resulting [quantum converse](../science/quantum_prediction.md#converse-for-arbitrary-quantum-memory) matches the construction up to a universal constant. A protocol using disjoint consecutive pairs already attains the same order; repeated recycling improves its constant. Thus the scaling claim rests on coherent comparison and the classical converse, rather than on a claim that indefinitely recycling one register is necessary.

<a id="source-and-noise"></a>

## What the source and noise extensions require

The exact Haar model specifies a distribution, not an efficient preparation algorithm. [M28](MILESTONES.md#m28) supplies a separate construction using approximate unitary designs from [Brandão, Harrow, and Horodecki](../references/RELATED_WORK.md#brandao2016). Watrous's channel norms explain the approximation language; the circuit construction comes from that research source.

The [source proof](../science/efficient_sources.md) compares normalized moments in trace norm and controls the tail of the current epoch's age. It also enforces the first moment $`I/d`$ exactly. This distinction is useful: the classical transfer needs sufficiently many accurate moments, whereas the quantum overlap recurrence needs only pure draws and that exact first moment. Preparation is polynomial in qubit count for fixed or inverse-polynomial refresh rates under the stated construction. The whole Haar crossover does not thereby acquire a uniform polynomial preparation guarantee.

The sampled circuit and seed remain private to the source. Both learner classes receive the same single specimens and are charged the same source costs. There is no preparation oracle, QRAM access, or free conversion of classical data into amplitudes.

[M29](MILESTONES.md#m29) uses diamond distance for a different purpose: comparing the entire implemented instrument with the intended instrument, including both its prediction and retained output. That guarantee includes behavior on correlated inputs. A per-gate error statement does not automatically give a dimension-independent error bound for the complete operation. The [implementation page](../science/implementation_and_noise.md) states the uniform error bound and the separately solvable global-depolarization model. Neither supplies a threshold for constant local physical noise or an error-correction construction.

<a id="reading-the-frontier"></a>

## Reading the final law with the correct quantifiers

The conclusion in [M27](MILESTONES.md#m27) and [M30](MILESTONES.md#m30) concerns optimal long-run **expected** advantage over a fair guess:

```math
\beta_C=\Theta\!\left(\frac{q}{1+rd}\right),
\qquad
\beta_Q=\Theta(q),
\qquad 0<r<1,\quad d\ge2.
```

The dimension $`d`$ competes with the typical number of still-relevant arrivals, of order $`1/r`$. When $`rd`$ is large, the matched bounds separate the two memory resources. When $`rd`$ is small, they give the same order and do not claim a quantum improvement in every numerical constant. The [model page](../science/model.md) states the supremum over allowed policies and the finite-horizon qualifications.

At $`r=1`$, every signal is an independent draw and both advantages vanish. At $`r=0`$ and fixed dimension, a classical learner can eventually identify the stationary source well enough to approach the same known-state optimum as a quantum learner. These endpoints require their own statements. The Haar-initialized process is stationary in distribution even when its latent state refreshes; the finite correlation lifetime is the changing physical condition relevant to the theorem.

Watrous provides the tools for making those distinctions exact. The project's added content is their combination into this causal experiment, its two matching mechanisms, and the explicitly delimited source and implementation extensions. [Related work](../references/RELATED_WORK.md) records which intermediate ingredients are inherited and which conclusions are derived here.
