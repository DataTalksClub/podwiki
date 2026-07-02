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
[[machine learning]] model can
predict an error. The model has to fit an
[[industrial-ml-applications|industrial ML application]]
where wafers and tools define part of the context. Quals, engineers, and
production staff define the operating constraints.

This pattern comes from semiconductor production work at Microchip
([[person:dashelruizperez|Dashel Ruiz Perez]],
[[podcast:from-semiconductor-data-to-applied-machine-learning|From Semiconductor Data to Applied Machine Learning]]).
The example starts on the fab floor and moves through yield analytics and
[[data engineering]] to a practical boundary. A prediction is useful only if
supervisors and engineers can understand it and act on it in
[[production]]
([[podcast:from-semiconductor-data-to-applied-machine-learning|4:49-5:49, 18:07-20:40, 23:29-29:06, 37:29-43:38]]).

## Fab Telemetry

The semiconductor example begins with physical tool behavior rather than a
modeling technique. Chip processes run in large fab tools, and engineers look at
tool log files when they run experiments or diagnose issues. Those logs include
tool identity and process steps. They also record pressure, gas amounts, and
other details at millisecond resolution.

That creates far more data than a technician can comfortably review by hand
([[podcast:from-semiconductor-data-to-applied-machine-learning|8:49-11:06]]).

It makes manufacturing predictive maintenance a telemetry and workflow problem
before it's an algorithm problem. A person needs to know which fab area
produced the signal and which process step was running. They also need to know
what the tool was supposed to do, plus which error messages or measurements
matter. Dashel's path from expediter to process technician mattered because
walking wafers through the fab gave him context. Later experiment work gave him
more context for interpreting the logs, not just access to files
([[podcast:from-semiconductor-data-to-applied-machine-learning|4:49-5:49, 8:49-10:23]]).

## Yield Analytics

Yield analytics depended on getting cross-area data into a usable format. The
yield role involved cleaning production data with Python and loading it into an
Oracle database, plus writing small PL/SQL applications so a supervisor could
access the results. Yield work needs a whole-fab view of failures, passes,
source areas, and production contacts who could answer follow-up questions
([[podcast:from-semiconductor-data-to-applied-machine-learning|18:07-20:40]]).

The work is close to [[data engineering]]
inside a manufacturing process. A single clean training table wasn't the main
asset; knowing where data lived, how tools mapped to fab areas, and how to make
answers reachable for the people requesting them mattered more.

Production roles, technician roles, and engineering work teach where to go and
whom to ask when a yield request arrives
([[podcast:from-semiconductor-data-to-applied-machine-learning|19:11-20:40]]).

## Wafers at Risk

A fab can estimate when a tool should be checked, acting before the normal
schedule allows too many wafers to be exposed to risk. Tools had weekly,
biweekly, or monthly qualification checks called quals. The open question was
whether the schedule should depend on the number of wafers processed rather than
elapsed time
([[podcast:from-semiconductor-data-to-applied-machine-learning|21:39-23:29]]).

A "wafers at risk" project counted wafer process steps across the production
database for the whole fab, then calculated risk by tool and area. Those counts
project how many wafers would be at risk if the fab kept running at the current
pace. A useful forecast could tell engineers to run quals earlier, for example
after ten days instead of fifteen, reducing waste and improving yield
([[podcast:from-semiconductor-data-to-applied-machine-learning|23:29-25:16]]).

The decision target wasn't an abstract accuracy score, but a way to tell
engineers that a tool might have a probable issue within a window. They could
then monitor the tool and plan a check between roughly three and twelve days if
measurements stayed in range
([[podcast:from-semiconductor-data-to-applied-machine-learning|27:55-29:06]]).
Use [[model monitoring]] for the
broader production work where teams keep watching model inputs, predictions,
and business outcomes after deployment.

## Explainability

The manufacturing constraint is that a better number isn't enough. Algorithms
such as Bayesian methods and random forests moved accuracy from around 65% to
around 85% after tweaks, but the result still couldn't be used because the steps
couldn't be explained to a supervisor
([[podcast:from-semiconductor-data-to-applied-machine-learning|25:16-26:08]]).

In a fab, practical [[interpretability]]
supports maintenance or yield decisions. The explanation needs to cover the
tool, the window, the risk level, and the action an engineer should take.
Predictions need to be both better and explainable enough for the people
responsible for the tools
([[podcast:from-semiconductor-data-to-applied-machine-learning|25:35-28:33]]).

## Production Use

Notebook results contrast with systems other people can use, built with tools
such as Flask and REST APIs, simple authentication, cloud deployment, and
containers
([[podcast:from-semiconductor-data-to-applied-machine-learning|From Semiconductor Data to Applied Machine Learning]]).

Access mattered because someone should be able to send data and get a result.
At Microchip, the supervisor didn't only care that a prediction existed; they
needed to know how to get the data and result
([[podcast:from-semiconductor-data-to-applied-machine-learning|37:29-43:38]]).

For manufacturing predictive maintenance, the path from telemetry to impact
runs through deployable software and operational handoff. A model for wafers at
risk needs the fab database and a repeatable data pipeline. It also needs an
interface or report that engineers can access. Production teams need enough
context for a choice. They can run a qual, watch a tool or wait because
processing has stopped
([[podcast:from-semiconductor-data-to-applied-machine-learning|18:38-20:40, 23:29-29:06, 41:08-43:38]]).

These patterns extend to chemical and coating production
([[person:rosonaeldred|Rosona]],
[[podcast:industrial-data-small-data-production-machine-learning|Industrial Data and Small-Data Production ML]]).
Quality control here monitors input-output ratios — one kilo in, one kilo out —
and flags anomalies that trigger a technician visit. Packing-peanut and
blue-paint production show that predictive maintenance in process industries
depends more on fixed sensor placement and batch traceability than on
internet-scale data volume. The regulatory layer adds sustainability and
compliance tracking, which can force reformulation using small historical
experiment data.

## Related Pages

These pages give the surrounding vocabulary for Dashel's semiconductor example.

- [[Industrial ML Applications]] for physical and operational ML systems beyond semiconductor fabs.
- [[Machine Learning]] for applied modeling, evaluation, deployment, and business tradeoffs.
- [[Data Engineering]] for the pipeline and database work behind usable manufacturing analytics.
- [[Interpretability]] for explaining model behavior well enough to support decisions.
- [[Model Monitoring]] for watching deployed models, inputs, predictions, and outcomes.
- [[Production]] for the operating boundary where people depend on a system.
