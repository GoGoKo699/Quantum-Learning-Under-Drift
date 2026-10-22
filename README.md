# Quantum Learning Under Drift

**How long must an unknown quantum signal remain correlated before a learner can classify each new specimen, and what changes when the learner retains quantum memory?**

A source emits one $`n`$-qubit specimen per round. With equal probability it is an unknown pure signal or maximally mixed background. Between arrivals, the hidden signal is independently refreshed with probability $`r`$. Each prediction must be made before the next specimen arrives; labels and refresh times are not revealed.

Write $`d=2^n`$ and $`q=1-r`$. The optimal long-run expected accuracy above random guessing obeys

```math
\boxed{
\beta_{\mathrm C}(d,r)=\Theta\!\left(\frac{q}{1+rd}\right),
\qquad
\beta_{\mathrm Q}(d,r)=\Theta(q).
}
```

The constants are uniform for $`d\ge2`$ and $`0<r<1`$. The classical-record learner may use arbitrary adaptive quantum measurements of each input and unlimited classical storage and computation. It retains no quantum information between arrivals. One retained $`n`$-qubit register suffices for the quantum scaling, while the quantum upper bound permits unlimited memory.

| Result | Meaning | Proof |
|---|---|---|
| Universal classical bound | Even revealed refresh boundaries and pure training copies measured before the test give advantage at most $`(1-1/d)q/[2(rd+q)]`$. | [Classical prediction](science/classical_prediction.md) |
| Matching classical algorithm | Fixed-basis measurements and a cache of $`\lfloor\min(d,1/r)\rfloor`$ recent outcomes attain the same scaling. | [Cache construction](science/classical_prediction.md) |
| Explicit quantum algorithm | A retained-register SWAP measurement gives exact stationary advantage $`(1-1/d)q/[8(1+r)]`$. | [Quantum prediction](science/quantum_prediction.md) |
| Efficient source | Finite-gate approximate designs preserve the matching scaling, with polynomial preparation for fixed or inverse-polynomial refresh rates. | [Source construction](science/efficient_sources.md) |

At fixed $`0<r<1`$, the classical advantage is $`\Theta(2^{-n})`$ and the quantum advantage is constant. The crossover is set by $`rd`$: classical prediction needs a correlation lifetime comparable to the state-space dimension. This is an accuracy comparison on native quantum inputs. The explicit quantum protocol need not classify almost perfectly; at $`r=1/2`$ its accuracy approaches $`13/24\approx54.17\%`$.

## Read the science

Start with the [operational model and exact results](science/model.md). The [Haar posterior lemma](science/haar_posterior.md) supplies an inherited state-estimation ingredient. The two prediction pages establish the complete matching law; [interpretation](science/interpretation.md) connects the bounds to correlation lifetime and their resource meaning.

| Scientific question | Authoritative account |
|---|---|
| What is known, what is supplied, and when must a prediction be made? | [Model and theorem statements](science/model.md) |
| What can a classical record reveal about a future quantum test? | [Haar posterior and discrimination](science/haar_posterior.md) |
| Why does unlimited classical history not remove the drift penalty? | [Classical converse and matching cache](science/classical_prediction.md) |
| How does one coherent register track the signal? | [Quantum protocol, converse and finite horizon](science/quantum_prediction.md) |
| Can the hidden states be prepared with polynomial resources? | [Efficient native sources](science/efficient_sources.md) |
| Which instrument and noise assumptions support the claim? | [Implementation and noise](science/implementation_and_noise.md) |
| What does the crossover say, and where does it stop applying? | [Physical interpretation](science/interpretation.md) |
| Which ingredients and nearby results are established prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

[The LLM reading guide](llms.txt) maps questions to these authoritative files.

## Reproduce the checks

See [verification instructions](verification/README.md) for dependencies, commands, expected outputs and the scope of each check. The suite checks the physical SWAP instrument, symmetric-subspace posterior identities, and the cache formula against an independent exact enumeration. The analytical bounds rest on the written proofs; finite checks do not establish a general theorem or priority.

## Scope

The exact matching law uses an independent Haar refresh model and a product source conditioned on its hidden state path. The observed stream is stationary in distribution; its latent signal has a finite lifetime. The source-construction corollary has its own approximation and efficiency regime. Both learners receive the same native quantum specimens without a source description, extra-copy oracle or QRAM.

The quantum implementation assumes ideal or protected logical inputs and memory. Constant global depolarization and constant independent local noise have different consequences. The comparison is an expected prediction-accuracy law, with finite-horizon startup bounds, rather than a full runtime speedup or a worst-case guarantee on every realized stream.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
