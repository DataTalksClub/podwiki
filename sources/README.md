# Sources

Raw podcast sources live in the neighboring website repository:

```text
../datatalksclub.github.io/_podcast
```

Each source file is a Markdown episode page with YAML-like frontmatter containing:

- title, season, episode, date, duration, links, and image
- guest IDs
- existing broad topics
- quotable clips with start and end offsets
- transcript lines with speaker and timestamp

This directory intentionally does not copy those files. The import script reads
them in place and generates wiki pages under `../wiki`.
