# Thirty milestones for quantum learning under drift

These milestones organize the scientific dependencies of the prediction law. Phase I, **M01–M12**, builds the background from operators and individual states to a complete measurement-and-prediction experiment. Phase II, **M13–M30**, begins with one causal prediction, develops the classical and quantum mechanisms, and assembles their global consequences and physical scope.

The anchor is John Watrous, *The Theory of Quantum Information* (2018), using the [author's prepublication draft][watrous]. Section and printed-page locators refer to that draft; PDF viewer pages are eight greater than the printed page numbers. The [Watrous bridge](WATROUS_BRIDGE.md#source-map) connects those foundations to the repository's notation and arguments. Watrous supplies the background framework; the source pointers below separately identify the canonical project derivations and the primary sources for imported results.

Dependencies refer only to earlier milestones. Each record identifies a scientific question, its conceptual dependencies, and its place in the argument.

## Phase I — Background and preliminaries

<a id="m01"></a>
### M01 — Spectral calculus for states and effects

- **Central question:** How do positivity, eigenvalues, and projectors encode admissible states and measurement effects?
- **Understanding target:** Positive semidefinite operators have nonnegative spectra; density operators have trace one; effects lie between zero and the identity. The positive and negative parts of a Hermitian operator turn a discrimination objective into a spectral calculation.
- **Dependencies and story role:** No earlier milestone is required. This establishes the operator language used by every state, probability, and norm bound.
- **Conceptual connection:** The same spectral decomposition certifies physical admissibility and identifies the optimal binary decision rule.
- **Source pointers:** Watrous [§1.1.2][w-operators] and [§1.1.3][w-norms]; project [posterior-to-classification argument](../science/haar_posterior.md#from-the-posterior-to-a-classification-bound).

<a id="m02"></a>
### M02 — States, mixtures, and the maximally mixed reference

- **Central question:** What distinguishes an unknown pure signal from a maximally mixed background?
- **Understanding target:** The signal is a rank-one projector $`P`$, the background is $`I/d`$, and averaging over an unobserved fair label gives $`(P+I/d)/2`$. An ensemble average and the state conditioned on its latent parameter answer different statistical questions.
- **Dependencies and story role:** [M01](#m01). This identifies the local objects emitted by the source before temporal correlations are introduced.
- **Conceptual connection:** Equal one-specimen averages can coexist with different correlations between specimens; the distinction enables prediction from retained information.
- **Source pointers:** Watrous [§2.1.2][w-states]; project [source and timing](../science/model.md#1-source-and-timing).

<a id="m03"></a>
### M03 — Composite registers and partial trace

- **Central question:** How are joint states represented, and what remains when one register is discarded?
- **Understanding target:** Tensor products describe conditionally independent specimens, while partial trace describes the state available on retained registers. Averaging a product source over a shared hidden state can create statistical correlations without changing the conditional product assumption.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). This supplies the register bookkeeping for training bundles, current tests, and retained memory.
- **Conceptual connection:** The conditional independence of a new specimen and old memory is compatible with their unconditional correlation through the hidden signal.
- **Source pointers:** Watrous [§2.1.3][w-reductions]; project [conditional source model](../science/model.md#1-source-and-timing) and [averaged memory update](../science/quantum_prediction.md#exact-averaged-memory-update); bridge [states and records](WATROUS_BRIDGE.md#states-and-records).

<a id="m04"></a>
### M04 — Quantum channels and complete positivity

- **Central question:** Which transformations remain physically valid when an input is part of a larger system?
- **Understanding target:** Completely positive, trace-preserving maps describe quantum channels, including appending ancillas, discarding registers, and replacing a state by $`I/d`$. Kraus and dilation representations describe the same operational transformation.
- **Dependencies and story role:** [M01](#m01), [M03](#m03). This makes the later comparison experiments explicit compositions of allowed operations.
- **Conceptual connection:** Randomly replacing a pure training copy by background is a channel, so the stronger training experiment can simulate the actual unlabeled history.
- **Source pointers:** Watrous [§2.2.1][w-channels] and [§2.2.2][w-channel-representations]; project [per-round comparison experiment](../science/classical_prediction.md#the-per-round-comparison-experiment).

<a id="m05"></a>
### M05 — Measurements, records, and classical control

- **Central question:** How does a quantum specimen become a classical record that can control future measurements?
- **Understanding target:** A POVM assigns outcome probabilities through positive effects summing to the identity. Classical postprocessing can turn a richer outcome into a binary prediction, and the measurement choice may depend on an arbitrarily large earlier record.
- **Dependencies and story role:** [M02](#m02), [M04](#m04). This describes the full within-round freedom granted to the classical learner.
- **Conceptual connection:** A restriction on information surviving between arrivals does not restrict ancilla count, measurement complexity, or classical computation within a round.
- **Source pointers:** Watrous [§2.3.1][w-measurements] and [§2.3.2][w-measurement-notions]; project [learner classes](../science/model.md#2-learner-classes).

<a id="m06"></a>
### M06 — Instruments and conditional versus averaged updates

- **Central question:** What additional information is needed beyond measurement outcome probabilities to predict the state left behind?
- **Understanding target:** An instrument specifies completely positive outcome maps whose sum is a channel. A normalized conditional state differs from the nonselective state obtained by averaging outcomes; the same POVM can admit different retained-state dynamics.
- **Dependencies and story role:** [M03](#m03), [M04](#m04), [M05](#m05). This is the prerequisite for a physically specified memory update.
- **Conceptual connection:** Matching SWAP outcome statistics does not by itself reproduce the channel needed for future predictions.
- **Source pointers:** Watrous [§2.3.2, printed pp.111–113, Eqs.2.255–2.262][w-instruments]; project [outcome statistics and the memory update](../science/implementation_and_noise.md#outcome-statistics-do-not-specify-the-memory-update).

<a id="m07"></a>
### M07 — Binary state discrimination and trace distance

- **Central question:** How does a difference between two density operators determine the best binary success probability?
- **Understanding target:** For equal priors, the optimum is $`1/2+\|\rho_1-\rho_0\|_1/4`$. In particular, knowing $`P`$ gives success $`1-1/(2d)`$ for the pair $`P,I/d`$. The trace norm and the half-trace-norm distance must remain distinct.
- **Dependencies and story role:** [M01](#m01), [M05](#m05). This translates state-information bounds into the prediction loss used throughout the project.
- **Conceptual connection:** The posterior converse and the unlimited-quantum-memory converse use the same binary decision theorem on different conditional states.
- **Source pointers:** Watrous [§3.1.1][w-discrimination], especially [Theorem 3.4, Eq.3.11, printed p.128][w-helstrom]; project [classification bound](../science/haar_posterior.md#from-the-posterior-to-a-classification-bound).

<a id="m08"></a>
### M08 — Contractivity and complete-instrument distance

- **Central question:** Which norm controls every decision made after a state or channel is approximated?
- **Understanding target:** Channel processing cannot increase trace distance between states. The diamond norm controls a channel difference even with an auxiliary register; its half-norm convention bounds changes in event probabilities. This applies to the complete instrument, including its retained quantum output.
- **Dependencies and story role:** [M04](#m04), [M07](#m07). This supplies the error language for source replacement and physical implementation.
- **Conceptual connection:** Approximation must be controlled before conditioning on rare outcomes, and hardware error must include the memory update as well as the current label.
- **Source pointers:** Watrous [§3.3.2][w-diamond], especially [Definition 3.43, Eq.3.256, printed p.170][w-diamond-definition], and [§3.3.3][w-channel-distances]; project [complete-instrument error](../science/implementation_and_noise.md#uniform-error-of-the-complete-instrument).

<a id="m09"></a>
### M09 — SWAP as a two-register comparison

- **Central question:** How can two physical states be compared without first estimating either state?
- **Understanding target:** The swap operator obeys $`\mathrm{Tr}[S(\sigma\otimes\rho)]=\mathrm{Tr}(\sigma\rho)`$. Its symmetric and antisymmetric projectors are $`(I\pm S)/2`$, so a binary symmetry measurement accesses an overlap.
- **Dependencies and story role:** [M03](#m03), [M06](#m06). This isolates the local quantum comparison primitive before its streaming implementation.
- **Conceptual connection:** A specimen retained from the past can act as a physical reference, without becoming a classical description of the hidden signal.
- **Source pointers:** Watrous [§7.1.1][w-permutations] for permutation operators and [§2.3.2][w-measurement-notions] for projective measurements; project [SWAP instrument](../science/quantum_prediction.md#a-physical-retained-register-swap-instrument).

<a id="m10"></a>
### M10 — Symmetric tensor powers and permutation projectors

- **Central question:** What structure is shared by several identical copies of one unknown pure state?
- **Understanding target:** The vector underlying $`P^{\otimes m}`$ lies in the symmetric subspace. Its projector $`\Pi_m`$ is a permutation average, and its dimension is $`D_m=\binom{d+m-1}{m}`$. The copy number $`m`$ and one-register dimension $`d`$ have different roles.
- **Dependencies and story role:** [M01](#m01), [M09](#m09). This extends the two-register symmetry mechanism to a collective training bundle.
- **Conceptual connection:** Symmetric-subspace normalization produces the dimension-dependent denominator in the posterior prediction bound.
- **Source pointers:** Watrous [§7.1.1][w-permutations], especially [Corollary 7.3, Eq.7.24, printed p.395][w-symmetric-dimension]; project [arbitrary-effect posterior calculation](../science/haar_posterior.md#posterior-mean-for-an-arbitrary-training-effect).

<a id="m11"></a>
### M11 — Haar averages and normalized state moments

- **Central question:** How does averaging an unknown direction simplify a many-copy experiment?
- **Understanding target:** The normalized Haar moment is $`\mathbb E[P^{\otimes m}]=\Pi_m/D_m`$, with first moment $`I/d`$. Higher moments encode correlations between repeated specimens and cannot be inferred from the first moment alone.
- **Dependencies and story role:** [M02](#m02), [M10](#m10). This connects the source distribution to finite-dimensional operators that can enter a proof.
- **Conceptual connection:** The quantum recurrence needs only purity and the first moment, whereas a classical training-record bound must control more copies jointly.
- **Source pointers:** Watrous [§7.2.1][w-haar], especially [Lemma 7.24, Eq.7.159, printed p.416][w-haar-moment]; project [Haar posterior](../science/haar_posterior.md#posterior-mean-for-an-arbitrary-training-effect) and [source moments](../science/efficient_sources.md).

<a id="m12"></a>
### M12 — From ensembles and measurements to predictive states

- **Central question:** What state should represent a future specimen after a classical training outcome has been observed?
- **Understanding target:** A training effect reweights the prior distribution of $`P`$. For any subsequent one-specimen measurement, its conditional probabilities depend on the posterior mean $`R_z=\mathbb E[P\mid z]`$. Replacing that density operator by a guessed pure state is a different decision procedure.
- **Dependencies and story role:** [M05](#m05), [M07](#m07), [M11](#m11). This combines Phase I into a complete training-record-test experiment.
- **Conceptual connection:** Bayesian conditioning on a classical record and linearity of quantum outcome probabilities meet in one predictive density operator.
- **Source pointers:** Watrous [§1.2.2][w-probability] and [§2.3.3][w-ensembles] for the probabilistic and ensemble framework; project [training experiment](../science/haar_posterior.md#experiment-and-exact-optimum); bridge [worked qubit example](WATROUS_BRIDGE.md#worked-qubit-example).

## Phase II — Narrative and innovation

<a id="m13"></a>
### M13 — One arrival and the causal prediction deadline

- **Central question:** What information is available when the current label must be predicted?
- **Understanding target:** One native specimen arrives, a label must be output before the next arrival, and no labels, refresh flags, circuit descriptions, or extra copies are provided. Conditioned on the hidden path and labels, the source emits a product state and cannot be affected by learner operations.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M12](#m12). This fixes the local prediction event from which the temporal argument is built.
- **Conceptual connection:** A causal deadline distinguishes this task from postponing all decisions until a joint measurement of an entire dataset.
- **Source pointers:** Watrous [§2.1.1][w-registers] and [§2.3.1][w-measurements] for register and outcome semantics; project [source and timing](../science/model.md#1-source-and-timing).

<a id="m14"></a>
### M14 — Cross-arrival memory as the operational resource

- **Central question:** Which restriction separates the classical and quantum learner classes?
- **Understanding target:** The classical learner has unlimited records, precision, computation, adaptive measurements, and fresh ancillas, but retains no quantum information between arrivals. The quantum comparison permits arbitrary persistent memory; the explicit protocol will need only one $`d`$-dimensional register. Both begin independently of the source.
- **Dependencies and story role:** [M06](#m06), [M13](#m13). This identifies the resource responsible for a possible separation without weakening the classical operations.
- **Conceptual connection:** A state freshly prepared from a classical record remains inside the classical class; a retained unknown specimen carries different information.
- **Source pointers:** Watrous [§2.2.1][w-channels] and [§2.3.2][w-instruments]; project [learner classes](../science/model.md#2-learner-classes) and [optimality quantifiers](../science/model.md#3-accuracy-and-optimality).

<a id="m15"></a>
### M15 — Epoch age and the information still relevant

- **Central question:** How much of an arbitrarily long history can concern the current hidden state?
- **Understanding target:** Given the refresh boundaries, older epochs are independent of the current draw. The current age has stationary law $`\Pr(A=a)=rq^a`$ and mean $`q/r`$; the initialized age $`A_t`$ is truncated at $`t-1`$. The source itself is stationary in distribution even though its hidden state changes.
- **Dependencies and story role:** [M13](#m13), [M14](#m14). This replaces total archive length by the amount of potentially relevant within-epoch history.
- **Conceptual connection:** The latent state's correlation lifetime limits the amount of training information available for the current decision.
- **Source pointers:** Watrous [§1.2.2][w-probability] for probability and expectation; project [age distribution](../science/classical_prediction.md#age-distribution-and-the-upper-bound) and [source interpretation](../science/interpretation.md#1-why-an-unlimited-archive-does-not-replace-current-information).

<a id="m16"></a>
### M16 — The Haar posterior for an arbitrary training effect

- **Central question:** What can an unrestricted collective measurement of pure training copies reveal about a future test?
- **Understanding target:** Compress the training effect to the symmetric subspace, normalize it to $`B_z`$, and let $`\tau_z`$ be its one-particle reduction. Haar moments and a permutation identity give $`R_z=(I+m\tau_z)/(d+m)`$ without a rank-one assumption on the effect.
- **Dependencies and story role:** [M10](#m10), [M11](#m11), [M12](#m12). This introduces the inherited arbitrary-effect identity used by the classical converse.
- **Conceptual connection:** An unrestricted measurement record has a constrained posterior predictive state, even when its classical description is unlimited.
- **Source pointers:** Watrous [§7.1.1][w-permutations] and [§7.2.1][w-haar-moment] for the symmetry machinery; [Hayashi, Dasgupta, and Warsi](../references/RELATED_WORK.md#hayashi2026) for the posterior identity; project [full derivation](../science/haar_posterior.md#posterior-mean-for-an-arbitrary-training-effect).

<a id="m17"></a>
### M17 — Exact classification after a classical training record

- **Central question:** How does the posterior constraint bound—and exactly characterize—the test accuracy?
- **Understanding target:** Trace-distance discrimination yields success $`1/2+m(d-1)/[2d(d+m)]`$. A covariant training POVM followed by a projector test attains the bound. At zero training copies, the averaged hypotheses coincide and the advantage vanishes.
- **Dependencies and story role:** [M07](#m07), [M16](#m16). This converts the inherited state identity into the fixed-age classification quantity required by the temporal argument.
- **Conceptual connection:** The weight $`m/(d+m)`$ measures how much usable predictive information a classical record can carry about an unknown direction.
- **Source pointers:** Watrous [§3.1.1, Theorem 3.4][w-helstrom]; project [classification bound](../science/haar_posterior.md#from-the-posterior-to-a-classification-bound) and [attaining measurement](../science/haar_posterior.md#attainment-by-a-covariant-training-measurement); bridge [worked example](WATROUS_BRIDGE.md#worked-qubit-example).

<a id="m18"></a>
### M18 — Domination by a per-round pure-copy experiment

- **Central question:** Why does a static training-record bound apply to every adaptive classical online policy?
- **Understanding target:** At a fixed round, reveal the refresh boundaries and supply $`A_t`$ pure training copies. Random replacement by background simulates the real earlier inputs, and the adaptive history becomes a collective POVM with a classical output. The bundle must be measured before the current test; it is a per-round upper-bound device.
- **Dependencies and story role:** [M04](#m04), [M14](#m14), [M15](#m15), [M17](#m17). This is the causal bridge from the static lemma to the online learner class.
- **Conceptual connection:** A stronger comparison experiment proves an impossibility bound without supplying its extra resources to either actual algorithm.
- **Source pointers:** Watrous [§2.2.1][w-channels] and [§2.3.1][w-measurements] for channel composition and POVMs; project [domination argument](../science/classical_prediction.md#the-per-round-comparison-experiment); bridge [classical mechanism](WATROUS_BRIDGE.md#classical-mechanism).

<a id="m19"></a>
### M19 — The classical upper bound from geometric age

- **Central question:** What remains of the fixed-age learning bound after hidden refreshes are averaged?
- **Understanding target:** The bound is $`(1-1/d)\mathbb E[A/(d+A)]/2`$. Concavity and $`\mathbb EA=q/r`$ give $`(1-1/d)q/[2(rd+q)]`$, hence $`O(q/(1+rd))`$. The domination is uniform over policies and finite horizons, supporting the stated supremum-of-limsup optimum.
- **Dependencies and story role:** [M15](#m15), [M18](#m18). This completes the converse against unlimited classical records.
- **Conceptual connection:** Dimension and latent lifetime enter the same denominator because state information must be acquired before it becomes irrelevant.
- **Source pointers:** Watrous [§1.2.1][w-convexity] and [§1.2.2][w-probability] for concavity and averaging; project [age bound](../science/classical_prediction.md#age-distribution-and-the-upper-bound) and [accuracy definition](../science/model.md#3-accuracy-and-optimality).

<a id="m20"></a>
### M20 — Prediction by a fixed-basis repetition cache

- **Central question:** Can an explicit classical policy achieve the upper bound's order without labels or refresh flags?
- **Understanding target:** Measure each specimen in a fixed basis and predict signal if the current symbol occurs in the previous $`L`$ outcomes. Within an epoch, an unlabeled outcome has probability $`z_j=(p_j+1/d)/2`$. Cache membership uses only observed symbols and $`O(L\log d)`$ bits.
- **Dependencies and story role:** [M05](#m05), [M13](#m13), [M19](#m19). This begins the constructive half of the classical result.
- **Conceptual connection:** Repeated basis outcomes can reveal a persistent signal statistically without reconstructing its complete quantum state.
- **Source pointers:** Watrous [§2.3.1][w-measurements]; project [cache classifier](../science/classical_prediction.md#an-explicit-cache-classifier).

<a id="m21"></a>
### M21 — Why every refresh partition contributes nonnegative advantage

- **Central question:** Why can favorable no-refresh histories furnish a lower bound without being canceled by other histories?
- **Understanding target:** Conditioning on the cache's epoch partition separates older avoidance factors from the current epoch. The remaining signal-minus-background difference is a negative covariance between $`p`$ and a decreasing avoidance function, and is therefore nonnegative for every partition.
- **Dependencies and story role:** [M15](#m15), [M20](#m20). This supplies the sign argument that makes the cache lower bound rigorous.
- **Conceptual connection:** Conditional independence and monotonicity allow an average-case algorithm to retain one favorable event while controlling all complementary events.
- **Source pointers:** Watrous [§1.2.2][w-probability] and [§7.2.1][w-haar] for the probabilistic setting; project [partition positivity proof](../science/classical_prediction.md#every-refresh-history-contributes-nonnegative-advantage).

<a id="m22"></a>
### M22 — The Beta identity and the matching cache window

- **Central question:** What window length balances collecting useful repetitions against retaining obsolete outcomes?
- **Understanding target:** A Haar basis probability has law $`\mathrm{Beta}(1,d-1)`$. Integration by parts converts the covariance into a positive integral and gives an explicit lower bound. Choosing $`L=\lfloor\min(d,1/r)\rfloor`$ and using $`q^L\ge q/e`$ yields advantage at least $`q/[128e^3(1+rd)]`$.
- **Dependencies and story role:** [M11](#m11), [M21](#m21). This matches the classical converse uniformly over the allowed rates and dimensions.
- **Conceptual connection:** The useful window ends at the smaller of the state-information scale and the correlation lifetime.
- **Source pointers:** Watrous [§7.2.1][w-haar] for the random-state foundation; project [Beta identity, constants, and window choice](../science/classical_prediction.md#the-beta-identity-and-an-explicit-constant).

<a id="m23"></a>
### M23 — Exact cache accuracy and finite horizons

- **Central question:** How does the constructive cache behave before and after its initial window is filled?
- **Understanding target:** The avoidance quantities $`h_k,G_m`$ satisfy an exact renewal recurrence, and the full advantage sums the contributions of all possible current-epoch ages. Initial fair guesses give finite-horizon factor $`(1-L/T)_+`$. Exact rational cases check the recurrence without replacing its proof.
- **Dependencies and story role:** [M15](#m15), [M20](#m20), [M22](#m22). This closes the classical branch with an evaluable formula and a causal startup statement.
- **Conceptual connection:** A stationary source distribution does not imply a learner begins with a populated memory.
- **Source pointers:** Watrous [§1.2.2][w-probability]; project [exact recurrence](../science/classical_prediction.md#exact-cache-recurrence) and [finite horizons](../science/classical_prediction.md#finite-horizons).

<a id="m24"></a>
### M24 — The global SWAP instrument and its retained state

- **Central question:** Which physical comparison both produces the current prediction and leaves a usable memory?
- **Understanding target:** The global projectors $`(I\pm S)/2`$ are implemented with a controlled register swap and ancilla readout. After the input is discarded, the nonselective memory becomes $`(\sigma+\rho)/2`$. Destructive readout or refinement into local swap measurements generally changes this retained-state channel.
- **Dependencies and story role:** [M06](#m06), [M09](#m09), [M14](#m14). This specifies the constructive quantum operation at the instrument level.
- **Conceptual connection:** Measurement backaction is part of the algorithm's information dynamics, rather than an implementation detail that can be omitted.
- **Source pointers:** Watrous [§2.3.2, Eqs.2.255–2.262][w-instruments]; project [physical instrument](../science/quantum_prediction.md#a-physical-retained-register-swap-instrument) and [averaged update](../science/quantum_prediction.md#exact-averaged-memory-update); bridge [quantum mechanism](WATROUS_BRIDGE.md#quantum-mechanism).

<a id="m25"></a>
### M25 — Overlap dynamics and the quantum tracking advantage

- **Central question:** How does repeated comparison maintain useful alignment with a changing hidden state?
- **Understanding target:** The excess overlap obeys $`y_{t+1}=qy_t/2+q(1-1/d)/4`$. Its solution gives stationary advantage $`(1-1/d)q/[8(1+r)]`$ and an exact geometric startup correction. Only pure redraws with exact first moment $`I/d`$ are needed for this calculation.
- **Dependencies and story role:** [M15](#m15), [M24](#m24). This turns the local instrument into the quantum achievability theorem.
- **Conceptual connection:** Information enters from each new specimen while old alignment decays through both measurement and source refresh.
- **Source pointers:** Watrous [§2.2.1][w-channels] and [§1.2.2][w-probability] for linear channels and averaging; project [overlap recurrence](../science/quantum_prediction.md#correlation-recursion-and-stationary-accuracy) and [finite-horizon formula](../science/quantum_prediction.md#finite-horizon-accuracy).

<a id="m26"></a>
### M26 — Unlimited-memory converse and the disjoint-pair baseline

- **Central question:** What limits even an unrestricted quantum learner, and how much of the scaling requires recycling?
- **Understanding target:** A fresh redraw gives no label information, while knowing the pure state on a persistent transition gives the Helstrom ceiling. This bounds advantage by $`q(1-1/d)/2`$. Disjoint adjacent pairs already achieve $`q(1-1/d)/16`$, so rolling retention improves a constant by at most two.
- **Dependencies and story role:** [M07](#m07), [M15](#m15), [M25](#m25). This establishes quantum constant-factor optimality and identifies what recycling contributes.
- **Conceptual connection:** The persistent advantage relies on coherent comparison across arrivals; indefinite reuse of one learned program is not necessary.
- **Source pointers:** Watrous [§3.1.1][w-discrimination]; project [arbitrary-memory converse](../science/quantum_prediction.md#converse-for-arbitrary-quantum-memory) and [pair baseline](../science/quantum_prediction.md#disjoint-pairs-already-achieve-the-quantum-scaling).

<a id="m27"></a>
### M27 — The optimal dimension-times-refresh frontier

- **Central question:** What law emerges when both learner classes have matching upper and lower bounds?
- **Understanding target:** The optimal advantages satisfy $`\beta_C=\Theta(q/(1+rd))`$ and $`\beta_Q=\Theta(q)`$, uniformly for $`d\ge2`$ and $`0<r<1`$. Their advantage ratio is $`\Theta(1+rd)`$. At fixed refresh probability and $`d=2^n`$, the classical advantage is exponentially small in $`n`$ even over arbitrarily long deployment.
- **Dependencies and story role:** [M19](#m19), [M22](#m22), [M25](#m25), [M26](#m26). This assembles the principal theorem from the two mechanism-specific arguments.
- **Conceptual connection:** The separation concerns excess accuracy above chance, not a ratio of total success probabilities or an automatic runtime speedup.
- **Source pointers:** Watrous [§3.1.1][w-discrimination] for the operational accuracy measure; project [matching law](../science/model.md#4-matching-prediction-law) and [parameter regimes](../science/interpretation.md#3-three-parameter-regimes); bridge [reading the frontier](WATROUS_BRIDGE.md#reading-the-frontier).

<a id="m28"></a>
### M28 — Efficient native sources through finite designs

- **Central question:** Can the required hidden signals be generated without assuming inexpensive exact Haar preparation?
- **Understanding target:** A strong unitary-design guarantee controls normalized pure-state moments, and a private Pauli twirl enforces first moment $`I/d`$ exactly. Transferring the classical converse adds at most $`q\epsilon/2+q^K/2`$; preserving the cache lower bound additionally requires $`K\ge L+1`$. Suitable finite-gate preparations are polynomial for fixed or inverse-polynomial refresh rates.
- **Dependencies and story role:** [M08](#m08), [M11](#m11), [M18](#m18), [M21](#m21), [M27](#m27). This places the statistical separation in a preparation-accounted source model.
- **Conceptual connection:** Source approximation is controlled on joint experiments before conditioning, and its moment order is tied to the lifetime of relevant information.
- **Source pointers:** Watrous [§7.2.1][w-haar] and [§3.3.2][w-diamond] for invariant measures and channel norms; [BHH construction](../references/RELATED_WORK.md#brandao2016); project [efficient-source theorem](../science/efficient_sources.md#a-sufficient-parameter-choice-and-its-cost); bridge [source and noise](WATROUS_BRIDGE.md#source-and-noise).

<a id="m29"></a>
### M29 — Logical instrument error and the local-noise boundary

- **Central question:** Which implementation errors preserve a quantified prediction advantage?
- **Understanding target:** A uniform half-diamond error $`\delta`$ on the complete logical instrument gives memory-error recursion $`e_{t+1}\le e_t/2+\delta`$ and accuracy loss at most $`3\delta/2`$, uniformly in time. The exactly solvable global-depolarization model is separate from independent physical noise on each qubit or gate.
- **Dependencies and story role:** [M06](#m06), [M08](#m08), [M24](#m24), [M25](#m25). This connects the ideal comparison to a specified implementation guarantee.
- **Conceptual connection:** Contractive memory dynamics can prevent error accumulation with stream length, but they do not supply a fault-tolerance construction or a local-noise threshold.
- **Source pointers:** Watrous [§2.3.2][w-instruments], [§3.3.2][w-diamond], and [§3.3.3][w-channel-distances]; project [uniform instrument bound](../science/implementation_and_noise.md#uniform-error-of-the-complete-instrument) and [global-noise model](../science/implementation_and_noise.md#an-exactly-solvable-global-noise-model).

<a id="m30"></a>
### M30 — Endpoints, resource accounting, and the complete scientific conclusion

- **Central question:** What physical conclusion survives when the theorem's assumptions, endpoints, and resource costs are considered together?
- **Understanding target:** At $`r=1`$ both advantages vanish; at $`r=0`$ sparse informationally complete sampling lets classical prediction approach the known-state optimum. For intermediate rates, the matching law concerns expected causal accuracy on native quantum specimens, with unlimited classical records, one sufficient coherent register, accounted source preparation, and the stated logical-noise assumptions.
- **Dependencies and story role:** [M23](#m23), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). This combines the mechanisms into the complete physical interpretation and its domain of validity.
- **Conceptual connection:** A stationary observed process can have a changing latent state, and an unlimited archive need not replace a short-lived quantum reference.
- **Source pointers:** Watrous [§2.1.2][w-states] and [§3.1.1][w-discrimination] for state and decision semantics; project [endpoints](../science/model.md#6-endpoints-and-interpretation), [resource accounting](../science/interpretation.md#4-resources-that-are-charged), and [scope](../science/interpretation.md#5-scope-of-the-source-and-noise-models); bridge [complete frontier interpretation](WATROUS_BRIDGE.md#reading-the-frontier).

[watrous]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf
[w-operators]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=16
[w-norms]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=32
[w-convexity]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=43
[w-probability]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=55
[w-registers]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=66
[w-states]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=69
[w-reductions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=75
[w-channels]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=80
[w-channel-representations]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=85
[w-measurements]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=108
[w-measurement-notions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=113
[w-instruments]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=119
[w-ensembles]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=121
[w-discrimination]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=133
[w-helstrom]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=136
[w-diamond]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=174
[w-diamond-definition]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=178
[w-channel-distances]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=183
[w-permutations]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=399
[w-symmetric-dimension]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=403
[w-haar]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=416
[w-haar-moment]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=424
