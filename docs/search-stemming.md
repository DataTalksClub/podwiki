# Search stemming (Porter)

The exploration search stems tokens so singular/plural and other word forms
match (e.g. a search for `startups` also finds `startup`). It is implemented in
the shared [`stemlite`](https://github.com/alexeygrigorev/stemlite) library and
exposed by `zerosearch` via `Index(stemmer="porter")`. zerosearch imports
`stemlite` lazily and declares it as the optional `stemming` extra, so it stays
zero-required-dependency.

Enabled in the deployed Lambda:

- `requirements.txt` pins `zerosearch[stemming]>=0.5.0`, so the SAM build installs
  the stemming-enabled `zerosearch` and the tiny `stemlite` from PyPI.
- `.github/workflows/deploy-search.yml` builds the index with `--stemmer porter`.
  The stemmer name is baked into the `.zsx` and restored automatically when the
  Lambda loads it, so queries stem without extra config.

The browser fallback search uses `zerosearch-node`, which has a Porter port
verified to match the Python output word-for-word, so both paths agree.

## Verify locally

```
python scripts/build_search_index.py --stemmer porter --index /tmp/idx.zsx \
  --corpus /tmp/c1.json --browser-corpus /tmp/c2.json
```

Singular and plural queries return the same top pages. The stemmer name is baked
into the `.zsx` and restored automatically on load.

## Changing the stemmer

Build locally with a different stemmer via `make index STEMMER=snowball` (or
`--stemmer`). To turn stemming off, build without the flag; the `.zsx` then
records no stemmer and the Lambda serves unstemmed results. Keep the CI flag in
`deploy-search.yml` in sync with what you want deployed.

Dependencies: `stemlite` and the stemming-enabled `zerosearch` (>=0.5.0) are on
PyPI and pulled by the `zerosearch[stemming]` pin in `requirements.txt`.
