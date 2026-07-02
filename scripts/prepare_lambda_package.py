#!/usr/bin/env python3
"""Create the minimal directory SAM should package for the search Lambda."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "lambda_package"
SIBLING_STEMLITE = ROOT.parent / "stemlite"


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    if PACKAGE.exists():
        shutil.rmtree(PACKAGE)

    shutil.copytree(ROOT / "search_lambda", PACKAGE / "search_lambda")
    copy_file(ROOT / "requirements.txt", PACKAGE / "requirements.txt")
    copy_file(
        ROOT / "artifacts" / "search" / "search-index.zsx",
        PACKAGE / "artifacts" / "search" / "search-index.zsx",
    )
    # Vendor the stemlite package so a stemming-built index can resolve its
    # stemmer at query time without depending on a published PyPI release.
    # Harmless when stemming is off (the package is simply unused).
    if (SIBLING_STEMLITE / "stemlite").exists():
        shutil.copytree(
            SIBLING_STEMLITE / "stemlite", PACKAGE / "stemlite",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        print("vendored stemlite into package")
    else:
        print("stemlite not found beside repo; skipping (stemming stays off)")
    print(f"prepared {PACKAGE}")


if __name__ == "__main__":
    main()
