---
layout: article
tags: ["transition"]
title: "Game AI to LLM Agents"
summary: "How Micheal Lanham connects game AI, reinforcement learning, multi-agent workflows, support assistants, and modern LLM agents."
related_wiki:
  - Agent Engineering
  - Multi-Agent Systems
  - Reinforcement Learning
  - Evolutionary Algorithms
  - Prompt Engineering
---

Game AI to LLM agents connects older game and simulation techniques to modern
[[agent-engineering=>agent engineering]]. The bridge runs through state and
action modeling, feedback, search, and evaluation. Game systems model behavior
inside an environment. Modern agents add language, tools, handoffs, and support
workflows.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

[[person:micheallanham=>Micheal Lanham]] treats LLM agents as a continuation of
older AI problems rather than a clean break. Teams still define objectives and
decompose behavior. They also search over alternatives, coordinate actors, and
evaluate whether the system behaved consistently.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Lanham's career and history bridge treats evolutionary algorithms as one search
tradition. He places them alongside game AI and reinforcement learning, plus
simulation and agent orchestration. For fitness functions and mutation, use
[[evolutionary-algorithms=>Evolutionary Algorithms]]. For architecture search,
prompt search, and optimization tradeoffs, use the same algorithm-family hub.

## Behavior Under Feedback

The shared idea across game AI, reinforcement learning, evolutionary search,
and LLM agents is behavior under feedback. A system presents tasks or possible
actions, observes outcomes, and uses those outcomes to choose the next
attempt.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

For LLM agents, that feedback loop now sits inside software workflows. Agents
can retrieve information, call tools, and hand work to other agents. They can
also produce user-facing results. The design still depends on objectives, task
boundaries, and evaluation.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## From Games and Simulation to Agent Workflows

The game-AI side starts with interaction environments, not chatbots. In one
academic project, a game tested children's executive functions. Simple neural
networks and evolutionary algorithms generated patterns, then analyzed player
behavior.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Lanham's augmented reality, Unity, sound-design, and Python game-development
work reinforce the same engineering structure. Games force designers to model
state, actions, feedback, and simultaneous behavior. Those concerns transfer to
[[agent engineering]].[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Reinforcement Learning and Search Traditions

[[Reinforcement learning]] kept older agent vocabulary in view. Goals,
behavior, feedback, and environments existed before LLM systems made "agent" a
product term.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Evolutionary deep learning adds search through hyperparameter tuning and
architecture changes.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
For that algorithmic side, use
[[evolutionary-algorithms=>Evolutionary Algorithms]]. In Lanham's story,
evolutionary deep learning mainly shows how older search traditions stayed
relevant as he moved toward modern agents.

The connection to LLM agents isn't that every agent uses RL or evolutionary
training. Many agent problems still look like search under feedback. The system
generates candidates, scores behavior, and refines the next attempt.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Evolutionary Prompting and LLM Behavior

Teams can use evolutionary algorithms to search for prompt variants that
produce better LLM or agent outputs. That connects evolutionary methods
directly to [[prompt engineering]].[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
Prompt engineering then sits near older optimization work.

Prompts become candidates, model outputs become observable behavior, and
teams evaluate which candidates survive. In the Game AI lineage, evolutionary
prompting shows how older search ideas still appear in agent work.
For the prompt-search mechanics, use
[[evolutionary-algorithms=>Evolutionary Algorithms]].

Evolutionary prompt search can be computationally expensive. Prompt variations
can also expose unexpected LLM behavior.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
The game-AI lineage doesn't remove production discipline. It increases the need
for evaluation, cost control, and clear task boundaries.

## Multi-Agent Design: Flow, Orchestration, Collaboration

Multi-agent work stays more tractable when each agent stays lean. Loading one
agent with too many tools and instructions makes the system harder to reason
about. Task-specific agents keep the workflow decomposed.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
That makes this topic a concrete companion to
[[multi-agent-systems=>Multi-Agent Systems]] and
[[Agent Engineering]].

The episode distinguishes three coordination designs. In a flow, requirements
agents pass work to planning agents, and planning agents pass work to execution
agents.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

In orchestration, a front-facing manager agent calls other agents, checks their
outputs, and loops back when the work no longer matches requirements.
Collaboration uses a shared message channel where agents exchange
outputs.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Collaboration can be powerful, but it's also expensive and weak for real-time
responses.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## Support Assistants and Agent Tooling

Support assistants give the bridge a production target. Multi-agent support
systems can include deep-research operator agents and other advanced
tools.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
The game-AI lineage moves into support workflows.

Agents move from simulated actors into software components that help users with
investigation, planning, retrieval, and action.

The OpenAI Agent SDK supports guardrails and handoffs. MCP servers and
sequential-thinking scratchpads sit nearby in the tooling stack.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
Scratchpad-style reasoning and inter-agent communication are different
surfaces. Agents usually pass results to one another instead of every private
reasoning step.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

## NPC Behavior, Game Building, and Generated Worlds

The NPC thread is narrow because the episode doesn't present a complete NPC
architecture. Generative AI could eventually produce more competent AI
opponents. It could also generate levels, quests, challenges, and whole playable
experiences from prompts.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

The coding-agent examples are narrower and more immediate. LLMs can generate a
Spider Solitaire game, and a stronger model can produce a complete React
implementation after bug-fix iterations.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

The Space Invaders example adds harder game constraints. The model has to
handle bullet physics, collision logic, and simultaneous movement.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Game development stress-tests modern LLM agents because output must compile,
run, coordinate state, and feel playable.

## Evaluation Keeps the Bridge Honest

Agent systems need feedback mechanisms to assess performance consistency and
understand output variance. Production applications also need evaluation
pipelines, variable control, behavior explanation, and monitoring tools such as
Arize Phoenix.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Games and RL supply mental models for action and feedback. Evolutionary
algorithms add a search lens. Modern [[agent-engineering=>LLM agents]] add
language, tools, orchestration, and support workflows. The engineering problem
is to keep the system small enough to evaluate. It still needs enough
coordination, tooling, and feedback to act usefully.

## Related Pages

The closest companion pages are:

- [[Agent Engineering]]
- [[Multi-Agent Systems]]
- [[Reinforcement Learning]]
- [[Evolutionary Algorithms]]
- [[Prompt Engineering]]
