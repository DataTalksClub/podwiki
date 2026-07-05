---
layout: wiki
title: "ML Portfolio Projects"
summary: "Choose ML portfolio projects that show framing, baselines, data work, evaluation, production thinking, and maintainable code."
related:
  - Portfolio Projects
  - Machine Learning
  - Machine Learning System Design
  - MLOps
  - DataOps
  - Production ML Project Checklist
  - Data Science
  - Evaluation
  - Job Search
  - Open Source Portfolio Evidence
  - ML System Design Documents
  - Data Scientist CV and Portfolio
  - Data Scientist Interview Roadmap
---

Use a machine learning portfolio project to prove model judgment. It should
turn a decision problem into a working [[machine learning]] system or analysis.
ML-specific proof should show why ML is needed. Name the first baseline, the
label source, the evaluation method, and where the model runs.

The strongest projects aren't model demos alone because they explain the
decision, data, baseline, and [[evaluation]]. They also show the operating
boundary that makes the work reviewable and reproducible. The CRISP-DM
[[cite:crisp-dm=>CRISP-DM]] and the
[[machine-learning-system-design-interview=>ML system design interview]]
discussion set the review boundary by starting with problem framing and
baselines. They then move to metrics, labels, validation, and operating limits
[[cite:machine-learning-system-design-interview=>ML System Design Interviews]].

Start with the broader
[[Portfolio Projects]] hub when
you're choosing between role-specific project types or shaping the general
reviewable evidence. For applied
[[data science]],
[[machine-learning-engineer-role=>machine learning engineer]],
and [[job search]] use cases, start
here. Architecture interview practice belongs with
[[Machine Learning System Design]].

[[Data Engineering Portfolio Projects]] covers cases where the main artifact is
a data pipeline, platform, or modeled data product. If that pipeline produces
features for a model, keep the pipeline evidence there. ML portfolio evidence
owns the baseline, validation, evaluation, and serving story.

[[MLOps vs DataOps]] covers deployment and monitoring context, while
[[Production ML Project Checklist]] covers a production-aware implementation
pass. [[ML System Design Documents]] covers the architecture narrative behind a
project.
If you use a project to prove machine learning engineering readiness, follow
the [[machine-learning-engineer-roadmap=>ML Engineer Roadmap]] sequence from
baseline to deployment, monitoring, and operations evidence.
For a data scientist, the same project can become transition proof when it
shows the move from analysis and modeling into
[[data-scientist-to-machine-learning-engineer=>machine learning engineering]]
ownership.

## Reviewable ML Project

A good ML portfolio project proves judgment under constraints.

Reviewers should be able to answer five questions:

- Why does ML belong in the problem?
- Which baseline does the model beat?
- How were the data and labels built?
- How was the result evaluated?
- How can another person run or review the work?

CRISP-DM gives the basic lifecycle from business understanding
through deployment [[cite:crisp-dm=>CRISP-DM]]. The classified-listing example
starts with the business problem, uses a rule-based category classifier as a
baseline, and checks whether the baseline is enough. It then asks whether more
model complexity serves the business objective.

[[person:valeriybabushkin=>Valeriy Babushkin]] gives the
interview version by connecting metrics, baselines, and model outputs [[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
He then adds labels, feature access, and loss functions. He also adds
validation, online evaluation, and distribution shift. He covers class
imbalance, monitoring, broken models, and fallbacks.

A reviewer should see a small system design exercise, not a notebook
leaderboard entry.
For project-driven learning,
Machine Learning Bookcamp structures a path through real ML projects rather
than isolated exercises [[book:20201214-ml-bookcamp=>Machine Learning Bookcamp]].

The DataTalks.Club community discussion makes the same point through ML Zoomcamp
and Machine Learning Bookcamp. Projects are meant to be end-to-end. The learning
path includes deployment topics such as Flask, AWS Lambda, Kubernetes, and
Kubeflow
([[cite:datatalksclub-building-scaling-data-community@38:22=>Project-Based ML Learning]]
[[cite:datatalksclub-building-scaling-data-community@39:06=>Deployment Focus]]).
[[book:20220919-kaggle-book=>The Kaggle Book]]
compiles competition-winning approaches that translate into portfolio-grade
work.

Side projects can also prove cadence and product judgment. Pauline Clavelloux
kept a data-science day job while allocating nights, weekends, and available
breaks to indie projects. For an ML portfolio, that kind of routine matters when
the project shows steady shipping, not just a finished notebook. Link the work
back to [[portfolio-projects=>portfolio projects]] and explain what the project
taught about users, data, deployment, or operations
[[cite:data-scientist-and-indie-hacker-bootstrapping-side-projects@8:58=>Indie Hacking Side Projects]].

Recruiting and interview guidance applies the same standard to presentation. In
Land Data Scientist Roles, [[person:lukewhipps=>Luke Whipps]] says projects
should back up the skills claimed on a resume. That's also the
[[data-science-recruiter=>data science recruiter]] screen: visible projects
need to support the candidate's stated tools and role fit. He includes Python,
SQL, TensorFlow, and PyTorch as examples [[cite:get-data-scientist-job=>Land Data Scientist Roles]].

In Ace Data Interviews, [[person:nicksingh=>Nick Singh]] treats project
walkthroughs as a way to test model choice and metrics. He also uses them to
test validation, ownership, and impact [[cite:data-interview-behavioral-and-portfolio-prep-guide=>Ace Data Interviews]].

[[person:arsenykravchenko=>Arseny Kravchenko]] adds the
design-document version in Building Scalable and Reliable Machine Learning
Systems [[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]].
He recommends a lightweight design phase, then uses the solution blueprint to
cover the baseline and metrics. It also covers pipeline components and data
strategy, diagrams, dependencies, and the batch-versus-real-time choice. Use
the same structure in a portfolio README at smaller scale.

A social-impact project can make that full arc especially visible. The
Building a Domestic Risk Assessment Tool project starts with problem framing
and mixed-source data cleaning and linking
[[cite:building-domestic-risk-assessment-tool@10:45=>Mixed Data Sources]]
[[cite:building-domestic-risk-assessment-tool@14:20=>Cleaning and Linking]].
It continues through risk modeling and evaluation
[[cite:building-domestic-risk-assessment-tool@18:00=>Risk Scoring Architecture]]
[[cite:building-domestic-risk-assessment-tool@21:40=>Validation and Bias Assessment]].
Later work covers [[privacy engineering for ML]], legal constraints, and
deployment into frontline decision support
[[cite:building-domestic-risk-assessment-tool@25:15=>Privacy and Ethics]]
[[cite:building-domestic-risk-assessment-tool@32:10=>Frontline Workflow Deployment]].
It also covers monitoring and [[data product adoption]]
[[cite:building-domestic-risk-assessment-tool@39:05=>Stakeholder Training and Adoption]]
[[cite:building-domestic-risk-assessment-tool@42:20=>Monitoring and Alerts]].

As portfolio evidence, the strongest version isn't just a model score. It shows
how the project links data, evaluation, governance, and workflow integration
around a decision that matters.

## Review Signals

The guests mostly agree on the bar for credible work, but they value different
signals. The CRISP-DM framing centers process:
a project is convincing when the path from problem framing through evaluation
and deployment is visible [[cite:crisp-dm=>CRISP-DM]].
[[person:valeriybabushkin=>Valeriy Babushkin]] centers
defensibility in ML System Design Interviews, including the outline-first advice
and simple baseline discussion [[cite:machine-learning-system-design-interview=>ML System Design Interviews]].

[[person:arsenykravchenko=>Arseny Kravchenko]] centers
constraints in Building Scalable and Reliable Machine Learning Systems [[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]].
He frames ML system design as decisions under constraints. His mobile ML example
adds latency, energy use, and model size to the modeling problem. It also adds
user experience and platform choice. He argues that the problem part of a design
document should cover goals, non-goals, assumptions, and metrics before solution
details.

[[person:benwilson=>Ben Wilson]] connects
maintainability and adoption in Production ML Best Practices [[cite:machine-learning-engineering-production-best-practices=>Production ML Best Practices]].
He criticizes large "god function" code and explains that projects fail
production when they lack buy-in or cost too much to maintain.

[[person:nadianahar=>Nadia Nahar]] centers software
engineering boundaries in Software Engineering for ML [[cite:software-engineering-for-machine-learning=>Software Engineering for ML]].
She argues that ML has to become part of a larger software system. She also
names weak requirements, data access, unrealistic expectations, and deployment
gaps.

Her empirical open-source study is a useful portfolio lens too. The study
reviewed roughly 300 open-source ML products to distinguish full products from
models or APIs. That reinforces why a portfolio project should show the
surrounding software, user workflow, and operational boundary
([[cite:software-engineering-for-machine-learning@15:17=>Open-Source ML Product Dataset]]
[[cite:software-engineering-for-machine-learning@21:54=>ML Product Criteria]]).
Together, these perspectives make the portfolio bar broader than model quality.

Show the decision, baseline, and data path. Also show the evaluation plan,
software boundary, and maintenance story. The disagreement is mostly about
emphasis. Some guests stress process or interview defensibility. Others stress
constraints, maintainability, or software
integration.

## Predictive Service Projects

A predictive service is the strongest default when the target role involves
applied modeling plus production awareness. Build a classifier or forecaster,
or use fraud scoring, churn prediction, or ranking. Start from the decision
that changes if the prediction works.

The CRISP-DM classified-listing example follows this structure [[cite:crisp-dm=>CRISP-DM]].
The model is judged against a baseline and
against whether moderators spend less time correcting categories. It isn't
judged only against an offline score.

For review, include a simple baseline, a leakage check, and a metric tied to
false positives or false negatives. Include a fallback path too. State whether
the system would run as batch scoring, an API, or a human-in-the-loop review
step.

[[person:valeriybabushkin=>Valeriy Babushkin]]'s checklist in
ML System Design Interviews covers labels, feature
access, and validation. It also covers online evaluation and distribution shift.
It covers class imbalance, monitoring, and fallbacks [[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
For more context on metrics and experiments, connect the project to
[[Evaluation]] and
[[a-b-testing=>A/B Testing]].

## Production ML Pipeline Projects

A production ML pipeline project can use a simple model because the lifecycle is
the proof. Reviewers should see reproducible training and testable code. They
should also see batch or online inference, packaging, deployment notes, and a
monitoring plan.

[[person:benwilson=>Ben Wilson]]'s
production ML engineering example connects this project type to engineering
practice [[cite:machine-learning-engineering-production-best-practices=>Production ML Best Practices]].
He describes a production capstone with unit tests, integration tests, and
monitoring. The capstone also includes A/B testing, deployments, and CI/CD
around an open-source dataset.

Earlier in the same episode, [[person:benwilson=>Ben Wilson]]
criticizes "god function" code and recommends breaking it into smaller,
testable pieces. That makes code structure part of the portfolio evidence.
Reviewers should be able to find training and feature preparation. They should
also find inference, tests, and configuration without reading one large notebook
or script.

Make the run path visible outside a notebook.
[[person:nadianahar=>Nadia Nahar]] treats ML as part of a larger software
system, not an isolated experiment [[cite:software-engineering-for-machine-learning=>Software Engineering for ML]].

In a compact version, include a training command, model artifact, and scoring
job. Add a Docker setup, CI check, and monitoring sketch. Link that version to
[[MLOps vs DataOps]] and
[[Production ML Project Checklist]].
Also link it to the
[[Machine Learning Engineer Roadmap]]
when the project is meant to prove readiness for engineering-heavy roles.
For data scientists using a production pipeline project as transition evidence,
connect it to
[[data-scientist-to-machine-learning-engineer=>data scientist to machine learning engineer]].

## Recommendation and Ranking Projects

Recommendation projects fit product ML roles, and search-ranking or marketplace
projects can show the same role signal. Include candidate generation, ranking
features, and cold-start behavior. Also include offline metrics, serving
assumptions, and user-facing tradeoffs.

[[person:valeriybabushkin=>Valeriy Babushkin]]'s
system design interview episode uses recommender and ranking examples to tie
metrics and baselines to product outcomes. Model choice comes after that
framing [[cite:machine-learning-system-design-interview=>ML System Design Interviews]].
[[person:arsenykravchenko=>Arseny Kravchenko]]'s
scalable ML systems episode adds the design-doc focus through his photostock
search example [[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]].
Constraints, data flow, latency, and failure modes come before an embedding demo.

For portfolio review, state the served surface and target metric.
Link search projects to
[[Search and RAG Project Checklist]]
only when retrieval or ranking behavior is part of the implementation.

Link product behavior projects to
[[Recommendation Systems]].
Also link them to
[[Product Analytics]] and
[[a-b-testing=>A/B Testing]] because product ML work separates online impact
from offline model score.

## Computer Vision and NLP Projects

Computer vision and NLP projects are strongest when the data work is visible.
Include a deployment constraint too.
[[person:tatianagabruseva=>Tatiana Gabruseva]] discusses
that transition in Switch to Computer Vision and Deep Learning [[cite:from-physics-to-computer-vision-career-transition=>Switch to Computer Vision and Deep Learning]].

She covers Kaggle projects, internships and Omdena-style collaborations. She
also covers pet projects and data collection, then connects labeling,
deployment, and Docker to the same transition.

[[person:arsenykravchenko=>Arseny Kravchenko]]'s mobile ML example in
Building Scalable and Reliable Machine Learning Systems shows why runtime
constraints can matter more than model novelty. Those
constraints include model size, frame rate, battery use, and platform support.
[[Computer Vision]]
portfolio work is stronger when it states the runtime target, not only the model
architecture [[cite:building-scalable-and-reliable-machine-learning-systems=>Building Scalable and Reliable Machine Learning Systems]].

Open-source and community NLP work can also become portfolio evidence when the
artifact is concrete. Hugging Face Contributions and NLP Portfolio treats
Spaces demos and documentation as public proof of applied NLP capability. GitHub
work gives the same signal [[cite:hugging-face-contributions-and-nlp-portfolio=>Hugging Face Contributions and NLP Portfolio]].
In From Biology to ML, [[person:isabellabicalho=>Isabella Bicalho]] connects
open-source and AI-for-good work to job-ready experience. Her computer vision
and transformer projects stay grounded in collaboration and practical
implementation [[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]].

## Kaggle and Notebook Projects

Kaggle projects can work as portfolio evidence when they show understanding,
because rank alone isn't enough.
The same rule applies to
[[competitions-beyond-kaggle=>competitions beyond Kaggle]]. The useful signal
comes from code, reports, evaluation notes, and reproducible runs. Public
leaderboard position matters less.

[[person:andradaolteanu=>Andrada Olteanu]] describes Kaggle notebooks and
GitHub as public proof. That proof helped a hiring conversation
[[cite:analytics-to-data-science-with-kaggle-portfolio@32:14=>Kaggle Portfolio]].
Her path matters for analysts because the notebooks made Python and modeling
visible. She also preserved data validation, domain knowledge, and exploratory
analysis as strengths from analytics
[[cite:analytics-to-data-science-with-kaggle-portfolio@36:41=>Analyst Skills]].

Treat the notebook as part of the proof. A reviewer should see the
reimplementation path, debugging trail, and candidate's own changes, not only a
copied competition solution.

Olteanu's learning method was to study strong notebooks and rebuild them in a
fresh notebook. She renamed variables, changed steps, and debugged the result
until she understood the code path
[[cite:analytics-to-data-science-with-kaggle-portfolio@45:16=>Notebook Reproduction]].
Public discussion around the notebook can also create feedback and mentorship.
Olteanu connected with Gabi Preda through Kaggle activity, then turned that
visibility into mentoring and a hiring conversation
[[cite:analytics-to-data-science-with-kaggle-portfolio@18:09=>Kaggle Mentorship]].
Link the notebook from the
[[data-scientist-cv-and-portfolio=>Data Scientist CV & Portfolio]] page and
prepare to defend it in a
[[Data Scientist Interview Roadmap=>data scientist interview]].

For a credible Kaggle project, name the baseline and credit borrowed ideas.
Explain the data validation and feature choices. Add original analysis and
connect the notebook to the claimed skill.
[[person:lukewhipps=>Luke Whipps]] applies the same standard to recruiting.
He expects resume skills to link to concrete projects rather than
disconnected tool names [[cite:get-data-scientist-job=>Land Data Scientist Roles]].

[[person:tatianagabruseva=>Tatiana Gabruseva]]'s
computer vision transition sets the boundary [[cite:from-physics-to-computer-vision-career-transition=>Switch to Computer Vision and Deep Learning]].
Kaggle is useful for learning because the data, task, and metric are already
chosen. It doesn't show how to collect data or define a business metric. It
also doesn't show deployment or packaging work.

For a machine learning engineer portfolio, pair a Kaggle-style experiment with
an end-to-end pet project or convert the notebook into a small reproducible
service.
[[competitions-beyond-kaggle=>Competitions beyond Kaggle]] covers non-Kaggle
options where a hosted evaluation can show stronger evidence than a notebook
alone. A Docker-based run, conference challenge, or domain challenge may be a
better fit.

## Open Source ML Projects

An open-source-oriented ML portfolio can be smaller than a full application if
the work makes a project easier to use, run, test, or maintain. In Contribute
to Open Source ML, [[person:vincentwarmerdam=>Vincent Warmerdam]] treats
documentation, examples, and contribution guides as part of project stewardship.
He also includes packaging, tests, and CI. His scikit-lego and Rasa discussion
shows why small, [[scikit-learn=>Scikit-Learn]]-compatible tools can be stronger
evidence than unfinished large projects [[cite:open-source-ml-contributions=>Contribute to Open Source ML]].
[[open-source-ml-contributions=>Open-source ML contributions]] covers the issue,
docs, tests, and maintainer-etiquette mechanics behind that route.

This route fits candidates who want public collaboration evidence. Link issues,
pull requests, examples, or docs work to a clear user problem. For more detail
on that signal, use
[[Open Source Portfolio Evidence]]
and the
[[Open Source Contributor Roadmap]].

## Portfolio Writeups

A case-study writeup can explain the project when deployment is private,
expensive, or unsafe to publish. In Technical Writing for Data Scientists,
[[person:eugeneyan=>Eugene Yan]] describes writing as communication practice.
He uses outlines with section headers, topic sentences, and supporting evidence.
That same structure works for a portfolio case study and connects to
[[Technical Writing]] [[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].

Use the writeup to cover the problem and decision before the data, baseline,
and model. Also cover the metric, result, limitations, and next decision so the
interview story is ready.
[[person:nicksingh=>Nick Singh]] uses project walkthroughs to test whether the
candidate can defend assumptions and model choices. He also tests metrics,
validation, and impact [[cite:data-interview-behavioral-and-portfolio-prep-guide=>Ace Data Interviews]].

## Related Pages

These pages cover adjacent role, system, and evaluation context.

- [[Machine Learning]]
- [[Machine Learning System Design]]
- [[ML System Design Documents]]
- [[Machine Learning Engineer Roadmap]]
- [[MLOps vs DataOps]]
- [[Production ML Project Checklist]]
- [[Evaluation]]
- [[Recommendation Systems]]
- [[Computer Vision]]
- [[Open Source Portfolio Evidence]]
- [[career-transitions-in-data=>Career Transition]]
- [[Job Search]]
