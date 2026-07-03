---
layout: wiki
title: "Model Optimization"
summary: "How DataTalks.Club guests explain making ML models smaller, faster, and cheaper with quantization, distillation, compression, and task-specific LLMs."
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
distillation, pruning, and on-device inference optimization. These techniques
apply in contexts from autonomous driving to LLM serving, where general-purpose
models are often too slow or expensive for real-world deployments.

The topic connects to
[[LLM Deployment]],
[[AI Infrastructure]], and
[[Production]].

## On-Vehicle Inference Constraints

On-vehicle inference faces extreme performance constraints. Models running in a
car must process camera feeds with near-zero latency. You can't wait seconds for
an LLM to decide whether a pedestrian is in view. The system must react within
milliseconds, which rules out large general-purpose models for real-time perception
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|From Computer Vision Research to Autonomous Driving AI]]).

Model compression techniques include quantization and other speedups. Teams
reduce model size while maintaining accuracy, so models fit the compute budget
of automotive hardware. Teams stage deployment, and every release goes through
multiple safety checks and real-world validation before it reaches vehicles.
Some improvements roll out every few weeks, while major updates take longer
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|From Computer Vision Research to Autonomous Driving AI]]).

## Distillation and Fine-Tuning Priorities

Fine-tuning and distillation are active practice, not just theory. As
you start to productionize what you build, or want lower latency, you may want
smaller models that run on a phone. At that point, these techniques matter more
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

Teams will discover patterns in agent solutions and ask whether they can convert
them into structured data science exercises. Low-latency traditional ML models
can be a better fit. For example, instead of using an LLM for search at high
latency, you could use the data the model generates to train an XGBoost model.
That model is fast and deployable
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).
This connects to [[Machine Learning System Design]].

Once you have a big enough use case, distillation and fine-tuning become
necessary. While learning, theoretical awareness is sufficient. Once you deploy
to a self-driving car, you need to learn about distillation
([[podcast:s23e07-understanding-ai-engineer-role|Understanding the AI Engineer Role]]).

## Serving Challenges: Model Size and Compression

Model compression is a deployment necessity. Serving challenges center on model
size, compression, and inference optimization. TitanML focuses on making LLMs
smaller and cheaper to deploy.

API providers can serve models quickly because they run on expensive hardware.
Most businesses deploy on smaller GPUs or CPUs. On that hardware, compression
and optimization tools can deliver comparable or faster speeds at much lower cost
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

TitanML frames the work as Train, Optimize, and Takeoff, with optimization
reducing model size for target hardware. Shifting from API to self-hosted models
gives teams control over model versioning. Model drift is a risk when API
providers change models under the hood. Production behavior shifts, and
self-hosting optimized open-source models avoids this
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

## Local Models and Smaller Task-Focused LLMs

People increasingly run LLMs locally on private GPUs because hosted models and
bandwidth get expensive. GPUs are becoming affordable enough for people to run
models themselves
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to Modern AI Agents]]).

Smaller, task-focused models will emerge. Current models are huge and
general-purpose, but future models will be more efficient and specialized.
Speakers cite capable 120-billion-parameter open-source models paired with
low-latency providers. Those providers can offer one-to-two-second response
times compared to four or five seconds for larger models
([[podcast:from-game-ai-to-modern-ai-agents|From Game AI to Modern AI Agents]]).
This connects to [[LLMs]] and
[[LLM Deployment]].

## Specialized Models for Cost and ROI

Model optimization connects to enterprise economics. Rather than paying high
costs and latency with a general-purpose LLM API, enterprises fine-tune models
and bring them to a smaller scale. They do this to save cost and improve ROI.
Companies also develop agents for specific purposes in finance or marketing
using smaller, optimized models
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

Enterprises also use specialized models for agent governance. The move toward
fine-tuned, smaller models isn't just about cost. It also improves control over
what the agent does, which matters for regulated industries
([[podcast:s23e03-future-of-ai-agents|The Future of AI Agents]]).

## Related Pages

For more deployment and infrastructure context, see:

- [[LLM Deployment]]
- [[AI Infrastructure]]
- [[MLOps]]
- [[Production]]
- [[LLMs]]
- [[Machine Learning System Design]]
- [[LLM Cost Optimization]]
