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
other agents, and plan safe motion. It is an engineering discipline rather than
a single model: the vehicle runs a stack of perception, prediction, and planning
systems, each validated and released in stages
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Tesla]],
[[podcast:from-computer-vision-research-to-autonomous-driving-ai|Waymo]]).

[[person:aishwaryajadhav|Aishwarya Jadhav]], a Machine Learning Engineer at
Waymo and former Tesla Autopilot team member, has worked across the full pipeline
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
Her career moved from finance data engineering at Morgan Stanley, through
[[computer vision]] research at
Carnegie Mellon, into perception and video understanding at Tesla, and then to
gesture and pedestrian semantics at Waymo. That arc places autonomous driving
AI next to
[[deep learning]],
[[model optimization]], and
[[production]] ML systems.

[[person:pauliusztin|Paul Iusztin]]'s first AI research job did deep learning on
autonomous driving from day zero: 3D object detection, 3D tracking, and fusing
multimodal data from images, radar, and LiDAR
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering]]).
That background shaped his later move into
[[AI engineering]].

## Sensor Tradeoffs: Cameras, LiDAR, and Radar

The first architectural decision in autonomous driving is the sensor stack, and
it drives everything downstream. Companies split between camera-first and
sensor-fusion approaches.

LiDAR is expensive, and its cost varies widely by quality. For assistive and
consumer products like the AI Guide Dog navigation app, avoiding LiDAR in favor
of mobile phone cameras keeps costs down, and everyone already has a phone. LiDAR
uses light rays (similar to radar but with light frequencies instead of radio
waves) to estimate objects and movement
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

Some self-driving companies use LiDAR for fully autonomous systems with no
driver, while Tesla relies solely on cameras for scalability. In Tesla's
camera-first approach, cameras all around the car provide a 360-degree view. The
models process these different views to understand the surroundings, giving the
car a more holistic view of the world than a human driver who cannot see behind
or to the sides simultaneously
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

An early research role involved fusing multimodal data from images, radar, and
LiDAR, working with Nvidia DGX systems and deploying models on a prototype
autonomous vehicle
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering]]).
The fusion approach is more common in companies building fully driverless systems
like Waymo, while the camera-first approach prioritizes scalability and cost.

## Perception Pipelines and Multimodal Understanding

Perception is the part of the stack that turns raw sensor data into an
understanding of the world: detecting objects, classifying gestures, and
recognizing pedestrians. Gesture recognition and pedestrian semantics are
specialized subfields within it
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

Gesture recognition for traffic control includes police and construction
signals. This perception task requires the system to understand human intent
from visual cues, not just detect that a human is present. The car constantly
monitors surroundings with multiple sensors, predicts motion paths, and reacts
within milliseconds, prioritizing safety by slowing or stopping when needed
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

3D object detection and 3D tracking are the foundational perception tasks,
overwhelming at first and sometimes requiring reading a paper twenty times to
understand it
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering]]).
The perception pipeline fuses these detections across sensors and time to build
a coherent world model.

The perception layer connects to broader
[[multimodal LLMs]] research. Some
companies already use multimodal LLMs for end-to-end self-driving because LLMs
are pretrained on massive data and carry world knowledge; the challenge is
making them fast enough for real-time inference
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

## On-Vehicle Inference and Model Compression

A car has limited compute, limited power, and hard real-time constraints.
Models that work in the cloud may be too slow or too large for on-vehicle
deployment. This is where [[model optimization]]
becomes critical.

On-vehicle inference is bound by tight performance constraints: models must run
within tight latency budgets on hardware that is already loaded with multiple
systems. Model compression techniques, including quantization and other speedups,
reduce model size and inference time without unacceptable accuracy loss
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

The same logic applies across the autonomous driving stack. Every component,
from perception to prediction to planning, competes for the same on-vehicle
compute budget. Compression techniques that shave latency from one model free
resources for another.

## Data Collection, Labeling, and Sensor Data Management

Autonomous driving systems are data-hungry. They need massive, diverse, and
well-labeled datasets covering rare edge cases across geographies and weather
conditions.

Sensor data management covers the huge volumes of sensor data collected,
handling collection, privacy, and scale through internal tooling and automation
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

In the labeling strategy, human labelers handle complex cases while automated
systems take care of repetitive tasks. The combination improves both speed and
accuracy, and labeling quality is constantly refined so models learn from the
best data possible
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

This data pipeline is itself a production system. It connects to
[[machine learning system design]]
and the broader [[production]] discipline.

## Validation: Simulation, Closed Tracks, and On-Road Testing

Validation in autonomous driving is staged and safety-first. No model goes
directly from training to public roads.

The validation pipeline has three stages. The first is simulation, where models
are tested in virtual environments. The second is closed-track testing on
private facilities. The third is on-road testing with safety drivers before full
deployment
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

The evaluation approach for sensitive cases starts by inheriting tests from past
events and rerunning new models on those cases. Next comes a broader set of
real-world scenarios, and finally a slow rollout to drivers that then expands
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
This staged approach means that even a small change to a perception model
triggers a cascade of evaluations before it reaches production vehicles.

## Model Release Cadence and Staged Deployment

Model release cadence depends on project cycles and validation results. Some
improvements roll out every few weeks, while major updates take longer. Every
release goes through multiple safety checks and real-world validation before
deployment
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

Waymo has specialized teams for perception, data, and simulation. Collaboration
is essential because every component affects others, and even a small change can
influence performance across the system. Building autonomous driving technology
requires expertise in software, hardware, sensors, and safety
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

This staged deployment discipline connects autonomous driving to the broader
[[production]] and
[[llmops|MLOps]] conversations in the podcast.

## Perception vs Reinforcement Learning

A key distinction in the autonomous driving stack is between perception and
behavior. Perception makes the agent understand the world; reinforcement
learning comes in when teaching an agent how to behave in the world. These are
two separate parts of the stack
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

[[person:aishwaryajadhav|Aishwarya Jadhav]] has never worked on the
reinforcement learning side despite working in the self-driving industry, having
skipped RL courses in college as too hard
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
RL resembles a fun emulator project more than production work, and whether her
team uses it in production is unclear.

All training environments, whether reinforcement learning or other methods, have
constraints: rules of the world are imposed, like not driving against traffic,
so the model is not completely free to learn however it wants. Chess and Go are
a contrast, where RL achieved state-of-the-art results
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
In chess, the rules are fixed and limited, so the model can explore freely within
those limits. In self-driving, the rules are constantly evolving, with an
infinite number of rules across different geographies and driving cultures.

## Real-World Complexity and Edge Cases

A surprising aspect of working at Waymo is how complex real-world driving is.
Even simple-looking actions involve multiple models and systems working together,
and the amount of coordination and testing required to make everything reliable
is enormous
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

Geographic complexity compounds the problem. Even within a country, different
cities have different driving patterns: some aggressive, some following rules
more closely. The system needs to adapt and remain constrained. Because
everything changes so much across geographies, self-driving is such a hard
problem
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

This is why data diversity and edge case coverage matter so much. The system
cannot rely on a single dataset or geography. It must generalize across
conditions, and that requirement flows back into data collection, labeling, and
validation.

## Cross-Domain Transfer

Autonomous driving technology transfers to other domains. Perception,
prediction, and planning models have applications beyond autonomous driving, and
similar approaches can be used in robotics, drones, and industrial automation
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
This makes the autonomous driving pipeline relevant to anyone building
[[computer vision]] or perception
systems for physical agents.

## Career Entry into Self-Driving AI

Entering self-driving starts with deep learning fundamentals and relevant
projects. The AI Guide Dog project, which used vision and navigation, led
directly to Tesla. Computer vision projects help a resume stand out so companies
know the candidate is familiar with the space
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).

A strong foundation in machine learning and computer vision, hands-on experience
with data and simulation, and knowledge of safety-critical systems all matter
because reliability is key in this field
([[podcast:from-computer-vision-research-to-autonomous-driving-ai|Lessons from Applied AI]]).
These entry points connect to the broader
[[AI engineering]] and
[[career-transitions-in-data|career transition]] discussions
in the podcast.

Deep learning work on autonomous driving offers another route into AI, even as a
path that later moves toward engineering and away from research
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering]]).
The autonomous driving domain forces engineers to confront the full stack: data,
models, hardware, deployment, and validation. That breadth translates well to
other AI engineering roles.

## Related Pages

- [[Computer Vision]]
- [[Machine Learning System Design]]
- [[Model Optimization]]
- [[Production]]
- [[Deep Learning]]
- [[AI Engineering]]
- [[Multimodal LLMs]]
