---
layout: wiki
title: "AI Coding Tools"
summary: "How guests use Cursor, Copilot, Claude Code, notebook-to-agent workflows, and human review for AI-generated code."
related:
  - AI Engineering
  - Agent Engineering
  - Software Engineering
  - AI Tooling
  - Prompt Engineering
  - AI Engineer Role
  - Production
---

AI coding tools are IDE-integrated or terminal-based assistants that use large
language models to generate, complete, refactor, and review code. Cursor,
GitHub Copilot, Claude Code, and web-based prototyping tools like Lovable all
belong here. They're a practical shift in how AI engineers build products, not a
replacement for engineering judgment. They bring productivity gains, workflow
changes, and the risk of building systems you don't understand.

The topic spans [[AI Engineering]] and [[Agent Engineering]]. Coding assistants
are both a daily tool and an example of agents embedded inside developer
environments.

## The Cursor Workflow

Cursor can serve as a primary coding assistant for professional work. It doesn't
generate an entire application from one prompt, but it helps with smaller
functions. Given a function signature and docstring, it can generate the rest
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

Against GitHub Copilot, Cursor's key advantage is referencing files directly
without copy-paste. Its composer can edit multiple files or run command-line
commands. Copilot was strong when it first came out, but Cursor is now
considered much better
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

For non-coders, Cursor is recommended because it's more visual. For coders,
specialized tools give you a lot for twenty dollars a month. GitHub Copilot at
ten dollars a month provides far more than ten dollars in value
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## Agentic Coding and Notebook Replacement

The shift from notebooks to agentic coding tools changes how AI engineers
organize their work. Creating Streamlit applications or CLI tools has become
cheap enough that a Streamlit app can explore a new model instead of relying on
notebooks. Notebooks are becoming less relevant for production work, partly
because agentic coding tools make other approaches more practical
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

With agentic coding, keep report notebooks small. Put any code not intended for
the report in `.py` files next to the notebook. Then use the notebook mostly
for imports and helper calls, while the scripts stay reusable. Claude Code can
strip JSON out of Jupyter notebooks entirely, producing plain Python notebooks
in about an hour
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

## Vibe Coding and Prototyping with AI Dev Tools

Vibe coding means prompting AI tools to build applications instead of writing
code manually. An AI Dev Tools bootcamp taught it by starting with Lovable to
create a UI
([[podcast:s23e04-how-to-become-ai-engineer-after-career-break|Career Break to AI Engineer]]).
It then prompted for a front end, back end, and database before integrating
them. Building Vigilance AI this way gave the confidence to convert an idea into
a working project.

The natural tendency is to let the AI write code without understanding it. For
production systems, every single line should be understood. For personal
projects, less depth is acceptable. When using AI-generated code, ask what's
happening on every line. Rename things for clarity and treat the generated code
as a learning opportunity
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## LLMs as Sparring Partners, Accelerators, and Review Targets

LLMs can start code from a blank screen. They can also pressure-test
architecture questions about platforms, permissions, and pipeline design. The
caveat is that confident answers still need an engineer who can validate the
details. That matters most when the answer is hard to check with a normal search
[[cite:how-to-grow-your-ml-engineering-career|Growing an ML Engineering Career]].

This connects [[Prompt Engineering]] to [[Software Engineering]]. The prompt can
produce a useful draft, but tests, review, and architecture judgment decide
whether generated code belongs in the system.

LLM assistance can compress multi-day coding work
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling to Tesla Data Engineering]].
It helps most with code generation and refactoring. It also helps with
documentation and platform support. The risk is treating that speed as proof
that AI can solve every engineering problem.

Code needs review before shipping
[[cite:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]].
A prototype can seem to work while hiding data, migration, or architecture
mistakes. For production-facing systems, responsible use means asking the tool
for the patch. Then check access paths and tests. Also check operating impact
and long-term code quality.

Depth matters before breadth in [[AI Tooling]] and [[Agent Engineering]]
[[cite:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]].

Start with one known framework or code assistant. Build enough judgment to
compare alternatives later for a specific use case or vendor constraint. Coding
assistants follow the same approach. Broad tool awareness is useful, but the
productivity gain comes from knowing how one tool edits files. It also comes
from knowing how that tool uses context, runs commands, and fails.

## Token Management and Prompting Strategies

Running out of tokens is a practical constraint. Plan mode avoids burning
tokens, and starting from templates rather than generating a frontend from
scratch saves many tokens. A Next.js template avoids generating every file.
Thinking clearly about what to build before prompting also reduces waste. Figma
mockups or brainstorm mode can narrow scope
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

Voice mode can dump a brain-worth of context into the AI over five minutes,
looking at the problem from several perspectives. The AI then generates a
structured summary that becomes the prompt, instead of requiring careful phrasing
by hand
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## Embedded Agents in IDEs and Workflows

Some agents live inside normal interfaces, and Cursor and Devon can run in
Slack. An assistant can be tagged to update documentation or perform tasks
directly. The progression starts with copy-pasting between ChatGPT and the IDE.
It moves through code completion and agents in IDEs or terminals. Background
agents now do code reviews and continuous integration
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A GitHub issue can be assigned to Copilot and come back as a pull request within
half an hour. Proactive agents extend this by flagging production events or
organizing a schedule. Multiplayer agents remain a problem. When multiple people
ping the same agent it gets confused, and models may need fine-tuning for
multiplayer conversations
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

## Learning with AI Instead of Just Coding

Coding tools double as learning tools. Notebooks become a place for quick
exploration or reports, while the main pipeline runs as a CLI tool built with
agentic coding. LLMs plus coding agents can replace notebooks with Streamlit
apps when reproducibility matters
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

Reading everything the AI generates builds knowledge. Engineers who use Claude
over time see more TypeScript and SQL code elements. That shifts attention
toward how code should look and scale rather than syntax details like semicolons
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
This connects to [[Software Engineering]] and [[Prompt Engineering]], where the
engineer's role shifts toward architecture and review.

## Related Pages

These pages cover the surrounding engineering, tooling, and production topics.

- [[AI Engineering]]
- [[Agent Engineering]]
- [[Software Engineering]]
- [[AI Tooling]]
- [[Prompt Engineering]]
- [[AI Engineer Role]]
- [[Production]]
