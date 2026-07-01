---
layout: wiki
title: "Manufacturing Predictive Maintenance and Yield Analytics"
summary: "How semiconductor manufacturing ML turns fab telemetry, tool logs, and wafers-at-risk calculations into yield decisions that engineers can explain and use in production."
related:
  - Industrial ML Applications
  - Interpretability
  - Model Monitoring
  - Machine Learning
  - Data Engineering
  - Production
---

Manufacturing predictive maintenance and yield analytics use production
telemetry to decide when a tool needs attention and how much product is at
risk. In semiconductor manufacturing, the decision isn't only whether a
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) model can
predict an error. The model has to fit an
[industrial ML application]({{ '/wiki/industrial-ml-applications/' | relative_url }})
where wafers and tools define part of the context. Quals, engineers, and
production staff define the operating constraints.

[Dashel Ruiz Perez]({{ '/people/dashelruizperez/' | relative_url }}) describes
this from semiconductor production work at Microchip in
[From Semiconductor Data to Applied Machine Learning]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }}).
His example starts on the fab floor and moves through yield analytics and
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}). It ends
with a practical boundary. A prediction is useful only if supervisors and
engineers can understand it and act on it in
[production]({{ '/wiki/production/' | relative_url }})
([4:49-5:49, 18:07-20:40, 23:29-29:06, 37:29-43:38]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

## Fab Telemetry

Dashel's semiconductor example begins with physical tool behavior rather than a
modeling technique. He explains that chip processes run in large fab tools.
Engineers look at tool log files when they run experiments or diagnose issues.
Those logs include tool identity and process steps. They also record pressure,
gas amounts, and other details at millisecond resolution.

That creates far more data than a technician can comfortably review by hand
([8:49-11:06]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

It makes manufacturing predictive maintenance a telemetry and workflow problem
before it's an algorithm problem. A person needs to know which fab area
produced the signal and which process step was running. They also need to know
what the tool was supposed to do, plus which error messages or measurements
matter. Dashel's path from expediter to process technician mattered because
walking wafers through the fab gave him context. Later experiment work gave him
more context for interpreting the logs, not just access to files
([4:49-5:49, 8:49-10:23]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

## Yield Analytics

Yield analytics in Dashel's account depended on getting cross-area data into a
usable format. In his yield role, he cleaned production data with Python and
put it into an Oracle database. He also wrote small PL/SQL applications so his
supervisor could access the results. He describes yield work as needing a
whole-fab view of failures, passes, source areas, and production contacts who
could answer follow-up questions
([18:07-20:40]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

The work is close to [data engineering]({{ '/wiki/data-engineering/' | relative_url }})
inside a manufacturing process. A single clean training table wasn't the main
asset. Dashel needed to know where data lived and how tools mapped to fab
areas. He also had to make answers reachable for the people requesting them.

He says that production roles, technician roles, and engineering work let him
know where to go. Those roles also taught him whom to ask when a yield request
arrived
([19:11-20:40]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

## Wafers at Risk

Dashel asked whether a fab could estimate when a tool should be checked. The
fab needed to act before the normal schedule allowed too many wafers to be
exposed to risk. Tools had weekly, biweekly, or monthly qualification checks
called quals. Dashel questioned whether the schedule should depend on the
number of wafers processed rather than elapsed time
([21:39-23:29]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

His "wafers at risk" project counted wafer process steps across the production
database for the whole fab, then calculated risk by tool and area. Once he had
those counts, he wanted to project how many wafers would be at risk if the fab
kept running at the current pace. A useful forecast could tell engineers to run
quals earlier, for example after ten days instead of fifteen, reducing waste and
improving yield
([23:29-25:16]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

Dashel's later description shows the decision target. The goal wasn't an
abstract accuracy score, but a way to tell engineers that a tool might have a
probable issue within a window. They could then monitor the tool and plan a
check between roughly three and twelve days if measurements stayed in range
([27:55-29:06]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).
Use [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
broader production work where teams keep watching model inputs, predictions,
and business outcomes after deployment.

## Explainability

The manufacturing constraint in Dashel's story is that a better number isn't
enough. He remembers running algorithms such as Bayesian methods and random
forests. After tweaks, accuracy moved from around 65% to around 85%. He still
couldn't use the result because he couldn't explain the steps to his supervisor
([25:16-26:08]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

In a fab, practical [interpretability]({{ '/wiki/interpretability/' | relative_url }})
supports maintenance or yield decisions. The explanation needs to cover the
tool, the window, the risk level, and the action an engineer should take.
Dashel's answer was to keep learning analytics and ML so he could make better
predictions. They also needed to be explainable enough for the people
responsible for the tools
([25:35-28:33]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

## Production Use

In the same episode, Dashel contrasts notebook results with systems other
people can use. His examples include Flask and REST APIs. They also include
simple authentication, cloud deployment, and containers.

Access mattered because someone should be able to send data and get a result.
He ties this back to Microchip by recalling that his supervisor didn't only care
that a prediction existed. The supervisor needed to know how to get the data and
result
([37:29-43:38]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

For manufacturing predictive maintenance, the path from telemetry to impact
runs through deployable software and operational handoff. A model for wafers at
risk needs the fab database and a repeatable data pipeline. It also needs an
interface or report that engineers can access. Production teams need enough
context for a choice. They can run a qual, watch a tool or wait because
processing has stopped
([18:38-20:40, 23:29-29:06, 41:08-43:38]({{ '/podcasts/from-semiconductor-data-to-applied-machine-learning/' | relative_url }})).

[Rosona]({{ '/people/rosonaeldred/' | relative_url }}) extends these patterns to
chemical and coating production in
[Industrial Data and Small-Data Production ML]({{ '/podcasts/industrial-data-small-data-production-machine-learning/' | relative_url }}).
She describes quality control as monitoring input-output ratios — one kilo in,
one kilo out — and flagging anomalies that trigger a technician visit. Her
discussion of packing-peanut and blue-paint production shows that predictive
maintenance in process industries depends more on fixed sensor placement and
batch traceability than on internet-scale data volume. The regulatory layer adds
sustainability and compliance tracking, which can force reformulation using
small historical experiment data.

## Related Pages

These pages give the surrounding vocabulary for Dashel's semiconductor example.

- [Industrial ML Applications]({{ '/wiki/industrial-ml-applications/' | relative_url }}) for physical and operational ML systems beyond semiconductor fabs.
- [Machine Learning]({{ '/wiki/machine-learning/' | relative_url }}) for applied modeling, evaluation, deployment, and business tradeoffs.
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) for the pipeline and database work behind usable manufacturing analytics.
- [Interpretability]({{ '/wiki/interpretability/' | relative_url }}) for explaining model behavior well enough to support decisions.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for watching deployed models, inputs, predictions, and outcomes.
- [Production]({{ '/wiki/production/' | relative_url }}) for the operating boundary where people depend on a system.
