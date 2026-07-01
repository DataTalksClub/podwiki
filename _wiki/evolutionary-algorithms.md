---
layout: wiki
title: "Evolutionary Algorithms"
summary: "How DataTalks.Club podcast discussions connect evolutionary algorithms to game AI, evolutionary deep learning, prompt search, optimization, and modern agent systems."
related:
  - Machine Learning
  - Deep Learning
  - Reinforcement Learning
  - AI Agents
  - Agent Engineering
  - Evaluation
---

In DataTalks.Club podcast discussions, [Micheal Lanham]({{ '/people/micheallanham/' | relative_url }})
gives the clearest evolutionary-algorithms thread. He connects the topic to game
AI and numerical optimization. He also connects it to evolutionary deep
learning, prompt search, and modern
[AI agents]({{ '/wiki/ai-agents/' | relative_url }})
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
1:07-14:09). The podcast evidence is narrow, so this article maps
that discussion rather than giving a complete textbook treatment of
evolutionary computation.

Lanham puts evolutionary algorithms beside
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) and
[deep learning]({{ '/wiki/deep-learning/' | relative_url }}). He also links
them to [reinforcement learning]({{ '/wiki/reinforcement-learning/' | relative_url }}).
At 2:36-2:55, he describes early work with games, simple neural networks, and
evolutionary methods for cognitive testing. Later, Lanham returns to
evolutionary algorithms for pipeline-corrosion numerical analysis. He explains
why they were attractive before modern deep learning frameworks became dominant
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
4:19-5:01).

## Common Definition

In the interview, genetic algorithms are framed as a type of evolutionary
algorithm. You start with a population and score each candidate by fitness.
Fitter candidates reproduce, random mutations appear, and the search repeats
until it converges or resources run out. Lanham adds that some variants also pair
parents to combine traits
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
11:30-12:59).

Lanham treats evolutionary algorithms as search methods that explore many
candidates when no answer is obvious. He says they were seen around 2006
as a promising path to intelligence. He also emphasizes heavy computation and
looser constraints than a hand-designed optimization method
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
13:21-13:44).

## Game AI and Industry Optimization

Lanham starts with game-like environments rather than a generic algorithm
catalog. In early academic work, his team built a game for testing children's
executive function. They then used simple neural networks and evolutionary
algorithms to create test sequences and analyze player data
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
2:36-2:55).

That makes the method part of a simulated interaction where the system can try
candidate tests, collect behavior, and compare outcomes.

The industrial example is more direct optimization. After oil-and-gas product
work, Lanham returned to consulting and used evolutionary algorithms for
numerical analysis related to pipeline corrosion. He says the methods could
adapt faster and process data efficiently in that setting. Their compute cost
and weaker integration with the frameworks that boosted deep learning helped
push them aside
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
4:19-5:01).

That caveat is important: the episode doesn't claim evolutionary
algorithms replaced mainstream [ML]({{ '/wiki/machine-learning/' | relative_url }}).
It treats them as a useful family of search techniques with a recurring compute
tradeoff.

## Evolutionary Deep Learning

Lanham later wrote "Evolutionary Deep Learning," and he summarizes the idea in
the episode as combining deep learning with evolutionary algorithms. The
concrete uses he names are hyperparameter search and network architecture
modification, especially for convolutional neural networks
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
9:09-9:29). In archive terms, this connects evolutionary algorithms to model
selection and architecture tuning rather than to everyday supervised modeling.

Lanham distinguishes training weights from design search because a CNN learns
from data while an evolutionary method searches over architecture variants or
hyperparameters. These approaches can work well, but Lanham warns that they're
computationally intensive
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
9:09-9:29). Read this with
[Deep Learning]({{ '/wiki/deep-learning/' | relative_url }}) and
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}). Those pages cover
baselines, deployment constraints, and the decision the model supports.

## Prompt Search and Generative AI

Lanham's most modern example is prompt engineering. He says recent work applies
evolutionary algorithms to prompts for LLMs and agents. The system generates
prompt variants, scores the results, and evolves toward prompts that perform
better
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
14:09-14:28). He describes this as promising because LLM behavior is complex
and prompt variants can produce unexpected outputs.

Lanham also says prompt search can be computationally expensive. He agrees that
one small example repo may take about a week of computation to produce results
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
14:59-15:23). Read evolutionary prompt search with
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).
The search needs a scoring method. The compute cost has to be justified by
better behavior on the target task.

## Optimization and Decision Systems

[Dan Becker]({{ '/people/danbecker/' | relative_url }}) doesn't focus on
evolutionary algorithms in his decision-optimization episode, but his framing
helps set the boundary around optimization work. He argues that a model's
`.predict` answers "what will happen," while a decision function answers "what
should I do about it." His examples include airline pricing and fraud review
thresholds. He also discusses business rules that combine predicted
probabilities with value or cost
([Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }}),
5:11-18:52, 21:06-25:00).

That boundary helps interpret Lanham's evolutionary-algorithm examples.
Evolutionary search can propose or tune candidates, but the team still needs a
fitness function, simulator, or evaluation target. Becker makes the same point
from the decision side. Teams often need to simulate different decision rules
and propagate outcomes over time. They also need domain knowledge rather than a
supervised model that tries to optimize the whole business objective
([Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }}),
19:19-31:53).

Evolutionary algorithms fit this archive theme when they search over candidate
actions, prompts, or architectures against a meaningful outcome measure.

## Connection to Agent Systems

Lanham's episode also links evolutionary thinking to current
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}). He
teaches agents through minimal task decomposition first. He then distinguishes
sequential flows from manager-agent orchestration and collaborative multi-agent
designs
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
20:57-31:17). At 27:45, he compares collaborative agents that iterate and
refine solutions to evolutionary algorithms.

That comparison should stay modest. The episode doesn't say every
[multi-agent system]({{ '/wiki/multi-agent-systems/' | relative_url }}) is an
evolutionary algorithm. It says collaboration can resemble evolutionary search
when agents generate candidate outputs and exchange feedback. They then refine a
result.

Lanham applies that comparison to complex problems. In those problems, the
input and desired output are known but the path is detailed
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
26:25-29:35). Teams still need a scoring target, a stopping rule, and a compute
budget.
