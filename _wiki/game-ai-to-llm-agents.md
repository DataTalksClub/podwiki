---
layout: wiki
title: "Game AI to LLM Agents"
summary: "How Micheal Lanham connects game AI, reinforcement learning, evolutionary algorithms, multi-agent workflows, NPC behavior, support assistants, and modern LLM agents."
related:
  - AI Agents
  - Agent Engineering
  - Multi-Agent Systems
  - Reinforcement Learning
  - Evolutionary Algorithms
  - Prompt Engineering
---

Game AI to LLM agents links older game and simulation ideas to modern
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}). It also brings search
and optimization ideas into agent workflows. The grounding episode is
[From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
In it,
[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) traces that
lineage from game-like cognitive testing and evolutionary methods to current
work on multi-agent support assistants.

The episode doesn't treat LLM agents as a clean break from earlier AI. Lanham's
view is that modern agent work inherits familiar problems. Teams still define
objectives and decompose behavior. They also search over alternatives,
coordinate actors, and evaluate whether the system behaved consistently
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
2:36-5:28 and 57:39-58:04).

## From Games and Simulation to Agent Workflows

Lanham's starting point isn't a chatbot. He describes early academic work where
a team built a game to test children's executive functions. The team used simple
neural networks and evolutionary algorithms to generate patterns and analyze
player behavior
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
2:36-2:55). In [Lanham's]({{ '/people/micheallanham/' | relative_url }})
example, game AI works as an interaction environment. A system presents tasks,
observes behavior, and adjusts what happens next.

The same game background reappears in Lanham's work on augmented reality and
Unity. It also shows up in his sound-design and Python game-development
teaching
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
5:45-7:36 and 19:42-20:23). The bridge is engineering structure rather than
genre. Games force designers to model state, actions, feedback, and simultaneous
behavior. Those are also core concerns in
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}).

## Reinforcement Learning and Search Traditions

Lanham places his move into
[reinforcement learning]({{ '/wiki/reinforcement-learning/' | relative_url }})
after game and signal-analysis work. In the interview, he names Alberta.
He also names
Richard Sutton as part of the research context that introduced him to RL
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
8:01-8:45). That [Lanham]({{ '/people/micheallanham/' | relative_url }})
background matters because older agent vocabulary already had goals, behavior,
feedback, and environments before LLM systems made "agent" a product term.

Lanham then returns to evolutionary methods through evolutionary deep learning.
He describes using evolutionary algorithms for hyperparameter search and
network architecture modification, especially around convolutional neural
networks
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
9:09-9:29). The bridge to LLM agents isn't that every agent is trained with RL
or evolutionary search. In [Lanham's]({{ '/people/micheallanham/' | relative_url }})
discussion, many agent problems still look like search under feedback. The
system generates candidates, scores behavior, and refines the next attempt.

## Evolutionary Prompting and LLM Behavior

The most direct connection from evolutionary algorithms to LLMs appears in the
prompt-engineering part of the interview. Lanham says recent systems use
evolutionary algorithms to evolve prompts for LLMs and agents. The search looks
for variants that produce better outputs
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
14:09-14:28). In [Lanham's]({{ '/people/micheallanham/' | relative_url }})
framing, [prompt engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
sits near older optimization work.

Prompts become candidates, model outputs become observable behavior, and
evaluation decides which candidates survive.

Lanham also keeps the tradeoff visible. He calls evolutionary prompt search
computationally expensive and notes that prompt variations can expose
unexpected LLM behavior
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
14:28-17:58). [Lanham's]({{ '/people/micheallanham/' | relative_url }})
game-AI lineage doesn't remove the need for ordinary production
discipline. It increases the need for evaluation, cost control, and clear task
boundaries.

## Multi-Agent Design: Flow, Orchestration, Collaboration

Lanham's strongest practical guidance is to keep agents lean. He warns against
loading one agent with too many tools and instructions. He recommends breaking
the workflow into tasks for individual agents
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
20:49-20:57). [Lanham's]({{ '/people/micheallanham/' | relative_url }})
advice makes this topic a concrete companion to
[Multi-Agent Systems]({{ '/wiki/multi-agent-systems/' | relative_url }}) and
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}).

He distinguishes three coordination designs. In a flow, requirements agents pass
work to planning agents. Planning agents then pass work to execution agents
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
23:48).

In [Lanham's]({{ '/people/micheallanham/' | relative_url }})
orchestration design, a front-facing manager agent calls other agents. It
checks their outputs and loops back when the work no longer matches requirements
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
25:20 and 30:09). Lanham also describes collaboration, where agents exchange
outputs through a shared message channel.

He calls collaboration powerful, but
expensive and weak for real-time responses
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
26:25-29:05).

## Support Assistants and Agent Tooling

Lanham's present-day work gives the bridge a production target. He says he's
building AI support assistants powered by multiple agents. The work includes
deep research operator agents and other advanced tools
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
5:28). In [Lanham's]({{ '/people/micheallanham/' | relative_url }}) example,
the game-AI lineage moves into support workflows.

Agents move from simulated actors into software components that help users with
investigation, planning, retrieval, and action.

For implementation, Lanham references the OpenAI Agent SDK because it supports
guardrails and handoffs. He also connects agent workflows to MCP servers and
sequential-thinking scratchpads
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
31:31-33:25). [Lanham]({{ '/people/micheallanham/' | relative_url }})
separates scratchpad-style reasoning from inter-agent communication. Agents
usually pass results to one another instead of every private reasoning step
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
34:03).

## NPC Behavior, Game Building, and Generated Worlds

The NPC thread in this episode is narrow because Lanham doesn't present a
complete NPC architecture. He does argue that generative AI could eventually
produce more competent AI opponents in games
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
41:14). [Lanham]({{ '/people/micheallanham/' | relative_url }}) also imagines
generative systems creating levels and quests. He also includes challenges and
whole playable experiences from prompts
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
38:57-40:57).

The practical coding-agent examples are narrower and more immediate. Lanham
describes asking LLMs to build a Spider Solitaire game. He later used a
stronger model to produce a complete React implementation after bug-fix
iterations
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
36:29-38:45).

The Space Invaders example adds hard game-implementation
constraints. The model has to handle bullet physics, collisions, and
simultaneous movement
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
41:42-42:46). In [Lanham's]({{ '/people/micheallanham/' | relative_url }})
conversation, game development becomes a stress test for modern LLM agents. The
output must compile, run, coordinate state, and feel playable.

## Evaluation Keeps the Bridge Honest

Lanham closes the technical arc with evaluation and monitoring. He says agent
systems need feedback mechanisms to assess performance consistency and
understand output variance
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
57:39). For production applications,
[Lanham]({{ '/people/micheallanham/' | relative_url }}) emphasizes evaluation
pipelines and variable control. He also emphasizes behavior explanation and
monitoring tools such as Arize Phoenix
([From Game AI to LLM Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}),
58:04).

That's the durable lesson of the game-AI-to-agent bridge. Games and RL supply
useful mental models for action and feedback, while evolutionary algorithms add
a search lens. Modern [LLM agents]({{ '/wiki/ai-agents/' | relative_url }}) add
language, tools, orchestration, and support workflows. The engineering problem
is to keep the system small enough to evaluate while still giving it enough
coordination, tooling, and feedback to act usefully.
