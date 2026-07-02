# Search stemming (wired, OFF by default)

The exploration search can stem tokens so singular/plural and other word forms
match (e.g. a search for `startups` also finds `startup`). It is implemented in
the shared [`stemlite`](https://github.com/DataTalksClub/stemlite) library and
exposed by `zerosearch` via `Index(stemmer="porter")`. zerosearch imports
`stemlite` lazily, so it stays a zero-required-dependency library.

It is **off in the committed/deployed build** on purpose: turning it on requires
`stemlite` and the stemming-enabled `zerosearch` to be available to the Lambda,
plus a browser-search parity fix. Local development already works (both siblings
are added to `sys.path`).

## Verify locally

```
python scripts/build_search_index.py --stemmer porter --index /tmp/idx.zsx \
  --corpus /tmp/c1.json --browser-corpus /tmp/c2.json
```

Singular and plural queries return the same top pages. The stemmer name is baked
into the `.zsx` and restored automatically on load.

## To enable in production

1. **stemlite** must be importable in the Lambda. Either publish it to PyPI and
   add `stemlite>=0.1.0` to `requirements.txt`, or rely on the vendored copy:
   `prepare_lambda_package.py` already copies `../stemlite/stemlite` into the
   package when present.
2. **zerosearch** in the Lambda must be the stemming-enabled version. The Lambda
   installs `zerosearch` from PyPI (`requirements.txt`), so publish the updated
   zerosearch (with the `stemmer=` support) and bump the pin — or vendor it too.
3. Build the index with the stemmer: `make index STEMMER=porter` (or pass
   `--stemmer porter`). Then `make lambda-package` and deploy.
4. **Browser parity:** the browser fallback search (`assets/search.js`, backed by
   `zerosearch-node`) must apply the *same* stemmer to the query and corpus, or
   plural queries won't bridge in the fallback. Port stemming to `zerosearch-node`
   before enabling, so the Lambda and browser paths agree.

Until steps 1-4 are done, leave the build unstemmed (the default).
