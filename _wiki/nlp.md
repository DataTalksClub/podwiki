---
layout: wiki
title: "NLP"
summary: "How DataTalks.Club guests discuss natural language processing across language data, annotation, LLMs, speech, search, and production systems."
related:
  - LLMs
  - Embeddings
  - Search, RAG, and Knowledge Systems
  - LLM Production Patterns
  - LLM Evaluation Workflows
---

Natural language processing (NLP) is the part of machine learning that works
with language data. In the DataTalks.Club podcast, that language data includes
text and speech as well as documents, dialogue, and translation. Guests treat
NLP as the work of turning language into useful software, not only training a
model.

Guests repeatedly put NLP next to data collection and annotation. They also tie
it to linguistics, deployment, and evaluation. User safety and product
constraints matter too. In
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }}),
[Christiaan Swart]({{ '/people/christiannswart/' | relative_url }}) starts
from label definitions and annotation guides. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) starts from
prompt injection, hallucinations, and output validation.

Podcast discussions tie older NLP work to modern
[LLMs]({{ '/wiki/llms/' | relative_url }}),
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[RAG]({{ '/wiki/rag/' | relative_url }}). In
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}),
[Ivan Bilan]({{ '/people/ivanbilan/' | relative_url }}) describes NLP teams
as production teams at 14:07-16:45, not only research groups. Later episodes
use the same production frame for
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
search, speech recognition, and chatbot safety.

## Language Systems and Roles

Across the interviews, NLP means turning language data into useful software.
Some episodes cover text classification, information extraction, and document
analysis. Others cover search, translation, and chatbots. Speech recognition
and LLM-powered assistants also appear across these episodes.

Ivan's definition in
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }})
is role-oriented. At 16:45 he says NLP engineers need skills such as
tokenization and linguistic judgment. They also need task framing and model
deployment. At
24:36 he separates NLP engineering from general
[ML engineering]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
through inference optimization, deployment, and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). At 34:57 he turns the definition
into a chain of annotation, task engineering, testing, and production work.

[Christiaan Swart]({{ '/people/christiannswart/' | relative_url }}) gives the
data-side definition in
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }}).
At 6:51 he compares automated, manual, and hybrid dataset creation. At 18:36
and 20:57 he makes annotation guides and model-assisted labeling part of the
system. In that view, an NLP project starts before model training because the
team has to define what the labels mean.

[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) gives the ecosystem
definition in
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).
At 12:46 she explains the Hugging Face Hub through tasks, models, datasets,
and demos. At 38:02 and 51:12 she links NLP learning to spaCy and Keras
examples. She also links it to Streamlit, Gradio, and Hugging Face Spaces. For
career and portfolio work, NLP is a set of reproducible projects that other
people can run.

[Mastering spaCy]({{ '/books/20211213-mastering-spacy/' | relative_url }})
by Duygu Altinok is a practical reference for the spaCy NLP library that Merve
recommends as a learning entry point.

## Role Boundaries and Failure Modes

Guests agree that NLP works on language data, but they stress different
failure modes.

Ivan focuses on team structure and production ownership. In
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}),
the 14:07 section compares centralized NLP teams with cross-disciplinary
product teams. At 30:11 he argues that teams need NLP specialists when task
complexity, data needs, and feature engineering justify the hire. His view
centers the role boundary between general ML skill and specialized language
expertise.

Christiaan focuses on label quality and annotation economics. In
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }}),
the 37:42 section uses inter-annotator agreement, throughput, and fatigue as
quality signals. At 42:51-48:24 he adds active learning, distant supervision,
and weak supervision. His view centers the dataset: teams can waste model
effort if they skip label definitions and expert review. They also need
annotation tooling.

[Johannes Hötter]({{ '/people/johanneshotter/' | relative_url }}) focuses on
tooling for messy text data. In
[Build Open-Source NLP Tools]({{ '/podcasts/building-open-source-nlp-tool/' | relative_url }}),
the 10:14 section discusses text metadata and messy labels. At 13:22-17:34 he
combines ChatGPT as a labeling heuristic with active learning and crowd labels.
He also brings in Hugging Face, [embeddings]({{ '/wiki/embeddings/' | relative_url }}),
and data management. His view
centers the workflow around weak supervision and developer control.

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) focuses on
trust and safety. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
the 9:28-18:01 sections cover prompt injection, data exfiltration, and
hallucinations. They also cover output validation, query analysis, and non-LLM
classifiers.
Her view keeps older NLP controls relevant because a generative interface can
fail in ways that a narrower classifier may avoid.

## Datasets and Annotation

In
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }}),
Christiaan makes task definition the start of NLP data work. At 9:02, he
starts with stakeholder alignment so the team knows which language decisions
matter. At 18:36, the annotation
guidebook becomes living documentation for ambiguous cases. At 24:01, expert
knowledge capture turns domain understanding into instructions annotators can
use.

Human baselines matter before automation. At 29:28 in the same episode,
Christiaan uses human performance and prototypes to test whether the task is
feasible and valuable. At 35:02-37:42, annotation UX and hotkeys become part
of the data system. Agreement metrics and annotator fatigue matter too. A
model trained on poorly defined labels inherits those problems.

Both Christiaan and Johannes discuss weak supervision. Christiaan covers
distant supervision and Snorkel-style labeling functions at 44:57-48:24 in
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }}).
He also covers programmatic heuristics. Johannes shows the tooling version in
[Build Open-Source NLP Tools]({{ '/podcasts/building-open-source-nlp-tool/' | relative_url }}),
at 6:33 and 18:33. Refinery and Bricks help teams combine heuristics rather
than hand-label every example.

NLP portfolio work often starts from [open source]({{ '/wiki/open-source/' | relative_url }})
datasets and demos. In
[Contribute to Hugging Face and Build an NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}),
Merve describes dataset scripts, CI learning, and contributor onboarding at
8:13-10:31. For people learning NLP, a dataset contribution can show practical
skill more clearly than a notebook that no one can reproduce.

## Transformers and LLMs

The transformer architecture behind this shift is covered in depth by
[Natural Language Processing with Transformers]({{ '/books/20220425-natural-language-processing-with-transformers/' | relative_url }})
by Leandro von Werra, Lewis Tunstall, and Thomas Wolf, built around the
Hugging Face library that recurring NLP episodes rely on.

LLMs change the interface to NLP. DataTalks.Club guests still treat them as a
continuation of language-system work rather than a replacement for it. Ivan's
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }})
episode already makes this transition visible. At 38:55, he discusses GPT-3
and prompting as ways to simplify some NLP applications.

At 43:05-46:10, Ivan describes cost and control tradeoffs before moving to
bias and privacy. He also discusses MVP strategy and open-source alternatives.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives a later
production view in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 10:24 she distinguishes generative and non-generative models and introduces
transformers. At 13:45-18:46 she compares open-source models with API models.
She also covers control, privacy, fine-tuning, and hidden API model drift. Her
discussion belongs with [LLMs]({{ '/wiki/llms/' | relative_url }}) and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
because it treats NLP systems as deployed software with latency, cost, and
versioning constraints.

Retrieval keeps language systems grounded in changing knowledge. Meryem
contrasts retrieval with retraining at 40:46-42:02 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 48:01 she explains vector databases through embeddings, indexing, and
semantic search. Her retrieval discussion belongs next to
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
adds the builder's version in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 44:26-48:20 he focuses on chunking, embeddings, and context quality.

Long-context models add another tradeoff. In
[Applied LLM Research and Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}),
[Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }}) discusses
long-context evaluation at 10:15-15:28. She covers performance drop around
large context windows. She also discusses chunking, retrieval, summarization,
and industry publishing. That puts NLP evaluation into the same family as
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}):
teams need task-specific evidence, not only larger context windows.

## Speech and Text Use Cases

The NLP examples in these episodes include more than text classification. Ivan
covers chatbot UX and conversational designers at 26:19 in
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}).
At 28:38 he discusses parsing, information extraction, and multilingual needs.
Christiaan's dataset episode starts from sales-call transcription and CRM
integration at 5:12. Spoken language becomes structured business data only
after transcription, labeling, and integration work.

[Katarzyna Foremniak]({{ '/people/katarzynaforemniak/' | relative_url }})
extends NLP into speech in
[Human-Centered Speech Recognition]({{ '/podcasts/human-centered-ai-automatic-speech-recognition/' | relative_url }}).
At 15:25-23:19 she explains why phonetics, morpho-syntax, accents, and speech
disorders matter for automatic speech recognition. At 27:31-30:53 she explains
why standard speech datasets and deployment settings can fail for atypical
speech. At 40:17-47:28 she discusses transfer learning and limited data. She
also covers transcription, LLM post-correction, and contextual language models.

Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode adds translation and multilingual work. At 29:53-32:28 she discusses
AI-augmented translation and controlled machine translation with ChatGPT. At
53:01-56:52 she connects multilingual models to low-resource languages,
orthography, historical corpora, and data quality. Those examples show why
language coverage and writing systems still matter after LLM adoption.

[Verena Weber]({{ '/people/verenaweber/' | relative_url }}) shows how NLP
expertise becomes client work in
[Launching a Freelance Generative AI Business]({{ '/podcasts/practical-generative-ai-consulting-from-expertise-to-impact/' | relative_url }}).
At 23:11-27:47 she discusses a model-in-the-loop annotation study, annotation
outcomes, and evaluation. At 47:51 she explains why generative AI appealed to
her as an NLP-focused consultant. Her episode places NLP inside
[freelance]({{ '/wiki/freelance/' | relative_url }}) and practical AI adoption,
not only research.

## Production and Evaluation

Production NLP needs more than a model endpoint. Ivan links NLP engineering to
inference optimization, deployment, and MLOps at 24:36 in
[Lead NLP Teams]({{ '/podcasts/nlp-team-hiring-and-production-mlops/' | relative_url }}).
At 34:57 he includes testing and production in the NLP pipeline. That keeps
NLP connected to [production]({{ '/wiki/production/' | relative_url }}) and
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}).

Evaluation changes with the task. Christiaan's
[NLP Dataset Creation]({{ '/podcasts/nlp-dataset-creation-annotation-tools-workflows/' | relative_url }})
episode uses inter-annotator agreement and human baselines for dataset quality.
Meryem uses gold-standard examples and output-driven evaluation at 53:34-56:39
in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
Hugo uses evaluation sets, failure analysis, logs, and traces at 23:00-27:38
in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

Security and reliability add another layer. Maria's
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
episode shows why teams need query analysis, output validation, layered
defenses, and human review. At 17:00 she also presents non-LLM classifiers as
robust alternatives for some decisions.

Maria gives a direct NLP production lesson.
Choose the narrowest language system that can do the job safely. Then evaluate
it against the failure modes the product will face.
