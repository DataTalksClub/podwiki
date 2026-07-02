---
layout: wiki
title: "Evolutionary Algorithms"
summary: "How DataTalks.Club podcast discussions connect evolutionary algorithms to game AI, evolutionary deep learning, prompt search, optimization, and modern agent systems."
related:
  - Machine Learning
  - Deep Learning
  - Reinforcement Learning
  - Agent Engineering
  - Evaluation
---

Evolutionary algorithms are search methods for trying many candidate solutions
when the target can be scored but not directly derived. They span game AI,
numerical optimization, evolutionary deep learning, prompt search, and modern
[[agent-engineering|AI agents]]
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

Evolutionary algorithms sit near
[[machine learning]],
[[deep learning]], and
[[reinforcement learning]].
The shared structure is search under feedback: define a fitness signal, generate
candidate solutions, keep stronger candidates, and mutate or combine them until
the result converges or the compute budget runs out
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Search Mechanics

Genetic algorithms are a type of evolutionary algorithm, built from a population
of candidates, a fitness function, a mutation function, and sometimes a pairing
function for combining parents. Fitter candidates reproduce, random mutations
create new variants, and the search continues until convergence or resource
limits
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

The practical tradeoff is compute. Evolutionary algorithms became popular across
many applications because they explore many possible solutions with few hard
constraints, but they are computationally intensive. Around 2006 researchers
treated them as a possible path to intelligence; later
[[deep learning]]
frameworks became dominant
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

## Game AI and Industry Optimization

Game-like environments come before any generic algorithm catalog. Early academic
work built a game for testing children's executive function, then used simple
neural networks and evolutionary algorithms to create test sequences and analyze
player data
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

The method belongs to a simulated interaction. The team can try candidate tests,
collect behavior, and compare outcomes.

The industrial example is more direct optimization: after oil-and-gas product
work, evolutionary algorithms handled numerical analysis related to pipeline
corrosion, adapting faster and handling data efficiently. Their compute cost and
weaker fit with the frameworks that boosted deep learning helped push them aside
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

A broader algorithms-and-optimization toolkit places evolutionary algorithms
alongside graphs, and for optimization names random sampling, gradient descent,
simulated annealing, and genetic algorithms for permutation problems
([[podcast:algorithms-data-structures-for-engineers|Practical Algorithms for Engineers]]).

The combined picture is narrow but useful: evolutionary algorithms aren't a
replacement for mainstream
[[machine-learning|ML]]. They're search techniques
for cases where teams can score candidates and afford repeated trials.

## Evolutionary Deep Learning

The book "Evolutionary Deep Learning" by
[[person:micheallanham|Micheal Lanham]]
combines deep learning with evolutionary algorithms, with concrete uses in
hyperparameter search and network architecture modification, especially for
convolutional neural networks
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Evolutionary algorithms belong to model selection and architecture tuning rather
than everyday supervised modeling.

Weight training is separate from design search: a CNN learns from data, while an
evolutionary method searches over architecture variants or hyperparameters.
These approaches can work well, but they are computationally intensive
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

That makes [[evaluation]]
part of the design problem. Teams need baselines and deployment constraints
before spending compute on architecture or hyperparameter search. They also
need a clear decision the model supports.

## Prompt Search and Generative AI

The most modern example is prompt engineering. Evolutionary algorithms apply to
prompts for LLMs and agents: the system generates prompt variants, scores the
results, and evolves toward prompts that perform better
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
This is promising because LLM behavior is complex and prompt variants can produce
unexpected outputs.

Prompt search can be computationally expensive; one small example repo may take
about a week
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
It belongs with the broader
[[prompt engineering]] and
[[LLM evaluation workflows]]
pages. Prompt evolution needs a scoring method, and the compute cost has to buy
better behavior.

## APIs and Tooling

EVOL is an API-design example: an evolutionary algorithm library built to
simplify genetic algorithms, which often become nested `for` loops. It used
population and evolution objects with a functional API so the algorithm was
easier to use
([[podcast:open-source-ml-contributions|Contribute to Open Source ML]]).

The point is about [[open-source|open-source]]
tool design, not a new theory of evolutionary search. It shows why API design
matters for algorithm families that involve populations, scoring, mutation, and
repeated generations. A clearer API can make the search easier to maintain even
when the underlying method remains compute-heavy.

## Optimization and Decision Systems

Decision optimization sets the boundary around this work. A model's `.predict`
answers "what will happen," while a decision function answers "what should I do
about it," across cases like airline pricing and fraud review thresholds, with
business rules that combine predicted probabilities with value or cost
([[podcast:machine-learning-decision-optimization|Optimize Decisions with ML]]).

Evolutionary search sits on that boundary: it can propose or tune candidates,
but the team still needs a fitness function, simulator, or evaluation target.
The same holds from the decision side, where teams simulate different decision
rules, propagate outcomes over time, and rely on domain knowledge rather than a
supervised model that tries to optimize the whole business objective
([[podcast:machine-learning-decision-optimization|Optimize Decisions with ML]]).

A cautionary engineering example comes from laser-system design: genetic
algorithms first, then simple [[reinforcement learning]]
around 2014. The search produced interesting ideas, but some were impractical to
manufacture because the problem was poorly formulated outside the simulation
([[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design and Metrics Strategy]]).

Search methods can optimize the wrong target when the simulator leaves out
constraints, business objectives, or real-world costs. That laser-system example
gives the decision-optimization boundary a physical engineering case.

## Connection to Agent Systems

Evolutionary thinking also links to current
[[agent engineering]]. Agents can be
taught through minimal task decomposition first, then by distinguishing
sequential flows from manager-agent orchestration and collaborative multi-agent
designs, with collaborative agents that iterate and refine solutions compared to
evolutionary algorithms
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).

The comparison should stay modest. The episode doesn't say every
[[multi-agent-systems|multi-agent system]] is an
evolutionary algorithm. It says collaboration can resemble evolutionary search
when agents generate candidate outputs, exchange feedback, and refine a result.

That comparison applies to complex problems where the input and desired output
are known but the path is detailed
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to LLM Agents]]).
Teams still need a scoring target, a stopping rule, and a compute budget.
