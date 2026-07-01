---
layout: wiki
title: "Sensor ML with Personal Baselines"
summary: "A portfolio-project pattern for sensor machine learning where anomaly detection depends on each subject's long-term baseline rather than a global average."
related:
  - Machine Learning Portfolio Projects
  - Model Monitoring
  - Data Pipelines
  - Machine Learning System Design
  - Startups
  - AI Product Feedback Loops
---

Sensor ML with personal baselines uses longitudinal sensor history to learn what
is normal for one subject. The system can then raise alerts about deviations. In
[Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }}),
[Sofya Yulpatova]({{ '/people/sofyayulpatova/' | relative_url }}) describes
Fit Tails as a pet-health device. It treats dog behavior as an individual
anomaly-detection problem rather than a generic activity classifier.

Treat this as a concrete
[machine learning portfolio project]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).
A project version should collect sensor history, create simple labels, build a
personal baseline, and explain the product action. The topic sits near
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}), and
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) because the
hard part isn't only model choice. The project has to preserve history, handle
context changes, and make alerts useful to an owner or vet.

## Personal Baselines Before Health Alerts

Sofya's core framing is that early health signals appear as behavior changes
over time. Around 29:39 in
[Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }}),
she names sleep fragmentation and restlessness as useful signals. She also
includes movement variability, movement quality, and movement quantity. She
argues that this is closer to anomaly detection than classification because the
system needs a learned baseline for each dog.

Dogs vary by breed and size. They also vary in personality, health risks,
activity needs, and sleep. A global
"normal dog" can hide the signal that matters for one animal.

The baseline isn't available on day one. Around 43:35,
[Sofya]({{ '/people/sofyayulpatova/' | relative_url }}) says Fit Tails needs
two or three weeks to learn normal behavior. People, weather, new family
members, and changed routines can disturb a dog's routine
([episode]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).

Around 45:41, she separates population models from personal anomaly detection.
Initial models can use breed and age. They can use weight too. Those tasks
include steps, calories, and broad activity labels. Useful health alerts require
the individual baseline.

## Sleep and IMU Signals

The sensor data in Sofya's example comes from an IMU collar. Around 34:42 in
[Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }}),
she explains that the device uses gyroscope, accelerometer, and magnetometer
readings across axes. It tracks orientation and movement to infer activity
states such as walking, playing, running, and sleeping. Around 37:05, she
emphasizes sleep-cycle tracking. Fit Tails tracks day sleep, night sleep, total
sleep, and whether the dog moves during sleep.

The sleep focus matters because the product isn't trying to duplicate a human
wearable feature list. Around 41:27,
[Sofya]({{ '/people/sofyayulpatova/' | relative_url }}) says sleep is the
second-most important metric after weight for Fit Tails. Weight is visible but
often too late. Sleep changes can reveal pain or other issues before activity
changes appear
([episode]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).

At 42:29, she adds that owners can't easily observe nighttime awakenings or
sleep twisting. Sleep history from sensors can help a vet decide whether further
tests are needed.

## Long-Term History as Product Feedback

The product loop starts with a real owner problem. Around 26:48-28:40 in
[Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }}),
[Sofya]({{ '/people/sofyayulpatova/' | relative_url }}) describes anxiety over
her dog's health condition and frequent vet visits. She also describes
frustration that existing trackers showed steps or calories without deeper
behavioral insight. A useful product lesson follows for
[AI Product Feedback Loops]({{ '/wiki/ai-product-feedback-loops/' | relative_url }}):
the important signal isn't whether a user enjoys a metric. The stronger signal
is whether the long-term history helps explain a change and supports a next
action.

The same episode makes the feedback loop physical as well as analytical.
Around 52:26, Sofya says the first prototypes used assembled components. The
goal was to test whether they could capture useful signals and understand the
data
([Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).

For a sensor-ML project, the product feedback loop includes hardware comfort
and sampling reliability. It also includes owner behavior and whether derived
features help interpret an anomaly. The work sits near
[Startups]({{ '/wiki/startups/' | relative_url }}) as well as ML systems. A
small team has to learn from prototypes before scaling the device or the model.

## Portfolio Project Version

A credible portfolio version should make the personal-baseline constraint
visible. Use a simple global model first, then show why it's insufficient for
health-like alerts. Sofya's distinction around 45:41 between population models
for initial classification and individualized anomaly detection gives the
project its evaluation story
([Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).
In a README, explain which tasks work immediately. Also explain which tasks
require weeks of history and what contextual changes can invalidate an alert.

The system-design version should include a small
[data pipeline]({{ '/wiki/data-pipelines/' | relative_url }}) for raw IMU
events, derived activity and sleep features, and per-subject baseline storage.
It should also produce alert outputs and include a
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) story. Watch
for missing sensor data, changed routines, device placement issues, and baseline
drift as the dog ages. Sofya's 43:35-46:14 discussion of multi-week history,
environmental distractors, aging, and continuous change gives the operating
requirements
([episode]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).

For reviewers, the strongest artifact isn't a high-capacity model alone. A
compact [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
should show the data path and baseline period. It should also show the alert
threshold, false-alarm tradeoff, and product response. In Sofya's Fit Tails
framing, a useful alert means something seems off for that specific dog. The
system can make that claim
after enough history has been collected around 46:14
([Building Pet Health Tech]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})).

The result proves applied ML judgment better than a standalone notebook with
generic sensor labels.

## Related Pages

Use these pages for the neighboring portfolio, system-design, and product
contexts.

- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [AI Product Feedback Loops]({{ '/wiki/ai-product-feedback-loops/' | relative_url }})
- [Startups]({{ '/wiki/startups/' | relative_url }})
- [Sofya Yulpatova]({{ '/people/sofyayulpatova/' | relative_url }})
- [Building Pet Health Tech: ML, Sensors, and Dog Behavior Data]({{ '/podcasts/s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data/' | relative_url }})
