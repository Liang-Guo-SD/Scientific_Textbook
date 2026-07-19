from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "scientific-textbook"
    / "scripts"
    / "validate_harness.py"
)
SPEC = importlib.util.spec_from_file_location("validate_harness", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class HarnessValidatorTests(unittest.TestCase):
    def make_harness(self, root: Path) -> None:
        for name in MODULE.CORE_FILES:
            content = f"# {name}\n"
            if name == "TOC.md":
                content += "| C01 | Example | planned |\n"
            if name == "PROGRESS.md":
                content += "Currently: nothing\nNext: C01\nBlockers: none\n"
            (root / name).write_text(content, encoding="utf-8")

    def test_valid_baseline_harness(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_harness(root)
            self.assertEqual(MODULE.validate(root), [])

    def test_missing_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_harness(root)
            (root / "PRD.md").unlink()
            self.assertIn("missing core file: PRD.md", MODULE.validate(root))

    def test_broken_local_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_harness(root)
            (root / "PRD.md").write_text("[Missing](missing.md)\n", encoding="utf-8")
            self.assertIn("broken local link: PRD.md -> missing.md", MODULE.validate(root))


if __name__ == "__main__":
    unittest.main()
