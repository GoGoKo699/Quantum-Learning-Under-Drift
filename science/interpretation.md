# Correlation lifetime and predictive information

The [matching theorem](model.md#4-matching-prediction-law) identifies a competition between two scales: the dimension $`d`$ of an unknown quantum state and the number $`1/r`$ of arrivals over which that state typically persists. Its quantum and classical protocols use the same incoming systems and must answer at the same time. Their difference is what information remains available across that boundary.

## 1. Why an unlimited archive does not replace current information

Classical records from earlier epochs refer to independent hidden states. They can influence measurement choices, but they do not reveal the current state. The classical converse makes this precise by strengthening the learner: reveal every refresh boundary and replace all earlier inputs in the current epoch by pure training copies. Even then, after those copies have been converted to a classical record, the current test is governed by the posterior mean

```math
R_z=\frac{I+m\tau_z}{d+m},
```

where $`m`$ is the number of previous specimens in the current epoch and $`\tau_z`$ is a density operator. The informative part has weight only $`m/(d+m)`$. Averaging over the geometric epoch age produces the dimension-times-refresh crossover. The [posterior proof](haar_posterior.md) and [causal reduction](classical_prediction.md) are separate parts of that argument.

This conclusion does not impose a small classical buffer. An unlimited record, arbitrarily difficult measurements, and unlimited classical computation are already included. The explicit matching cache is a constructive algorithm inside that larger class.

## 2. What coherent comparison retains

A previous quantum specimen supplies a physical reference correlated with the current signal. A global SWAP measurement can test that relation without reconstructing a classical description of the unknown state. Its nonselective retained-register update is an exact averaging channel. The resulting overlap with the current hidden state follows a scalar linear recurrence, yielding the [closed-form accuracy](quantum_prediction.md).

The information refreshed into the register is sufficient to sustain an order-one prediction advantage when $`r`$ is fixed below one. The register need not be a high-fidelity copy of the latent state. The theorem establishes the rolling protocol's optimality only up to a universal constant factor. Comparing independent disjoint pairs already gives the same quantum scaling. Retaining the postmeasurement state improves the constant and gives a prediction opportunity at every round after startup; state recycling itself is an established technique, discussed in [related work](../references/RELATED_WORK.md).

## 3. Three parameter regimes

| Regime | Classical optimum above chance | Quantum optimum above chance | Consequence |
|---|---|---|---|
| $`rd\ll1`$ | Order $`q`$ | Order $`q`$ | The source persists long enough for useful classical prediction; there is no growing scaling separation. |
| $`rd\gg1`$ | Order $`q/(rd)`$ | Order $`q`$ | Coherent retention gives a growing advantage ratio of order $`rd`$. |
| $`r\to1`$ | Both include the small factor $`q=1-r`$ | Both include the small factor $`q=1-r`$ | Most tests follow an independent redraw, so absolute prediction advantages vanish. |

For fixed $`0<r<1`$ and $`d=2^n`$, the classical prediction advantage remains exponentially small in $`n`$ even after arbitrarily long deployment, while the SWAP learner's startup is independent of dimension. The theorem is about accuracy at the stated arrival rate and causal deadline. It does not convert these quantities into an unqualified runtime or total-experiment speedup.

### A numerical reference point

At $`r=1/2`$, the explicit SWAP advantage and the classical upper bound are

```math
B_{\mathrm{swap}}=\frac{d-1}{24d},
\qquad
\beta_{\mathrm C}\le\frac{d-1}{2d(d+1)}.
```

| Number of qubits $`n`$ | SWAP accuracy | Upper bound on every classical-record learner |
|---:|---:|---:|
| 4 | $`53.90625\%`$ | $`52.75735\%`$ |
| 10 | $`54.16260\%`$ | $`50.04873\%`$ |
| 20 | $`54.16666\%`$ | $`50.00005\%`$ |

The classical column is an upper bound, not the measured performance of the cache or a claim of exact optimality. The displayed quantum policy retains a useful but modest advantage; its success is not close to certainty. Small dimensions need not show a separation between this particular policy and the best classical one.

## 4. Resources that are charged

| Resource | Scope of the comparison |
|---|---|
| Incoming data | One physical quantum specimen per round for both learners. |
| Classical storage and processing | Unlimited in the converse; the matching cache uses $`O(L\log d)`$ bits. |
| Persistent coherent memory | None for the classical class; $`n`$ logical qubits suffice for the constructive quantum bound. |
| Quantum processing per arrival | Arbitrary within-round measurements are allowed to the classical class; the explicit quantum policy uses $`O(n)`$ controlled-SWAP gates in the stated logical circuit model. |
| Source preparation | Exact Haar is an ideal statistical model. The finite-design corollary pays polynomial preparation cost in its specified regime. |
| Time and coherence | Memory must remain usable across the actual interval between arrivals; hardware scheduling and error correction contribute physical overhead. |
| Auxiliary access | No source description, inverse, extra-copy oracle, refresh flags or labels are provided. |

The quantum protocol uses at most $`2n+1`$ qubits during the global comparison, counting memory, current input and ancilla. A classical learner may use arbitrarily many fresh ancillas within a round; the converse is not a qubit-count restriction on those operations. [Implementation and noise](implementation_and_noise.md) explains why replacing the global projective SWAP instrument by a destructive local readout would change the retained-memory dynamics.

## 5. Scope of the source and noise models

The refresh experiment is an explicit model of an unknown signal with finite lifetime. A full refresh draws an independent state; it does not represent every possible slowly varying Hamiltonian, adversarial drift sequence, or noisy channel. The observed stream is stationary in law, while its latent state changes.

The efficient-source corollary addresses the cost of preparing hidden signals. Its moment-order requirement grows as the refresh probability decreases, so it must be distinguished from the exact all-rate Haar theorem. It does not grant the learner the source's private circuit seed.

The input background $`I/d`$ is a class in the statistical experiment. It is not a model of implementation errors in the learner. The latter are treated separately: a controlled bound on the full logical instrument, or a global depolarizing memory model, has an explicit consequence. Fixed independent local noise can suppress the relevant many-qubit overlap and is not covered by a dimension-independent global-noise parameter.

## 6. Established ingredients and added conclusion

State comparison, Haar-state estimation, quantum-memory separations, streaming purification and online quantum learning are established research directions. The [related-work account](../references/RELATED_WORK.md) compares their actual inputs, outputs, memory restrictions and loss functions.

The result developed here is the matching per-specimen prediction law in the specified renewal experiment, including a classical strategy that needs neither labels nor refresh flags, a converse against unlimited classical records, and a source-preparation corollary. Its limitations are part of that conclusion. Finite checks validate the stated identities and examples; the universal law is supported by the analytical proofs.
