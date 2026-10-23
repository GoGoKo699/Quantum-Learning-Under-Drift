# Related work and provenance

The question studied here is causal classification of a stream of physical quantum specimens. A hidden pure state in dimension $`d\ge2`$ is retained with probability $`q=1-r`$ or independently refreshed from Haar measure with probability $`0<r<1`$. Each arrival supplies one specimen, either that state or $`I/d`$, with equal prior probabilities. The learner must predict its label before the next arrival. The classical comparator may retain unlimited classical information and perform unlimited computation, but no quantum register survives between arrivals. Labels, refresh times, and source preparation descriptions are not supplied.

The results developed in this repository are the matching orders

```math
\beta_{\mathrm C}=\Theta\!\left(\frac{q}{1+rd}\right),
\qquad \beta_{\mathrm Q}=\Theta(q),
```

for advantage above random guessing, together with an explicit retained-register protocol, an efficient-source regime, and specified implementation-error bounds. See the [classical](../science/classical_prediction.md) and [quantum](../science/quantum_prediction.md) derivations. The comparison below concerns this particular experiment. It does not support a claim to the first quantum memory advantage, the first streaming quantum algorithm, or the first quantum learning result with a changing target. With Haar initialization, the joint source law is stationary; it is the latent state that changes.

## Which ingredients are inherited?

| Ingredient | Attribution and use here |
| --- | --- |
| Haar moments and the arbitrary-effect posterior identity | The identity $`\mathbb E[P\mid E]=(I+m\rho_E)/(d+m)`$ is inherited from [Hayashi, Dasgupta, and Warsi, Lemma 10](#hayashi2026). Its binary signal-versus-background consequence and covariant attainment are derived in [Haar posterior prediction](../science/haar_posterior.md). These consequences use standard state discrimination. |
| Reduction of a causal classical history to a training effect | Developed in [classical prediction](../science/classical_prediction.md): reveal refresh boundaries, provide pure copies for the current epoch, and absorb replacements, adaptive measurements, and independent earlier records into a POVM. This gives $`\Pr(h\mid P)=\operatorname{Tr}(E_hP^{\otimes m})`$. The reduction and the refresh assumptions are not claims of the posterior paper. |
| Matched dependence on dimension and refresh rate | The geometric-age converse, the fixed-basis cache lower bound, and their combination into the displayed frontier are developed in this repository. The sources below establish related experiments and tools, rather than this causal per-arrival risk law. This is a scoped comparison, not an exhaustive priority claim. |
| SWAP measurement and retention of a measured register | The comparison primitive is standard; see [Buhrman et al.](#buhrman2001). Streaming purification and repeated-SWAP change detection are direct protocol antecedents: [Childs et al.](#childs2025) and [Zheng](#zheng2026). The nonstopping, nonselective memory recursion and its prediction accuracy are worked out here. |
| Polynomial-size approximate designs | The construction and approximation norm are inherited from [Brandão, Harrow, and Horodecki](#brandao2016). The exact first-moment twirl, current-epoch risk transfer, age truncation, and private-source access specification are developed in [efficient sources](../science/efficient_sources.md). |
| Physical noise assessment | The exact channel recursions and uniform instrument-error estimate are developed in [implementation and noise](../science/implementation_and_noise.md). [Cotler, Gong, and Kannan](#noisy2026) supplies relevant noisy-access obstructions, not these formulas. |

## Closest comparisons

| Work | Data and prediction objective | Relevant resource or result | Distinction from the present experiment |
| --- | --- | --- | --- |
| [Streaming quantum state purification](#childs2025) | Repeated noisy copies of one fixed unknown pure state; output a purified quantum state | Streaming SWAP-based purification with small quantum storage and dimension-independent sample cost at fixed noise | The present output is a new classical label at every arrival, and the hidden state repeatedly refreshes. |
| [Zheng, Chapter 5](#zheng2026) | Unknown pure states before and after a change; stop upon detection without false alarms | A repeated-SWAP procedure retains one postmeasurement system; its conditional update and stopping performance are analyzed | Here prediction continues after every outcome, background inputs are mixed, and errors are allowed and charged at every arrival. |
| [Distinguishing quantum processes with bounded coherent memory](#zonnios2026) | Discriminate two specified multi-time processes | Bounded coherent memory with unrestricted classical records; a hierarchy of process-discrimination strategies | The present target is each fresh latent label, with analytic dimension-versus-refresh bounds for an unknown source. |
| [Zhao et al., Theorem 4 and Theorem F.12](#zhao2026) | Classical training data refreshed in blocks; classify classical test vectors | Small quantum sketches compared with classical machines below a specified memory-size threshold | The present classical comparator has unlimited classical storage, and its inputs are single physical quantum specimens. |
| [Adaptive Online Learning of Quantum States](#chen2024) | Track changing density-state hypotheses using supplied observables and loss or approximate expectation feedback | Adaptive and dynamic regret controlled by shifts or path variation | Here there is one specimen per arrival and no external label or Born-probability feedback. The comparison concerns what remains coherent between arrivals. |

## Annotated references

Stable anchors on this page match the keys in [references.bib](references.bib). Preprint versions identify the texts used for the stated theorem or model comparisons; a published paper and a later corrected preprint can have different dates.

<a id="watrous2018"></a>

### Watrous: the selected educational foundation

John Watrous. **The Theory of Quantum Information.** Cambridge University Press (2018). [DOI](https://doi.org/10.1017/9781316848142) · [Author-hosted prepublication draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf).

This is the project's single educational anchor. Chapter 2 supplies the state, channel, measurement, and instrument framework; Theorem 3.4 gives binary state discrimination; Section 3.3.2 treats the completely bounded trace norm; Chapter 7 supplies symmetric subspaces and Haar averages. The [source bridge](../learning/WATROUS_BRIDGE.md) gives verified section pointers, translates conventions, and supplies the additional steps to the refresh model. The arbitrary-effect posterior attribution below and the approximate-design construction remain separate research dependencies. The book is linked rather than reproduced.

<a id="hayashi2026"></a>

### Hayashi, Dasgupta, and Warsi: arbitrary-effect Haar posterior

Masahito Hayashi, Ayanava Dasgupta, and Naqueeb Ahmad Warsi. **Haar-Bayesian Pure-State Prediction under Relative-Entropy Loss: Arbitrary-Effect Reduction and Global Optimality.** arXiv:2609.10072v1, 9 September 2026. [Primary record](https://arxiv.org/abs/2609.10072v1) · [Full text](https://arxiv.org/pdf/2609.10072v1) · [DOI](https://doi.org/10.48550/arXiv.2609.10072).

Lemma 10, equations (51)–(52), gives the posterior mean for an arbitrary positive effect on the symmetric subspace of the training copies. The density matrix $`\rho_E`$ is the normalized one-particle reduction of that effect. The paper optimizes relative-entropy prediction loss. We use the posterior identity and then derive a trace-distance classification bound; neither the causal reconstruction of a classical history nor the refresh-rate frontier is attributed to this paper.

<a id="brandao2016"></a>

### Brandão, Harrow, and Horodecki: approximate designs from circuits

Fernando G. S. L. Brandão, Aram W. Harrow, and Michał Horodecki. **Local Random Quantum Circuits are Approximate Polynomial-Designs.** *Communications in Mathematical Physics* **346**(2), 397–434 (2016). [DOI](https://doi.org/10.1007/s00220-016-2706-8) · [arXiv:1208.0692v4](https://arxiv.org/abs/1208.0692v4), corrected version dated 9 July 2019 · [Full text](https://arxiv.org/pdf/1208.0692v4).

Definition 2 uses relative completely-positive order; Lemma 3 converts that guarantee to a diamond-norm bound. Corollaries 6–7 give polynomial-length random circuits, including a fixed finite universal gate set with inverses and algebraic matrix entries. These statements justify the dimension-safe moment approximation used here. They do not by themselves establish a drifting-source prediction result, and the present efficient preparation guarantee is restricted to fixed or inverse-polynomial refresh rates.

<a id="buhrman2001"></a>

### Buhrman, Cleve, Watrous, and de Wolf: SWAP comparison

Harry Buhrman, Richard Cleve, John Watrous, and Ronald de Wolf. **Quantum fingerprinting.** *Physical Review Letters* **87**, 167902 (2001). [DOI](https://doi.org/10.1103/PhysRevLett.87.167902) · [arXiv:quant-ph/0102001v1](https://arxiv.org/abs/quant-ph/0102001v1), 1 February 2001.

Quantum fingerprint comparison supplies the familiar ancilla-controlled SWAP test. The repository uses its global two-outcome Lüders instrument, including the retained state, rather than only its outcome probabilities. The streaming recursion and the changing-source classification task are separate developments.

<a id="childs2025"></a>

### Childs et al.: streaming purification

Andrew M. Childs, Honghao Fu, Debbie Leung, Zhi Li, Maris Ozols, and Vedang Vyas. **Streaming quantum state purification.** *Quantum* **9**, 1603 (2025). [Journal article and DOI](https://doi.org/10.22331/q-2025-01-21-1603) · [arXiv:2309.16387v4](https://arxiv.org/abs/2309.16387v4), final journal version dated 1 January 2025.

The input is a depolarized copy of a fixed unknown pure state. The recursive SWAP procedure purifies while retaining only a logarithmic number of qudits in the sample count; at fixed input noise, its sample complexity is independent of dimension. Section 2 develops the procedure, and Section 4.2 compares purification with tomography. This is a direct antecedent for retaining useful quantum information in a stream. Its output is a purified state, rather than a causal label for every specimen under repeated source refresh.

<a id="zheng2026"></a>

### Zheng: online change detection with retained quantum memory

Alice Zheng. **Quantum Online Learning.** PhD dissertation, Virginia Polytechnic Institute and State University, 6 July 2026. [Institutional record](https://vtechworks.lib.vt.edu/items/808fc73c-9573-4f8c-be0b-ef85bc88b905) · [Full dissertation](https://vtechworks.lib.vt.edu/bitstreams/353a1eff-4a86-4316-909a-9320adf937e2/download).

Chapter 5, *Changepoint detection in unknown quantum states with no false alarms*, studies a stopping task. Section 5.3, Algorithm 5.1, and Lemma 5.10 analyze repeated SWAP tests while retaining one system. Equation (5.12) gives the conditional state after a symmetric outcome. These are close instrument-level precedents. The present learner instead continues after both outcomes and is evaluated by minimum-error label prediction throughout a stream containing mixed background states and repeated latent refreshes.

<a id="zonnios2026"></a>

### Zonnios and Binder: coherent memory with unrestricted classical records

Magdalini Zonnios and Felix C. Binder. **Distinguishing quantum processes with bounded coherent memory.** arXiv:2606.19511v1, 17 June 2026. [Primary record](https://arxiv.org/abs/2606.19511v1) · [Full text](https://arxiv.org/html/2606.19511v1) · [DOI](https://doi.org/10.48550/arXiv.2606.19511).

The framework separates bounded coherent memory from unrestricted classical records, and develops a hierarchy for distinguishing quantum processes. Sections III–V establish its relation to general strategies and examine repeated-interaction examples. This is a close resource-model antecedent: unlimited classical storage is not a new framework introduced here. The process-hypothesis objective differs from continual prediction of fresh labels, and the dimension-refresh law is not a result of that paper.

<a id="zhao2026"></a>

### Zhao et al.: dynamic classification of classical data

Haimeng Zhao, Alexander Zlokapa, Hartmut Neven, Ryan Babbush, John Preskill, Jarrod R. McClean, and Hsin-Yuan Huang. **Exponential quantum advantage in processing massive classical data.** arXiv:2604.07639v2, 1 October 2026; first submitted 8 April 2026. [Primary record](https://arxiv.org/abs/2604.07639v2) · [Full text](https://arxiv.org/pdf/2604.07639v2) · [DOI](https://doi.org/10.48550/arXiv.2604.07639).

Theorem 4 and the detailed formulation in Task F.10 and Theorem F.12 include classification with periodically refreshed classical training data. The separation compares small quantum sketches against classical machines whose storage is below a dimension-dependent threshold, even when classical time is unrestricted. Its input-access model and storage restriction distinguish it from unlimited classical-record processing of physical quantum specimens. The existence of this dynamic setting precludes a broad novelty claim based merely on continually refreshed data.

<a id="chen2024"></a>

### Chen et al.: adaptive and dynamic regret

Xinyi Chen, Elad Hazan, Tongyang Li, Zhou Lu, Xinzhao Wang, and Rui Yang. **Adaptive Online Learning of Quantum States.** *Quantum* **8**, 1471 (2024). [Journal article and DOI](https://doi.org/10.22331/q-2024-09-12-1471) · [arXiv:2206.00220v2](https://arxiv.org/abs/2206.00220v2), 9 September 2024 · [Full text](https://arxiv.org/html/2206.00220v2).

This work gives adaptive and dynamic regret guarantees for quantum-state prediction under changing comparators. The learner receives observables and convex-loss feedback; expectation-value prediction statements use supplied approximate Born probabilities. Section 1, including footnote 2, and Section 2 specify that access. These guarantees concern a different feedback experiment from a single unknown physical input with a fresh hidden label and no subsequent label feedback.

<a id="chen2022"></a>

### Chen, Cotler, Huang, and Li: learning with and without quantum memory

Sitan Chen, Jordan Cotler, Hsin-Yuan Huang, and Jerry Li. **Exponential separations between learning with and without quantum memory.** In *2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS)*, pp. 574–585, published 2022. [DOI](https://doi.org/10.1109/FOCS52979.2021.00063) · [arXiv:2111.05881v2](https://arxiv.org/abs/2111.05881v2), 18 November 2021.

The work proves exponential sample-complexity separations for learning properties of quantum states and dynamics, including against adaptive learners that retain only classical measurement records. It establishes the underlying information-resource distinction used by the present comparison. The present contribution is a particular causal prediction frontier for repeatedly refreshed hidden states, rather than the general observation that quantum retention can outperform classical records.

<a id="sentis2019"></a>

### Sentís et al.: unsupervised quantum classification

Gael Sentís, Alex Monràs, Ramon Muñoz-Tapia, John Calsamiglia, and Emilio Bagan. **Unsupervised Classification of Quantum Data.** *Physical Review X* **9**, 041029 (2019). [DOI](https://doi.org/10.1103/PhysRevX.9.041029) · [arXiv:1903.01391v3](https://arxiv.org/abs/1903.01391v3), 8 November 2019.

The task groups an array drawn from two unknown pure-state classes, with a universal global measurement and an output partition. This is a central antecedent for classification directly from quantum data. The two classes are fixed, and the joint partition objective does not impose a label deadline before each next arrival.

<a id="monras2017"></a>

### Monràs, Sentís, and Wittek: inductive supervised learning

Alex Monràs, Gael Sentís, and Peter Wittek. **Inductive Supervised Quantum Learning.** *Physical Review Letters* **118**, 190503 (2017). [DOI](https://doi.org/10.1103/PhysRevLett.118.190503) · [arXiv:1605.07541v2](https://arxiv.org/abs/1605.07541v2), 13 May 2017.

A non-signalling formulation of inductive learning and a channel de Finetti argument yield an asymptotic description in which the training information is converted into classical knowledge before many test predictions. This cautions against assuming a permanent quantum-memory benefit in every learning architecture. Our online learner updates its retained state using successive test specimens; the present experiment does not impose that inductive non-signalling condition.

<a id="sentis2012"></a>

### Sentís et al.: optimal reusable classification without quantum memory

G. Sentís, J. Calsamiglia, R. Muñoz-Tapia, and E. Bagan. **Quantum learning without quantum memory.** *Scientific Reports* **2**, 708 (2012). [Journal article and DOI](https://doi.org/10.1038/srep00708). The extended preprint is titled **Robust optimal quantum learning without quantum memory**, [arXiv:1208.0663v2](https://arxiv.org/abs/1208.0663v2), 8 October 2012.

For two unknown pure qubit classes with labeled training data, a suitable joint training measurement produces a reusable classical record. It attains optimal classification in the balanced pure-state setting, with further asymptotic robustness results for noise and training composition. The result is important evidence that quantum retention is task dependent. Its fixed two-class qubit experiment does not settle high-dimensional, repeatedly refreshed signal-versus-background prediction.

<a id="noisy2026"></a>

### Cotler, Gong, and Kannan: noisy access to quantum data

Jordan Cotler, Weiyuan Gong, and Ishaan Kannan. **Noisy quantum learning theory.** *Nature Communications* (2026), published 29 May 2026. [Journal article and DOI](https://doi.org/10.1038/s41467-026-73693-x) · [Journal PDF](https://www.nature.com/articles/s41467-026-73693-x.pdf) · [arXiv:2512.10929v2](https://arxiv.org/abs/2512.10929v2), 14 January 2026 · [Preprint full text](https://arxiv.org/html/2512.10929v2).

The paper studies noisy interfaces to quantum data, including purity testing and shadow tomography. Its local-depolarization obstruction shows that ideal coherent-access separations cannot automatically be advertised as tolerating constant local noise. The noise location and access assumptions matter: the repository's exact global retained-memory model and complete-instrument error bound are separate statements, not consequences of this paper.

<a id="ng2026"></a>

### Ng et al.: online sequence classification with bounded memory

Keith K. Ng, Haochen Jay Li, Mile Gu, and Jayne Thompson. **Single-shot online sequence classification with unbounded quantum memory advantage.** arXiv:2608.23669v1, 24 August 2026. [Primary record](https://arxiv.org/abs/2608.23669v1) · [Full text](https://arxiv.org/html/2608.23669v1).

The input is a classical symbol stream and the learner classifies a word at its delimiter. Quantum machines of bounded dimension can outperform classical machines with insufficiently many internal states. The memory-size comparison and classical inputs differ from the present unlimited-classical-storage, quantum-specimen experiment. This is another reason to state the specific statistical model whenever discussing an online quantum advantage.
