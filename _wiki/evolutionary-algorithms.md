---
layout: wiki
title: "Evolutionary Algorithms"
summary: "How podcast discussions connect evolutionary algorithms to game AI, evolutionary deep learning, prompt search, optimization, and agent systems."
related:
  - Machine Learning
  - Deep Learning
  - Reinforcement Learning
  - Game AI to LLM Agents
  - Agent Engineering
  - Prompt Engineering
  - Evaluation
---

Evolutionary algorithms are search methods for trying candidate solutions when
the target can be scored but not directly derived. The podcast archive connects
them to game AI and numerical optimization. It also connects them to evolutionary
deep learning, prompt search, and modern [[agent-engineering=>AI agents]]
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

As an algorithm family, evolutionary algorithms center on fitness functions,
mutation, and selection. They also cover architecture search, prompt search, and
optimization tradeoffs. For the career and history bridge from game AI into
modern agent workflows, use the related
[[game-ai-to-llm-agents=>Game AI to LLM Agents]] page.

Evolutionary algorithms sit near
[[machine learning]],
[[deep learning]], and
[[reinforcement learning]].
The shared structure is search under feedback. A team defines a fitness signal
and generates candidate solutions. It keeps stronger candidates, then mutates or
combines them until the result converges or the compute budget runs out
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

## Search Mechanics

Genetic algorithms use a population of candidates, a fitness function, a mutation
function, and sometimes a pairing function for combining parents. Fitter
candidates reproduce, random mutations create new variants, and the search
continues until convergence or resource limits
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

The practical tradeoff is compute. Evolutionary algorithms became popular across
many applications because they explore many possible solutions with few hard
constraints, but they're computationally intensive. Around 2006 researchers
treated them as a possible path to intelligence. Later
[[deep learning]]
frameworks became dominant
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

## Game AI and Industry Optimization

Game-like environments come before any generic algorithm catalog. Early academic
work built a game for testing children's executive function. The same work then
used simple neural networks and evolutionary algorithms to create test sequences
and analyze player data
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

The method belongs to a simulated interaction. The team can try candidate tests,
collect behavior, and compare outcomes.

The industrial example is more direct optimization. After oil-and-gas product
work, evolutionary algorithms handled numerical analysis related to pipeline
corrosion. They adapted faster and handled data efficiently. Their compute cost
and weaker fit with the frameworks that boosted deep learning helped push them
aside
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

A broader algorithms-and-optimization toolkit places evolutionary algorithms
alongside graphs. For optimization, it names random sampling, gradient descent,
and simulated annealing. It also names genetic algorithms for permutation
problems
([[cite:algorithms-data-structures-for-engineers=>Practical Algorithms for Engineers]]).

The combined picture is narrow but useful: evolutionary algorithms aren't a
replacement for mainstream
[[machine-learning=>ML]]. They're search techniques
for cases where teams can score candidates and afford repeated trials.

## Evolutionary Deep Learning

The book "Evolutionary Deep Learning" by
[[person:micheallanham=>Micheal Lanham]]
combines deep learning with evolutionary algorithms. The concrete uses include
hyperparameter search and network architecture modification, especially for
convolutional neural networks
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).
Evolutionary algorithms belong to model selection and architecture tuning rather
than everyday supervised modeling.

Weight training is separate from design search: a CNN learns from data, while an
evolutionary method searches over architecture variants or hyperparameters.
These approaches can work well, but they're computationally intensive
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

That makes [[evaluation]]
part of the design problem. Teams need baselines and deployment constraints
before spending compute on architecture or hyperparameter search. They also
need a clear decision the model supports.

## Prompt Search and Generative AI

The most modern example is prompt engineering, where evolutionary algorithms
apply to prompts for LLMs and agents. The system generates prompt variants,
scores the results, and evolves toward prompts that perform better
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).
This is promising because LLM behavior is complex and prompt variants can produce
unexpected outputs.

Prompt search can be computationally expensive. One small example repo may take
about a week
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).
It belongs with the broader
[[prompt engineering]] and
[[LLM evaluation workflows]]
pages. Prompt evolution needs a scoring method, and the compute cost has to buy
better behavior. For the lineage from game environments to LLM agent behavior,
see [[game-ai-to-llm-agents=>Game AI to LLM Agents]].

## APIs and Tooling

EVOL is an API-design example. It's an evolutionary algorithm library built to
simplify genetic algorithms, which often become nested `for` loops. It used
population and evolution objects with a functional API so the algorithm was
easier to use
([[cite:open-source-ml-contributions=>Contribute to Open Source ML]]).

This is about [[open-source=>open-source]]
tool design, not a new theory of evolutionary search. It shows why API design
matters for algorithm families that involve populations, scoring, mutation, and
repeated generations. A clearer API can make the search easier to maintain even
when the underlying method remains compute-heavy.

## Optimization and Decision Systems

Decision optimization sets the boundary by separating prediction from action
selection. A model's `.predict` answers "what will happen." A decision function
answers "what should I do about it." Airline pricing and fraud review thresholds
are examples where business rules combine predicted probabilities with value or
cost
([[cite:machine-learning-decision-optimization=>Optimize Decisions with ML]]).

Evolutionary search sits on that boundary. It can propose or tune candidates,
but the team still needs a fitness function, simulator, or evaluation target.
The same holds from the decision side. Teams simulate different decision rules
and propagate outcomes over time. They rely on domain knowledge rather than a
supervised model that tries to optimize the whole business objective
([[cite:machine-learning-decision-optimization=>Optimize Decisions with ML]]).

A cautionary engineering example comes from laser-system design: genetic
algorithms first, then simple [[reinforcement learning]]
around 2014. The search produced interesting ideas, but some were impractical to
manufacture because the problem was poorly formulated outside the simulation
([[cite:ml-engineering-kpis-and-metrics-strategy=>KPI Design and Metrics Strategy]]).

Search methods can optimize the wrong target when the simulator leaves out
constraints, business objectives, or real-world costs. That laser-system example
gives the decision-optimization boundary a physical engineering case.

## Connection to Agent Systems

Evolutionary thinking also links to current
[[agent engineering]]. Agents can be taught through minimal task decomposition
first, and the episode then distinguishes sequential flows, manager-agent
orchestration, and collaborative multi-agent designs. Collaborative agents can
iterate and refine solutions in a way the guest compares to evolutionary
algorithms
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).

The comparison should stay modest. The episode doesn't say every
[[multi-agent-systems=>multi-agent system]] is an
evolutionary algorithm. It says collaboration can resemble evolutionary search
when agents generate candidate outputs, exchange feedback, and refine a result.

That comparison applies to complex problems where the input and desired output
are known but the path is detailed
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).
Teams still need a scoring target, a stopping rule, and a compute budget.
Lanham's comparison stays narrow: collaborative agents can resemble
evolutionary search without becoming evolutionary algorithms. For the transition
from game AI to LLM agents, see [[game-ai-to-llm-agents=>Game AI to LLM Agents]].
