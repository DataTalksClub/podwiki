# Wiki Taxonomy Log

Record deliberate changes to the working vocabulary here so future agents can
see why a topic exists and what it should connect to.

## 2026-09-04

- Added the event entity family: `_events/` registry (webinars, workshops,
  conferences synced from `../datatalksclub.github.io/_data/events.yaml`),
  `event` graph node type, `[[event:<video-id>=>Label]]` chips, and
  event->speaker / event->topic graph edges. Concept extraction from recordings
  introduced five new topic labels with no existing wiki page:
  `bayesian-inference` (PyMC parameter-estimation webinar),
  `prometheus` (Python app observability workshop), `feature-selection`
  (feature-engine/scikit-learn webinar), `geospatial-data` (Planet geospatial
  stack webinar), and `time-series-forecasting` (two forecasting events). Each
  should graduate to a wiki concept hub when podcast evidence for it
  accumulates.

## 2026-09-04

- Added the Zoomcamp course page family, grounded in the course repositories
  under `../` (DataTalksClub GitHub org repos) and in podcast learner and
  teaching evidence: `_course_wiki/zoomcamps.md` as the family hub plus
  `_course_wiki/machine-learning-zoomcamp.md`,
  `_course_wiki/data-engineering-zoomcamp.md`,
  `_course_wiki/mlops-zoomcamp.md`, `_course_wiki/llm-zoomcamp.md`,
  `_course_wiki/ai-dev-tools-zoomcamp.md`, and
  `_course_wiki/stock-markets-analytics-zoomcamp.md`, in a separate
  `course_wiki` collection served under `/course-wiki/` (plain Markdown links;
  the chips extension only processes `_wiki/`). Requested via
  datatalksclub.github.io issue #89 (knowledge layer over the Zoomcamp
  courses). Course pages are untagged reference pages: each carries the
  module map, prerequisites, project/certificate rules, and the podcast
  discussions around the course. They route to the concept hubs ([[Machine
  Learning]], [[Data Engineering]], [[MLOps]], [[LLMs]], [[AI Coding Tools]],
  [[Python Stock Analysis]]) and the matching roadmap, portfolio, and
  certification pages; those hubs link back. Maintenance rule: when a course
  repo changes its syllabus or cohort model, refresh the matching wiki page
  from the repo README and keep podcast citations episode-grounded.

## 2026-07-06

- Added `_wiki/data-contracts.md` as a concept hub for producer-consumer
  agreements around schemas, quality, ownership, service levels, and change
  review. It connects Data Mesh, DataOps, data governance, data quality,
  streaming, self-service platforms, and data product management.
