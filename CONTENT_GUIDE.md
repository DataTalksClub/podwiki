# Content Guide

This project has two different content products.

## Page Quality Gate

Every public page must pass three checks before it is committed:

- Grounded: every substantive section must cite actual DataTalks.Club podcast
  discussions. Link public episode evidence through
  `https://datatalks.club/podcast.html` and keep claims tied to those
  references.
- Linked: every page must visibly link to related wiki pages and podcast
  interviews. Articles should use `related_wiki` frontmatter and body links.
  Wiki pages should use `related` frontmatter and body links.
- Focused: every page centers one topic, role, transition, comparison, roadmap,
  or project type. Split mixed pages instead of writing a broad generic essay.

Do not publish maintenance notes, agent instructions, evidence appendixes, guest
description appendixes, or SEO scaffolding such as `Search Intent` sections.
Use inline references in the relevant section, like Wikipedia citations.

When the source episode is known, link to the specific podcast page:
`https://datatalks.club/podcast/<source-file-slug>.html`. Use
`https://datatalks.club/podcast.html` only when the specific episode slug is not
known yet.

## Wiki Pages

Wiki pages live in `_wiki/` and are archive-derived reference pages. They should
answer: "What has the DataTalks.Club podcast collectively taught about this topic?"

Required structure:

1. Opening definition: 1-3 short paragraphs that define the topic and link to
   the most important related wiki pages.
2. Link map: a compact section with related wiki pages, adjacent articles when
   useful, and 3-8 specific podcast interviews for the topic.
3. Common definition: what the podcast archive converges on, with inline
   episode links.
4. Where guests differ: disagreements, boundary differences, or tradeoffs, with
   inline episode links.
5. Topic sections: concrete subtopics with podcast references inside the
   section where the claim appears.
6. Related pages: a short final list when the body needs a navigational close.

Use these reader-facing headings where they fit:

```markdown
## Link Map
## Common Definition
## Where Guests Differ
## <Concrete Topic Section>
## Related Pages
```

Do not use these headings in public pages:

```markdown
## Contents
## Search Intent
## Archive Evidence
## Episode Evidence
## Guest Descriptions
## Recurring Archive Themes
## Maintenance Notes
## Agent Maintenance Notes
```

Wiki pages should not target arbitrary SEO keywords. They should be comprehensive
knowledge pages built from the podcast archive.

## Podcast Summaries

Podcast summaries live in `_podcast_summaries/`. They are not replacement podcast
pages and must not copy full transcripts. Their job is to help future agents decide
whether to open the original source episode in `../datatalksclub.github.io`.

Required structure:

- why the episode matters
- chapter-level summary from clips or transcript sections
- key concepts
- useful-for / probably-skip-if guidance for agents
- source pointers back to `https://datatalks.club/podcast.html` and source files

## People Pages

People pages live in `_people/`. They collect guest/contributor information from
`../datatalksclub.github.io/_people` and podcast participation. They should link
people to wiki concepts, articles, and podcast summaries where relevant. Public
episode references should use `https://datatalks.club/podcast.html`.

## Articles

Articles live in `_articles/` and are keyword-driven editorial pages. They should
answer: "What page can rank for this specific keyword while still using podcast
evidence?"

Do not create article pages until the target keyword list is provided.

Required structure once keywords exist:

- exact target keyword in frontmatter
- one topic-centered opening that states what the page helps the reader do
- article outline matched to the keyword without a public `Search Intent` section
- podcast-backed examples and expert quotes or paraphrases
- links back to relevant wiki pages and podcast interviews

Article sections should still follow the wiki evidence rule: cite specific
podcast interviews inline when making claims.

## Evidence Rules

- Every content section should include actual podcast references when it makes a
  claim about the topic.
- Prefer transcript clips and timestamped episode links over generic claims.
- Do not cite a guest as supporting a claim unless the transcript evidence is
  present in the episode page.
- If pages disagree, preserve the disagreement instead of smoothing it away.
- Avoid shallow topic labels. A page must explain the actual mechanism,
  workflow, tradeoff, or pattern discussed in the archive.
