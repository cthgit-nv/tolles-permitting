#!/usr/bin/env python3
"""Mechanical pre-flight for a document headed to an agency, the county, or the public.

Catches what a tired reader misses. The red-team agent runs this first, then reads.

    python3 tools/check_outward.py <file.docx|.md|.txt> --project chip

Checks:
  1. Privilege markers (counsel names, "privileged", "attorney-client", "per counsel"): ERROR.
  2. Project-specific terms that should not appear in OUTWARD text
     (projects/<project>/outward-terms.txt, one per line): WARNING.
  3. Legal citations with no card in library/authorities: WARNING ("no card, no claim").
  4. Em-dashes (house style): WARNING.

Standard library only. .docx text is read straight from word/document.xml, including
text inside tracked insertions.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from verify_library import load_cards  # noqa: E402

PRIVILEGE_MARKERS = [
    r"attorney[- ]client", r"\bprivileged\b", r"work product", r"holland\s*&\s*hart",
    r"\bper counsel\b", r"\bcounsel (advises|advised|recommends|recommended|believes|thinks)\b",
    r"\bour counsel\b", r"\bdo not (forward|distribute)\b",
]

CITATION_PATTERNS = [
    # 605 U.S. 168 ; 753 F.3d 1304 ; 260 F. Supp. 2d 997 ; 143 S. Ct. 1322
    r"\b(\d{1,4})\s+(U\.S\.|S\.\s?Ct\.|F\.\s?(?:2d|3d|4th)?|F\.\s?Supp\.\s?(?:2d|3d)?|IBLA)\s+(\d{1,5})\b",
    # 42 U.S.C. § 4336e ; 43 U.S.C. 1764(g)
    r"\b(\d{1,2})\s+U\.S\.C\.\s*§*\s*(\d+[a-z]?(?:-\d+)?)",
    # 43 C.F.R. § 46.210 ; 43 C.F.R. Part 429
    r"\b(\d{1,2})\s+C\.F\.R\.\s*(?:§+\s*|[Pp]art\s+)(\d+)(?:\.(\d+))?",
    # 90 Fed. Reg. 10610
    r"\b(\d{2,3})\s+Fed\.\s?Reg\.\s+(\d{1,6})\b",
    # NRS 704.820
    r"\bNRS\s+(\d{3}[A-Z]?)\.(\d{3,4})",
]


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf8", "replace")
        xml = re.sub(r"<w:delText[^>]*>.*?</w:delText>", "", xml, flags=re.S)  # deleted text is gone
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return path.read_text(errors="replace")


def citation_keys(text: str) -> set[str]:
    keys = set()
    for pat in CITATION_PATTERNS:
        for m in re.finditer(pat, text):
            parts = [p for p in m.groups() if p]
            keys.add(" ".join(re.sub(r"\s+", "", p).lower() for p in parts))
    return keys


def carded_keys() -> set[str]:
    keys = set()
    for _, meta, body in load_cards("authorities").values():
        blob = f"{meta.get('citation', '')}\n{meta.get('id', '')}\n{body}"
        keys |= citation_keys(blob)
    # A card for a C.F.R. part covers its sections; a card for a section covers the part.
    expanded = set(keys)
    for k in keys:
        bits = k.split()
        if len(bits) >= 2 and bits[0].isdigit():
            expanded.add(" ".join(bits[:2]))
    return expanded


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", type=Path)
    ap.add_argument("--project", help="chip | fmdp | denim (loads outward-terms.txt)")
    args = ap.parse_args(argv)

    text = read_text(args.file)
    errors, warnings = [], []

    for pat in PRIVILEGE_MARKERS:
        for m in re.finditer(pat, text, flags=re.I):
            errors.append(f"ERROR line {line_of(text, m.start())}: privilege marker '{m.group(0)}'")

    if args.project:
        terms_file = ROOT / "projects" / args.project / "outward-terms.txt"
        if terms_file.exists():
            for term in terms_file.read_text().splitlines():
                term = term.strip()
                if not term or term.startswith("#"):
                    continue
                for m in re.finditer(re.escape(term), text, flags=re.I):
                    warnings.append(f"warn  line {line_of(text, m.start())}: outward term '{term}'")

    known = carded_keys()
    for key in sorted(citation_keys(text)):
        bits = key.split()
        if key not in known and " ".join(bits[:2]) not in known:
            warnings.append(f"warn  citation with no library card: {key}")

    for m in re.finditer("—", text):
        warnings.append(f"warn  line {line_of(text, m.start())}: em-dash")

    for line in errors + warnings:
        print(line)
    print(f"\n{args.file.name}: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
