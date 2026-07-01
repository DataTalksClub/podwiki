---
layout: wiki
title: "Reinforcement Learning"
summary: "How DataTalks.Club podcast guests discuss reinforcement learning through agents, rewards, simulators, games, robotics, autonomous driving, optimization, and practical limits."
related:
  - Machine Learning
  - AI Agents
  - Agent Engineering
  - Multi-Agent Systems
  - Evolutionary Algorithms
  - Computer Vision
  - Metrics
  - Machine Learning System Design
---

DataTalks.Club guests use reinforcement learning to reason
about agents that act. They also use it to discuss objectives and environments
where the cost of experimentation matters. Guests rarely treat it as a
standalone algorithm menu.

They use it to explain why games and simulations make agent learning easier.
They also use it to show why robotics and autonomous driving need constraints.
Business teams often choose simpler optimization or experimentation methods
when they don't have a reliable simulator.

For a structured introduction to the topic, the [Reinforcement Learning]({{ '/books/20210111-reinforcement-learning/' | relative_url }}) Book of the Week by Phil Winder covers industrial applications and the practical boundary between simulated environments and real-world deployment.
[Grokking Deep Reinforcement Learning]({{ '/books/20210517-grokking-deep-reinforcement-learning/' | relative_url }})
by Miguel Morales is a complementary learning path: it builds intuition for Q-learning, policy gradients, and actor-critic methods through annotated code and visual walkthroughs.

Start with
[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }})
for the historical path from game AI and reinforcement learning to modern
agents. Pair that with
[Dan Becker]({{ '/people/danbecker/' | relative_url }}) in
[Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }})
for the practical boundary. Reinforcement learning needs an environment where
you can try actions and observe outcomes. For deployed physical systems, use
[Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }}) in
[Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})
to separate perception from behavior in robotics and self-driving systems.

## Agents, Objectives, and Modern Agent Language

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) gives the
cleanest bridge between older reinforcement-learning agents and current
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}). In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
the conversation compares current agent language with reinforcement-learning
courses from the early 2010s. At 12:01, Ranjitha says the older agent was
tasked with completing a goal or objective. Teams tuned it to improve
performance against an objective function.

At 12:31, she moves to LLM agents. They still act toward a task, but they
orchestrate LLM calls.

They also use tools, memory, and knowledge stores.

That bridge matters because reinforcement learning and
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}) share the
language of goals, actions, and feedback. They don't share the same
implementation default. A reinforcement-learning agent usually learns by
interacting with an environment. A modern LLM agent may plan, call tools, or
retrieve context without training a policy through trial and error. Guests keep
that distinction visible instead of treating every autonomous workflow as
reinforcement learning.

Lanham adds the historical arc. At 8:01 in
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
he describes moving from sound design and waveform work into reinforcement
learning. He names the University of Alberta as an important research center.

At 9:09, he says he wrote reinforcement-learning and deep-learning books before
returning to [evolutionary algorithms]({{ '/wiki/evolutionary-algorithms/' | relative_url }}).
That path explains why his later discussion of
[multi-agent systems]({{ '/wiki/multi-agent-systems/' | relative_url }})
doesn't start from chatbots. It starts from games, simulation, search, and
agents that act inside a constrained world.

## Simulators Decide What Is Feasible

Becker sets the strongest practical boundary for reinforcement learning. In
[Optimize Decisions with ML]({{ '/podcasts/machine-learning-decision-optimization/' | relative_url }}),
he contrasts prediction with deciding what to do next. At 21:58, he describes
reinforcement learning as optimizing an objective in a complex environment. He
also says the best-known breakthroughs, including game systems such as AlphaGo
and OpenAI's Dota agent, worked in settings with simulators.

The same episode explains why many business problems stop short of full
reinforcement learning. At 23:03, Becker says teams need simulators for
dynamic real-world environments. A supervised model can't optimize a broader
objective alone. At 24:27, he says teams often encode known rules inside a
decision function and combine those rules with machine-learning predictions.
This links reinforcement learning to
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

A deployed system may contain predictions and rules. It may also include
constraints and a simulator-like evaluation layer even when no reinforcement
learner is trained.

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) makes the same
constraint concrete from the metrics side. In
[KPI Design and Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}),
he says at 56:35 that reinforcement learning is useful when a team has a good,
cheap simulator. He adds that this case is rare. When historical data is useful
and the team's actions don't strongly change the world, he uses backtesting as
a more practical option. That keeps reinforcement learning close to
[metrics]({{ '/wiki/metrics/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
decision evaluation rather than treating it as a universal optimizer.

## Rewards Need Measurement

Sroka's laser-design story shows why reward design isn't separate from
measurement. At 2:22 in
[KPI Design and Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}),
he says he used reinforcement learning while designing laser components during
his computational physics doctorate. At 9:00, he explains the setup. He had
ray-tracing software and MATLAB automation, then attached a rudimentary
reinforcement-learning search routine to explore component parameters.

Sroka doesn't argue that every physical-design problem should use
reinforcement learning. He says the system produced interesting designs, but
some were poorly formulated or impractical to manufacture. At 12:06, he turns
that into a metrics lesson.

Laser design has threshold metrics for power and beam geometry. It also has
thresholds for operating temperature, pulse length, and safety standards. A
reinforcement learner can search for a system that hits those thresholds.

The harder problem is comparing many acceptable solutions and weighting the
metrics into a merit function.

[Loris Marini]({{ '/people/lorismarini/' | relative_url }}) adds a second
research example in
[Practical Skills for Data Professionals in SaaS]({{ '/podcasts/data-professionals-business-skills-in-saas/' | relative_url }}).
At 8:30, he describes using reinforcement learning for a hard optimization
problem. Actors took competing actions until a network converged to a
near-optimal solution in a small number of iterations.

Use this example narrowly because reinforcement learning becomes useful only
when the team can define actors and actions. The team also needs effects and a
convergence target. Without that structure, the method has no clear reward to
learn from.

## Robotics and Autonomous Driving Need Constraints

Jadhav separates the perception and behavior parts of autonomous systems. In
[Applying Computer Vision Research]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}),
she says at 45:37 that her first interaction with reinforcement learning was
through college robotics. Reinforcement learning remains important in robotics.
At 45:55, she defines the split. Computer vision helps the agent understand the
world, while reinforcement learning teaches the agent how to
behave in that world.

That split keeps reinforcement learning connected to
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}) without
collapsing the two topics. A self-driving stack needs perception models that
detect lanes, obstacles, traffic signals, and gestures. It may also need
behavior policies, planning, and control. Jadhav says at 46:31 that she works
mostly on perception, not the reinforcement-learning part.

The autonomous-driving discussion also shows why physical-world reinforcement
learning needs guardrails. At 47:56, Jadhav says training environments still
impose rules such as not driving against traffic. At 49:24-51:02, she contrasts
fixed-rule games like chess and Go with self-driving environments that change
across cities, countries, and driving cultures. The car can't freely explore
the real world. It needs constraints, simulation, controlled testing, and
staged validation before it can act around people.

## Explore, Exploit, or Use Something Simpler

Guests also describe simpler methods when the problem only needs a
limited version of reinforcement-learning thinking. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) discusses the
explore-exploit tradeoff at 45:49. He brings up Thompson sampling for the
multi-armed bandit problem and calls it much simpler to implement than a full
reinforcement-learning neural network.

Product and MLOps teams need that distinction. A bandit can help choose between
options when the action space is small and feedback arrives quickly. A full
reinforcement-learning setup needs a richer state, action, reward, and
environment model. Becker's decision-optimization episode and Sroka's metrics
episode both give the same practical sequence.

Start from the decision, the metric, and the evaluation surface. Use
reinforcement learning only when the team can define an objective, run many
trials safely, and trust the environment used for learning.

For the broader machine-learning context, use
[Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}). For
production agents that use LLMs and tools, use
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) and
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}). Those pages also cover
retrieval and memory. For game-derived agent design and collaboration
structures, use
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) and
[Evolutionary Algorithms]({{ '/wiki/evolutionary-algorithms/' | relative_url }}).
