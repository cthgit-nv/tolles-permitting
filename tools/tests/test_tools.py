"""Run with: python3 -m unittest discover -s tools/tests"""
import datetime as dt
import sys
import tempfile
import textwrap
import unittest
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import check_outward  # noqa: E402
import verify_library  # noqa: E402

AUTH = textwrap.dedent("""\
    ---
    id: A-case-example
    type: case
    citation: "Example v. Agency, 605 U.S. 168 (2025)"
    court: SCOTUS
    weight: binding
    status: good-law
    source_file: library/sources/A-case-example.txt
    verified_on: 2026-09-24
    verified_by: agent-free-sources
    keycite: pending
    propositions: [P-example]
    sensitivity: PUBLIC
    ---

    ## Quotes

    > "the textually mandated focus of NEPA is the proposed action" (slip op. at 12)
    """)

PROP = textwrap.dedent("""\
    ---
    id: P-example
    statement: "Scope follows the proposed action."
    status: settled
    supporting: [A-case-example]
    adverse: []
    last_reviewed: 2026-09-24
    sensitivity: PUBLIC
    ---
    """)


class LibraryFixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        for d in ("library/authorities", "library/propositions", "library/sources", "projects/chip"):
            (root / d).mkdir(parents=True)
        (root / "library/authorities/A-case-example.md").write_text(AUTH)
        (root / "library/propositions/P-example.md").write_text(PROP)
        (root / "library/sources/A-case-example.txt").write_text(
            "SOURCE: x\n...the textually\nmandated focus of NEPA is the “proposed action”...")
        self.root = root
        self._saved = (verify_library.ROOT, verify_library.LIB, check_outward.ROOT)
        verify_library.ROOT, verify_library.LIB = root, root / "library"
        check_outward.ROOT = root

    def tearDown(self):
        verify_library.ROOT, verify_library.LIB, check_outward.ROOT = self._saved
        self.tmp.cleanup()


class VerifyLibraryTest(LibraryFixture):
    def run_check(self, today="2026-09-25"):
        rep, _, _ = verify_library.check(dt.date.fromisoformat(today))
        return rep

    def test_clean_library_passes(self):
        rep = self.run_check()
        self.assertEqual(rep.errors, [])

    def test_quote_survives_line_breaks_and_curly_quotes(self):
        self.assertEqual(self.run_check().errors, [])

    def test_fabricated_quote_fails(self):
        p = self.root / "library/authorities/A-case-example.md"
        p.write_text(p.read_text().replace("proposed action", "entire program"))
        errors = self.run_check().errors
        self.assertTrue(any("quote not found" in e for e in errors), errors)

    def test_settled_needs_binding_support(self):
        p = self.root / "library/authorities/A-case-example.md"
        p.write_text(p.read_text().replace("weight: binding", "weight: persuasive"))
        self.assertTrue(any("no binding supporting" in e for e in self.run_check().errors))

    def test_missing_authority_card_is_error(self):
        p = self.root / "library/propositions/P-example.md"
        p.write_text(p.read_text().replace("adverse: []", "adverse: [A-case-missing]"))
        self.assertTrue(any("A-case-missing has no card" in e for e in self.run_check().errors))

    def test_vacated_support_is_error(self):
        p = self.root / "library/authorities/A-case-example.md"
        p.write_text(p.read_text().replace("status: good-law", "status: vacated"))
        self.assertTrue(any("is vacated" in e for e in self.run_check().errors))

    def test_stale_card_warns(self):
        warnings = self.run_check(today="2028-01-01").warnings
        self.assertTrue(any("stale" in w for w in warnings), warnings)

    def test_watchlist_shortens_window(self):
        (self.root / "library/watchlist.md").write_text("- A-case-example\n")
        warnings = self.run_check(today="2026-11-15").warnings
        self.assertTrue(any("window 30 days" in w for w in warnings), warnings)


class CheckOutwardTest(LibraryFixture):
    def write_docx(self, body_xml: str) -> Path:
        path = self.root / "draft.docx"
        with zipfile.ZipFile(path, "w") as z:
            z.writestr("word/document.xml", f"<w:document><w:body>{body_xml}</w:body></w:document>")
        return path

    def test_privilege_marker_is_error(self):
        path = self.root / "d.md"
        path.write_text("As Holland & Hart advised, the crossings qualify.\n")
        self.assertEqual(check_outward.main([str(path)]), 1)

    def test_deleted_tracked_text_is_ignored(self):
        path = self.write_docx("<w:p><w:del><w:r><w:delText>privileged</w:delText></w:r></w:del>"
                               "<w:r><w:t>Clean text.</w:t></w:r></w:p>")
        self.assertEqual(check_outward.main([str(path)]), 0)

    def test_carded_citation_is_known(self):
        keys = check_outward.carded_keys()
        self.assertIn("605 u.s. 168", keys)

    def test_uncarded_citation_detected(self):
        found = check_outward.citation_keys("See 408 F.3d 1113 and 43 C.F.R. § 46.210.")
        self.assertIn("408 f.3d 1113", found)
        self.assertIn("43 46 210", found)

    def test_outward_terms(self):
        (self.root / "projects/chip/outward-terms.txt").write_text("# comment\nTolles\n")
        path = self.root / "d.md"
        path.write_text("Tolles will construct the road.\n")
        self.assertEqual(check_outward.main([str(path), "--project", "chip"]), 0)


if __name__ == "__main__":
    unittest.main()
