---
layout: wiki
title: "Synthetic Data"
summary: "How DataTalks.Club episodes frame synthetic data for medical imaging, speech augmentation, industrial tabular data, privacy, and validation limits."
related:
  - Machine Learning
  - Generative AI
  - Deep Learning
  - Evaluation
  - Privacy Engineering for ML
  - Data Governance
  - Data Quality and Observability
  - Healthcare ML Validation and Adoption
  - LLMOps
  - AI-Powered Business Intelligence
  - Industrial ML Applications
---

Synthetic data is generated data. Teams use it when real examples are scarce or
sensitive. They also use it when they need controlled variants for training,
testing, or safe sharing. In medical discussions, the examples are simulated
images and augmented speech. In data-sharing discussions, the examples are
synthetic industrial tables and masked urban datasets.
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]
[[cite:urban-data-science=>Urban Data]]

Synthetic data sits between [[Machine Learning]], [[Generative AI]],
[[Deep Learning]], and [[Evaluation]]. It also belongs close to
[[Privacy Engineering for ML]], [[Data Governance]], and
[[Data Quality and Observability]]. Generation changes a dataset, but it
doesn't remove the need to preserve the signal, protect sensitive records, and
prove value on a real decision.

## Generated Examples as a Data Intervention

In these episodes, teams use synthetic data as a data intervention. They
generate or alter examples to cover missing variation, protect records, or make
experimentation possible. Marysia Winkels' data-centric AI discussion places
synthetic data beside labeling, profiling, and data versioning. It also places
generation beside error analysis and subject-matter review. The model result
points back to the data changes that can improve the task.
[[cite:data-centric-ai=>Data-Centric AI]]

The episodes separate the goals by domain. Disordered-speech ASR and medical
imaging show how synthetic examples can fill a known training gap.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]
Industrial modeling uses synthetic tabular data in a small-data setting.
Experiments are expensive, and domain measurements are hard to replace.
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]
For publishing and collaboration, synthetic or masked data can reduce exposure
while keeping the useful structure of a transport dataset.
[[cite:urban-data-science=>Urban Data]]

## Fit Conditions and Domain Limits

The guests don't disagree that synthetic data can help, but they draw the
boundary in different places. Orell Garten's medical-imaging story starts from a
technology capability: simulate imaging physics to produce AI training data.
His lesson is that a technically strong generator still needs a customer problem
and a clinical workflow that create demand.
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]

Katarzyna Foremniak's ASR discussion starts from people and linguistic
variation. Synthetic speech is useful when it targets known articulation,
fluency, or consonant-cluster gaps. It can also target accent and language
coverage. It isn't a substitute for real speakers or personalized evaluation.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]

Rosona Eldred's industrial-data discussion puts the emphasis on production
constraints. Synthetic tabular rows must respect ingredients, recipes, sensors,
and material properties. They also have to preserve quality tests and hidden
production knowledge. More rows alone don't solve the small-data problem if the
generated rows violate the physical process.
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]

Rachel Lim's urban-data discussion uses synthetic data more cautiously, as a
possible [[Generative AI]] application for complex or sensitive datasets. The
goal there isn't only better model accuracy. It's also privacy-preserving
publication and analysis without exposing fare-card identifiers or other
confidential information.
[[cite:urban-data-science=>Urban Data]]

## Simulated Medical Imaging

In simulated medical imaging, teams generate synthetic data from a model of the
imaging process. Orell Garten described a startup that simulated MRI and X-ray
machine physics. The team used those simulations to create training data for AI
systems that analyze medical images.
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]
This belongs near [[Simulation and Digital Twins]] because the generator isn't a
random image model. It's tied to physics, high-performance computing, and data
infrastructure for moving simulation inputs and outputs.

The adoption boundary matters because synthetic medical images can make model
development possible when real labeled examples are scarce. They don't by
themselves prove clinical value. Orell's go-to-market lesson was that the
startup began with technology before confirming that hospitals or medical
companies treated the need as urgent. That keeps synthetic imaging connected to
[[Healthcare ML Validation and Adoption]], not only [[Computer Vision]] or
[[Deep Learning]].
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]

## Speech Augmentation

Speech augmentation targets a recognition failure. Katarzyna Foremniak
explained that ASR systems are usually trained on standard speech. They can
struggle with speech disorders, accents, and child speech. They can also
struggle with dialects and idiosyncratic pronunciations. When collection is
difficult, teams can artificially simulate disordered speech or known phonetic
variants.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]

The human-variation boundary matters because synthetic audio can expand a small
specialized dataset around specific sounds or consonant clusters. It remains
part of a larger [[NLP]] and accessibility workflow. Teams still collect
specialized data and use transfer learning. They also consider multimodal
signals such as lip reading and test with the users the system is meant to
serve.

A personalized ASR model may work for one speaker. A universal model across
disorders, languages, accents, and deployment settings remains much harder.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]

## Industrial Tabular Data

Industrial synthetic data is mostly a tabular and process-data problem.
Rosona Eldred separates industrial R&D from production. R&D experiments can be
expensive, slow, destructive, or shaped by long-term quality tests. Production
systems may stream high-volume sensor and quality data from equipment that
wasn't designed for data science.
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]

The process-fidelity boundary matters because a generated table has to preserve
ingredients, recipes, spectra, and material properties. It also has to preserve
application tests, batches, sensor placement, and traceability. If the real
process contains hidden variables or tacit domain knowledge, domain experts must
review the synthetic data. This is why industrial synthetic data belongs near
[[Industrial ML Applications]] and
[[manufacturing-predictive-maintenance-yield-analytics=>Manufacturing Predictive Maintenance and Yield Analytics]], not only generic
[[Machine Learning]].
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]

## Privacy-Preserving Sharing

Synthetic data can reduce exposure when teams share or publish sensitive
records, but it doesn't replace privacy engineering. Rachel Lim framed
generative AI as one way to create synthetic versions of complex or sensitive
datasets. Those versions can mask confidential information while retaining
essential characteristics.
[[cite:urban-data-science=>Urban Data]]

Urban transport shows the privacy problem directly. Fare-card records, journey
definitions, sensor streams, and planning signals can be useful for analysis.
Public data still needs masking before release. Synthetic sharing only works
when the generated data keeps the structure needed for transport planning, demand
analytics, and data-quality checks without exposing the original identifiers.
[[cite:urban-data-science=>Urban Data]]

Speech data adds another privacy boundary because disordered-speech examples can
be clinical and personally identifying. Data collection also runs into GDPR and
language-coverage constraints. Generation must stay inside the same
[[Privacy Engineering for ML]] and [[Data Governance]] decisions. Teams still
decide what they can collect, transform, retain, and publish.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]

## Validation Limits

Synthetic data changes the data, so validation has to check whether that change
helped the real task. In data-centric AI, teams build a baseline, analyze
errors, and look at gaps. They then involve subject-matter experts, edit or
augment the dataset, version the change, and evaluate again.
[[cite:data-centric-ai=>Data-Centric AI]]

Each domain adds a different validation question. In medical imaging, a
generated dataset can make a model trainable. It still doesn't prove product
fit, workflow fit, or clinical value.
[[cite:from-academic-research-to-data-engineering-freelancing=>Medical Imaging]]

In speech recognition, synthetic variations need evaluation against real
speakers and real usage contexts.
[[cite:human-centered-ai-automatic-speech-recognition=>Speech Recognition]]

In industrial tabular work, generated rows need review against physical
constraints, quality measurements, and domain assumptions.
[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data]]

Urban data needs journey flows and fare logic to survive generation and
publication. Sensor reliability and planning questions must survive too.
[[cite:urban-data-science=>Urban Data]]

## Related Pages

These pages cover the adjacent validation, privacy, and production concerns:

- [[Privacy Engineering for ML]] for data minimization, masking, and privacy
  controls around ML systems.
- [[Healthcare ML Validation and Adoption]] for clinical validation, scarce
  labels, and workflow fit.
- [[Industrial ML Applications]] for sensor, production, and physical-process
  constraints.
- [[Simulation and Digital Twins]] for physics-based generation and
  simulation-to-ML workflows.
- [[Deep Learning]] for model families that often need image, speech, or sensor
  data at scale.
- [[LLMOps]] and [[Evaluation]] for feedback loops, synthetic examples, and
  production checks.
