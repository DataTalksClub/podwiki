---
layout: wiki
title: "NLP"
summary: "Natural language processing across language data, annotation, LLMs, speech, search, and production systems."
related:
  - LLMs
  - Embeddings
  - Retrieval-Augmented Generation
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Annotation Quality Workflows
  - Privacy Engineering for ML
  - Responsible AI and Governance
  - Security
---

Natural language processing (NLP) is the part of machine learning that works
with language data. That includes text, speech, documents, and dialogue. It
also includes translation. NLP turns language into useful software, not only
trained models.

NLP work connects data collection, annotation and linguistics to deployment,
evaluation, user safety and product constraints.

Label definitions and annotation guides define the dataset before training
starts. For more detail, see [[Annotation Quality Workflows]].[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Prompt injection, hallucinations, and output validation set the production
boundary. Those controls connect NLP to [[security]],
[[Privacy Engineering for ML]], and
[[Responsible AI and Governance]].[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Older NLP work connects to modern [[LLMs]], [[embeddings]], and
[[retrieval-augmented-generation=>RAG]]. NLP teams are production teams, not
only research groups.[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]
The same production frame appears in [[LLM production patterns]] and chatbot
safety. It also appears in search and speech recognition.

## Language Systems

NLP systems turn language data into useful software. Teams use them for text
classification, information extraction, document analysis, and search. Teams
also use them for translation, chatbots, speech recognition, and LLM-powered
assistants.

NLP engineers need tokenization, linguistic judgment, task framing, and model
deployment skills. NLP engineering differs from general
[[machine-learning-engineer-role=>ML engineering]]
through inference optimization, deployment, and [[MLOps]]. NLP engineers also
work across annotation, task engineering, testing, and production.[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]

Data-side NLP starts from dataset creation. Automated, manual, and hybrid
labeling all depend on annotation guides and model-assisted review. An
NLP project starts before model training because the team must define what the
labels mean.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

The Hugging Face ecosystem organizes NLP through tasks, models, and datasets.
It also organizes demos. NLP learning runs through spaCy and Keras examples.
Application demo tools include Streamlit, Gradio, and Hugging Face Spaces. For
career and portfolio work, NLP becomes a set of reproducible projects that other
people can run.[[cite:hugging-face-contributions-and-nlp-portfolio=>Contribute to Hugging Face and Build an NLP Portfolio]]

[[book:20211213-mastering-spacy=>Mastering spaCy]]
by Duygu Altinok is a practical reference for the spaCy NLP library, a
recommended learning entry point.

## Role Boundaries

NLP works on language data, but different practitioners stress different failure
modes.

Teams draw one boundary around production ownership. A centralized NLP team can
work alongside cross-disciplinary product teams. A specialist hire makes sense when
task complexity, data needs, and feature engineering require deeper language
expertise.[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]

For label quality, inter-annotator agreement, throughput, and fatigue act as
quality signals. Active learning, distant supervision, and
weak supervision reduce labeling cost. Teams can still waste model effort if
they skip label definitions, expert review, and annotation tooling.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Messy text data pushes teams toward tooling. Text metadata, messy labels,
ChatGPT-based labeling heuristics, and active learning all matter. So do crowd
labels, [[embeddings]], and data management. Together they become part of weak
supervision and developer control.[[cite:building-open-source-nlp-tool=>Build Open-Source NLP Tools]]

Trust and safety changes the failure mode again. Prompt injection and data
exfiltration keep older NLP controls relevant, as do hallucinations, output
validation, and query analysis. Non-LLM classifiers can still be useful because
a generative interface can fail in ways that a narrower classifier may avoid.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## Datasets and Annotation

Teams start NLP data work by defining the task, and stakeholder alignment tells
them which language decisions matter. The annotation guidebook documents
ambiguous cases, and expert-knowledge capture turns domain understanding into
annotator instructions.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Before automation, human performance and prototypes test whether the task is
feasible and valuable. Annotation UX, hotkeys, agreement metrics, and annotator
fatigue become part of the data system. A model trained
on poorly defined labels inherits those problems.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Weak supervision appears in dataset work and tooling through distant
supervision, labeling functions and programmatic heuristics.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Tools such as Refinery and Bricks help teams combine heuristics instead of
hand-labeling every example.[[cite:building-open-source-nlp-tool=>Build Open-Source NLP Tools]]

NLP portfolio work often starts from [[open source]]
datasets and demos, including dataset scripts, CI learning, and contributor
onboarding. A dataset contribution can show practical
skill more clearly than a notebook that no one can reproduce.[[cite:hugging-face-contributions-and-nlp-portfolio=>Contribute to Hugging Face and Build an NLP Portfolio]]

## Transformers and LLMs

The transformer architecture behind modern NLP is covered in depth by
[[book:20220425-natural-language-processing-with-transformers=>Natural Language Processing with Transformers]]
by Leandro von Werra, Lewis Tunstall, and Thomas Wolf. The book uses the
Hugging Face library that recurring NLP episodes rely on.

LLMs change the interface to NLP but continue language-system work rather than
replace it. GPT-3 and prompting can simplify some NLP applications. Cost,
control, bias, and privacy remain part of the decision. So do MVP strategy and
open-source alternatives.[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]

A production view distinguishes generative and non-generative models and
compares open-source models with API models. Control, privacy, fine-tuning, and
hidden API model drift drive the choice. This belongs with
[[LLMs]] and
[[LLM Production Patterns]]
because it treats NLP systems as deployed software with latency, cost, and
versioning constraints.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Teams use retrieval to keep language systems grounded in changing knowledge.
Retrieval contrasts with retraining, and vector databases work through
embeddings, indexing, and semantic search. This belongs next to
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

[[book:20210419-transformers-for-natural-language-processing=>Transformers for Natural Language Processing]]
by Denis Rothman covers attention mechanisms, fine-tuning, and downstream NLP
tasks. [[book:20210726-applied-natural-language-processing-in-the-enterprise=>Applied Natural Language Processing in the Enterprise]]
by Ankur A. Patel and Ajay Uppili Arasanipalai covers practical NLP pipelines
from data labeling through production deployment.
[[book:20211018-blueprints-for-text-analytics-using-python=>Blueprints for Text Analytics Using Python]]
by Jens Albrecht, Sidharth Ramachandran, and Christian Winkler provides reusable
blueprint patterns for text-mining workflows.

The builder's version focuses on chunking, embeddings, and context quality
inside RAG systems.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Long-context models add an evaluation tradeoff when performance drops around
large context windows. Chunking, retrieval and summarization remain design
choices, so NLP evaluation belongs with
[[LLM Evaluation Workflows]]. Teams need task-specific evidence, not only larger
context windows.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research and Career Growth]]

## Speech and Text Use Cases

The NLP examples in these episodes include more than text classification. They
cover chatbot UX, conversational design, parsing, and information extraction.
They also cover multilingual needs.[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]
NLP data work can start from sales-call transcription and CRM integration.
Spoken language becomes structured business data after transcription, labeling,
and integration work.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Machine translation shows how modern NLP often works as a controlled assistant,
not a replacement for language expertise. Maria Sukhareva describes technical
translation as a place where terminology, company standards, and safety-sensitive
wording still require human review. ChatGPT prompts can control choices such as
formal or informal address. The workflow still needs a translator to check
accuracy and consistency.[[cite:generative-ai-chatbots-in-production-security@29:53=>AI-Augmented Translation]]
[[cite:generative-ai-chatbots-in-production-security@32:28=>Controlled MT Prompts]]

Automatic speech recognition extends NLP into phonetics, morpho-syntax, accents
and speech disorders. Standard speech datasets and deployment settings can fail
for atypical speech. Transfer learning and limited data address those gaps.
Transcription, LLM post-correction, and contextual language models help too.[[cite:human-centered-ai-automatic-speech-recognition=>Human-Centered Speech Recognition]]

NLP expertise also becomes client work, through a model-in-the-loop annotation
study, annotation outcomes, and evaluation. Generative AI can fit an NLP-focused
consulting practice. That places NLP inside
[[freelance]] and practical AI adoption,
not only research.[[cite:practical-generative-ai-consulting-from-expertise-to-impact=>Launching a Freelance Generative AI Business]]

## Low-Resource and Multilingual NLP

Low-resource NLP appears when the team lacks enough representative language data.
The gap can involve a group of speakers. It can also involve dialects, writing
systems, or speech patterns the system must serve. In the speech-recognition
discussion, Katarzyna Foremniak treats this as
more than a generic accuracy question. ASR models trained on standard speech can
fail on atypical speech and speech disorders. They can also miss accents and
language varieties outside the training distribution.[[cite:human-centered-ai-automatic-speech-recognition=>Human-Centered Speech Recognition]]

Teams have to start with people and data before model choice. Teams can use
specialized datasets for disordered speech. Broad collection remains difficult
because clinical data has GDPR constraints and language variety matters.

Data augmentation and transfer learning help teams work with limited examples.
Multimodal cues such as lip reading and personalized fine-tuning help too.
Teams still need careful labeling and review. This puts the work next to
[[Annotation Quality Workflows]]. It also links the work to
[[Privacy Engineering for ML]] and
[[Responsible AI and Governance]].[[cite:human-centered-ai-automatic-speech-recognition=>Human-Centered Speech Recognition]]

Maria Sukhareva describes the text side through low-resource and historical
languages. English is a high-resource language. A team can't assume an LLM or
translation system will behave the same way for languages with fewer digital
resources. Her examples include Gothic, Middle Low German, Sumerian, and other
historical languages.

Historical corpora create another data-quality problem because spelling,
punctuation, and orthography may not be standardized. Some scripts mix phonetic,
grammatical, and semantic signals.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Multilingual models reduce older machine-translation patterns that pivot through
English. They can also generalize across language pairs. They don't remove the
need to look at the data, writing system, and user context.

NLP teams should test the language varieties the product will serve. They should
use human review where language quality affects safety or trust. They should
also include low-resource cases in [[LLM Evaluation Workflows]].

In production chatbots, those same language gaps sit beside prompt injection and
data exfiltration. Output validation and [[security]] controls still apply.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

## Production and Evaluation

Production NLP needs more than a model endpoint because NLP engineering includes
inference optimization, deployment, and MLOps. Testing and production are part
of the NLP pipeline. That keeps NLP connected to [[production]] and
[[software engineering]].[[cite:nlp-team-hiring-and-production-mlops=>Lead NLP Teams]]

Evaluation changes with the task. Inter-annotator agreement and human baselines
gauge dataset quality.[[cite:nlp-dataset-creation-annotation-tools-workflows=>NLP Dataset Creation]]

Production models use gold-standard examples and output-driven
evaluation.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

RAG systems use evaluation sets, failure analysis, logs, and traces.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Teams add query analysis, output validation, layered defenses, and human review
for security and reliability. Non-LLM classifiers can be robust alternatives for
some decisions.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]

Production teams should choose the narrowest language system that can do the job
safely. They should evaluate it against the failure modes the product will
face.[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]]
