# Wiki Taxonomy Log

Record deliberate changes to the working vocabulary here so future agents can
see why a topic exists and what it should connect to.

## 2026-09-04

- Added the event entity family: `_events/` registry (webinars, workshops,
  conferences synced from `../datatalksclub.github.io/_data/events.yaml`),
  `event` graph node type, `[[event:<video-id>=>Label]]` chips, and
  event->speaker / event->topic graph edges. Concept extraction from 182
  recording transcripts introduced ten new topic labels with no existing wiki
  page: `bayesian-inference` (PyMC parameter-estimation webinar),
  `prometheus` (Python app observability workshop), `feature-selection`
  (feature-engine/scikit-learn webinar), `geospatial-data` (Planet geospatial
  stack webinar), `time-series-forecasting` (two forecasting events),
  `llm-fine-tuning` (Qwen3 LoRA fine-tuning workshop),
  `knowledge-graphs` (dlt + Cognee knowledge-graph workshop),
  `data-storytelling` (Altair storytelling workshop), `terraform`
  (Terraform for data engineering workshop), and `neuroscience-data-science`
  (brain-modeling webinar). Each should graduate to a wiki concept hub when
  podcast evidence for it accumulates.

## 2026-09-04

- Added the Zoomcamp course page family, grounded in the course repositories
  under `../` (DataTalksClub GitHub org repos). Amended 2026-09-04 after the
  standalone-wiki decision: the collection carries course pages plus concept
  pages extracted from course content, holds no podcast citations or wiki
  links, and forms an isolated component of the graph (label resolution is
  collection-scoped; `related_course:` resolves only within the collection).
  Extended 2026-09-04 to the full Course -> Module -> Video structure from the
  issue: 40 generated module pages and 285 generated per-video note pages
  (shared note template: notes, key concepts, Related Notes, source links),
  produced by `scripts/build_course_wiki.py` from the course repos: `_course_wiki/zoomcamps.md` as the family hub plus
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
