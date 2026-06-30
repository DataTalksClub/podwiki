---
layout: wiki
title: "Deep Learning"
summary: "Archive-backed guide to deep learning as the neural-network layer of applied AI, covering vision, transformers, labels, production constraints, and portfolio signals."
related:
  - Machine Learning
  - Computer Vision
  - AI
  - Generative AI
  - MLOps
  - Production
  - AI Engineering
  - Machine Learning Portfolio Projects
  - Evaluation
---

Deep learning is the part of
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) that uses
neural networks to learn representations from data. In the DataTalks.Club
archive, guests use it most often for
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}) and large
language models. They also use it for medical imaging, remote sensing, and
autonomous-driving perception. The topic sits inside
[AI]({{ '/wiki/ai/' | relative_url }}), but the archive treats it as engineering
work rather than a magic model choice.

Guests make a pragmatic case for deep learning when simpler approaches struggle
with images, text, audio, or sensor streams. It also helps with other
high-dimensional unstructured data. Deep learning adds cost too. Teams need
enough labels and a reliable evaluation plan. They also need deployable
inference and a reason the neural model beats a simpler baseline.

## Start With These Discussions

These episodes anchor the topic:

- [Switch to Computer Vision and Deep Learning]({{ '/podcasts/from-physics-to-computer-vision-career-transition/' | relative_url }}) with [Tatiana Gabruseva]({{ '/people/tatianagabruseva/' | relative_url }}) for a career roadmap, Kaggle work, pet projects, labeling, deployment, and Docker.
- [Applying Computer Vision Research to Building Production-Ready AI Systems]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}) with [Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }}) for autonomous-driving perception, sensor tradeoffs, edge inference, validation stages, and release safety.
- [From Biology to ML]({{ '/podcasts/from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers/' | relative_url }}) with [Isabella Bicalho]({{ '/people/isabellabicalho/' | relative_url }}) for open-source computer vision, transformer projects, green-space segmentation, and portfolio building.
- [Data-Centric AI]({{ '/podcasts/data-centric-ai/' | relative_url }}) with [Marysia Winkels]({{ '/people/marysiawinkels/' | relative_url }}) for label quality, data edits, transfer learning, dataset gaps, and production feedback.
- [Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}) for the warning that SQL, statistics, or a simpler ML model may beat a hard-to-maintain deep learning system.
- [From Software Engineering to Machine Learning]({{ '/podcasts/from-software-engineer-to-machine-learning/' | relative_url }}) with [Santiago Valdarrama]({{ '/people/svpino/' | relative_url }}) for the software-engineer path into ML, project-first learning, deployment basics, and MLOps fundamentals.
- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}) with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) for transformers, generative versus non-generative tasks, fine-tuning, retrieval, model compression, latency, cost, and evaluation.
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}) with [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) for large neural networks in production and the wider AI engineering skill stack.
- [Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }}) with [Dan Becker]({{ '/people/danbecker/' | relative_url }}) for the boundary between model predictions and the decision systems that consume them.

## Archive Definition

Across the archive, deep learning means using neural networks when a model must
learn useful features rather than rely only on hand-built columns. Tatiana's
career-transition episode ties deep learning to computer vision work. She
covers Python, ML and DL courses, Kaggle practice, and end-to-end pet projects.
Those projects include data collection, labeling, deployment, and Docker
([Switch to Computer Vision and Deep Learning]({{ '/podcasts/from-physics-to-computer-vision-career-transition/' | relative_url }})).

Aishwarya makes the same definition concrete in autonomous driving. Her
discussion covers camera and LiDAR tradeoffs, traffic-control gesture
recognition, on-vehicle inference, and quantization. She also covers sensor
data management, human annotation, and automated labeling. Simulation,
closed-track testing, and staged releases come later in the same discussion
([Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})).
In that setting, the neural network is one part of a perception system that has
to run fast, handle edge cases, and pass safety checks.

Meryem extends the definition to large language models. She separates
generative and non-generative models, then connects transformer-based LLMs to
classification and generation. She also covers fine-tuning, retrieval,
open-source deployment, and API tradeoffs
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).
For current [generative AI]({{ '/wiki/generative-ai/' | relative_url }}), deep
learning is often the model layer inside the product. Retrieval, evaluation,
and serving decide whether that product works.

## Neural Network Use Cases

Deep learning matters most in the archive when the input is hard to summarize
by hand. Vision examples include guide-dog navigation, autonomous-driving
perception, and traffic gestures. Other examples include malaria mapping from
satellite data and green-space segmentation. Aishwarya's episode emphasizes the system side of
these use cases. The team has to validate perception changes in simulation, on
closed tracks, and on roads before release
([Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})).

Isabella's episode shows a smaller project version, tracing a path from
statistics into transformers. She then discusses Hugging Face community work,
computer vision contributions, and a green-space segmentation project that
compares CNNs with transformers
([From Biology to ML]({{ '/podcasts/from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers/' | relative_url }})).
The useful signal for a portfolio isn't only that a transformer appears in the
notebook. The project has to explain the data, the task, the comparison, and
the practical reason for using that model family.

LLM work follows the same rule. Meryem frames LLMs as useful for
unstructured text at scale, but she doesn't treat generation as the answer to
every problem. She distinguishes classification from generation, then explains
when teams choose fine-tuning and retrieval. She also compares API models with
open-source serving
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).
That makes deep learning adjacent to [AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}),
where the model is only one part of the shipped product.

## Simpler Baselines Still Matter

The archive doesn't treat deep learning as the default answer. In
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
Ben Wilson argues for maintainable solutions. He explicitly places SQL or
statistical approaches before deep learning when they solve the business
problem. Neural networks can add cloud cost, reproducibility issues, dependency
problems, and systems that are hard for the next engineer to operate.

Dan Becker's decision-optimization discussion gives a second boundary: a model
prediction isn't the same as a decision. In supply-chain and pricing examples,
teams still need objectives, constraints, and uncertainty handling. They also
need real-world impact metrics, monitoring, and organizational adoption
([Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }})).
A deep learning model may produce a better forecast, but the business result
depends on the decision system around it.

This is why the deep learning page should be read with
[model evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[machine learning portfolio projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).
The model choice belongs in a comparison. A strong project explains the
baseline, the metric, the error cases, and the operating constraint that makes
the neural model worth its added complexity.

## Data Quality and Labels

Deep learning work in the archive repeatedly returns to data quality. Marysia's
data-centric AI episode shifts attention from big data to good data. She
discusses transfer learning, fine-tuning, and a fixed-ResNet data-centric
competition. She also covers targeted relabeling with model confidence and
image embeddings. Dataset completeness, bias, acceptance criteria, and
production feedback belong in the same data-quality discussion
([Data-Centric AI]({{ '/podcasts/data-centric-ai/' | relative_url }})).

A neural network can expose label problems instead of fixing them. Marysia
starts with a baseline model and error analysis, then brings in subject-matter
experts and targeted data edits. She also covers low-tech labeling with
spreadsheets and automation scripts. Many teams improve a deep learning system
through better labels before they change the architecture.

Aishwarya's autonomous-driving discussion makes label quality operational
through sensor data management and privacy. She also covers human annotation
and automated labeling at scale
([Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})).
Those topics connect deep learning to [MLOps]({{ '/wiki/mlops/' | relative_url }}).
Teams maintain training data and labels as system assets. Validation sets and
release gates become maintained assets too, not one-time notebook inputs.

## Production Constraints

Production deep learning is constrained by inference speed, hardware, and cost.
Privacy, release safety, and maintainability constrain it too. Aishwarya covers
on-vehicle inference, model compression, and quantization. She also discusses
simulation and staged deployment.

She also covers geographic edge cases for autonomous driving
([Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})).
That discussion shows why production vision work isn't finished when the
offline score improves.

Meryem covers the LLM version of the same constraint. She discusses open-source
models versus API models and hidden API model changes. Model size, compression,
and inference optimization matter in the same deployment discussion.

She also covers fine-tuning data formats, retrieval for changing knowledge, and
vector databases. Latency and cost complete the production picture. So do
gold-standard examples and human evaluation
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).

That places transformer systems close to
[production]({{ '/wiki/production/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and the practical
[MLOps article]({{ '/articles/mlops/' | relative_url }}).

Paul's AI engineering discussion connects deep learning to the current product
stack. His background includes large neural networks in production. The
episode moves from autonomous-driving deep learning to full-stack AI products,
RAG, and knowledge management. It also covers technical pillars for shipping
and portfolio work
([Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }})).
For modern teams, deep learning skill is valuable when it's paired with
software delivery, evaluation, and product ownership.

## Career and Project Signals

The archive's career episodes treat deep learning as something to demonstrate
through projects, not only credentials. Tatiana recommends end-to-end computer
vision pet projects with data collection, labeling, deployment, and Docker.
She also discusses Kaggle, internships, mentors, and interview preparation. Her
learning roadmap includes Python, ML and DL courses, and SQL. It also includes
algorithms and system design
([Switch to Computer Vision and Deep Learning]({{ '/podcasts/from-physics-to-computer-vision-career-transition/' | relative_url }})).

Santiago gives the software-engineer version. He tells engineers to start
projects instead of overpreparing, communicate ML simply, analyze the problem
before coding, and learn deployment basics. Those basics include APIs, Docker,
and cloud providers. They also include data pipelines, monitoring, and MLOps
([From Software Engineering to Machine Learning]({{ '/podcasts/from-software-engineer-to-machine-learning/' | relative_url }})).
That path matters for deep learning because many useful neural-network
projects fail on engineering habits rather than model math.

Isabella's portfolio examples add open source and community work. Her episode
covers Hugging Face course contributions, computer vision review work, and
open-source project types. She also discusses green-space segmentation. Project
work becomes job-ready experience in the same discussion
([From Biology to ML]({{ '/podcasts/from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers/' | relative_url }})).

Together, these episodes set a high bar. A deep learning portfolio should show
problem framing, data work, and a baseline. It should also show evaluation and
some awareness of how the model would run after the notebook.

## Nearby Topics

Use [machine learning]({{ '/wiki/machine-learning/' | relative_url }}) for the
broader modeling discipline and
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}) for the
archive's strongest image and sensor examples. Use
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}) and
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) for transformer
applications, RAG, agents, and product work. Use
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[production]({{ '/wiki/production/' | relative_url }}), and
[model evaluation]({{ '/wiki/evaluation/' | relative_url }}) when the question
is whether a deep learning system is reliable enough to ship.
