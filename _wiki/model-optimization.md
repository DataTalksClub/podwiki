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

Model optimization makes machine learning models smaller, faster, and cheaper
to serve in production. It includes quantization, distillation, and pruning. It
also includes fine-tuning, specialized serving, and on-device inference.
DataTalks.Club discussions place the topic where model quality has to meet hard
constraints from [[LLM Deployment]], [[AI Infrastructure]], [[Production]], and
[[Machine Learning System Design]].

Optimization follows the deployment target rather than a blanket demand for
smaller models. Vehicle hardware and phones impose different limits from
enterprise servers and private GPUs.

## Deployment Constraints

Autonomous vehicles can't route sensor signals through slow agents or wait
seconds before reacting. Latency is the constraint.[[cite:s23e07-understanding-ai-engineer-role=>AI Engineer Role]]

In self-driving systems, in-car models run many times per second on vehicle
hardware. The deployed networks may differ from the training-time networks.[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving]]

For production LLMs, hardware cost and privacy matter alongside version control
and user-facing latency. API models are useful for fast prototyping, but
business-critical systems may need self-hosted or fine-tuned open-source models.
That gives teams control over versions, data handling, and performance.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
That production constraint connects model serving to
[[llm-cost-optimization=>LLM cost optimization]].
Teams compare hosted API calls with compression and self-hosted models.

Optimization can also happen during training rather than only at serving time.
Theofilos Papapanagiotou describes Kubeflow Katib as a Kubernetes-native
hyperparameter search component. Teams define the objective and search ranges,
run candidate training jobs as pods, and compare results before promotion
[[cite:mlops-kubeflow-model-monitoring@40:12=>Kubeflow Model Monitoring]].
That connects model optimization to [[MLOps]] and [[machine learning infrastructure]]
when the search process needs reproducible pipelines.

## Compression and Quantization

Quantization is one public example of model compression in autonomous driving:
it makes models smaller and faster, alongside other internal optimizations.
That matters because the vehicle has to understand the world in real time using
limited onboard compute.[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving AI]]

Compression is also a serving concern for language models. TitanML started from
deep-learning compression, and its deployment value comes from reducing the GPU
requirements for large models. The stack includes model fine-tuning, significant
compression for BERT-style models, and an optimized inference server for
on-premise or CPU-backed LLMs.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Distillation, Fine-Tuning, and Smaller Models

Fine-tuning and distillation are practical production techniques, but they're
not the first thing a beginner needs to master. They become important when a
prototype has to run faster or fit constrained hardware. They also help when the
model must become cheaper or better adapted to a task.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

Two optimization moves recur in these episodes: fine-tuning specializes a model,
while distillation and related compression techniques reduce serving cost or
latency. Both are most useful after the team knows what the system has to do in
production.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]][[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

## Replacing General LLM Calls

Some optimization is architectural rather than numeric because an LLM can help a
team structure unstructured data. The deployed system might later use those
generated labels or features to train a lower-latency traditional ML model. For
search, a slow LLM-based workflow can become an XGBoost-style model when the
task is stable enough.[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]

That tradeoff belongs with [[Machine Learning System Design]]. The production
model is chosen for latency, reliability, and maintainability, not for novelty.

## Local and Specialized LLMs

Local serving is another optimization path. Teams may find hosted model calls
and bandwidth expensive, while private GPUs make local models more plausible.
The same discussion points toward smaller task-focused models. They can replace
some general-purpose calls when the narrower model does the same work more
efficiently.[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to Modern AI Agents]]

A separate agent discussion frames specialization as enterprise economics.
High-volume finance, marketing, and legal use cases may justify fine-tuned or
smaller-scale models. The investment depends on API call volume, latency,
governance, and long-term ROI.[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]]

## Version Control and Drift

Optimization can also mean controlling the model artifact. API providers may
change models behind the scenes, which can shift product behavior without the
application team choosing a release. Teams that self-host open-source models can
pin versions. They decide when to distill, prune, or upgrade under their own
release process.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Related Pages

More deployment and infrastructure context:

- [[LLM Deployment]]
- [[AI Infrastructure]]
- [[MLOps]]
- [[Production]]
- [[LLMs]]
- [[Machine Learning System Design]]
- [[LLM Cost Optimization]]
