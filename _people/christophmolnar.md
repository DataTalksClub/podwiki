---
layout: "person"
title: "Christoph Molnar"
source_person: "../datatalksclub.github.io/_people/christophmolnar.md"
person_id: "christophmolnar"
summary: "Christoph Molnar's DataTalks.Club podcast contribution on interpretable machine learning, SHAP, conformal prediction, model trust, and technical writing."
expertise: ["machine learning", "data science", "interpretability", "tools", "practices"]
podcast_episodes: ["interpretable-machine-learning"]
source_url: "https://datatalks.club/people/christophmolnar.html"
curated: "true"
---

Christoph Molnar is a statistician, machine learning practitioner, and
technical author whose work centers on making machine learning easier to
understand. In
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html),
he discusses
[interpretability]({{ '/wiki/interpretability/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[data science]({{ '/wiki/data-science/' | relative_url }}) through model
debugging and uncertainty. He also explains why technical writing has to stay
connected to real modeling work.

## Interpretable Machine Learning Starts With Debugging

Christoph frames interpretability as a working tool, not only a
stakeholder-facing chart. Around 7:50 in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html),
he traces his interest back to statistics: he was used to thinking about the
data-generating mechanism and understandable models. When he moved toward more
complex machine learning models, some of that understanding disappeared.

At 9:27 in the same episode, he pushes back on the idea that competitions only
care about prediction accuracy. He describes a forecasting challenge where a
target-leakage feature made the score look better than it should have. A SHAP
feature-importance view surfaced that feature quickly. Christoph uses that case
to show why interpretability belongs in model debugging.

His discussion links to
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
The explanation was useful because it pointed back to a data and modeling
mistake.

## SHAP Helps, But One Plot Can't Establish Trust

Christoph's SHAP discussion is strongest when he treats the method as one tool
inside a broader review. At 23:44 in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html),
he describes writing "Interpreting Machine Learning Models with SHAP." SHAP was
popular with readers and versatile enough to deserve a deeper Python-focused
treatment. He also says SHAP isn't intuitive, which is why
examples matter.

At 25:37, he warns against relying on only one interpretation method. He would
still pick SHAP if he had to choose one. His view gives a useful counterweight
to generic [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
claims. A SHAP plot can help a practitioner look at feature effects. The team
still has to decide what question the explanation answers and what action
follows.

[Polina Mosolova](https://datatalks.club/people/polinamosolova.html) and
[Supreet Kaur](https://datatalks.club/people/supreetkaur.html) cover adjacent
explainability and governance questions in their own episodes, while Christoph
gives the method-level SHAP discussion.

## Conformal Prediction Communicates Uncertainty

Christoph uses conformal prediction to move model trust beyond a single score
or label. At 20:27 in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html),
he explains conformal prediction as a way to calibrate model uncertainty. A
classifier can return a set of possible classes with a probability guarantee
instead of only one class. A regression model can return calibrated intervals
instead of only one number.

He separates conformal prediction from interpretability at 22:33. The methods
are different, but both can be applied after a model is trained. This matters
for [data scientist roles]({{ '/wiki/data-scientist-role/' | relative_url }})
and [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) because a
prediction set changes the decision. A wide interval or ambiguous class set may
need more review, more data, or a safer fallback.

For another conformal prediction reference, use
[Olga Ivina](https://datatalks.club/people/olgaivina.html), whose
DataTalks.Club discussion mentions conformal prediction in air-pollution
research.

## Explanation Language Has Limits

At 26:17 in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html),
Christoph discusses the blurry boundary between explainable AI and
interpretable machine learning. He says he uses both terms as keywords because
practitioners use them with heavy overlap, but he's careful about the word
"explain." For him,
explaining a prediction is a strong claim, while interpreting leaves room for
partial understanding.

Readers should use
[Interpretability]({{ '/wiki/interpretability/' | relative_url }}) terms precisely.
A transparent model, a post-hoc SHAP explanation, and a calibrated prediction
set don't answer the same question. Christoph's terminology discussion also
fits [scikit-learn]({{ '/wiki/scikit-learn/' | relative_url }}) and
[Machine Learning Tools]({{ '/wiki/machine-learning-tools/' | relative_url }})
pages when the question is which method or library supports the review a team
needs.

## Technical Writing Keeps Models Practical

Christoph also explains how technical authors stay credible. At 15:55, he says
he published his first book chapter by chapter and used early feedback.
At 33:07, he explains why he returned to hands-on
competitions after a long writing stretch. He wanted to keep contact with messy
data, modeling choices, and real evaluation problems.

His logbook practice at 36:21 in
[Interpretable Machine Learning](https://datatalks.club/podcast/interpretable-machine-learning.html)
connects writing back to modeling. He uses short Obsidian notes to record what
he tried, where he got stuck, and what an experiment showed. His notes belong
beside
[Technical Writing]({{ '/wiki/technical-writing/' | relative_url }}) and
[Documentation]({{ '/wiki/documentation/' | relative_url }}), but it isn't only
a writing habit. In his account, the notes help him decide what to try next.
They also keep failed experiments from disappearing into memory.

At 44:51 and 48:36, Christoph gives the reader-facing side of the same craft.
For later books, he invited small groups of test readers and revised in phases.
That included the conformal prediction and SHAP books. For new technical
writers, he recommends starting with small published pieces rather than waiting
until a full book exists. Data and ML practitioners can use writing to teach,
test their understanding, and create public proof of work.

## Related Topics

These pages continue the themes Christoph covers in the episode.

- [Interpretable Machine Learning: SHAP, Conformal Prediction and Model Trust](https://datatalks.club/podcast/interpretable-machine-learning.html)
- [Interpretability]({{ '/wiki/interpretability/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Technical Writing]({{ '/wiki/technical-writing/' | relative_url }})
