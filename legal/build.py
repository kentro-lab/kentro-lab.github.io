#!/usr/bin/env python3
"""Generate the legal HTML pages for kentrolabs.ai from Markdown.

Source of truth:  legal/<product>/<page>.md
Served output:    <product>/<page>/index.html   (at the repo root, served by Pages)

e.g.  legal/kentro/privacy.md  ->  kentro/privacy/index.html
      ->  https://kentrolabs.ai/kentro/privacy

Each page's <title> is taken from its first `# ` heading. The HTML is wrapped in
legal/template.html ({{TITLE}} / {{CONTENT}}). Never hand-edit the generated
index.html files — edit the Markdown and re-run this script.

Usage:  python3 legal/build.py        (requires pandoc on PATH)
"""
import pathlib
import re
import subprocess
import sys

LEGAL = pathlib.Path(__file__).resolve().parent  # .../legal
ROOT = LEGAL.parent  # repo root (served by GitHub Pages)
TEMPLATE = (LEGAL / "template.html").read_text(encoding="utf-8")


def main() -> int:
    sources = sorted(LEGAL.glob("**/*.md"))
    if not sources:
        print("no source .md files under legal/", file=sys.stderr)
        return 1
    for md in sources:
        # Only product-scoped pages (legal/<product>/<page>.md) are published;
        # top-level files like legal/README.md are docs, not pages.
        if md.parent == LEGAL:
            continue
        rel = md.relative_to(LEGAL).with_suffix("")  # e.g. kentro/privacy
        text = md.read_text(encoding="utf-8")
        heading = re.search(r"^#\s+(.+)$", text, re.M)
        title = f"{heading.group(1).strip() if heading else md.stem} — Kentro"
        body = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html", str(md)],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.rstrip()
        html = TEMPLATE.replace("{{TITLE}}", title).replace("{{CONTENT}}", body)
        out = ROOT / rel / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"generated {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
