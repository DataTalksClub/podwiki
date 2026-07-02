---
layout: wiki
title: "AI Coding Tools"
summary: "How DataTalks.Club guests use AI-powered coding assistants like Cursor, Copilot, and Claude Code, the shift from notebooks to agentic workflows, and what vibe coding means for AI engineering practice."
related:
  - AI Engineering
  - Agent Engineering
  - Software Engineering
  - AI Tooling
  - Prompt Engineering
  - Production
---

AI coding tools are IDE-integrated or terminal-based assistants that use large
language models to generate, complete, refactor, and review code. They include
Cursor, GitHub Copilot, Claude Code, and web-based prototyping tools like
Lovable. They are a practical shift in how AI engineers build products, not a
replacement for engineering judgment, and they bring productivity gains,
workflow changes, and the risk of building systems you do not understand.

The topic spans
[[AI Engineering]] and
[[Agent Engineering]], where
coding assistants are both a daily tool and an example of embedded agents inside
developer environments.

## The Cursor Workflow

Cursor works well as a primary coding assistant for professional work. It does
not generate an entire application from one prompt, but it helps a lot with
smaller functions: given a function signature and docstring, it can generate the
rest ([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

Against GitHub Copilot, Cursor's key advantage is referencing files directly
without copy-paste, and a composer tool that can edit multiple files or run
command-line commands; Copilot was strong when it first came out but Cursor is
now considered much better
([[podcast:production-ready-ai-engineering|Production AI Engineering]]).

For non-coders, Cursor is recommended because it is more visual; for coders,
specialized tools give you a lot for twenty dollars a month, and GitHub Copilot
at ten dollars a month provides far more than ten dollars in value
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## Agentic Coding and Notebook Replacement

The shift from notebooks to agentic coding tools changes how AI engineers
organize their work. Creating Streamlit applications or CLI tools has become
very cheap: a Streamlit app can be spun up for exploring a new model instead of
relying on notebooks. Notebooks are becoming less relevant for production work,
partly because agentic coding tools make other approaches more practical
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

One rule for agentic coding: any code not intended for the report itself goes in
.py files next to the notebook, so the notebook ends up mostly imports and calls
to helpers, staying small while the scripts stay reusable. Claude Code can strip
JSON out of Jupyter notebooks entirely, producing plain Python notebooks in
about an hour
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

## Vibe Coding and Prototyping with AI Dev Tools

Vibe coding is building applications by prompting AI tools rather than writing
code manually. An AI Dev Tools bootcamp taught it by starting with Lovable to
create a UI, prompting for a front end, back end, and database, then integrating
them; a project called Vigilance AI built this way gave the confidence to
convert an idea into a working project
([[podcast:s23e04-how-to-become-ai-engineer-after-career-break|How to Become an AI Engineer After a Career Break]]).

The natural tendency is to let the AI write code without understanding it. For
production systems, every single line should be understood; for personal
projects, less depth is acceptable. The recommendation is to ask what is
happening on every line, rename things for clarity, and treat AI-generated code
as a learning opportunity
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## Token Management and Prompting Strategies

Running out of tokens is a practical constraint. Plan mode avoids burning
tokens, and starting from templates rather than generating a frontend from
scratch saves many tokens, since a Next.js template avoids generating every
file. Thinking clearly about what to build before prompting, and using Figma
mockups or brainstorm mode to narrow scope, further reduces waste
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

Voice mode can dump a brain-worth of context into the AI over five minutes,
looking at the problem from all perspectives, after which the AI generates a
structured summary that becomes the prompt, instead of carefully phrasing the
request by hand
([[podcast:s23e05-inside-ai-engineer-role-tools-skills-and-career-path|Inside the AI Engineer Role]]).

## Embedded Agents in IDEs and Workflows

Embedded agents live inside normal interfaces: Cursor and Devon in Slack, where
an assistant is tagged to update documentation or perform tasks directly. The
evolution runs from copy-pasting between ChatGPT and the IDE, to code
completion, to agents in IDEs and terminals, and now to background agents that
do code reviews and continuous integration
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A GitHub issue can be assigned to Copilot and come back as a pull request within
half an hour. Proactive agents extend this by flagging production events or
organizing a schedule. Multiplayer agents remain a problem: when multiple people
ping the same agent it gets confused, and models may need fine-tuning for
multiplayer conversations
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

## Learning with AI Instead of Just Coding

Coding tools double as learning tools. Notebooks become a place for quick
exploration or reports, while the main pipeline runs as a CLI tool built with
agentic coding, and LLMs plus coding agents replace notebooks with Streamlit
apps for reproducibility
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).

Reading everything the AI generates builds knowledge: sustained use of Claude
teaches more TypeScript and SQL through exposure to many more code elements,
shifting attention toward how code should look and scale rather than syntax
details like semicolons
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]]).
This connects to
[[Software Engineering]] and
[[Prompt Engineering]], where
the engineer's role shifts toward architecture and review.

## Related Pages

- [[AI Engineering]]
- [[Agent Engineering]]
- [[Software Engineering]]
- [[AI Tooling]]
- [[Prompt Engineering]]
- [[Production]]
</content>
