# Search stemming — non-obvious notes

Search uses Porter stemming (so `startups` matches `startup`). The dependency
and the build flag are visible in `requirements.txt` (`zerosearch[stemming]`) and
`deploy-search.yml` (`--stemmer porter`) — not repeated here. Only the
non-obvious parts:

- The stemmer **name is baked into the `.zsx`** and restored on load, so the
  Lambda stems queries with no runtime config. To change it, rebuild the index
  with a different `--stemmer` (or none); the pin/flag are the only knobs.
- **Keep the browser stemmer in sync.** The browser fallback uses `zerosearch-node`,
  whose Porter port matches Python exactly. If you switch the index to a stemmer
  `zerosearch-node` doesn't implement (currently only `porter`), the browser and
  Lambda will disagree.
