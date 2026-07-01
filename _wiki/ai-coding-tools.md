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
tools like Cursor, GitHub Copilot, Claude Code, and web-based prototyping tools
like Lovable. In podcast interviews, guests treat these tools as a
practical shift in how AI engineers build products, not as a replacement for
engineering judgment. They discuss productivity gains, workflow changes, and the
risk of building systems you do not understand.

The discussion spans
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) and
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}), where
coding assistants are both a daily tool and an example of embedded agents inside
developer environments.

## The Cursor Workflow

Several guests describe Cursor as their primary coding assistant. In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) explains at
42:05 that he uses Cursor as a paid product for all his work. He recommends it
for anyone coding professionally. Cursor does not generate an entire application
from one prompt, but it helps a lot with smaller functions. If you write the
function signature and docstring, it can generate the rest.

Bartosz compares Cursor with GitHub Copilot at 44:38. He used Copilot when it
first came out and found it great at the time, but considers Cursor much better
now. The key advantage is that Cursor can reference files directly without
copy-paste, and its composer tool can edit multiple files or run command-line
commands. He sticks with Cursor because he already pays for it and has not found
a significantly better alternative.

In
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }}),
[Ruslan Shchuchkin]({{ '/people/ruslanshchuchkin/' | relative_url }}) recommends
Cursor for non-coders because it is more visual. At 1:02:16 he notes that for
coders, specialized tools give you a lot for twenty dollars a month. Alexey
adds that GitHub Copilot at ten dollars a month provides way more than ten
dollars in value.

## Agentic Coding and Notebook Replacement

The shift from notebooks to agentic coding tools changes how AI engineers
organize their work. In
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) explains at
54:23 that creating Streamlit applications or CLI tools has become super cheap.
You can quickly create a Streamlit app for exploring a new model instead of
relying on notebooks. At 55:28 he argues that notebooks are becoming less
relevant for production work, partly because agentic coding tools make other
approaches more practical.

Alexey describes his own rule for agentic coding at 56:37: any code that is not
intended for the report itself goes in .py files next to the notebook. The
notebook ends up being mostly imports and calling helpers. This keeps the
notebook small and makes scripts reusable later. At 56:10 he describes using
Claude Code to eliminate JSON from Jupyter notebooks entirely, producing plain
Python notebooks in about an hour.

## Vibe Coding and Prototyping with AI Dev Tools

Vibe coding is the practice of building applications by prompting AI tools
rather than writing code manually. In
[How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }}),
[Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }}) describes
at 22:15 how her AI Dev Tools bootcamp taught vibe coding. You start with Lovable
to create a UI, give a prompt to create a front end, back end, and database, and
then integrate them. She built a project called Vigilance AI this way and says
it gave her the confidence to convert an idea into a working project.

Ruslan discusses vibe coding in
[Inside the AI Engineer Role]({{ '/podcasts/s23e05-inside-ai-engineer-role-tools-skills-and-career-path/' | relative_url }})
at 1:03:37. He warns that the natural tendency is to let the AI write code
without understanding it. For production systems, he insists on understanding
every single line. For personal projects, he sometimes does not go as deep. His
recommendation is to take time and ask what is happening on every line, rename
things for clarity, and treat the AI-generated code as a learning opportunity.

## Token Management and Prompting Strategies

Running out of tokens is a practical constraint when using coding assistants.
At 58:54 Ruslan recommends using plan mode to avoid burning tokens. Another tip
is to start from templates rather than asking the AI to build a frontend from
scratch. A Next.js template saves many tokens compared to generating every file.
At 59:15 he suggests thinking clearly about what you want to build before
prompting, and using Figma mockups or brainstorm mode to narrow the scope.

At 1:00:19 Ruslan describes using voice mode to dump his brain into the AI for
five minutes, looking at the problem from all perspectives, then asking the AI
to generate a structured summary. He passes that summary as the prompt instead
of spending time carefully phrasing the request himself.

## Embedded Agents in IDEs and Workflows

In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) discusses
embedded agents at 33:14. He describes using Cursor and Devon in Slack, where
you can tag an assistant to update documentation or perform tasks directly.
Bringing agentic systems into normal interfaces will become common. At 35:13 he
traces the evolution from copy-pasting between ChatGPT and the IDE, to code
completion, to agents in IDEs and terminals, and now to background agents that
do code reviews and continuous integration.

At 36:24 Alexey describes creating an issue in GitHub, assigning it to Copilot,
and getting a pull request back in half an hour. Hugo extends this to proactive
agents at 35:45 that tell you when something happens in production or organize
your schedule. He also raises multiplayer agents at 37:13, noting that when
multiple people ping the same agent, it gets confused, and models may need
fine-tuning for multiplayer conversations.

## Learning with AI Instead of Just Coding

A recurring theme is that coding tools double as learning tools. In
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano describes at 52:30 how notebooks have become a place for quick
exploration or reports, while the main pipeline runs as a CLI tool built with
agentic coding. The combination of LLMs and coding agents lets him build
Streamlit apps for reproducibility that used to require notebooks.

In
[AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) describes at 32:17
how he reads everything that AI generates. Since he started using Claude, he
knows a lot more TypeScript and SQL because he is exposed to so many more code
elements. He cares more about how the code should look and scale than about
syntax details like semicolons. This connects to
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}) and
[Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }}), where
the engineer's role shifts toward architecture and review.

## Related Pages

- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [AI Tooling]({{ '/wiki/ai-tooling/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
