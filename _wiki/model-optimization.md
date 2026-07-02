---
layout: wiki
title: "Model Optimization"
summary: "Techniques for making ML models smaller, faster, and cheaper to serve: quantization, knowledge distillation, pruning, on-device inference optimization, and the shift toward smaller task-focused LLMs."
related:
  - LLM Deployment
  - AI Infrastructure
  - MLOps
  - Production
  - LLMs
  - Machine Learning System Design
---

Model optimization covers techniques for making machine learning models smaller,
faster, and cheaper to serve in production. These include quantization, knowledge
distillation, pruning, and on-device inference optimization. DataTalks.Club
guests discuss these techniques in contexts from autonomous driving to LLM
serving, with a recurring theme that general-purpose models are too slow or
expensive for many real-world deployments.

The topic connects to
[LLM Deployment]({{ '/wiki/llm-deployment/' | relative_url }}),
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}).

## On-Vehicle Inference Constraints

In
[From Computer Vision Research to Autonomous Driving AI](https://datatalks.club/podcast/from-computer-vision-research-to-autonomous-driving-ai.html),
[Aishwarya Jadhav](https://datatalks.club/people/aishwaryajadhav.html) describes the
extreme performance constraints of on-vehicle inference. At 22:17 she explains
that models running on a car must process camera feeds with near-zero latency.
You cannot wait seconds for an LLM to decide whether a pedestrian is in view.
The system must react within milliseconds, which rules out large general-purpose
models for real-time perception.

At 23:28 she covers model compression techniques including quantization and other
speedups. The goal is to reduce model size while maintaining accuracy, so models
fit the compute budget of automotive hardware. She also describes staged
deployment: at 32:43 she explains that every release goes through multiple safety
checks and real-world validation before deployment, with some improvements rolling
out every few weeks and major updates taking longer.

## When to Prioritize Distillation and Fine-Tuning

In
[Understanding the AI Engineer Role](https://datatalks.club/podcast/s23e07-understanding-ai-engineer-role.html),
[Nasser Qadri](https://datatalks.club/people/nasserqadri.html) places model
optimization in the context of AI engineering career decisions. At 1:00:25 he
explains that fine-tuning and distillation are more than theory: they are active
practice. As you start to productionize what you build, or want lower latency,
you may want smaller models that run on a phone. Then it is worth digging into
these techniques more deeply.

At 56:55 Nasser discusses the future of latency and traditional ML integration.
He predicts that teams will discover patterns in agent solutions and ask whether
they can convert them into structured data science exercises with low-latency
traditional ML models. For example, instead of using an LLM for search at high
latency, you could use the data the model generates to train an XGBoost model
that is fast and deployable. This connects to
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

At 1:01:20 he confirms that once you have a big enough use case, distillation and
fine-tuning become necessary. While learning, theoretical awareness is sufficient.
Once you deploy to a self-driving car, you need to learn about distillation.

## Serving Challenges: Model Size and Compression

In
[Deploying LLMs in Production](https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html),
[Meryem Arik](https://datatalks.club/people/meryemarik.html) frames model compression
as a deployment necessity. At 25:26 she discusses serving challenges around model
size, compression, and inference optimization. Her company TitanML focuses on
making LLMs smaller and cheaper to deploy. At 49:57 she explains that while
API-based models are fast because they run on expensive hardware, most businesses
deploy on smaller GPUs or CPUs. With compression and optimization tools, you can
get comparable or faster speeds at much lower cost.

Meryem describes a product approach of Train, Optimize, and Takeoff at 23:37.
The optimization step specifically reduces model size for target hardware. She
also discusses the shift from API to self-hosted models for control over model
versioning. At 18:51 she warns about model drift: when API providers change models
under the hood, production behavior shifts. Self-hosting optimized open-source
models avoids this risk.

## Local Models and Smaller Task-Focused LLMs

In
[From Game AI to Modern AI Agents](https://datatalks.club/podcast/from-game-ai-to-modern-ai-agents.html),
[Micheal Lanham](https://datatalks.club/people/micheallanham.html) discusses the trend
toward running LLMs locally on private GPUs. At 45:40 he explains that paying for
hosted models and bandwidth gets expensive, and GPUs are becoming affordable
enough for people to run models themselves.

At 48:40 Micheal predicts that smaller, task-focused models will emerge. Current
models are huge and general-purpose, but future models will be more efficient and
specialized. He references working with a 120-billion-parameter open-source model
that is very capable, paired with low-latency providers offering one to two second
response times compared to four or five seconds for larger models. This connects
to [LLMs]({{ '/wiki/llms/' | relative_url }}) and
[LLM Deployment]({{ '/wiki/llm-deployment/' | relative_url }}).

## Specialized Models for Cost and ROI

In
[The Future of AI Agents](https://datatalks.club/podcast/s23e03-future-of-ai-agents.html),
[Aditya Gautam](https://datatalks.club/people/adityagautam.html) connects model
optimization to enterprise economics. At 24:02 he explains that rather than paying
high costs and latency with a general-purpose LLM API, enterprises understand they
need to fine-tune models. They bring them to a smaller scale to save cost and
ensure high ROI. This trend toward specialization means companies develop agents
for specific purposes in finance or marketing using smaller, optimized models.

Aditya also links specialized models to agent governance at 19:16. The move toward
fine-tuned, smaller models is not just about cost: it also improves control over
what the agent does, which matters for regulated industries.

## Related Pages

- [LLM Deployment]({{ '/wiki/llm-deployment/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [LLM Cost Optimization]({{ '/wiki/llm-cost-optimization/' | relative_url }})
