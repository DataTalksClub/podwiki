---
layout: wiki
title: "Autonomous Driving AI"
summary: "How DataTalks.Club guests describe the autonomous driving AI pipeline: sensor tradeoffs, perception models, on-vehicle inference, model compression, validation methodology, staged deployment, and the boundary between perception and reinforcement learning."
related:
  - Computer Vision
  - Machine Learning System Design
  - Model Optimization
  - Production
  - Deep Learning
  - AI Engineering
  - Multimodal LLMs
---

Autonomous driving AI applies machine learning, computer vision, and sensor
fusion to make a vehicle perceive its surroundings, predict the behavior of
other agents, and plan safe motion. DataTalks.Club guests who have worked at
[Tesla]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})
and
[Waymo]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }})
describe it as an engineering discipline rather than a single model. The vehicle
runs a stack of perception, prediction, and planning systems, each validated and
released in stages.

The clearest end-to-end account comes from
[Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }}), a Machine
Learning Engineer at Waymo and former Tesla Autopilot team member, in
[Lessons from Applied AI: Tesla, Waymo, and Beyond]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}).
Her career moved from finance data engineering at Morgan Stanley, through
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}) research at
Carnegie Mellon, into perception and video understanding at Tesla, and then to
gesture and pedestrian semantics at Waymo. That arc places autonomous driving
AI next to
[deep learning]({{ '/wiki/deep-learning/' | relative_url }}),
[model optimization]({{ '/wiki/model-optimization/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}) ML systems.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) adds an earlier-career
perspective. In
[AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
he describes his first AI research job doing deep learning on autonomous driving
from day zero: 3D object detection, 3D tracking, and fusing multimodal data from
images, radar, and LiDAR. That background shaped his later move into
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}).

## Sensor Tradeoffs: Cameras, LiDAR, and Radar

The first architectural decision in autonomous driving is the sensor stack, and
it drives everything downstream. Companies split between camera-first and
sensor-fusion approaches.

Aishwarya explains the tradeoff in her episode at 11:22. LiDAR is expensive, and
its cost varies widely by quality. For assistive and consumer products like the
AI Guide Dog navigation app, the team avoided LiDAR and relied on mobile phone
cameras because cost efficiency mattered and everyone already had a phone. At
12:08, she clarifies that LiDAR uses light rays (similar to radar but with light
frequencies instead of radio waves) to estimate objects and movement.

At 13:21, she describes the company-level split. Some self-driving companies use
LiDAR for fully autonomous systems with no driver. Tesla relies solely on
cameras for scalability. At 15:05, she details Tesla's camera-first approach:
cameras all around the car provide a 360-degree view. The models process these
different views to understand the surroundings, giving the car a more holistic
view of the world than a human driver who cannot see behind or to the sides
simultaneously.

Paul's experience at 7:08 reinforces the fusion approach. His first research job
involved fusing multimodal data from images, radar, and LiDAR. He worked with
Nvidia DGX systems and deployed models on a prototype autonomous vehicle. The
fusion approach is more common in companies building fully driverless systems
like Waymo, while the camera-first approach prioritizes scalability and cost.

## Perception Pipelines and Multimodal Understanding

Perception is the part of the stack that turns raw sensor data into an
understanding of the world: detecting objects, classifying gestures, and
recognizing pedestrians. Aishwarya works specifically on gesture recognition
and pedestrian semantics.

At 19:55, her episode covers gesture recognition for traffic control, including
police and construction signals. This is a perception task that requires the
system to understand human intent from visual cues, not just detect that a human
is present. At 35:43, she describes how the car constantly monitors surroundings
with multiple sensors, predicts motion paths, and reacts within milliseconds,
prioritizing safety by slowing or stopping when needed.

Paul's early work at 7:08 involved 3D object detection and 3D tracking, which
are the foundational perception tasks. He describes these as overwhelming at
first, sometimes requiring him to read a paper twenty times to understand it.
The perception pipeline fuses these detections across sensors and time to build
a coherent world model.

The perception layer connects to broader
[multimodal LLMs]({{ '/wiki/multimodal-llms/' | relative_url }}) research. At
52:53 in Aishwarya's episode, the discussion turns to whether multimodal LLMs
can be applied to self-driving. She notes that some companies are already using
multimodal LLMs for end-to-end self-driving because LLMs are pretrained on
massive data and carry world knowledge. The challenge is making them fast enough
for real-time inference.

## On-Vehicle Inference and Model Compression

A car has limited compute, limited power, and hard real-time constraints.
Models that work in the cloud may be too slow or too large for on-vehicle
deployment. This is where [model optimization]({{ '/wiki/model-optimization/' | relative_url }})
becomes critical.

At 22:17 in Aishwarya's episode, the discussion covers on-vehicle inference and
performance constraints. Models must run within tight latency budgets on
hardware that is already loaded with multiple systems. At 23:28, she covers
model compression techniques including quantization and speedups. These reduce
model size and inference time without unacceptable accuracy loss.

The same logic applies across the autonomous driving stack. Every component,
from perception to prediction to planning, competes for the same on-vehicle
compute budget. Compression techniques that shave latency from one model free
resources for another.

## Data Collection, Labeling, and Sensor Data Management

Autonomous driving systems are data-hungry. They need massive, diverse, and
well-labeled datasets covering rare edge cases across geographies and weather
conditions.

At 31:02, Aishwarya's episode covers sensor data management. The system
collects huge volumes of sensor data, and the team manages collection, privacy,
and scale. They rely on internal tooling and automation to handle the pipeline.

At 32:09, she addresses the labeling strategy. Human labelers handle complex
cases while automated systems take care of repetitive tasks. The combination
improves both speed and accuracy, and the team constantly refines labeling
quality to ensure models learn from the best data possible.

This data pipeline is itself a production system. It connects to
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and the broader [production]({{ '/wiki/production/' | relative_url }}) discipline.

## Validation: Simulation, Closed Tracks, and On-Road Testing

Validation in autonomous driving is staged and safety-first. No model goes
directly from training to public roads.

At 29:45 in Aishwarya's episode, the validation pipeline is described in three
stages. The first is simulation, where models are tested in virtual
environments. The second is closed-track testing on private facilities. The
third is on-road testing with safety drivers before full deployment.

At 51:28, she describes the evaluation approach for sensitive cases. Engineers
inherit tests from past events and rerun new models on those cases as the first
stage. Then they evaluate a broader set of real-world scenarios. Finally, they
roll out slowly to drivers and expand. This staged approach means that even a
small change to a perception model triggers a cascade of evaluations before it
reaches production vehicles.

## Model Release Cadence and Staged Deployment

At 32:43, Aishwarya's episode covers model release cadence. Updates depend on
project cycles and validation results. Some improvements roll out every few
weeks, while major updates take longer. Every release goes through multiple
safety checks and real-world validation before deployment.

At 33:24, she describes the team structure. Waymo has specialized teams for
perception, data, and simulation. Collaboration is essential because every
component affects others, and even a small change can influence performance
across the system. Building autonomous driving technology requires expertise in
software, hardware, sensors, and safety.

This staged deployment discipline connects autonomous driving to the broader
[production]({{ '/wiki/production/' | relative_url }}) and
[MLOps]({{ '/wiki/llmops/' | relative_url }}) conversations in the podcast.

## Perception vs Reinforcement Learning

A key distinction in the autonomous driving stack is between perception and
behavior. At 45:55, Aishwarya draws the line clearly. Her career has been on
the perception side, making the agent understand the world. Reinforcement
learning comes in when teaching an agent how to behave in the world. These are
two separate parts of the stack.

At 46:31, she notes that even though she works in the self-driving industry,
she has never worked on the reinforcement learning side. She skipped RL courses
in college because she found them hard. At 47:07, she adds that reinforcement
learning looks more like a fun project to do in an emulator, and she is not sure
if her team uses it in production.

At 47:56, she explains that all training environments, whether reinforcement
learning or other methods, have constraints. You impose rules of the world, like
not driving against traffic. The model is not completely free to learn however
it wants. At 50:29, she contrasts this with chess and Go, where RL achieved
state-of-the-art results. In chess, the rules are fixed and limited, so the
model can explore freely within those limits. In self-driving, the rules are
constantly evolving, with an infinite number of rules across different
geographies and driving cultures.

## Real-World Complexity and Edge Cases

At 37:18, Aishwarya describes what surprised her about working at Waymo: how
complex real-world driving is. Even simple-looking actions involve multiple
models and systems working together. The amount of coordination and testing
required to make everything reliable is enormous.

At 48:30, she addresses geographic complexity. Even within a country, different
cities have different driving patterns. Some are aggressive, and some follow
rules more closely. The system needs to adapt and remain constrained. At 49:24,
she notes that everything changes so much across geographies, which is why
self-driving is such a hard problem.

This is why data diversity and edge case coverage matter so much. The system
cannot rely on a single dataset or geography. It must generalize across
conditions, and that requirement flows back into data collection, labeling, and
validation.

## Cross-Domain Transfer

At 36:12, the episode discusses how much autonomous driving technology
transfers to other domains. Aishwarya notes that perception, prediction, and
planning models have applications beyond autonomous driving. Similar approaches
can be used in robotics, drones, and industrial automation. This makes the
autonomous driving pipeline relevant to anyone building
[computer vision]({{ '/wiki/computer-vision/' | relative_url }}) or perception
systems for physical agents.

## Career Entry into Self-Driving AI

At 55:25, Aishwarya gives career advice for entering self-driving. It starts
with deep learning fundamentals and relevant projects. Her AI Guide Dog project,
which used vision and navigation, led directly to Tesla. Computer vision
projects help a resume stand out so companies know the candidate is familiar
with the space.

At 38:03, she recommends building a strong foundation in machine learning and
computer vision, getting hands-on experience with data and simulation, and
learning about safety-critical systems because reliability is key in this field.
These entry points connect to the broader
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) and
[career transition]({{ '/wiki/career-transition/' | relative_url }}) discussions
in the podcast.

Paul's career arc at 7:08 offers another route. His deep learning work on
autonomous driving was the entry point to AI, even though he later moved toward
engineering and away from research. The autonomous driving domain forces
engineers to confront the full stack: data, models, hardware, deployment, and
validation. That breadth translates well to other AI engineering roles.

## Related Pages

- [Computer Vision]({{ '/wiki/computer-vision/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Model Optimization]({{ '/wiki/model-optimization/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Deep Learning]({{ '/wiki/deep-learning/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [Multimodal LLMs]({{ '/wiki/multimodal-llms/' | relative_url }})
