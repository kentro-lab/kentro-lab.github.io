# Kentro AI Labs website — build & update guide

This site is a **Hugo** static site using the **TailBliss** theme (Tailwind CSS 4 + Vite + Alpine.js), deployed to **GitHub Pages** at **kentrolabs.ai**.

- TailBliss theme + docs: https://github.com/nusserstudios/tailbliss
- Hugo docs: https://gohugo.io/documentation/

Requirements: Hugo **extended** (≥ 0.164), Node 20+. Install Hugo with `brew install hugo`.

---

## ⚠️ The one rule that matters: build CSS before Hugo

Tailwind CSS is compiled by **Vite** into `static/css/main.<hash>.css`. **Hugo only reads `static/css/` at the site root**, and that folder is **git-ignored** (it's a build artifact). So:

- **The Vite CSS build MUST run before every `hugo` build**, or the site renders **unstyled** (and `hugo` may error with `failed to read directory "static/css"`).
- Never commit `static/css/` — it is regenerated on every build (local and CI).

The npm scripts and the CI workflow already do this in the right order. If you run Hugo by hand, run the CSS build first.

---

## Local development

```bash
npm install            # first time only (see "install.js gotcha" below)
npm run dev            # build CSS once, then start Hugo at http://localhost:1313
# or, auto-rebuild CSS on change while editing Tailwind classes:
npm run dev:watch
```

- Editing **content/params/layouts** → Hugo live-reloads automatically.
- Editing **Tailwind classes or `assets/css/main.css`** → CSS must rebuild. `dev:watch` does it automatically; otherwise run `npm run rebuild`.

## Production build (what CI runs)

```bash
npm run build          # = vite build --mode production && hugo --minify --gc --cleanDestinationDir
```

Output goes to `public/`. Verify it's styled: `public/index.html` should link a `/css/main.<hash>.css` that exists under `public/css/`.

---

## Where to edit what

| To change… | Edit… |
|---|---|
| **Homepage** (hero, the 3 solution cards, why-it's-different, how-we-work, Agent K proof, final CTA) | **`hugo.yaml`** → `params` (`hero`, `moto`, `description`, `email`, `discovery_call_url`, and sections `p1`–`p5`). The layout is `layouts/index.html`. |
| **Solution pages** (Document processing, AI assistants, AI agents) | `content/solutions/*.md` (Markdown). List page: `content/solutions/_index.md` + `layouts/solutions/list.html`. |
| **About / Contact** | `content/about.md`, `content/contact.md` |
| **Nav / footer** | `layouts/partials/nav.html`, `layouts/partials/footer.html` |
| **Page `<title>` / meta / OG tags** | `layouts/partials/meta.html` (note: the home title uses `Site.Title — moto`, body meta description uses the long `description`) |
| **Colors, fonts, design tokens** | `assets/css/main.css` — Tailwind 4 CSS-first config via `@theme` (OKLCH colors; theme default is indigo). Rebuild CSS after. |
| **Site title, baseURL, author, social** | `hugo.yaml` top-level + `params` |

After editing content/params, just rebuild (`npm run build`) or let the dev server reload. After editing Tailwind classes or `main.css`, rebuild CSS.

---

## Legal and product pages (Hugo-managed)

Every page is now built by Hugo — there is no static-HTML passthrough. Edit these as Markdown content:

- **Legal:** `/kentro/privacy/`, `/kentro/terms/`, `/kentro/support/` → `content/kentro/{privacy,terms,support}.md`. These are real legal documents — **preserve the wording exactly**; only edit front matter unless the legal text itself changes. Rendered by `layouts/_default/single.html` (theme prose; the `title` front matter becomes the page `<h1>`).
- **Product:** `/products/agent-k/` → `content/products/agent-k.md`, rendered by `layouts/_default/single.html`.
- **Custom domain:** `static/CNAME` (= `kentrolabs.ai`) → published to `public/CNAME`.

> The old `legal/` build pipeline (`build.py` + `template.html`) and its `.github/workflows/legal-docs.yml` check were removed when the legal docs became Hugo content. There is no longer a separate generate-and-copy step.

---

## Deployment (GitHub Pages via Actions)

Pushing to **`main`** triggers `.github/workflows/hugo.yml`: checkout → setup Node + Hugo extended → `npm install` → `npx vite build --mode production` → `hugo --minify --gc` → upload `public/` → deploy to Pages. The CNAME flows through from `static/CNAME`.

> **One-time setting:** the repo's **Settings → Pages → Source** must be **"GitHub Actions"** (not "Deploy from a branch"). Hugo needs the build step, so branch-serving won't work.

---

## Gotchas

- **`install.js` hook:** `npm install` runs `node install.js`, which tries to fetch TailBliss demo content from an `origin/exampleSite` branch that does **not** exist here. It safely **skips** because `content/` already exists — keep `content/` present, and don't rely on this hook to scaffold anything.
- **`static/css/` is git-ignored** — never commit it; always rebuild (see the CSS rule above).
- **Theme is adopted as-is** (default indigo TailBliss look). Design changes go in `assets/css/main.css` and the `layouts/`.
- The theme's demo material (investor logos, testimonials, demo blog posts, hero rocket) was intentionally removed.

## Content guardrails (keep these when editing)

- **Anonymous firm** — no founder name/photo/bio; always "we / our team".
- **No fabricated proof** — no invented client logos, testimonials, or metrics. **Agent K is the only proof point.**
- Every primary CTA → `mailto:hello@kentrolabs.ai?subject=Discovery%20call` (the `discovery_call_url` param).
- Plain, non-technical language for the construction/trades audience; write out "and" in headings.

---

## Internal working material

Strategy docs, research, and prior homepage candidates live in `_internal/` (git-ignored — licensed data and planning notes, never published). Not part of the site build.
