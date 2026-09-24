#!/usr/bin/env python3
"""Check the research library for broken cards, unverifiable quotes, and stale entries.

Standard library only, so it runs anywhere Claude Code runs.

    python3 tools/verify_library.py              # full check, exit 1 on errors
    python3 tools/verify_library.py --keycite-list   # cases still awaiting a citator check
    python3 tools/verify_library.py --stale      # cards past their freshness window
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "library"

AUTHORITY_TYPES = {
    "case", "statute", "regulation", "federal-register", "agency-guidance",
    "ibla", "agency-precedent", "state-law",
}
AUTHORITY_STATUS = {
    "good-law", "questioned", "pending-challenge", "superseded", "vacated",
    "removed", "unverified",
}
WEIGHTS = {"binding", "persuasive", "agency-internal"}
PROP_STATUS = {"settled", "majority", "contested", "open", "advocacy"}
SENSITIVITY = {"PUBLIC", "OUTWARD", "INTERNAL", "PRIVILEGED"}
KEYCITE = {"pending", "clean", "flagged", "n/a"}

AUTHORITY_REQUIRED = [
    "id", "type", "citation", "weight", "status", "source_file",
    "verified_on", "verified_by", "sensitivity",
]
PROP_REQUIRED = ["id", "statement", "status", "supporting", "last_reviewed", "sensitivity"]

# Re-verify windows in days, by card type. Watchlist items use WATCH_DAYS.
FRESHNESS = {
    "case": 365, "statute": 365, "ibla": 365, "state-law": 365,
    "regulation": 182, "federal-register": 182, "agency-guidance": 182,
    "agency-precedent": 365,
}
WATCH_DAYS = 30

QUOTE_RE = re.compile(r'^>\s*"(.+)"\s*(\(.*\))?\s*$')


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Parse the small YAML subset the cards use: scalars and [a, b] lists."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block, body = text[3:end], text[end + 4:]
    meta: dict = {}
    for line in block.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value[:1] in {'"', "'"} and value.count(value[0]) >= 2:
            value = value[: value.index(value[0], 1) + 1]   # keep quoted text, drop trailing comment
        else:
            value = value.split(" #", 1)[0].strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("\"'") for v in value[1:-1].split(",")]
            meta[key] = [v for v in items if v]
        else:
            meta[key] = value.strip("\"'")
    return meta, body


def normalize(s: str) -> str:
    """Fold the differences that copying from PDFs and HTML introduces."""
    s = unicodedata.normalize("NFKC", s)
    for a, b in {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
                 "\u2013": "-", "\u2014": "-", "\u00a0": " ", "\u00ad": ""}.items():
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)          # rejoin hyphenated line breaks
    s = re.sub(r"\[?\*\d+\]?", " ", s)       # drop star-paging markers like *186
    s = re.sub(r"[\"'`]", "", s)            # nested quotation marks are not substantive
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def extract_quotes(body: str) -> list[str]:
    quotes, in_section = [], False
    for line in body.splitlines():
        if line.startswith("## "):
            in_section = line.strip().lower() == "## quotes"
            continue
        if in_section:
            m = QUOTE_RE.match(line.strip())
            if m and m.group(1).strip():
                quotes.append(m.group(1))
    return quotes


def parse_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def watchlist_ids() -> set[str]:
    path = LIB / "watchlist.md"
    if not path.exists():
        return set()
    return set(re.findall(r"\b([AP]-[a-z0-9-]+)\b", path.read_text()))


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"ERROR {where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"warn  {where}: {msg}")


def load_cards(folder: str) -> dict[str, tuple[Path, dict, str]]:
    cards = {}
    for path in sorted((LIB / folder).glob("*.md")):
        meta, body = parse_front_matter(path.read_text())
        cards[path.stem] = (path, meta, body)
    return cards


def check(today: dt.date) -> tuple[Report, dict, dict]:
    rep = Report()
    authorities = load_cards("authorities")
    propositions = load_cards("propositions")
    watched = watchlist_ids()

    for stem, (path, meta, body) in authorities.items():
        where = path.relative_to(ROOT).as_posix()
        for field in AUTHORITY_REQUIRED:
            if not meta.get(field):
                rep.error(where, f"missing '{field}'")
        if meta.get("id") and meta["id"] != stem:
            rep.error(where, f"id '{meta['id']}' does not match filename")
        for field, allowed in (("type", AUTHORITY_TYPES), ("status", AUTHORITY_STATUS),
                               ("weight", WEIGHTS), ("sensitivity", SENSITIVITY)):
            if meta.get(field) and meta[field] not in allowed:
                rep.error(where, f"{field} '{meta[field]}' not one of {sorted(allowed)}")
        if meta.get("keycite") and meta["keycite"] not in KEYCITE:
            rep.error(where, f"keycite '{meta['keycite']}' not one of {sorted(KEYCITE)}")

        quotes = extract_quotes(body)
        src = ROOT / meta.get("source_file", "")
        if meta.get("status") != "unverified":
            if not meta.get("source_file") or not src.is_file():
                rep.error(where, f"source_file '{meta.get('source_file')}' not found")
            elif not quotes:
                rep.warn(where, "no quotes to check against the source")
        if src.is_file() and quotes:
            haystack = normalize(src.read_text(errors="replace"))
            for q in quotes:
                if normalize(q) not in haystack:
                    rep.error(where, f"quote not found in source: \"{q[:70]}...\"")

        for pid in meta.get("propositions", []) or []:
            if pid not in propositions:
                rep.warn(where, f"links to missing proposition {pid}")

        verified = parse_date(meta.get("verified_on", ""))
        if verified is None:
            rep.error(where, "verified_on is not an ISO date")
        else:
            window = WATCH_DAYS if stem in watched else FRESHNESS.get(meta.get("type", ""), 365)
            if (today - verified).days > window:
                rep.warn(where, f"stale: verified {verified}, window {window} days")

    for stem, (path, meta, body) in propositions.items():
        where = path.relative_to(ROOT).as_posix()
        for field in PROP_REQUIRED:
            if not meta.get(field):
                rep.error(where, f"missing '{field}'")
        if meta.get("id") and meta["id"] != stem:
            rep.error(where, f"id '{meta['id']}' does not match filename")
        if meta.get("status") and meta["status"] not in PROP_STATUS:
            rep.error(where, f"status '{meta['status']}' not one of {sorted(PROP_STATUS)}")
        if meta.get("sensitivity") and meta["sensitivity"] not in SENSITIVITY:
            rep.error(where, f"sensitivity '{meta['sensitivity']}' invalid")
        for side in ("supporting", "adverse"):
            for aid in meta.get(side, []) or []:
                if aid not in authorities:
                    rep.error(where, f"{side} authority {aid} has no card")
                elif authorities[aid][1].get("status") in {"vacated", "superseded", "removed"}:
                    rep.error(where, f"{side} authority {aid} is {authorities[aid][1]['status']}")
                elif authorities[aid][1].get("status") in {"unverified", "questioned", "pending-challenge"}:
                    rep.warn(where, f"{side} authority {aid} is {authorities[aid][1]['status']}")
        if meta.get("status") == "settled" and not any(
            authorities.get(a, (None, {}))[1].get("weight") == "binding"
            for a in meta.get("supporting", []) or []
        ):
            rep.error(where, "status 'settled' but no binding supporting authority")

    return rep, authorities, propositions


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keycite-list", action="store_true", help="print cases awaiting a citator check")
    ap.add_argument("--stale", action="store_true", help="print only freshness warnings")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD)")
    args = ap.parse_args(argv)
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    rep, authorities, _ = check(today)

    if args.keycite_list:
        rows = [(m.get("citation", s), s) for s, (_, m, _) in authorities.items()
                if m.get("type") in {"case", "ibla"} and m.get("keycite", "pending") == "pending"]
        print(f"{len(rows)} decisions awaiting KeyCite / Shepard's:\n")
        for citation, stem in rows:
            print(f"- {citation}  [{stem}]")
        return 0

    if args.stale:
        for w in rep.warnings:
            if "stale:" in w:
                print(w)
        return 0

    for line in rep.errors + rep.warnings:
        print(line)
    print(f"\n{len(authorities)} authorities checked: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
