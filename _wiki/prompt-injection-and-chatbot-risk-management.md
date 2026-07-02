---
layout: wiki
title: "Prompt Injection and Chatbot Risk Management"
summary: "How production chatbot teams manage prompt injection, retrieval abuse, data exfiltration, hallucinations, legal exposure, layered defenses, red-team evaluation, and non-LLM safety classifiers."
related:
  - AI Red Teaming
  - Security
  - LLM Production Patterns
  - Prompt Engineering
  - Responsible AI and Governance
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Data Governance
---

Prompt injection and chatbot risk management cover the ways a
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}) product can be
manipulated or made to leak data. It also covers commitments the product owner
didn't intend. The topic sits near
[security]({{ '/wiki/security/' | relative_url }}) and
[prompt engineering]({{ '/wiki/prompt-engineering/' | relative_url }}). It also
belongs with [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[AI red teaming]({{ '/wiki/ai-red-teaming/' | relative_url }}), and
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) gives the
clearest DataTalks.Club account in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 9:28, she describes a 1,500-person chatbot hacking challenge where
participants tried to bypass restrictions and force prohibited outputs. At
13:20, she explains how a hidden value in a knowledge database was extracted
despite instructions and filtering. Those examples make chatbot risk a system
problem, not only a wording problem inside the prompt.

## Production Boundary

Prompt injection is an attack against the instruction boundary of an
[LLM]({{ '/wiki/llms/' | relative_url }}) application. In Maria's 13:20
data-exfiltration example, users overloaded the chatbot with irrelevant
instructions and dense characters. Some also used crafted API requests or
code-like retrieval attempts. The model ignored the original restriction and
exposed hidden knowledge-base content
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Chatbot risk management is broader than prompt injection. Maria treats unsafe
outputs and hallucinated commitments as one production problem. She puts
retrieval leakage and user trust in the same frame. She also includes legal
exposure and adoption risk.

At 11:38, she discusses chatbots inventing discounts or offers that a company
may have to honor. At 18:01 and 20:39, she links hallucinations and unhelpful
chatbot behavior to reputational damage and user confidence. She also links
those failures to safety and return on investment
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

The whole interaction defines the practical boundary. A production chatbot
needs controls over user influence and model retrieval. It also needs controls
over generated output and uncertain cases. Maria's 16:15 mitigation chapter
names query analysis, output validation, sensitive content classifiers, and
multiple layers of security. Her 25:34 chapter adds human review when the
answer shouldn't go directly to the user
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

## Production Emphases

Maria starts from adversarial trust. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
her 9:28 and 13:20 examples ask whether hostile users can route around bot
restrictions or leak retrieved data. They also test whether the bot can produce
unsafe answers. Her 16:15 and 17:00 mitigation chapters then place defenses
around the model instead of assuming one better prompt will hold.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) starts from
production AI engineering. In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
he argues at 25:27 and 27:45 that examples often work better than long prompt
explanations. At 30:00, he recommends an evaluation dataset with inputs and
expected outputs so teams can see when more examples stop improving behavior.
For chatbot security, that framing turns red-team failures into test cases
rather than treating each incident as a one-off prompt rewrite.

Their emphases differ, but they meet at the same production boundary. Maria
shows why prompt wording isn't enough under attack. Bartosz shows why prompt
changes need measurable evaluation and cost awareness, especially when examples
increase prompt size and serving cost at 29:33-31:45
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})).

## Attack Surface

A production chatbot attack surface includes user input, system instructions,
retrieved context, and output filters. It also includes API routes, logs, and
human handoff. Maria's 13:20 example matters because the hidden value lived in a knowledge
database, not in the user's message. The chatbot retrieved or exposed it after
attackers overloaded the prompt and bypassed a model-based output check
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

That makes [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
part of the risk model. The retrieval system shouldn't fetch documents the
current user isn't allowed to see. The answer generator shouldn't leak
restricted content through summaries or citations. Maria's 13:20 and 16:15
chapters support access-aware retrieval, query analysis, output validation, and
logging as one control set
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

The attack surface also includes the product promises the chatbot appears to
make. At 11:38, Maria gives examples of bots inventing discounts or deals that
create legal and financial exposure. The issue isn't only factual accuracy. A
generated answer can be interpreted as a company commitment
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

## Prompt Injection and Data Exfiltration

Prompt injection works because user-controlled text competes with developer
instructions inside the same model context. Maria explains at 13:34 that
attackers used overload and high-density characters to distract the bot from
its initial rules. Maria also mentions crafted API requests and programmatic
attempts.

The 15:12 recap makes the system boundary explicit. A normal prompt may include
confidentiality rules, and another layer may check the output. Attackers can
still extract data if the model loses the restriction
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Data exfiltration is the business version of that failure. A customer support
bot may read private tickets or internal policy documents. Prompt injection can
then expose information the user should never see. The same risk applies to
tenant data. Maria's 11:38-13:34 hidden knowledge-base challenge shows why
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[security]({{ '/wiki/security/' | relative_url }}) have to constrain retrieval
before the model writes an answer
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

## Hallucinations, Legal Risk, and Adoption

Hallucination risk becomes operational risk when users act on the output or when
the chatbot represents a company. Maria's 11:38 examples of fabricated
discounts and mistaken offers show why a chatbot can create legal or financial
obligations. Her 20:00 and 20:39 mushroom examples show the safety side:
non-experts may trust a plausible answer even when it's dangerous
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Trust and adoption are part of the same risk. At 18:01, Maria says repeated
hallucinations make a bot feel like an untrustworthy assistant. At 20:39, she
argues that inaccurate, verbose, or off-topic chatbot responses can make users
reject an expensive chatbot investment. A production risk review should track
user confidence, escalation rate, and support outcomes, not only model accuracy
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Prompt work can also become an operational sink. Maria warns at 23:19-24:25
that teams can spend large amounts of development time chasing perfect prompts,
only for behavior to change with a model update. Nondeterministic responses can
break the same prompt too.
Bartosz's 30:00 evaluation-dataset advice gives a way to stop that loop. Teams
can test representative inputs and expected outputs, then stop adding examples
when the measured behavior no longer improves
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }})).

## Layered Mitigations

Maria's main mitigation is defense in depth. At 16:15, she recommends analyzing
queries for extraction attempts and validating outputs for confidential
information. She also recommends classifiers that flag or filter sensitive
content. These controls map directly to
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

Input routing and retrieval constraints sit around the model. Output validation,
monitoring, and incident review do too
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Non-LLM classifiers fit where the risk is narrow enough to detect with a
simpler model or rule-like classifier. The 17:00-17:16 exchange explains why a
non-generative classifier can be harder to manipulate than the chatbot. It has
less open-ended behavior to exploit. That makes non-LLM classifiers useful for
sensitive-content detection, extraction-attempt detection, and output blocking.
The LLM can still handle the user conversation
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Human review is another layer, not an admission that the system failed. At
25:34, Maria describes a hybrid workflow where the chatbot drafts or routes an
answer. A human then approves or corrects it before it reaches the user. For
high-risk customer support and finance, the workflow keeps automation useful
while preserving accountable review. The same approach matters in health, safety,
and legal contexts
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

## Evaluation and Red Teaming

Red teaming finds failures that normal product demos miss. Maria's 9:28
challenge asked many people to attack the bot. The later 11:38-16:15 chapters
show the resulting failure categories. They include prohibited outputs and
hidden-data extraction. They also include hallucinated commitments and filter
bypasses
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

Those failures should become regression cases in
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).
Bartosz's production AI testing advice supports that move. At 10:44-14:04 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
he says tests give teams something to rely on while debugging. Snapshot tests
can encode expected behavior from sample inputs. At 30:00, his prompt
evaluation advice applies the same idea to inputs, expected outputs, and
measured improvement.

For a chatbot risk program, the evaluation set should include hostile prompts
and retrieval-abuse attempts. It should also include known sensitive-data
probes and hallucination-prone questions. Cases that should escalate to a human
belong there too.

Maria's 16:15 controls define what passing can mean. The system can block or
refuse the request when the input is unsafe. It can validate the output or route
the answer to review instead of leaking data or inventing an answer
([Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})).

## Related Pages

These nearby pages cover the controls around chatbot security, evaluation,
retrieval, and governance.

- [AI Red Teaming]({{ '/wiki/ai-red-teaming/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
