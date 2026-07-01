---
layout: article
title: "Competitions Beyond Kaggle"
keyword: "competitions beyond kaggle"
summary: "A practical guide to using competitions beyond Kaggle as portfolio and evaluation evidence, with guidance on specialized challenges, leaderboard limits, agentic AI benchmarks, code quality, collaboration, and when competitions are the wrong proof."
search_intent: "People searching for competitions beyond Kaggle usually want alternatives to leaderboard chasing and a practical way to turn ML, AI, or research competitions into credible portfolio evidence."
related_wiki:
  - Machine Learning Portfolio Projects
  - Open Source Portfolio Evidence
  - Evaluation
  - Applied Research
  - Career Growth
  - Portfolio Projects
  - Agent Engineering
---

Competitions beyond Kaggle are useful when they create evidence a reviewer can
look at. The proof can include code and reports. It can also include evaluation
choices, collaboration, and domain learning. They're weaker when they only
produce a rank.

[Tatiana Gabruseva]({{ '/people/tatianagabruseva/' | relative_url }}) separates
learning value from career value in
[Competitions: Beyond the Kaggle Leaderboard]({{ '/podcasts/s24e01-competitions-beyond-kaggle-leaderboard/' | relative_url }}).
Around 9:13, she describes Kaggle as a fast feedback loop with community
notebooks, discussions, and postmortems. Around 28:54 and 35:24, she separates
rank from career value. The value came from turning competition work into a
clean repository and interview discussion, not from the Kaggle Master title.

Use this guide with
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}),
and [Evaluation]({{ '/wiki/evaluation/' | relative_url }}). A competition can
be one strong portfolio project. The writeup still needs to explain the
problem, baseline, and metric. It should also cover data assumptions, result,
and limits. Otherwise it's just a score on someone else's task.

## Best Uses

Competitions help when you need a real problem before you have a job or client.
They also help before you have an internal dataset.

In the
[competition episode]({{ '/podcasts/s24e01-competitions-beyond-kaggle-leaderboard/' | relative_url }}),
Tatiana says around 10:05 that competitions can build skill. The best learning
comes from changing domains rather than repeating one narrow recipe.
She gives examples across time series and NLP around 10:53. She also names
segmentation, detection, and 3D computer vision. That makes competitions useful
for a candidate who needs breadth before interviews, especially when the target
role is still unclear.

The strongest use isn't "I ranked well." It's a fuller story about learning a
domain, building a baseline, and making submissions. It also means studying
stronger solutions and explaining tradeoffs. Around 23:04, the episode frames
competitions as problems that don't tell you how to solve them. Tatiana then
warns around 30:20 to ignore the leaderboard at first.

Read discussion threads and strong notebooks for learning. For a portfolio,
document that path in the same style as
[Portfolio Projects]({{ '/wiki/portfolio-projects/' | relative_url }}). Show
what you tried, what failed, and what improved the metric. Then explain what you
would change for a real system.

Competitions also help when the target evidence is closer to
[applied research]({{ '/wiki/applied-research/' | relative_url }}) than product
delivery. Tatiana describes an astronomy competition where a number 13
leaderboard solution became an arXiv report and later a journal publication
around 32:08-33:47. The key signal wasn't first place. It was a technical
writeup with findings, features, and enough novelty for a research audience.

## Competition Types Beyond Kaggle

Kaggle remains useful for beginners because it has active notebooks, discussion,
starter code, and visible feedback. Tatiana recommends it for a
first submission around 57:46 because newcomers can find a starter notebook,
read discussions, submit once, and iterate. For learning, that community is hard
to replace.

Beyond Kaggle, different platforms produce different evidence. Tatiana
recommends Topcoder around 26:01 for a fairer competition environment.
Participants submit a Docker container. The organizers run training or
inference under constraints, which reduces test-set manipulation. That form of
competition is stronger evidence for reproducibility and
engineering discipline because another system has to run the solution.

Research challenges create different artifacts. Around 45:53 and
47:03, Tatiana references AIcrowd and conference-hosted challenges. Strong
participants may become coauthors or submit reports to venues such as NeurIPS
and CVPR workshops.

Around 52:51-55:12, she recommends AIcrowd and
grand-challenge.org. She also names MICCAI challenges and conference challenge
pages for specialized domains such as medical imaging. Those competitions may
have less community discussion than Kaggle, but they can create conference
reports, workshop presentations, and research credibility.

Choose the platform by the evidence you need. Use Kaggle when you need a
learning loop and many public solutions. Use Docker-based or hosted-evaluation
competitions when you need reproducibility evidence. Use academic and
conference challenges when the target role values research communication,
domain expertise, or workshop participation. For computer-vision-heavy paths,
pair those choices with
[Computer Vision]({{ '/wiki/computer-vision/' | relative_url }}) and the
computer vision section of
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).

## Leaderboard Limits

A leaderboard is an evaluation surface, not a full evaluation plan. Tatiana says
around 15:29 that optimizing a single metric is one of the problems of Kaggle
versus production. Around 24:25 and 25:22, she adds that popular competition
formats can allow manipulation and cheating. They can also involve extra data
scraping or tiny metric differences between places. That makes rank a noisy
hiring signal unless the candidate can explain the validation setup and the
choices behind the result.

The guide-level rule is simple: never present the rank without the mechanism.
Explain the train-validation split and leakage checks. Add the baseline, metric,
and submission constraints.

If the method is an ensemble, explain what each model contributed. Then state
whether the same complexity would survive a production budget. If the solution
used external data, state whether the competition allowed it.

Those details align with the broader
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) standard. A model score
only matters when it maps to a decision, baseline, and operating boundary.

Tatiana's own examples show why rank isn't the whole story. Around 32:45, a
number 13 astronomy solution still became a publication. Around 35:24, a Top 5%
Lyft competition result became a hiring signal because the interviewers could
open the GitHub repository and discuss the approach. Around 37:28, she argues
that artifacts can create more opportunity than winning alone.

Those artifacts include a repository and publication. They can also include a
presentation, blog post, and LinkedIn distribution.

## Evaluation Design

Treat a competition as a constrained evaluation exercise. The organizer gives
the dataset and task, plus the metric and submission format. It often gives the
compute boundary too.

Your portfolio job is to explain which parts you trusted and which parts would
change outside the competition. Tatiana's Topcoder example around 26:01 is a
good template. A Docker submission, fixed inference environment, GPU-time
constraints, and organizer-run evaluation make the result easier to trust than a
notebook-only score.

For a portfolio writeup, include a short evaluation note:

1. The public metric and why it mattered for the competition.
2. The local validation setup and how it matched or failed to match the public
   leaderboard.
3. The simplest baseline you beat.
4. The largest source of leakage, data shift, or metric gaming risk.
5. The production or research question the competition didn't answer.

This keeps the competition connected to
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
instead of turning it into a medal list. It also helps in interviews because the
reviewer can ask about false positives, false negatives, and data drift. They
can also ask about compute cost or serving constraints and see whether you
understand the system beyond the leaderboard.

## Agentic AI Benchmarks

Competitions are becoming benchmark environments for agents, not only humans.
Tatiana discusses agentic AI benchmarks around 13:35 and says Kaggle can become
an environment where different agents compete. Around 15:29-16:29, she and
the host compare automated research and AutoML. They also compare
cross-validation and limited daily submissions. Together, those pieces form a
loop that an AI system can optimize.

That shift changes the portfolio signal. If an agent writes the code, the
candidate still needs to show evaluation judgment. Around 17:43-21:58, Tatiana
warns that automation can prevent deep learning if the person doesn't do the
hard parts themselves. The useful evidence isn't "Claude improved my score."
It's a reproducible experiment loop, a validation strategy, a critique of the
agent's changes, and a clear boundary between assisted work and personal
understanding.

For agent-heavy projects, connect the writeup to
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) and
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}). Show the task harness and
tool permissions. Include the submission budget, regression tests, and failure
cases. A competition can then prove evaluation design for an agentic system, not only
prompting skill.

## Portfolio Narrative

Turn the competition into a case study. Tatiana's strongest hiring example is
the Lyft competition around 34:59-35:24. She created a well-organized GitHub
repository with a proper README and put "Top 5%" on the resume. Interviewers
used the repository to discuss her approach. The offer came from reviewable
work, not from a private notebook or rank alone.

The minimum portfolio package should include:

1. A README that states the task, data, metric, baseline, and final result.
2. A reproducible run path for training or inference.
3. A short explanation of validation and leaderboard mismatch.
4. A clean notebook or report for exploration.
5. A blog post or case study that explains the idea in plain language.
6. Links to the competition, repository, report, and any presentation.

Tatiana recommends this artifact-first strategy around 37:28 and 42:34. She
also recommends using blog posts, LinkedIn, and simpler explanations when the
technical report is too dense for a general audience. Competitions sit
near [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and [Technical Writing]({{ '/wiki/technical-writing/' | relative_url }}).
Public code and clear explanation make the work easier to evaluate.

## Collaboration and Code Quality

Competitions can also prove collaboration. Around 59:24, Tatiana recommends
building a private GitHub pipeline instead of relying only on notebooks for
iteration. Around 1:00:56, she describes teaming up asynchronously with another
participant in a Slack channel after both had already shown commitment through
submissions and analysis. Around 1:01:08, the episode adds that a teammate
request is more credible when the person already has submissions near the same leaderboard
zone.

Use that lesson in the portfolio by stating your contribution. The contribution
may be data cleaning or validation. It may also be feature engineering,
modeling or inference packaging. It may be writeup or presentation work. Link
pull requests, commits, issues, or experiment notes when possible.

If the code is public, make it look like work another engineer could review. Use
small modules and setup instructions. Add tests where practical, and keep a clear
separation between exploration and reusable pipeline code.

That standard overlaps with
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}).
The portfolio claim is stronger when the repository shows maintainable work
under competition pressure, not only a final notebook.

## Bad Fit

Competitions are the wrong proof when the role requires evidence they can't
show. Tatiana says around 42:34-49:29 in
[Switch to Computer Vision and Deep Learning]({{ '/podcasts/from-physics-to-computer-vision-career-transition/' | relative_url }})
that Kaggle gives the task, data, and metric. It doesn't prove data collection
or labeling. It also doesn't prove deployment, Docker, or an end-to-end project.

The newer competition episode makes the same boundary sharper: around 15:29,
single-metric optimization can diverge from production usefulness. Around 56:16,
specialized
research challenges may offer better conference evidence but less community
learning than Kaggle.

Use a competition as the main proof when the target role values modeling and
domain learning. It can also support applied research and benchmarking.
Technical communication is another fit.

Use another project type when the target role values production ownership and
stakeholder discovery. Product metrics and data engineering also need broader
proof. Monitoring needs broader proof too. Maintainability in a live system
needs broader proof too.

For those cases, start from
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).
Use [Evaluation]({{ '/wiki/evaluation/' | relative_url }}) and the
[Data Scientist Interview Prep guide]({{ '/guides/data-scientist-interview/' | relative_url }})
to place the competition inside a broader project set.

The practical test is whether a reviewer can look at the work and learn how you
think. If the only visible fact is a leaderboard place, the proof is thin. If
the competition produced a repository and evaluation note, the proof gets
stronger. Add a writeup and collaboration trail. Honest limits also help the
work become strong evidence for
[career growth]({{ '/wiki/career-growth/' | relative_url }}) and hiring.
