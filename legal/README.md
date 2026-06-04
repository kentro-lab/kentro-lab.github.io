# Legal pages

Privacy / support / terms pages for Kentro AI Labs products, served from
`kentrolabs.ai`.

## How it works

- **Source of truth:** `legal/<product>/<page>.md` (Markdown).
- **Generated output:** `<product>/<page>/index.html` at the repo root, served by
  GitHub Pages.

  | Source | URL |
  | --- | --- |
  | `legal/kentro/privacy.md` | https://kentrolabs.ai/kentro/privacy |

- Run **`python3 legal/build.py`** (needs `pandoc`) to regenerate the HTML after
  editing any Markdown. The page is wrapped in `legal/template.html`
  (`{{TITLE}}` / `{{CONTENT}}`); its `<title>` comes from the first `# ` heading.
- **Never hand-edit the generated `index.html`** — edit the Markdown and rebuild.
  CI (`.github/workflows/legal-docs.yml`) fails if the committed HTML drifts from
  its source.

## Add a new page

1. Create `legal/<product>/<page>.md`.
2. `python3 legal/build.py`
3. Commit both the `.md` and the generated `<product>/<page>/index.html`.

e.g. `legal/agentk/privacy.md` → `https://kentrolabs.ai/agentk/privacy`.
