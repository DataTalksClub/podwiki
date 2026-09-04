#!/usr/bin/env python3
"""Generate the course wiki's module and per-video note pages.

Implements the knowledge layer described in datatalksclub.github.io issue #89
for the podwiki course wiki (_course_wiki/): a Course -> Module -> Video
hierarchy where every lesson gets a structured note page built from a shared
template (summary, notes, key concepts linked to the concept glossary, and an
auto-generated Related Notes section).

Source of truth is the course repositories cloned next to this repo
(../<repo>). Re-run after the repos change; the generated pages refresh in
place. Concept pages and the curated course pages are NOT touched by this
script — only module (`*-module-*`) and note (`*-lesson-*`) pages are managed
here, keyed by slug so reruns are idempotent.

Usage:
    python scripts/build_course_wiki.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_WIKI = ROOT / "_course_wiki"
REPOS = ROOT.parent

YT_RE = re.compile(r"https?://(?:www\.)?youtube\.com/(?:watch\?v=|live/)[\w\-&=]*")
YT_ID_RE = re.compile(r"(?:watch\?v=|live/)([\w\-]{6,})")
IMG_RE = re.compile(r"!\[\[[^\]]*\]\([^)]*\)|!\[[^\]]*\]\([^)]*\)")
HTML_ANCHOR_RE = re.compile(r"<a href=\"[^\"]*\">\s*</a>|<a [^>]*>.*?</a>", re.S)
HTML_IMG_RE = re.compile(r"<img[^>]*>")


@dataclass
class Lesson:
    """One video/lesson inside a module."""

    label: str
    title: str
    youtube: str | None
    repo_path: str | None
    body: str
    summary: str
    concepts: list[str] = field(default_factory=list)
    slug: str = ""
    module_slug: str = ""


@dataclass
class Module:
    label: str
    number: str
    title: str
    overview: str
    lessons: list[Lesson] = field(default_factory=list)
    slug: str = ""
    course: "Course | None" = None

    @property
    def concepts(self) -> list[str]:
        seen: list[str] = []
        for lesson in self.lessons:
            for c in lesson.concepts:
                if c not in seen:
                    seen.append(c)
        return seen


@dataclass
class Course:
    repo: str
    prefix: str
    name: str
    modules: list[Module] = field(default_factory=list)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def clean_body(text: str) -> str:
    text = re.sub(
        r"\[([^\]]*)\]\((?!https?://)[^)]*\)",
        r"\1",
        text,
    )
    text = IMG_RE.sub("", text)
    text = HTML_IMG_RE.sub("", text)
    text = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def yq(text: str) -> str:
    """Make a string safe for a double-quoted YAML scalar."""
    return re.sub(r'["\\]', "'", text).strip()


def tidy(text: str, limit: int = 240) -> str:
    text = re.sub(r"[\*`~^]|\$[^$]*\$", "", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(",;:. ") + "..."
    return text


def first_heading(text: str) -> str | None:
    m = re.search(r"^#{1,2}\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def find_youtube(text: str) -> str | None:
    m = YT_RE.search(text)
    url = m.group(0).rstrip("&=") if m else None
    if url and url.endswith("?v="):
        url = url[:-3]
    return url


# Concept glossary: slug -> (title, aliases). Aliases are matched as whole
# words inside lesson notes to build the Key Concepts section.
def load_concepts() -> dict[str, dict]:
    concepts: dict[str, dict] = {}
    alias_extra = {
        "gradient-boosting": ["xgboost", "boosting"],
        "serverless-deployment": ["aws lambda", "lambda function", "api gateway"],
        "classification-metrics": ["rmse", "roc", "auc", "precision", "recall", "confusion matrix", "f1"],
        "model-registry": ["model registry"],
        "workflow-orchestration": ["orchestrator", "orchestration"],
        "stream-processing": ["stream processing", "flink"],
        "context-engineering": ["agents.md", "context engineering"],
        "loop-and-graph-engineering": ["loop engineering", "graph engineering"],
        "agent-skills-and-subagents": ["skill.md", "subagent", "subagents", "skills"],
        "time-series-decomposition": ["seasonality", "trend", "decomposition"],
        "technical-indicators": ["ta-lib", "talib", "technical indicators", "indicators"],
        "backtesting": ["simulation", "backtest"],
        "llm-evaluation": ["llm-as-a-judge", "golden", "evaluation"],
        "hybrid-search": ["hybrid search"],
        "reranking": ["rerank", "reranking"],
        "deployment-automation": ["cron", "airflow", "automation"],
        "transfer-learning": ["transfer learning", "pretrained", "xception"],
        "neural-networks": ["neural network", "neural networks", "deep learning", "cnn", "convolutional"],
        "kubernetes": ["kubernetes", "kubectl"],
        "partitioning-and-clustering": ["partitioning", "clustering"],
        "analytics-engineering": ["analytics engineering"],
        "spec-driven-development": ["spec-driven", "specification", "backlog"],
        "openapi-contract": ["openapi"],
        "opentelemetry": ["opentelemetry", "loki", "tempo", "traces"],
        "playwright": ["playwright"],
        "mcp": ["mcp", "model context protocol"],
        "git-worktrees": ["worktree", "worktrees"],
        "ci-cd": ["ci/cd", "github actions", "continuous integration"],
        "evidently": ["evidently"],
        "prometheus-and-grafana": ["prometheus", "grafana"],
        "mlflow": ["mlflow"],
        "experiment-tracking": ["experiment tracking", "tracking"],
        "model-monitoring": ["monitoring"],
        "market-data-apis": ["yfinance", "finance api", "market data"],
        "pandas": ["pandas", "dataframe"],
        "embeddings": ["embedding", "embeddings"],
        "vector-search": ["vector search", "pgvector", "minsearch", "sqlitesearch"],
        "keyword-search": ["keyword search", "inverted index", "full-text"],
        "function-calling": ["function calling"],
        "dbt": ["dbt"],
        "bigquery": ["bigquery"],
        "spark": ["spark"],
        "kafka": ["kafka"],
        "dlt": ["dlt"],
        "kestra": ["kestra"],
        "docker": ["docker"],
        "fastapi": ["fastapi"],
        "terraform": ["terraform"],
        "bruin": ["bruin"],
        "rag": ["rag", "retrieval-augmented"],
        "agentic-rag": ["agentic"],
        "langchain": ["langchain"],
        "crisp-dm": ["crisp-dm", "crisp dm"],
        "regularization": ["regularization"],
        "linear-regression": ["linear regression"],
        "logistic-regression": ["logistic regression"],
        "decision-trees": ["decision tree", "decision trees", "random forest"],
        "model-deployment": ["deployment", "deploying"],
        "risk-management": ["risk management"],
        "trading-strategy": ["trading strategy", "strategy"],
        "mlops-maturity-model": ["maturity model"],
        "coding-agents": ["coding agent", "coding agents"],
        "playwright-placeholder": None,
    }
    for p in COURSE_WIKI.glob("*.md"):
        stem = p.stem
        if stem in {
            "zoomcamps", "machine-learning-zoomcamp", "data-engineering-zoomcamp",
            "mlops-zoomcamp", "llm-zoomcamp", "ai-dev-tools-zoomcamp",
            "stock-markets-analytics-zoomcamp",
        }:
            continue
        if "-" not in stem:
            continue
        t = p.read_text(encoding="utf-8")
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M)
        title = m.group(1) if m else stem
        aliases = alias_extra.get(stem, [])
        concepts[stem] = {"title": title, "aliases": sorted(set([title.lower()] + [a.lower() for a in aliases]), key=len, reverse=True)}
    concepts.pop("playwright-placeholder", None)
    return concepts


CONCEPTS = load_concepts()


def detect_concepts(text: str) -> list[str]:
    low = f" {text.lower()} "
    found = []
    for slug, meta in CONCEPTS.items():
        for alias in meta["aliases"]:
            if re.search(rf"(?<![\w-]){re.escape(alias)}(?![\w-])", low):
                found.append(slug)
                break
    return found


def parse_repo_readme_modules(repo_dir: Path) -> list[tuple[str, str, str]]:
    """(label, title, link) triples from the repo's main README syllabus."""
    readme = repo_dir / "README.md"
    out = []
    if not readme.exists():
        return out
    for m in re.finditer(r"^#{2,3}\s+\[?(Module[^\]]*?)\]?\(([^)]+)\)", readme.read_text(encoding="utf-8"), re.M):
        label_title, link = m.group(1).strip(), m.group(2).strip()
        mm = re.match(r"(Module\s*\d*)\s*:?\s*(.*)", label_title)
        label, title = mm.group(1).strip(), mm.group(2).strip()
        if title.endswith("/") or title.endswith(".md") or not title:
            title = label
        if link.startswith(("#", "http")):
            continue
        out.append((label, title, link))
    return out


def module_number(label: str, dir_name: str = "") -> int:
    m = re.search(r"(\d+)", label or "")
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)", dir_name or "")
    return int(m.group(1)) if m else -1


def parse_cohort_lessons(repo: str, prefix: str, name: str) -> Course:
    repo_dir = REPOS / repo
    course = Course(repo=repo, prefix=prefix, name=name)
    modules_info = parse_repo_readme_modules(repo_dir)
    cohort_dir = repo_dir / "cohorts" / "2026"
    dirs = sorted([d for d in cohort_dir.iterdir() if d.is_dir() and re.match(r"\d", d.name)]) if cohort_dir.exists() else []
    for d in dirs:
        num = d.name.split("-")[0]
        info = next((i for i in modules_info if module_number(i[0], "") == int(num)), None)
        label = info[0] if info else f"Module {num}"
        title = info[1] if info else d.name
        overview = ""
        readme = d / "README.md"
        if readme.exists():
            rt = readme.read_text(encoding="utf-8")
            overview = clean_body(rt)[:600]
        mod = Module(label=label, number=num, title=title, overview=overview)
        mod.course = course
        mod.slug = f"{prefix}-module-{num}"
        mod_root_dir = False
        files = sorted(d.glob("*.md"))
        for f in files:
            if f.name.lower() in {"homework.md", "project.md", "schedule.md"}:
                continue
            if f.name.lower() == "readme.md" and not mod_root_dir:
                continue
            raw = f.read_text(encoding="utf-8")
            ltitle = first_heading(raw) or f.stem.replace("-", " ").title()
            body = clean_body(raw)
            m = re.search(r"^## Notes\s*$", body, re.M)
            core = body[m.end():].strip() if m else body
            summary = next((p for p in re.split(r"\n\s*\n", core) if len(p.strip()) > 40), core[:280])
            rel = f.relative_to(REPOS)
            lesson = Lesson(
                label=f.stem,
                title=ltitle,
                youtube=find_youtube(raw),
                repo_path=f"{repo}/blob/main/{rel}",
                body=core[:4000],
                summary=summary[:300],
            )
            lesson.concepts = detect_concepts(f"{ltitle}\n{core}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        course.modules.append(mod)
    covered = {int(m.number) for m in course.modules if m.number.isdigit()}
    for label, title, link in modules_info:
        num = module_number(label)
        if num in covered or num == -1:
            continue
        d = repo_dir / link.strip("/")
        if not d.is_dir():
            continue
        mod = Module(label=label, number=str(num), title=title, overview="")
        mod.course = course
        mod.slug = f"{prefix}-module-{num:02d}"
        mod_root_dir = True
        for f in sorted(d.glob("*.md")):
            if f.name.lower() in {"homework.md", "project.md", "schedule.md"}:
                continue
            raw = f.read_text(encoding="utf-8")
            ltitle = first_heading(raw) or f.stem.replace("-", " ").title()
            body = clean_body(raw)
            summary = next((q for q in re.split(r"\n\s*\n", body) if len(q.strip()) > 40), body[:280])
            lesson = Lesson(
                label=f.stem,
                title=ltitle,
                youtube=find_youtube(raw),
                repo_path=f"{repo}/blob/main/{f.relative_to(REPOS)}",
                body=body[:4000],
                summary=summary[:300],
            )
            lesson.concepts = detect_concepts(f"{ltitle}\n{body}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        course.modules.append(mod)
        covered.add(num)
    course.modules.sort(key=lambda m: int(m.number) if m.number.isdigit() else 99)
    return course


def parse_readme_sections(repo: str, prefix: str, name: str, course_page_slug: str) -> Course:
    """MLOps-style: numbered `## N.M` sections with videos in module READMEs."""
    repo_dir = REPOS / repo
    course = Course(repo=repo, prefix=prefix, name=name)
    modules_info = parse_repo_readme_modules(repo_dir)
    module_dirs = sorted([d for d in repo_dir.iterdir() if d.is_dir() and re.match(r"\d", d.name)])
    for d in module_dirs:
        num = d.name.split("-")[0]
        info = next((i for i in modules_info if module_number(i[0], "") == int(num)), None)
        label = info[0] if info else f"Module {num}"
        title = info[1] if info else d.name
        if title == d.name and (d / "README.md").exists():
            title = first_heading((d / "README.md").read_text(encoding="utf-8")) or title
        mod = Module(label=label, number=num, title=title, overview="")
        mod.course = course
        mod.slug = f"{prefix}-module-{num}"
        readme = d / "README.md"
        if not readme.exists():
            course.modules.append(mod)
            continue
        raw = readme.read_text(encoding="utf-8")
        overview = clean_body(raw)[:600]
        sections = re.split(r"^###?\s+(?=\d+\.\d+[.\s])", raw, flags=re.M)
        if len(sections) <= 1:
            sections = re.split(r"^##\s+(?=\d+\.\d+)", raw, flags=re.M)[1:]
        for sec in sections[1:] if sections and not re.match(r"###?\s+\d", sections[0]) else sections:
            lines = sec.strip().split("\n")
            if not lines:
                continue
            head = lines[0].lstrip("#").strip()
            sm = re.match(r"(\d+\.\d+)[.\s]*(.*)", head)
            if not sm:
                continue
            ltitle = sm.group(2).strip() or f"Lesson {sm.group(1)}"
            sec_text = "\n".join(lines[1:])
            core = clean_body(sec_text)
            core = re.sub(r"\[See code here\]\([^)]*\)", "", core)
            summary = next((p for p in re.split(r"\n\s*\n", core) if len(p.strip()) > 40), core[:280])
            lesson = Lesson(
                label=sm.group(1),
                title=ltitle,
                youtube=find_youtube(sec_text),
                repo_path=f"{repo}/blob/main/{d.name}/README.md",
                body=core[:3500],
                summary=summary[:300],
            )
            lesson.concepts = detect_concepts(f"{ltitle}\n{core}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        if not mod.lessons:
            lesson = Lesson(
                label="overview",
                title=title,
                youtube=find_youtube(raw),
                repo_path=f"{repo}/blob/main/{d.name}/README.md",
                body=f"{clean_body(raw)[:2500]}",
                summary=f"Module overview and materials for {title}.",
            )
            lesson.concepts = detect_concepts(f"{title}\n{raw}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        course.modules.append(mod)
    return course


def parse_readme_videos(repo: str, prefix: str, name: str) -> Course:
    """DEZ-style: `:movie_camera:` video entries inside module READMEs."""
    repo_dir = REPOS / repo
    course = Course(repo=repo, prefix=prefix, name=name)
    modules_info = parse_repo_readme_modules(repo_dir)
    module_dirs = sorted([d for d in repo_dir.iterdir() if d.is_dir() and re.match(r"\d", d.name)])
    for d in module_dirs:
        num = d.name.split("-")[0]
        info = next((i for i in modules_info if module_number(i[0], "") == int(num)), None)
        label = info[0] if info else f"Module {num}"
        title = info[1] if info else d.name
        if title == d.name and (d / "README.md").exists():
            title = first_heading((d / "README.md").read_text(encoding="utf-8")) or title
        mod = Module(label=label, number=num, title=title, overview="")
        mod.course = course
        mod.slug = f"{prefix}-module-{num}"
        readme = d / "README.md"
        if not readme.exists():
            course.modules.append(mod)
            continue
        raw = readme.read_text(encoding="utf-8")
        blocks = re.split(r"^#{2,4}\s+", raw, flags=re.M)
        for block in blocks:
            head = block.split("\n", 1)[0]
            if ":movie_camera:" not in head and "workshop" not in head.lower():
                continue
            ltitle = re.sub(r":movie_camera:", "", head).strip()
            ltitle = re.sub(r"^[\d.]+\s*", "", ltitle).strip(" -")
            if not ltitle or len(ltitle) > 90:
                continue
            sec_text = block
            core = clean_body(sec_text)
            yt = find_youtube(sec_text)
            if not yt and "youtu" not in sec_text:
                # keep entry only when a video link exists
                continue
            summary = next((p for p in re.split(r"\n\s*\n", core) if len(p.strip()) > 40), core[:280])
            lesson = Lesson(
                label=slugify(ltitle)[:24],
                title=ltitle,
                youtube=yt,
                repo_path=f"{repo}/blob/main/{d.name}/README.md",
                body=core[:2500],
                summary=summary[:300],
            )
            lesson.concepts = detect_concepts(f"{ltitle}\n{core}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        entry_pats = [
            re.compile(
                r"\*\*(\d[\d.]+ - [^*\n]{3,90})\*\*.{0,220}?\((https?://(?:www\.)?youtu[^)\s]+)\)",
                re.S,
            ),
            re.compile(
                r"[:*]\s*:movie_camera:\s*(\d[\d.]*\s[^\n]{3,90})\s*\n.{0,220}?\((https?://(?:www\.)?youtu[^)\s]+)\)",
                re.S,
            ),
        ]
        seen_entries = set()
        for pat in entry_pats:
            for m in pat.finditer(raw):
                ltitle = m.group(1).strip()
                yt = m.group(2)
                if yt.startswith("https://youtu.be/"):
                    yt = "https://www.youtube.com/watch?v=" + yt.rsplit("/", 1)[-1].split("?")[0]
                key = slugify(ltitle)[:40]
                if key in seen_entries:
                    continue
                seen_entries.add(key)
                lesson = Lesson(
                    label=slugify(ltitle)[:24],
                    title=ltitle,
                    youtube=yt,
                    repo_path=f"{repo}/blob/main/{d.name}/README.md",
                    body=f"The recorded lesson for {ltitle.strip()} in {mod.label.lower()} of {course.name}.",
                    summary=f"Recorded lesson: {ltitle.strip()}.",
                )
                lesson.concepts = detect_concepts(ltitle)
                lesson.module_slug = mod.slug
                mod.lessons.append(lesson)
        if not mod.lessons:
            yt = find_youtube(raw)
            lesson = Lesson(
                label="overview",
                title=title,
                youtube=yt,
                repo_path=f"{repo}/blob/main/{d.name}/README.md",
                body=f"{clean_body(raw)[:2500]}",
                summary=f"Module overview and materials for {title}.",
            )
            lesson.concepts = detect_concepts(f"{title}\n{raw}")
            lesson.module_slug = mod.slug
            mod.lessons.append(lesson)
        seen_titles = set()
        deduped = []
        for lesson in mod.lessons:
            key = slugify(lesson.title)[:40]
            if key in seen_titles:
                continue
            seen_titles.add(key)
            deduped.append(lesson)
        mod.lessons = deduped
        course.modules.append(mod)
    return course


def parse_module_readmes(repo: str, prefix: str, name: str) -> Course:
    """SMA-style: one livestream + materials per module README."""
    repo_dir = REPOS / repo
    course = Course(repo=repo, prefix=prefix, name=name)
    modules_info = parse_repo_readme_modules(repo_dir)
    module_dirs = sorted([d for d in repo_dir.iterdir() if d.is_dir() and re.match(r"\d", d.name)])
    for d in module_dirs:
        num = d.name.split("-")[0]
        info = next((i for i in modules_info if module_number(i[0], "") == int(num)), None)
        label = info[0] if info else f"Module {num}"
        title = info[1] if info else d.name
        if title == d.name and (d / "README.md").exists():
            title = first_heading((d / "README.md").read_text(encoding="utf-8")) or title
        mod = Module(label=label, number=num, title=title, overview="")
        mod.course = course
        mod.slug = f"{prefix}-module-{num}"
        readme = d / "README.md"
        if not readme.exists():
            course.modules.append(mod)
            continue
        raw = readme.read_text(encoding="utf-8")
        core = clean_body(raw)
        links = re.findall(r"\[([^\]]{4,60})\]\((https?://[^\)]+)\)", raw)
        yt = find_youtube(raw)
        slides = next((u for t, u in links if "slides" in t.lower()), None)
        colab = next((u for t, u in links if "colab" in t.lower()), None)
        lesson = Lesson(
            label="livestream",
            title=title,
            youtube=yt,
            repo_path=f"{repo}/blob/main/{d.name}/README.md",
            body=f"{core[:2500]}",
            summary=f"Livestream, slides, and Colab materials for {title}.",
        )
        lesson.concepts = detect_concepts(f"{title}\n{core}")
        lesson.module_slug = mod.slug
        mod.lessons.append(lesson)
        course.modules.append(mod)
    return course


COURSE_SPECS = [
    ("machine-learning-zoomcamp", "mlz", "Machine Learning Zoomcamp", "cohort_lessons"),
    ("llm-zoomcamp", "llmz", "LLM Zoomcamp", "cohort_lessons"),
    ("ai-dev-tools-zoomcamp", "aidt", "AI Dev Tools Zoomcamp", "cohort_lessons"),
    ("mlops-zoomcamp", "mlops", "MLOps Zoomcamp", "readme_sections"),
    ("data-engineering-zoomcamp", "dez", "Data Engineering Zoomcamp", "readme_videos"),
    ("stock-markets-analytics-zoomcamp", "sma", "Stock Markets Analytics Zoomcamp", "module_readmes"),
]


def load_courses() -> list[Course]:
    courses = []
    for repo, prefix, name, kind in COURSE_SPECS:
        if kind == "cohort_lessons":
            courses.append(parse_cohort_lessons(repo, prefix, name))
        elif kind == "readme_sections":
            courses.append(parse_readme_sections(repo, prefix, name, ""))
        elif kind == "readme_videos":
            courses.append(parse_readme_videos(repo, prefix, name))
        else:
            courses.append(parse_module_readmes(repo, prefix, name))
    return courses


USED_SLUGS: set[str] = set()


def lesson_slug(course: Course, mod: Module, lesson: Lesson) -> str:
    base = f"{course.prefix}-m{mod.number.zfill(2)}-{slugify(lesson.title)[:48]}"
    slug = base
    n = 2
    while slug in USED_SLUGS:
        slug = f"{base}-{n}"
        n += 1
    USED_SLUGS.add(slug)
    return slug


def write_page(name: str, text: str) -> None:
    (COURSE_WIKI / name).write_text(text.strip() + "\n")


def build(courses: list[Course]) -> None:
    # clear previously generated module/note pages so renames don't leave
    # stale orphans behind (curated course pages and concept pages are kept).
    gen_re = re.compile(
        r"^(?:"
        + "|".join(spec[1] for spec in COURSE_SPECS)
        + r")-(?:module-\d+|m\d+-)"
    )
    for p in COURSE_WIKI.glob("*.md"):
        if gen_re.match(p.stem):
            p.unlink()

    # assign slugs
    all_lessons: list[tuple[Course, Module, Lesson]] = []
    for course in courses:
        for mod in course.modules:
            for lesson in mod.lessons:
                lesson.slug = lesson_slug(course, mod, lesson)
                all_lessons.append((course, mod, lesson))

    # Related notes: same-module siblings first, then same-course notes sharing
    # a concept, then same-course neighbors. Pairs are symmetric so every note
    # keeps at least six inbound links (the graph connectivity gate).
    partners: dict[str, set[str]] = {}
    for i, (c1, m1, l1) in enumerate(all_lessons):
        mine = partners.setdefault(l1.slug, set())
        for j, (c2, m2, l2) in enumerate(all_lessons):
            if i == j:
                continue
            same_module = c1 is c2 and m1 is m2
            same_course = c1 is c2
            shared = bool(set(l1.concepts) & set(l2.concepts))
            if same_module or (same_course and shared):
                mine.add(l2.slug)
    for i, (c1, m1, l1) in enumerate(all_lessons):
        mine = partners[l1.slug]
        if len(mine) < 6:
            for j, (c2, m2, l2) in enumerate(all_lessons):
                if len(mine) >= 6:
                    break
                if c1 is c2 and l2.slug != l1.slug:
                    mine.add(l2.slug)
        if len(mine) < 6:
            for j, (c2, m2, l2) in enumerate(all_lessons):
                if len(mine) >= 6:
                    break
                if l2.slug != l1.slug and set(l1.concepts) & set(l2.concepts):
                    mine.add(l2.slug)
        if len(mine) < 6:
            for j, (c2, m2, l2) in enumerate(all_lessons):
                if len(mine) >= 6:
                    break
                if l2.slug != l1.slug:
                    mine.add(l2.slug)
        for p in mine:
            partners.setdefault(p, set()).add(l1.slug)

    for course in courses:
        for mod in course.modules:
            for lesson in mod.lessons:
                lesson.partners = sorted(partners.get(lesson.slug, []))  # type: ignore[attr-defined]

    # module pages
    for course in courses:
        for mod in course.modules:
            lesson_rows = []
            for lesson in mod.lessons:
                video = f"[video]({lesson.youtube})" if lesson.youtube else ""
                lesson_rows.append(
                    f"| [{lesson.title}](/course-wiki/{lesson.slug}/) | {video} |"
                )
            concepts = ""
            if mod.concepts:
                concepts = "\n".join(
                    f"- [{CONCEPTS[c]['title']}](/course-wiki/{c}/)" for c in mod.concepts
                )
            siblings = [m for m in course.modules if m is not mod]
            sib = "\n".join(f"- [{m.label}: {m.title}](/course-wiki/{m.slug}/)" for m in siblings)
            write_page(f"{mod.slug}.md", f"""---
title: "{mod.label}: {mod.title} — {course.name}"
summary: "Lessons, materials, and key concepts for {mod.label.lower()} of {course.name}."
related_course:
  - {course.name}
---

[{course.name}](/course-wiki/{slugify(course.name)}/) > {mod.label}: {mod.title}

{mod.overview or (f"The lessons, homework, and materials of {mod.label.lower()} of {course.name}.")

if True else ""}

## Lessons

| Lesson | Video |
|---|---|
{chr(10).join(lesson_rows)}

## Key concepts

{concepts or "_See the lesson notes for the concepts covered in this module._"}

Homework and deadlines live in the course repository:
[{course.repo}](https://github.com/DataTalksClub/{course.repo}).

## Other modules in this course

{sib}
""")

    # note pages
    for course in courses:
        for mod in course.modules:
            for lesson in mod.lessons:
                concepts = "\n".join(
                    f"- [{CONCEPTS[c]['title']}](/course-wiki/{c}/)" for c in lesson.concepts
                )
                related = "\n".join(
                    f"- [{s}](/course-wiki/{s}/)" for s in lesson.partners
                )
                video = f"- [Video]({lesson.youtube})" if lesson.youtube else ""
                sources = "\n".join(x for x in [
                    video,
                    f"- [Lesson file](https://github.com/{lesson.repo_path})" if lesson.repo_path else "",
                ] if x)
                write_page(f"{lesson.slug}.md", f"""---
title: "{yq(lesson.title)} — {course.name} {yq(mod.label)}"
summary: "{yq(tidy(lesson.summary))}"
related_course:
  - {mod.slug}
---

[{course.name}](/course-wiki/{slugify(course.name)}/) › [{mod.label}: {mod.title}](/course-wiki/{mod.slug}/) › {lesson.title}

## Notes

{lesson.body}

## Key concepts

{concepts or "_No glossary concepts detected in this lesson._"}

## Related notes

{related}

## Sources

{sources}
""")

    total_lessons = sum(len(m.lessons) for c in courses for m in c.modules)
    total_modules = sum(len(c.modules) for c in courses)
    print(f"generated {total_modules} module pages and {total_lessons} note pages")


if __name__ == "__main__":
    build(load_courses())
