#!/usr/bin/env python3
"""Retired split-collection migration script.

The project no longer has `_guides`, `_comparisons`, `_roadmaps`, or `_how_tos`
collections. Public content now lives in `_wiki/`, typed by `tags`, and the
site has a strict no-redirect rule. This script used to create redirect stubs,
so keeping the old behavior would be unsafe.

If old split-collection content ever appears again, migrate it manually:

1. Move unique, grounded content into the canonical `_wiki/<slug>.md` page.
2. Add the appropriate `tags` value and `keyword` frontmatter.
3. Rewrite incoming links to the canonical `/wiki/<slug>/` URL.
4. Delete the old source page instead of leaving a redirect.
5. Run `python scripts/check_wiki_links.py` and `make check`.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(__doc__.strip(), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
