#!/usr/bin/env python3
"""Create the minimal directory SAM should package for the search Lambda."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "lambda_package"


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
    # stemlite is installed from PyPI via requirements.txt (zerosearch[stemming]),
    # not vendored — it is a tiny standard-library-only package, so pip pulls it
    # during the SAM build like zerosearch itself.
    print(f"prepared {PACKAGE}")


if __name__ == "__main__":
    main()
