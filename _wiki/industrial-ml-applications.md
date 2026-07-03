---
layout: wiki
title: "Industrial ML Applications"
summary: "How podcast guests frame industrial ML: fab telemetry, pet sensors, crowd routing, vehicles, validation, monitoring, and operator trust."
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
The source may be a semiconductor fab, sensor device, vehicle, or theme park. It
may also be a production tool or infrastructure system. The model is only one
part of the system. The useful work is to turn messy signals into decisions that
operators, customers, or embedded systems can trust.

[[person:dashelruizperez=>Dashel Ruiz Perez]] describes
semiconductor yield work where fab tools produce millisecond-level logs. In that
setting, predictive maintenance is measured by fewer wafers at risk
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).
[[person:sofyayulpatova=>Sofya Yulpatova]] describes pet
health ML as sensor-based anomaly detection around each dog's long-term baseline
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).

[[person:abouzarabbaspour=>Abouzar Abbaspour]] describes
theme-park crowd routing through queue prediction and capacity modeling.
Next-best-action recommendations depend on app adoption and live measurement
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
[[person:aishwaryajadhav=>Aishwarya Jadhav]] adds the
safety-critical version in autonomous driving. Sensor data, simulation,
closed-track tests, and labeling define what "production" means. Release staging
belongs to that same production boundary
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

Use [[Machine Learning System Design]]
for general architecture, and use [[Model Monitoring]]
for drift and feedback loops. Use [[Computer Vision]]
for perception systems, and [[Production]]
for release, recovery, and ownership.

## Operating Boundary

Across the episodes, industrial ML means applied modeling constrained by the
physical process that produces the data. The model has to respect tool cycles,
sensor limitations, and human movement. It also has to respect safety procedures
and product adoption.
Dashel's fab example starts with process telemetry and tool logs, not with model
choice. He explains that chip processes happen in large tools and that logs
capture pressure, gases, tool steps, and process details at high frequency
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).

The same structure appears outside manufacturing. Sofya's pet tracker collects
IMU signals and sleep behavior from a collar. It then turns those signals into
individual baselines because dogs differ by size, breed, routine, and
personality
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).

Abouzar's theme-park work converts transactions, ride data, and capacity into
crowd indexes. Route preferences guide the group recommendations
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
Aishwarya's autonomous-driving discussion uses cameras, LiDAR, radar, and GPS.
Metadata, simulation, and labeling pipelines also sit inside the ML system
rather than in background plumbing
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

This makes industrial ML a close neighbor of [[data products]].
The output has a user and a decision. The system may run a tool qualification
earlier or alert a pet owner or vet. It may also route a visitor group away from
a long queue or update a vehicle perception model after safety validation.

## Different Failure Costs

The guests center different failure costs. Dashel focuses on yield, waste, and
operator trust in a semiconductor fab. A prediction that can't be explained to a
supervisor isn't ready even if its accuracy jumps after model tweaks
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).
That puts [[interpretability]] near
the center of industrial ML.

Sofya's failure mode is false confidence from shallow consumer metrics. Existing
pet devices collected basic activity data, but she argues that early health
signals live in sleep fragmentation and restlessness. Movement quality and
changes over time matter too
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).
Her system needs a personal baseline before anomaly detection becomes useful.

Abouzar puts adoption and intervention design ahead of model sophistication. A
theme-park recommendation can only redistribute crowds if visitors use the app,
share preferences, and accept suggestions. His example includes free-coffee
incentives and route surveys. It also uses a deliberately simple
highest-probability recommendation
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
That emphasis links industrial ML to [[recommendation systems]]
and [[product analytics]].

Aishwarya's autonomous-driving example is stricter. The model is part of a
safety-critical stack with simulation, closed tracks, and on-road testing.
Sensor fusion and labeling quality belong in that stack too. The team also has
to manage staged releases and redundant systems
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

In that domain, [[computer vision]]
and [[production]] are inseparable from
regulatory review, hardware limits, and latency constraints. Safety review is
another production constraint.

## Data Collection and Instrumentation

Industrial ML starts with instrumentation because the model can only learn what
the environment records. Dashel's fab work depended on tool logs, Oracle
databases, JMP analysis, and PL/SQL applications. It also depended on
cross-area knowledge from production, process, yield, and software roles
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).
He could make useful yield data available because he knew where data lived and
which production people or engineers could explain it.

Sofya's tracker shows the hardware tradeoff more directly because the device
collects accelerometer, gyroscope, and magnetometer readings. Heart-rate extraction is
hard because fur and comfort make some sensors impractical.

Different breed physiology and signal noise add more constraints
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).
The product therefore leans on movement, breathing-related signals, sleep, and
longitudinal behavior rather than assuming every health metric is equally
collectable.

In theme-park operations, instrumentation includes behavioral participation.
Abouzar's crowd model used app usage, surveys, group preferences, and ride
capacity. It also used restaurant or stand transactions and route variations
from roughly 3,000 people
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
That makes [[data pipelines]] part of
the product. Missing events or weak app adoption change what the model can know.

Autonomous driving raises the scale and governance boundary. Aishwarya describes
collecting camera images, LiDAR scans, radar, and GPS. Driving-condition
metadata and system responses are part of the data too. The work also depends on
anonymization and internal tooling for large-scale management and labeling
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

## Baselines and Validation

Baselines in industrial ML are often physical, behavioral, or operational rather
than generic accuracy benchmarks. Dashel's "wafers at risk" project estimated how
many wafers could be affected if a tool kept running at the current pace. The
baseline was the existing qualification schedule, and the improvement was a better
timing recommendation for checks that could reduce waste
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).

Sofya's baseline is individual, and a dog needs two or three weeks of observation
before the system can know what's normal. Weather, people, and routines affect
behavior. Age and household changes matter too
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).
That makes validation a question of useful deviations, not a one-time classifier
score.

Abouzar validates recommendations through behavior and experiments, including
employee swiping experiments and [[a-b-testing|A/B testing]].
It also covers engagement metrics, accuracy results, and [[streaming]]
for live experiments
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
The queue model is successful only if it changes visitor flow and experience.

Aishwarya's validation stack moves from simulation to closed tracks, then to
on-road tests with safety drivers. Deployment to driverless cars comes after
that. She also describes human annotation, automated labeling, and multiple
safety checks before releases
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).
That's the safety-critical version of the same [[evaluation]]
principle. Offline model quality isn't enough when the model acts in a physical
world.

[[person:rosonaeldred=>Rosona]] broadens the industrial
data picture beyond semiconductors. In
[[podcast:industrial-data-small-data-production-machine-learning=>Industrial Data and Small-Data Production ML]],
paint and chemical production create a "tiny data" regime from ingredients,
infrared spectra, and material properties. Because neural nets rarely fit, the
answer combines statistical methods and transfer learning with domain experts
who hold tacit knowledge beyond the CSV. She splits industrial data into R&D
experiments and full-scale production. Regulatory and sustainability tracking
create new data gaps that force product redevelopment with small historical
datasets.

## Monitoring, Drift, and Safety

Industrial ML monitoring has to watch both model behavior and the operating
environment. In fabs, Dashel's planning example monitors tool readiness through
wafer counts, particles, and gases. Qualification timing matters too, and the
prediction changes
maintenance scheduling, so an unexplained model or stale process data can create
costly waste
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).

Pet health monitoring treats aging and routine changes as drift alongside sleep
and context. Sofya says deviations become meaningful only after the system learns
normal behavior. The baseline must also keep adapting as the dog changes
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).
It's a practical example of [[model monitoring]]
where feedback isn't just data distribution but lived behavior.

Theme-park monitoring is operational and product-facing. Abouzar's system has to
measure whether recommendations reduce queues, improve engagement, and remain
useful under live visitor flow. His later chapters tie this to streaming
experiments and rollout metrics rather than a static model report
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).

Autonomous driving makes safety monitoring explicit. Aishwarya describes strict
validation, redundancy, sensor data collection, and labeling quality. She also
describes staged releases and collaboration across perception, data, and
simulation teams. Hardware, sensor, and safety teams are part of the same loop
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).
The model is monitored as one layer in a larger system, not as an isolated
artifact.

## Explainability and Operator Trust

Industrial ML often serves domain experts who need to act on the output. Dashel
couldn't rely on a Bayesian model or random forest merely because accuracy moved
from 65 percent to 85 percent. He needed to explain the steps to his supervisor
before the model could support fab decisions
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).
Industrial ML doesn't always require simple models, but the explanation must
match the decision and the person accountable for it.

Sofya's pet-health example makes explainability user-facing. Owners and vets need
to understand why sleep fragmentation and nocturnal awakenings matter. Movement
changes matter too because the product is asking them to interpret a health
signal rather than merely count steps
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).

Abouzar's theme-park recommendations need a simple surface because the backend
can use crowd indexes and probabilistic routes. Visitors see a next move that
should feel useful and easy to accept
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).

For autonomous driving, the trust boundary moves from an individual explanation
to a validated safety process. Aishwarya's episode frames trust through sensors,
redundancy, staged rollout, and testing. It also depends on public confidence in
driverless rides
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

## Product Adoption and Operating Fit

Industrial ML succeeds only when it fits the workflow around it. Dashel's first
automation tool solved a daily manual calculation problem. The organization
didn't adopt the Java tool because IT wanted a different implementation path
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).
His later yield projects worked better because they fit the data access and
supervisor needs around Oracle, PL/SQL, JMP, and fab reporting
([[cite:from-semiconductor-data-to-applied-machine-learning|Semiconductor ML]]).

Abouzar's crowd-routing case makes adoption a first-order data problem. App usage
and incentives determine whether the park can collect enough preferences and
routes to recommend useful next actions
([[cite:theme-park-crowd-modeling-to-tesla-full-stack-data-engineering|Theme Park Crowd Modeling]]).
The ML product is part recommendation engine and part behavior-change system.

Sofya's product adoption depends on making a wearable practical for dogs and
owners. She rejects some heart-rate options because shaving dogs or using chest
straps wouldn't fit normal pet care
([[cite:s22e08-building-pet-health-tech-ml-sensors-and-dog-behavior-data|Pet Health Tech]]).
Aishwarya's autonomous-driving example shows a stricter adoption curve. Users
must trust a driverless ride. Regions also need safety, scalability, and
regulatory fit before expansion
([[cite:from-computer-vision-research-to-autonomous-driving-ai|Autonomous Driving CV]]).

Healthcare ML shows operating fit in a career transition because [[Data Science]]
skills can transfer into healthcare. Entry can start with
technical work, while research and device deployment roles need different
clinical context. Sepsis becomes working vocabulary with
context.[[cite:building-healthcare-machine-learning-systems|Healthcare ML Systems]]
That links [[healthcare-ml-validation-and-adoption=>healthcare ML validation]]
and [[career-transitions-in-data=>career transitions in data]] to the same
industrial ML boundary. Technical skill opens the door, but clinical context and
regulatory workflow determine whether the system is useful.[[cite:building-healthcare-machine-learning-systems|Healthcare ML Systems]]

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
