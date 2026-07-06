---
layout: wiki
title: "Sensor ML Personal Baselines"
summary: "A sensor ML portfolio project: use individual history for anomaly detection, product alerts, and baseline-aware health signals."
related:
  - Machine Learning Portfolio Projects
  - Model Monitoring
  - Data Pipelines
  - Machine Learning System Design
  - Startups
  - AI Product Feedback Loops
---

Sensor ML with personal baselines uses longitudinal sensor history to learn what
is normal for one subject. The system can then raise alerts about deviations.
Fit Tails, a pet-health device, treats dog behavior as an individual
anomaly-detection problem rather than a generic activity classifier.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

Treat this as a concrete
[[machine-learning-portfolio-projects=>machine learning portfolio project]].
A project version should collect sensor history, create simple labels, build a
personal baseline, and explain the product action. The topic sits near
[[Machine Learning System Design]], [[Data Pipelines]], and
[[Model Monitoring]] because the hard part isn't only model choice. The project
has to preserve history, handle context changes, and make alerts useful to an
owner or vet.

That makes it a small, product-shaped
[[industrial-ml-applications=>industrial ML application]]. The model depends on
physical sensors, deployment conditions, and a decision that someone can act on.
For a manufacturing analogue,
[[manufacturing-predictive-maintenance-yield-analytics=>fab maintenance and yield ML]]
uses tool telemetry and qualification schedules instead of a pet's personal
history.

## Personal Baselines Before Alerts

Early health signals can appear as behavior changes over time. Useful signals
include fragmented sleep and restlessness. Movement variability, movement
quality, and movement quantity can also matter. Those signals are closer to
anomaly detection than classification because the system needs a learned
baseline for each dog.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

Dogs vary by breed and size. They also vary in personality, health risks,
activity needs, and sleep. A global
"normal dog" can hide the signal that matters for one animal.

The baseline isn't available on day one. Fit Tails needs two or three weeks to
learn normal behavior. Weather and changed routines can disturb a dog's routine.
So can people and new family members.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

Human self-tracking follows the same baseline-first order. In
productivity tracking, logs and Notion dashboards create a personal record for
reflection. Steps, exercise, and hydration metrics add simple habit signals.
[[cite:biohacking-productivity-for-data-scientists-and-ml-engineers@38:07=>Productivity Tracking]]
[[cite:biohacking-productivity-for-data-scientists-and-ml-engineers@48:21=>Habit Metrics]]
Those measurements aren't an ML system by themselves. They're the personal
history that makes later modeling or alerting useful because the system has an
individual baseline to compare against.

Healthcare wearables make the same point in a clinical product context. In
remote monitoring, activity and heart-rate variability become more useful when a
product can compare them with the person's baseline and care context.
[[cite:ai-in-healthcare-and-digital-therapeutics@29:33=>Remote Monitoring and Wearables]]
That context keeps a low-activity day or HRV change from being treated as the
same event for everyone.

## Task Boundaries and Model Choice

Approaches differ by task boundary. Population models can use breed, age, and
weight for initial estimates. They can predict steps, calories, or broad
activity labels.
Useful health alerts require the individual baseline because the product has to
notice what changed for this subject, not only what matches a broad group.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

Healthcare sensor work adds a model-choice boundary for physiological signals.
A bed-mat ballistography system can capture movement caused by respiration and
heart activity without attaching electrodes. ECG can serve as the reference
signal while the system denoises the mat signal and extracts vitals.
[[cite:building-healthcare-machine-learning-systems@19:28=>Healthcare ML Systems]]

Sports physiology is another sensor-ML-adjacent domain. Leonid Kholkine
describes a career shift into a PhD in machine learning applied to sports and
sports physiology. He also did some recommender-systems work
[[cite:s23e09-starting-data-conference-data-makers-fest-story@06:13=>Sports Physiology ML]].
For this page, that connection matters as a domain pointer. Physiology models
need domain context about the subject and activity, not only generic sensor
classification.

Vehicle perception is the adjacent sensor-architecture case. The
[[camera-first-vs-lidar-autonomous-driving=>camera-first vs LiDAR]]
comparison shows how camera, LiDAR, and radar choices affect validation and
system boundaries
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving AI]].

Astronomy gives another measured-signal boundary. In
[[astroinformatics-scientific-data-pipelines=>astroinformatics scientific data pipelines]],
observations across radio through X-ray wavelengths have to stay attached to
their instrument context. That context matters before a team can make a source
or water-detection claim
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@06:45=>From Radio Astronomy to Applied ML]]
[[cite:machine-learning-for-asteroid-mining-and-water-detection@19:35=>Asteroid Mining]].

The modeling decision depends on signal strength. Respiration can be estimated
with filters and Fourier methods when the relevant frequency is strong enough.
Heart-rate estimation may justify [[deep-learning=>deep learning]] when the
signal is weaker, noisier, or overlaps with other motion.
[[cite:building-healthcare-machine-learning-systems@21:49=>Healthcare ML Systems]]

Filters and Fourier methods aren't only baselines. For simpler physiological
signals, they can be the preferred production answer. That matters in
[[healthcare-ml-validation-and-adoption=>healthcare ML]] settings where
interpretability, robustness, and deployment constraints matter.

In Eleni's ballistography work, respiration had a stronger frequency signal and
fit classical signal processing. Infant heart-rate estimation justified U-Net
because movement, overlapping frequencies, and weaker waveform structure made
the signal harder to isolate. U-Net becomes useful when the task shifts from
isolating a frequency band to finding heart-rate waveforms in noisy
ballistography.
[[cite:building-healthcare-machine-learning-systems@19:28=>Healthcare ML Systems]]
[[cite:building-healthcare-machine-learning-systems@21:49=>Healthcare ML Systems]]

## Sleep and IMU Signals

The sensor data in Fit Tails comes from an IMU collar. The collar uses
gyroscope, accelerometer, and magnetometer readings across axes. Those readings
track orientation and movement to infer activity states such as walking,
playing, running, and sleeping. The sleep features separate day sleep, night
sleep, total sleep, and movement during sleep.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

The sleep focus matters because the product isn't trying to duplicate a human
wearable feature list. Sleep is treated as a major pet-health metric because
weight is visible but often too late. Sleep changes can reveal pain or other
issues before activity changes appear. Owners can't easily observe nighttime
awakenings or sleep twisting, so sensor sleep history can help a vet decide
whether further tests are needed.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

## Long-Term History as Product Feedback

Fit Tails starts with a real owner problem. Owners may be anxious about a dog's
health condition and make frequent vet visits. Step and calorie trackers can
still leave them without deeper behavioral insight.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]
For [[AI Product Feedback Loops]], the important signal isn't whether a user
enjoys a metric. The stronger signal is whether long-term history helps explain
a change and supports a next action.

Early prototypes used assembled components to test whether the team could
capture useful signals and understand the data.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

For a sensor-ML project, the product feedback loop includes hardware comfort
and sampling reliability. It also includes owner behavior and whether derived
features help interpret an anomaly. The work sits near
[[Startups]] as well as [[industrial-ml-applications=>industrial ML applications]].
A small team has to learn from prototypes before scaling the device or the
model.

## Portfolio Project Version

A credible portfolio version should make the personal-baseline constraint
visible. Use a simple global model first, then show why it's insufficient for
health-like alerts. The distinction between population models for initial
classification and individualized anomaly detection gives the project its
evaluation story.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]
In a README, explain which tasks work immediately. Also explain which tasks
require weeks of history and what contextual changes can invalidate an alert.

The system-design version should include a small
[[data-pipelines=>data pipeline]] for raw IMU events, derived activity and
sleep features, and per-subject baseline storage. It should also produce alert
outputs and include a [[model monitoring]] story. Watch for missing sensor data,
changed routines, device placement issues, and baseline drift as the dog ages.
Multi-week history, environmental distractors, aging, and continuous change set
the operating requirements.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

For reviewers, the strongest artifact isn't a high-capacity model alone. A
compact [[machine learning system design]]
should show the data path and baseline period. It should also show the alert
threshold, false-alarm tradeoff, and product response. In Sofya's Fit Tails
framing, a useful alert means something seems off for that specific dog. The
system can make that claim after enough history has been collected.
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]]

This project version shows applied ML judgment better than a standalone notebook
with generic sensor labels.

## Related Pages

Sensor baselines connect portfolio projects, ML system design, pipelines, and
industrial ML.

- [[Machine Learning Portfolio Projects]]
- [[Machine Learning System Design]]
- [[Data Pipelines]]
- [[astroinformatics-scientific-data-pipelines=>Astroinformatics Scientific Data Pipelines]]
- [[Model Monitoring]]
- [[AI Product Feedback Loops]]
- [[Startups]]
- [[person:sofyayulpatova=>Sofya Yulpatova]]
- [[podcast:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Building Pet Health Tech: ML, Sensors, and Dog Behavior Data]]
