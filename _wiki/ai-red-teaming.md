---
layout: wiki
title: "AI Red Teaming"
summary: "How DataTalks.Club podcast guests frame AI red teaming as adversarial testing for prompt injection, data exfiltration, unsafe outputs, and agent abuse."
related:
  - Security
  - Responsible AI and Governance
  - Generative AI
  - LLM Evaluation Workflows
---

AI red teaming is adversarial testing for AI systems. Teams use it to find ways
that an AI product can fail under hostile input. The product might leak data,
follow a malicious instruction, hallucinate a risky answer, or act outside the
boundary the team intended.

DataTalks.Club guests anchor this topic in production systems, not only
model benchmarks. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) describes a
large chatbot hacking exercise at 9:28. Participants tried to make a restricted
assistant reveal hidden knowledge-base content and produce answers the product
should block. In that example, red teaming tests
[security]({{ '/wiki/security/' | relative_url }}) failures in
[LLMs]({{ '/wiki/llms/' | relative_url }}) and
[generative AI]({{ '/wiki/generative-ai/' | relative_url }}) products.

## Adversarial Test Scope

DataTalks.Club guests define AI red teaming as attacking the deployed AI
product before customers, employees, or malicious users discover the same
failures.

For a chatbot, the test target includes the prompt and retrieved documents. It
also includes output filters, the user interface, and the handoff path. Maria's
13:20 chapter in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }})
covers overloaded prompts and knowledge-base retrieval as data-exfiltration
paths. The model is only one part of the system. A red-team exercise has to
test the whole [retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
flow when the assistant can read private or semi-private content.

For agents, the target grows to include tools, memory, and logs. It also
includes permissions and automation boundaries.

In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) connects
enterprise agents to guardrails and auditability at 30:26. He also ties them
to lineage and compliance. Later, at 43:30 and 50:18, he connects evaluation to
golden datasets and LLM judges. He also brings in human labels and scale. Red
teaming fits that same engineering discipline because adversarial examples
become evaluation cases the next version must pass.

## Risk Lenses Across Chatbots, Agents, and Governance

Guests agree that AI systems need adversarial testing, but they start from
different risks.

Maria starts from user-facing chatbot abuse, and her episode focuses on prompt
injection and hidden-content extraction. It also covers hallucinated commitments
and layered defenses. At 16:15 and 17:00 in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
she discusses output validation, query analysis, and non-LLM classifiers. Her
view fits production LLM systems where a team needs controls around the model,
retrieval system, and product surface.

Aditya starts from agent reliability and enterprise deployment. In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
the 13:13 chapter discusses reliability in legal and healthcare settings. The
56:40 chapter covers deployment risks. His framing pushes red teaming toward
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}).

Teams have to test whether someone can game the agent, trigger the wrong tool,
bypass a guardrail, or create failures that only appear at scale.

[Supreet Kaur]({{ '/people/supreetkaur/' | relative_url }}) starts from
responsible AI and governance. In
[Responsible & Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }}),
she distinguishes explainable AI from responsible AI at 8:20. At 14:39 and
17:20, she discusses PII handling and feature necessity. She also brings in
product owners, subject matter experts, and compliance. Her view matters when
red-team findings require policy decisions, not only technical filters.

## Prompt Injection and Unsafe Outputs

LLM red teaming tests whether a system can keep its instructions, data, and
output boundaries under hostile input. In Maria's chatbot episode, the 9:28
challenge shows why normal demos don't provide enough evidence. A demo usually
shows the assistant answering intended questions. Red teaming asks whether the
assistant can be pushed into revealing instructions, leaking retrieved content,
or giving unsafe advice.

Prompt injection is one failure mode. A user can add instructions that compete
with the system prompt or ask the model to ignore the product rules. Documents
retrieved by the system can also include hostile text. That's why the problem
belongs near
[RAG]({{ '/wiki/rag/' | relative_url }}) and
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), not only near prompt
writing. Maria's 13:20 data-exfiltration chapter ties that risk to overloaded
prompts and knowledge-base retrieval.

Unsafe output is another failure mode. At 11:38 and 18:01, Maria connects
hallucinations to legal exposure and user trust. She also connects them to
safety and adoption. The red-team question isn't only whether the answer is
wrong. It's whether the wrong answer creates a commitment, recommendation, or
action that the product owner can't accept.

## Security Testing for AI Behavior

AI red teaming overlaps with security testing, but it adds model behavior and
retrieval behavior to the normal attack surface. A web security test may check
authentication, authorization, input handling, and logging. It may also check
data access. An AI red-team test asks whether a natural-language interaction can
route around those controls.

Maria's 16:15 and 17:00 chapters describe defenses that map directly to test
cases. Teams can test query analysis, retrieval constraints, and output
validation. They can also test layered defenses and classifiers that don't rely
on the same generative model.
They should test those controls with adversarial prompts and encoded
instructions. They should also test attempted data extraction and requests that
look safe until the system includes retrieved context.

This is where [Security]({{ '/wiki/security/' | relative_url }}) and AI red
teaming split. Security covers access controls, privacy, secure model
artifacts, and deployment approvals. AI red teaming asks whether the AI behavior
still respects those controls when the user tries to manipulate the system.

## Regression Evaluation for Red-Team Cases

Red-team cases should become part of the evaluation set. A team can start with
failures found in a live exercise. It can then preserve them as regression tests
for prompts, retrieval changes, model updates, and agent releases.

Aditya's evaluation discussion in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }})
supports this approach. At 43:30, he discusses evaluating agents for
multi-tenancy and scale. At 50:18, he discusses aligning LLM judges with human
labels. Red-team cases need the same discipline because a judge can miss the
risk if it only scores helpfulness or semantic similarity.

Red-team work therefore depends on
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [Evaluation]({{ '/wiki/evaluation/' | relative_url }}). The evaluation
should verify whether the system refuses, routes to review, limits retrieval,
or answers with enough uncertainty. A single accuracy score usually hides those
outcomes.

## Production Controls

Red teaming is useful only when teams turn findings into controls. In
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}),
Maria's 25:34 chapter covers human-in-the-loop review. That review path matters
when the system handles high-stakes requests, ambiguous user intent, or outputs
that can harm trust.

Production controls can include retrieval allowlists and prompt templates. They
can also include output validators, non-LLM classifiers, and audit logs. Rate
limits and escalation to a person belong in the same control set. Teams should
monitor repeated attack attempts. For agents, Aditya's 30:26 discussion of
guardrails, data lineage, and auditability adds tool-call traces and permission
boundaries.

The production version of a red-team finding should be concrete. If the system
leaked a retrieved paragraph, tighten retrieval and output checks. If it made an
unsafe recommendation, add refusal criteria and human review. If an agent called
the wrong tool, add permission checks, tool mocks in tests, and traces that make
the failure reviewable.

## Risk Acceptance and Human Oversight

Governance decides which failures are unacceptable and who can approve the
tradeoff. Supreet's
[Responsible & Explainable AI]({{ '/podcasts/responsible-explainable-ai-bias-detection/' | relative_url }})
episode makes this explicit. At 27:38, she discusses cross-functional
governance with subject matter experts, compliance, and leadership. At 35:28,
she covers human oversight and the limits of automation.

Those governance decisions set red-team priorities. A customer-support bot
doesn't need the same refusal policy as a healthcare assistant or finance
copilot. They also don't need the same approval chain. The team has to decide
what data the assistant can access and what advice it can give. It also has to
decide when a person must review the answer and how incidents are reported.

For broader policy and accountability, use
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}),
[Governance]({{ '/wiki/governance/' | relative_url }}), and
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}). AI red
teaming supplies evidence for those pages. It produces concrete failures,
concrete controls, and a record of which risks the team accepted.

## Adjacent AI Safety Topics

AI red teaming sits closest to these DataTalks.Club topic pages:

- [Security]({{ '/wiki/security/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
