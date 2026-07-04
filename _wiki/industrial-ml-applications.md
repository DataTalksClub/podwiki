---
layout: wiki
title: "Industrial ML Applications"
summary: "Industrial ML across fab telemetry, pet sensors, crowd routing, vehicles, validation, monitoring, and operator trust."
related:
  - Machine Learning
  - Machine Learning System Design
  - Model Monitoring
  - Computer Vision
  - Data Products
  - Production
  - Interpretability
  - Data Pipelines
  - Recommendation Systems
  - Streaming
---

Industrial ML applications are production [[machine learning]]
systems where data comes from physical processes or operational environments.
Data may come from a semiconductor fab, sensor device, vehicle, or theme park.
It may also come from a production tool or infrastructure system. The model is
only one part of the system. Teams still have to turn messy signals into
decisions that operators, customers, or embedded systems can trust.

Semiconductor yield work depends on fab tools that produce millisecond-level
logs. In that setting, predictive maintenance is measured by fewer wafers at
risk[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].
Pet-health ML uses sensor-based anomaly detection around each dog's long-term
baseline[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].

Theme-park crowd routing depends on queue prediction and capacity modeling.
Next-best-action recommendations depend on app adoption and live
measurement[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
Autonomous-driving work is the safety-critical version. Sensor data,
simulation, closed-track tests, and labeling define production. Release staging
belongs to that same boundary[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

Use [[Machine Learning System Design]]
for general architecture, and use [[Model Monitoring]]
for drift and feedback loops. Use [[Computer Vision]]
for perception systems, and [[Production]]
for release, recovery, and ownership.

## Operating Boundary

Industrial ML means applied modeling constrained by the physical process that
produces the data. The model has to respect tool cycles and sensor limitations.
It also has to respect human movement, safety procedures, and product adoption.

Semiconductor yield work starts with process telemetry and tool logs, not with
model choice. Chip processes happen in large tools, and their logs capture
pressure and gases. They also capture tool steps and process details at high
frequency[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

The same structure appears outside manufacturing. Sofya's pet tracker collects
IMU signals and sleep behavior from a collar. It then turns those signals into
individual baselines because dogs differ by size, breed, routine, and
personality
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].

Abouzar's theme-park work converts transactions, ride data, and capacity into
crowd indexes. Route preferences guide the group recommendations
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
Aishwarya's autonomous-driving discussion uses cameras, LiDAR, radar, and GPS.
Metadata, simulation, and labeling pipelines also sit inside the ML system
rather than in background plumbing
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

Industrial ML is a close neighbor of [[data products]] because each output has a
user and a decision. A system may run a tool qualification earlier or alert a
pet owner or vet. It may route a visitor group away from a long queue or update
a vehicle perception model after safety validation.

## Failure Costs

Industrial ML applications differ most in their failure costs. Semiconductor
yield work centers yield, waste, and operator trust in a fab. Even after an
accuracy jump, a prediction that can't be explained to a supervisor isn't ready
for fab decisions[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].
That puts [[interpretability]] near
the center of industrial ML.

Pet-health failure can come from false confidence in shallow consumer metrics.
Existing pet devices collected basic activity data. Early health signals live in
sleep fragmentation, restlessness, movement quality, and changes over time
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].
Anomaly detection needs a personal baseline before it becomes useful.

Theme-park crowd routing puts adoption and intervention design ahead of model
sophistication. A recommendation can only redistribute crowds if visitors use
the app, share preferences, and accept suggestions. The example includes
free-coffee incentives and route surveys. It also uses a deliberately simple
highest-probability recommendation
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
That emphasis links industrial ML to [[recommendation systems]]
and [[product analytics]].

Autonomous driving is stricter because the model is part of a safety-critical
stack with simulation, closed tracks, and on-road testing.
Sensor fusion and labeling quality belong in that stack too. The team also has
to manage staged releases and redundant systems
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

In that domain, [[computer vision]]
and [[production]] are inseparable from
regulatory review, hardware limits, and latency constraints. Safety review is
another production constraint.

## Data Collection and Instrumentation

Industrial ML starts with instrumentation because the model can only learn what
the environment records. Semiconductor fab work depended on tool logs, Oracle
databases, JMP analysis, and PL/SQL applications. It also depended on
cross-area knowledge from production, process, yield, and software
roles[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].
Useful yield data became available because the work connected database access
with production and engineering context.

Sofya's tracker shows the hardware tradeoff more directly because the device
collects accelerometer, gyroscope, and magnetometer readings. Heart-rate extraction is
hard because fur and comfort make some sensors impractical.

Different breed physiology and signal noise add more constraints
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].
The tracker therefore uses movement, breathing-related signals, sleep, and
longitudinal behavior rather than assuming every health metric is equally
collectable.

In theme-park operations, instrumentation includes behavioral participation.
Abouzar's crowd model used app usage, surveys, group preferences, and ride
capacity. It also used restaurant or stand transactions and route variations
from roughly 3,000 people
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
That makes [[data pipelines]] part of
the product. Missing events or weak app adoption change what the model can know.

Autonomous driving raises the scale and governance boundary because the data
spans sensors, location, driving conditions, and system responses. The work also
requires anonymization and internal tooling for large-scale management and labeling
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

## Baselines and Validation

Baselines in industrial ML are often physical, behavioral, or operational rather
than generic accuracy benchmarks. Dashel's "wafers at risk" project estimated how
many wafers could be affected if a tool kept running at the current pace. The
baseline was the existing qualification schedule, and the improvement was a better
timing recommendation for checks that could reduce waste
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

Sofya's baseline is individual, and a dog needs two or three weeks of observation
before the system can know what's normal. Weather, people, and routines affect
behavior. Age and household changes matter too
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].
That makes validation a question of useful deviations, not a one-time classifier
score.

Abouzar validates recommendations through behavior and experiments, including
employee swiping experiments and [[a-b-testing=>A/B testing]].
It also covers engagement metrics, accuracy results, and [[streaming]]
for live experiments
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
The queue model is successful only if it changes visitor flow and experience.

Aishwarya's validation stack moves from simulation to closed tracks, then to
on-road tests with safety drivers. Deployment to driverless cars comes after
that. Human annotation, automated labeling, and multiple safety checks come
before releases
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].
That's the safety-critical version of the same [[evaluation]]
principle. Offline model quality isn't enough when the model acts in a physical
world.

Paint and chemical production create a "tiny data" regime from ingredients,
infrared spectra, and material properties. Neural nets rarely fit that setting,
so the work combines statistical methods and transfer learning with domain
experts who hold tacit knowledge beyond the CSV. Industrial data splits between
R&D experiments and full-scale production. Regulatory and sustainability
tracking create new data gaps that force product redevelopment with small
historical datasets[[cite:industrial-data-small-data-production-machine-learning=>Industrial Data and Small-Data Production ML]].

## Monitoring, Drift, and Safety

Industrial ML monitoring has to watch both model behavior and the operating
environment. In fabs, Dashel's planning example monitors tool readiness through
wafer counts, particles, and gases. Qualification timing matters too, and the
prediction changes
maintenance scheduling, so an unexplained model or stale process data can create
costly waste
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

Pet health monitoring treats aging and routine changes as drift alongside sleep
and context. Deviations become meaningful only after the system learns normal
behavior. The baseline must also keep adapting as the dog changes
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].
It's a practical example of [[model monitoring]]
where feedback isn't just data distribution but lived behavior.

Theme-park monitoring is operational and product-facing. Abouzar's system has to
measure whether recommendations reduce queues, improve engagement, and remain
useful under live visitor flow. His later chapters tie this to streaming
experiments and rollout metrics rather than a static model report
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].

Autonomous driving makes safety monitoring explicit. Strict validation,
redundancy, sensor data collection, and labeling quality guide the release
path. Teams also stage releases and coordinate perception, data, and simulation
work. Hardware, sensor, and safety teams are part of the same feedback loop
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].
The model is monitored as one layer in a larger system, not as an isolated
artifact.

## Explainability and Operator Trust

Industrial ML often serves domain experts who need to act on the output. Dashel
couldn't rely on a Bayesian model or random forest merely because accuracy moved
from 65 percent to 85 percent. He needed to explain the steps to his supervisor
before the model could support fab decisions
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].
Industrial ML doesn't always require simple models, but the explanation must
match the decision and the person accountable for it.

Sofya's pet-health example makes explainability user-facing. Owners and vets need
to understand why sleep fragmentation and nocturnal awakenings matter. Movement
changes matter too because the product is asking them to interpret a health
signal rather than merely count steps
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].

Abouzar's theme-park recommendations need a simple surface because the backend
can use crowd indexes and probabilistic routes. Visitors see a next move that
should feel useful and easy to accept
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].

For autonomous driving, the trust boundary moves from an individual explanation
to a validated safety process. Teams build that trust through sensors,
redundancy, staged rollout, and testing. Public confidence in driverless rides
matters too
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

## Product Adoption and Operating Fit

Industrial ML succeeds only when it fits the workflow around it. Dashel's first
automation tool solved a daily manual calculation problem. The organization
didn't adopt the Java tool because IT wanted a different implementation path
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].
His later yield projects worked better because they fit the data access and
supervisor needs around Oracle, PL/SQL, JMP, and fab reporting
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

Abouzar's crowd-routing case makes adoption a first-order data problem. App usage
and incentives determine whether the park can collect enough preferences and
routes to recommend useful next actions
[[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering=>Theme Park Crowd Modeling]].
The ML product is part recommendation engine and part behavior-change system.

Sofya's product adoption depends on making a wearable practical for dogs and
owners. She rejects some heart-rate options because shaving dogs or using chest
straps wouldn't fit normal pet care
[[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data=>Pet Health Tech]].
Aishwarya's autonomous-driving example shows a stricter adoption curve. Users
must trust a driverless ride. Regions also need safety, scalability, and
regulatory fit before expansion
[[cite:from-computer-vision-research-to-autonomous-driving-ai=>Autonomous Driving CV]].

Healthcare ML shows operating fit in a career transition because [[Data Science]]
skills can transfer into healthcare. Entry can start with
technical work, while research and device deployment roles need different
clinical context. Sepsis becomes working vocabulary when the practitioner learns
the clinical setting [[cite:building-healthcare-machine-learning-systems@53:31=>Healthcare ML Systems]].
That links [[healthcare-ml-validation-and-adoption=>healthcare ML validation]]
and [[career-transitions-in-data=>career transitions in data]] to the same
industrial ML boundary. Technical skill opens the door, but clinical context and
regulatory workflow determine whether the system is useful [[cite:building-healthcare-machine-learning-systems@55:46=>Healthcare ML Systems]].

## Related Pages

These pages cover the design, monitoring, and operating disciplines around
industrial ML systems.

- [[Machine Learning]]
- [[Machine Learning System Design]]
- [[Model Monitoring]]
- [[Computer Vision]]
- [[Production]]
- [[Data Products]]
- [[Interpretability]]
- [[Data Pipelines]]
- [[Recommendation Systems]]
- [[Streaming]]
