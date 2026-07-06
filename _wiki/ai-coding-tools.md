---
layout: wiki
title: "AI Coding Tools"
summary: "How Cursor, Copilot, Claude Code, notebook-to-agent workflows, and human review shape AI-generated code."
related:
  - AI Engineering
  - Agent Engineering
  - Software Engineering
  - AI Tooling
  - Prompt Engineering
  - AI Engineer Role
  - Production
---

AI coding tools are assistants that sit in IDEs, terminals, and repositories.
They use large language models to generate code, complete snippets, refactor
files, and review diffs. Cursor, GitHub Copilot, Claude Code, and web-based
prototyping tools like Lovable all belong here.

These tools are now a practical part of [[AI Engineering]] and
[[Software Engineering]]. They speed up prototypes and help developers move
across stacks. They also make review discipline more important.

Use the codebase as the boundary. Use this page when the assistant changes code,
reads project files, or opens pull requests. It also fits prototypes that turn
an idea into runnable code.

Use [[AI Tooling]] for the broader stack around model APIs and RAG. It also
covers evaluation, deployment, and observability. Use [[Agent Engineering]] when
the main question is planning, tool use, memory, and workflow autonomy rather
than code generation.

For broader daily work, use
[[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
alongside this page. Coding assistants are one case where the prompt, context,
diff, and test result have to stay visible. The same applies to review and
debugging.

## Cursor and Copilot in Daily Coding

In Production AI Engineering, [[person:bartoszmikulski=>Bartosz Mikulski]]
describes Cursor as useful for
professional coding when it's applied to bounded work. It may not generate an
entire application from one prompt, but it can fill in a function from a
signature and docstring. It also sped up his Chrome extension work, even when
the generated code needed correction [[cite:production-ready-ai-engineering@42:05=>Production AI Engineering]].

Cursor fit Bartosz's workflow because it referenced files directly and avoided
copy-paste. Its composer could edit multiple files and run commands [[cite:production-ready-ai-engineering@44:38=>Production AI Engineering]].
He contrasts that with earlier Copilot use. Copilot helped with autocomplete and
refactoring, but it was less integrated with multi-file coding workflows than
Cursor in his current setup [[cite:production-ready-ai-engineering@44:38=>Production AI Engineering]].

For non-coders, [[person:ruslanshchuchkin=>Ruslan Shchuchkin]]
recommends Cursor
because it's visual [[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside AI Engineer Role]].
He also says specialized coding tools and GitHub Copilot can offer strong value
for working developers.

Hugo describes the same progression from copy-pasting between ChatGPT and an IDE
to Copilot, Cursor, IDE agents, and background coding agents. The assistant moves
closer to the repository, pull request, or CI job. The developer can review
concrete diffs instead of detached snippets
[[cite:practical-llm-engineering-and-rag@31:56=>Developer Tools and IDE Agents]]
[[cite:practical-llm-engineering-and-rag@33:14=>Embedded Coding Agents]].
For the broader product-tooling boundary around these assistants, use
[[llm-tools=>LLM Tools for Real Products]].

The workflow is also moving into collaboration surfaces. Coding assistants can
appear in Slack, code review, and background jobs, which makes them closer to
embedded agents than autocomplete tools. That raises the bar for permissions,
traceability, and review.

## Prototypes and Vibe Coding

Vibe coding means prompting an AI dev tool to turn an idea into a prototype. In
the career-break episode, Revathy's version includes a UI plus a backend and
database.
[[person:revathyramalingam=>Revathy Ramalingam]] describes starting with
Lovable for the UI. She then used prompts to assemble a project called Vigilance
AI. That gave her confidence that an idea could become a working artifact [[cite:s23e04-how-to-become-ai-engineer-after-career-break=>Career Break to AI Engineer]].

As portfolio evidence, this belongs with
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]] because
the artifact shows product framing, implementation, and current tool fluency.

This use is mostly prototyping and learning.
In From Notebook to Production, [[person:marianosemelman=>Mariano Semelman]]
gives the caution.

Agentic coding can turn an idea into working code and help with bugs. But he
warns that sustainability is questionable when the developer has no
expertise in the area and relies only on the agent [[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems@29:06=>Notebook to Production]].
That keeps the page's center of gravity on engineering judgment rather than
generic "AI can build anything" advice.

Hugo Bowne-Anderson adds the monitoring version of the same caution: teams need
logs and traces for vibe-coded MVPs. They also need debuggable paths because
LLM output can fail. Retrieval steps and tool calls can break too.
That connects AI coding tools to [[LLM Evaluation Workflows]] and
[[Model Monitoring]], not only to faster prototyping
[[cite:practical-llm-engineering-and-rag@27:38=>Vibe Coding and Monitoring]].

In [[game-ai-to-llm-agents=>Game AI to LLM Agents]], generated game code has to
run and coordinate state. It also has to survive debugging passes. That keeps AI
coding close to [[evolutionary-algorithms=>evolutionary algorithms]] when code
variants are generated and tested against feedback
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]].

Ask the coding assistant to build the debugging surface too. Show traces,
function calls, retrieved context, and intermediate outputs while the MVP is
still small.

## LLMs as Sparring Partners, Accelerators, and Review Targets

LLMs help with more than code generation. In the ML engineering career episode,
[[person:krzysztofszafanek=>Krzysztof Szafanek]] describes using them to get
unstuck and draft code. He also uses them to pressure-test architecture
questions, while still validating platform, permission, and pipeline details
himself [[cite:how-to-grow-your-ml-engineering-career=>Growing an ML Engineering Career]].

That links [[Prompt Engineering]] to [[Software Engineering]] because the prompt
can produce a useful draft. Tests, debugging, and architecture review decide
whether it belongs in the system.

Abouzar Abbaspour makes the same point. LLM assistance can compress coding and
refactoring work [[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park to Tesla]].
But speed doesn't remove responsibility for understanding the product,
deployment path, and data behavior.

Nasser Qadri makes the production bar explicit because code generated by AI
still sits inside software systems. Those systems need
engineering rigor, not just API calls or a working demo [[cite:s23e07-understanding-ai-engineer-role=>AI Engineer Role]].

## Token Management and Prompting Strategies

Ruslan treats token limits as a design constraint in coding sessions. He uses
plan mode, starts from templates, and passes Figma mockups or screenshots. He
also thinks through the build before asking the model to generate files [[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path@61:07=>Inside the AI Engineer Role]].

This is the coding-tools version of [[context-engineering=>Context Engineering]].
The assistant performs better when the developer supplies clear scope, existing
files, and reusable starting points. It performs worse when asked to invent the
whole application from scratch.

Voice mode is another way to gather context. Ruslan uses it to dump several
minutes of problem context. The model's structured summary then becomes the
working prompt [[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path=>Inside the AI Engineer Role]].
The value isn't magic phrasing. The value is getting enough relevant project
state into the assistant.

## Notebooks, CLI Tools, and Streamlit

Agentic coding changes how some data teams organize exploratory work. Mariano
still uses notebooks for quick exploration or reports. Main pipelines or large
evaluations often belong in CLI tools or production scripts. Because agentic
coding makes Streamlit apps and CLIs cheaper to create, teams can move some
notebook work into reusable interfaces [[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

For notebooks, keep report notebooks small. Put analysis logic or functionality
into `.py` files next to the notebook. Then the notebook mostly imports helpers
and shows output [[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].
The episode also gives a concrete Claude Code example. Claude Code removed
Jupyter JSON and produced a plain Python notebook format in about an hour [[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems@56:10=>From Notebook to Production]].

## Embedded Agents in Developer Workflows

Some agents live inside normal interfaces. Hugo mentions Cursor and Devon in
Slack, where a tagged assistant can update documentation or perform tasks. The
sequence starts with copy-pasting between ChatGPT and the IDE. It then moves
through code completion and agents in IDEs or terminals. Background agents now
do code reviews and continuous integration [[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

The [[game-ai-to-llm-agents=>Game AI to LLM Agents]] game-building examples keep
generated code tied to runtime behavior. The code has to coordinate state and
survive debugging passes [[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]].

A GitHub issue can be assigned to Copilot and come back as a pull request within
half an hour. Proactive agents extend this by flagging production events or
organizing a schedule. Multiplayer agents remain a problem. When multiple people
ping the same agent it gets confused, and models may need fine-tuning for
multiplayer conversations. That coordination problem is one bridge to
[[multi-agent-systems=>Multi-Agent Systems]]
[[cite:practical-llm-engineering-and-rag@33:14=>Practical LLM Engineering and RAG]].

## Learning from AI-Generated Code

Developers learn most when they actively review generated code. Ruslan warns
that people tend to let the tool write code without understanding it. For
production systems, the developer should understand every line. They
should ask what's happening and rename things until the code is clear [[cite:s23e05-inside-ai-engineer-role-tools-skills-and-career-path@63:37=>Inside the AI Engineer Role]].

Paul Iusztin gives the same lesson from the AI engineer skill stack. He reads
the code generated by Claude or Cursor. That repeated exposure expanded his
TypeScript and SQL knowledge. It shifted his attention from syntax details to
how code should look and scale [[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]].
Used this way, coding assistants become review targets and learning surfaces,
not just code printers.

For software developers adding ML, that review habit belongs with the
[[software-engineer-to-machine-learning=>software engineer to machine learning]]
transition. Use
[[machine-learning-for-software-engineers=>machine learning for software engineers]]
for the modeling and evaluation work.

## Related Pages

Adjacent topics connect coding tools to AI engineering, software work, and
prompt practice.

- [[AI Engineering]]
- [[Agent Engineering]]
- [[Software Engineering]]
- [[AI Tooling]]
- [[Prompt Engineering]]
- [[AI Engineer Role]]
- [[Production]]
