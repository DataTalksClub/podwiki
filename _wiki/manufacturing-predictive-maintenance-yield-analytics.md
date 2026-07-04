---
layout: wiki
title: "Fab Maintenance and Yield ML"
summary: "How semiconductor teams use fab telemetry, tool logs, and wafers-at-risk forecasts to make explainable maintenance and yield decisions."
related:
  - Industrial ML Applications
  - Interpretability
  - Model Monitoring
  - Machine Learning
  - Data Engineering
  - Production
---

Manufacturing predictive maintenance and yield analytics use fab telemetry to
decide when a tool needs attention and how much product is at risk. In
semiconductor manufacturing, a [[machine learning]] model can't stop at
predicting an error. It has to fit an
[[industrial-ml-applications=>industrial ML application]]
where wafers and tools define part of the context. Quals, engineers, and
production staff define the operating constraints.

[[person:dashelruizperez=>Dashel Ruiz Perez]]'s semiconductor work at Microchip
starts on the fab floor, then moves through yield analytics and
[[data engineering]] to a practical boundary. A prediction is useful only when
supervisors and engineers can understand it in
[[production]]
and act on it.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

## Fab Telemetry

The semiconductor example begins with physical tool behavior rather than a
modeling technique. Chip processes run in large fab tools, and engineers look at
tool log files when they run experiments or diagnose issues. Those logs include
tool identity and process steps. They also record pressure, gas amounts, and
other details at millisecond resolution. That creates far more data than a
technician can comfortably review by hand.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

It makes manufacturing predictive maintenance a telemetry and workflow problem
before it's an algorithm problem. A person needs to know which fab area
produced the signal and which process step was running. They also need to know
what the tool was supposed to do, plus which error messages or measurements
matter. Production and process experience matters because walking wafers
through the fab gives analysts context for interpreting logs, not just access
to files.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

## Yield Analytics

Yield analytics depended on getting cross-area data into a usable format.
Dashel cleaned production data with Python and loaded it into an Oracle
database. He also wrote small PL/SQL applications so a supervisor could access
the results. Yield work needs a whole-fab view of failures, passes, source
areas, and production contacts who could answer follow-up questions.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

Dashel's yield role sat close to [[data engineering]]
inside a manufacturing process. The main asset wasn't one clean training table.
The yield role needed knowledge of where data lived, how tools mapped to
fab areas, and how requesters could reach the answers.

Production roles, technician roles, and engineering work teach where to go and
whom to ask when a yield request arrives.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

## Wafers at Risk

A fab can estimate when a tool should be checked, acting before the normal
schedule allows too many wafers to be exposed to risk. Tools had weekly,
biweekly, or monthly qualification checks called quals. The open question was
whether the schedule should depend on the number of wafers processed rather than
elapsed time.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

A "wafers at risk" project counted wafer process steps across the production
database for the whole fab, then calculated risk by tool and area. Those counts
project how many wafers would be at risk if the fab kept running at the current
pace. A useful forecast could tell engineers to run quals earlier, for example
after ten days instead of fifteen, reducing waste and improving yield.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

The decision target wasn't an abstract accuracy score. Engineers needed a way
to know that a tool might have a probable issue within a window. If
measurements stayed in range, they could monitor the tool and plan a check
between roughly three and twelve days.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

Use [[model monitoring]] for the
broader production work where teams keep watching model inputs, predictions,
and business outcomes after deployment.

## Explainability

A better number isn't enough in manufacturing. Algorithms such as Bayesian
methods and random forests moved accuracy from around 65% to around 85% after
tweaks. The result still couldn't be used because the steps couldn't be
explained to a supervisor.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

In a fab, practical [[interpretability]]
supports maintenance or yield decisions. The explanation needs to cover the
tool, the window, the risk level, and the action an engineer should take.
Predictions need to be both better and explainable enough for the people
responsible for the tools.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

## Production Use

Notebook results differ from systems other people can use. Making predictions
accessible can involve Flask and REST APIs, simple authentication, cloud
deployment, and containers.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

Access mattered because someone should be able to send data and get a result.
At Microchip, the supervisor didn't only care that a prediction existed. They
needed to know how to get the data and result.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

For manufacturing predictive maintenance, the path from telemetry to impact
runs through deployable software and operational handoff. A model for wafers at
risk needs the fab database and a repeatable data pipeline. It also needs an
interface or report that engineers can access. Production teams need enough
context for a choice. They can run a qual, watch a tool or wait because
processing has stopped.[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]]

These maintenance and yield patterns extend to chemical and coating production.
In [[person:rosonaeldred=>Rosona Eldred]]'s small-data industrial ML examples,
quality control monitors input-output ratios and flags anomalies that trigger a
technician visit. Packing-peanut and blue-paint production show that predictive
maintenance in process industries depends more on fixed sensor placement and
batch traceability than on internet-scale data volume. The regulatory layer adds
sustainability and compliance tracking, which can force reformulation using
small historical experiment data.[[cite:industrial-data-small-data-production-machine-learning=>Industrial Small-Data ML]]

## Related Pages

These pages give the surrounding vocabulary for Dashel's semiconductor example.

- [[Industrial ML Applications]] for physical and operational ML systems beyond semiconductor fabs.
- [[Machine Learning]] for applied modeling, evaluation, deployment, and business tradeoffs.
- [[Data Engineering]] for the pipeline and database work behind usable manufacturing analytics.
- [[Interpretability]] for explaining model behavior well enough to support decisions.
- [[Model Monitoring]] for watching deployed models, inputs, predictions, and outcomes.
- [[Production]] for the operating boundary where people depend on a system.
