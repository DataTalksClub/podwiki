#!/usr/bin/env python3
"""Regression test: source sync reconciles stale source-derived records itself.

A source-derived record whose upstream source was removed or renamed must not
break the scheduled "Sync source records" job. Each sync script removes stale
target files (instead of only reporting them) so ``check_source_records.py``
passes right after ``make sources``.

Run: ``python scripts/test_sync_stale_reconciliation.py``
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sync_book_pages import main as book_main  # noqa: E402
from sync_event_pages import expected_slugs, sync as sync_events  # noqa: E402
from sync_people_pages import main as people_main  # noqa: E402
from sync_podcast_pages import main as podcast_main  # noqa: E402


def write_events_yaml(path: Path, rows: list[dict]) -> None:
    import yaml

    path.write_text(yaml.safe_dump(rows, sort_keys=False), encoding="utf-8")


class StaleReconciliationTest(unittest.TestCase):
    def test_event_sync_removes_stale_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "events.yaml"
            target = tmp_path / "_events"
            people_source = tmp_path / "_people_source"
            people_source.mkdir()
            target.mkdir()
            write_events_yaml(
                source,
                [
                    {
                        "time": "2026-12-15 16:30:00",
                        "title": "Kept Webinar",
                        "speakers": [],
                        "type": "webinar",
                    }
                ],
            )
            stale = target / "2026-01-01-removed-webinar.md"
            stale.write_text("---\ntitle: stale\n---\n", encoding="utf-8")

            self.assertEqual(sync_events(source, target, people_source), 0)
            self.assertFalse(stale.exists(), "stale event record was not removed")
            self.assertEqual(expected_slugs(source), {p.stem for p in target.glob("*.md")})

    def test_event_rename_old_slug_removed_new_slug_written(self) -> None:
        """Upstream date change (same title, new date) swaps the filename slug."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "events.yaml"
            target = tmp_path / "_events"
            people_source = tmp_path / "_people_source"
            people_source.mkdir()
            target.mkdir()
            title = "Hireable With AI #3: AI Engineering for Experienced Developers"
            old_slug = "2026-12-07-hireable-with-ai-3-ai-engineering-for-experienced-developers"
            (target / f"{old_slug}.md").write_text(
                "---\ntitle: old\n---\n", encoding="utf-8"
            )
            write_events_yaml(
                source,
                [
                    {
                        "time": "2026-12-15 16:30:00",
                        "title": title,
                        "speakers": [],
                        "type": "webinar",
                    }
                ],
            )

            self.assertEqual(sync_events(source, target, people_source), 0)
            self.assertFalse(
                (target / f"{old_slug}.md").exists(),
                "renamed-away event slug was not removed",
            )
            self.assertEqual(len(list(target.glob("*.md"))), 1)
            new_file = next(target.glob("*.md"))
            self.assertTrue(new_file.stem.startswith("2026-12-15-"))

    def test_podcast_sync_removes_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            podcast_source = tmp_path / "_podcast"
            podcast_source.mkdir()
            (podcast_source / "kept-episode.md").write_text(
                "---\ntitle: Kept\n---\nbody\n", encoding="utf-8"
            )
            target = tmp_path / "_summaries"
            target.mkdir()
            stale = target / "removed-episode.md"
            stale.write_text("stale", encoding="utf-8")
            people_source = tmp_path / "_people_src"
            people_source.mkdir()

            argv = sys.argv
            sys.argv = [
                "sync_podcast_pages",
                "--source",
                str(podcast_source),
                "--people-source",
                str(people_source),
                "--target",
                str(target),
            ]
            try:
                podcast_main()
            finally:
                sys.argv = argv
            self.assertFalse(stale.exists())
            self.assertTrue((target / "kept-episode.md").exists())

    def test_people_sync_removes_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            people_source = tmp_path / "_people_upstream"
            people_source.mkdir()
            (people_source / "kept-person.md").write_text(
                "---\ntitle: Kept Person\n---\nbio\n", encoding="utf-8"
            )
            podcast_source = tmp_path / "_podcast_upstream"
            podcast_source.mkdir()
            event_source = tmp_path / "events.yaml"
            write_events_yaml(event_source, [])
            target = tmp_path / "_people"
            target.mkdir()
            (target / "removed-person.md").write_text("stale", encoding="utf-8")

            argv = sys.argv
            sys.argv = [
                "sync_people_pages",
                "--people-source",
                str(people_source),
                "--podcast-source",
                str(podcast_source),
                "--event-source",
                str(event_source),
                "--target",
                str(target),
            ]
            try:
                people_main()
            finally:
                sys.argv = argv
            self.assertFalse((target / "removed-person.md").exists())
            self.assertTrue((target / "kept-person.md").exists())

    def test_book_sync_removes_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            book_source = tmp_path / "_books_upstream"
            book_source.mkdir()
            (book_source / "kept-book.md").write_text(
                "---\ntitle: Kept Book\n---\nbody\n", encoding="utf-8"
            )
            target = tmp_path / "_books"
            target.mkdir()
            stale = target / "removed-book.md"
            stale.write_text("stale", encoding="utf-8")
            people_dir = tmp_path / "_people"
            people_dir.mkdir()

            argv = sys.argv
            sys.argv = [
                "sync_book_pages",
                "--source",
                str(book_source),
                "--target",
                str(target),
                "--people-dir",
                str(people_dir),
            ]
            try:
                book_main()
            finally:
                sys.argv = argv
            self.assertFalse(stale.exists())
            self.assertTrue((target / "kept-book.md").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
