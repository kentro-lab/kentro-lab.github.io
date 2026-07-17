# Round 2 — two structurally different homepage candidates

## Why this round exists (owner feedback on round 1)

All five round-1 candidates — and most benchmark sites — share one skeleton: full-width hero (headline left, visual right) → alternating color bands → three-card service grid → numbered process card row → dark final CTA band → footer. Changing fonts and palettes five times did not change the skeleton, and the skeleton is what reads as "AI-generated template." Round 2 changes the structure itself. UI/UX fundamentals (readability, navigability, accessibility, scroll as the primary interaction) stay intact.

**Owner decisions:** build A ("Follow the invoice") and B ("The working memo") · industry-neutral (no construction wedge; Agent K stays a footer link) · the c3 readiness check survives as a compact embedded module in each candidate.

## BANNED PATTERNS (both candidates — these defined round 1's sameness)

- No classic hero: no full-width opening with big-headline-left / visual-right and a subhead+button stack.
- No alternating full-width background bands as the section rhythm.
- No three-card service grid; no card-grid of any kind for services.
- No numbered process card row (01/02/03 cards side by side).
- No dark full-width final CTA band.
- No "for technical teams" segregated section — the technical layer is delivered through annotation (margin notes / sidenotes), not a separate audience band.

## Dual-audience mechanism (both candidates)

One shared narrative read at two depths. The main text speaks plain business English (an owner never hits jargon). Technical depth lives in a parallel annotation layer — margin notes (C6) or numbered sidenotes (C7) — covering evals, integrations, orchestration, logging, cost-per-run, GCP/AWS. On mobile, annotations collapse to inline expandable notes (native `<details>` or minimal JS). An engineer reads the same page and finds the machinery; an owner reads it and is never interrupted.

## Content to reuse (adapt, don't re-skin)

- `candidates/c1-blueprint.html` — the Assess / Build / Operate engagement shapes with concrete deliverables; "you can stop after any stage"; honest-disqualification copy.
- `candidates/c2-fieldnotes.html` — method commitments (evaluate before launch, every run traceable, safe rollback, you own what we build); honest anonymized team-experience framing.
- `candidates/c3-diagnostic.html` — the eight readiness lenses, question wording, scoring/tier logic (Exploring 0–3 / Piloting 4–6 / Production-ready 7–8), and prefilled-mailto pattern — for the compact module.
- `candidates/c4-warmcounsel.html` — situation-recognition copy ("We're drowning in paperwork", "We tried a pilot and it stalled") and the plain-spoken honesty register.

## Compact readiness-check module (both candidates)

A small, single-column panel — visually subordinate, never a page-dominating hero. 8 yes/no questions as a stepper, score /8, named tier, "address these two lenses first," prefilled mailto carrying the tier. Pure client-side JS, keyboard accessible, `aria-live` result, no-JS fallback = link to the eight lenses listed in text + standard CTA. Reuse c3's question copy and logic verbatim where possible.

---

# Candidate 6 — "Follow the invoice"
**File:** `candidates/c6-invoice.html`

**Concept:** The homepage is one worked example. A single invoice arrives at the top of the page and the entire scroll follows it through an agentic workflow to the end of the month. Services, method, and engagement content attach to the stations where they naturally belong. The page demonstrates the product instead of describing it.

**Honesty labeling (critical):** A clearly visible label at the start of the walkthrough — "An illustrative walkthrough. This is the shape of what we build — not a specific client system." — and repeated in small print at the month-end report. Numbers inside the scenario (timestamps, counts) are openly fictional scenario detail; this is the allowed "here's how we'd approach it, clearly labeled" pattern. No client attribution anywhere.

**Opening (not a hero):** Quiet top bar: wordmark left, two anchor links + small "Book a call" button right. Then the page begins with the artifact itself: a realistic invoice document rendered in HTML/CSS (supplier name, line items, total — plausible generic detail), timestamped `07:42 — arrives in the inbox`. Above it, one line of narration: "This is how work moves through a system we build." and one plain sentence introducing Kentro (AI engineering firm; strategy through deployment for small and mid-sized businesses). That's the whole opening.

**The spine — six stations along a vertical rail.** A thin timeline rail with mono timestamps runs down the page; the invoice artifact re-renders at each station, progressively annotated (highlighted fields, flags, stamps). Stations:

1. **07:42 — It arrives.** Email with a PDF. Narration: nobody has touched it; this used to be where the retyping started.
2. **07:43 — It gets read.** The invoice re-rendered with extracted fields and per-field confidence marks. Margin note: OCR + LLM extraction, schema validation, confidence thresholds.
3. **07:43 — It gets checked.** Matched against the purchase order and vendor history; one line item doesn't match — a red flag appears on the artifact. Margin note: deterministic checks before model judgment; every decision logged.
4. **07:44 — A person decides.** The exception goes to a named-role human ("your accounts payable lead") with a one-line explanation and approve/reject. Narration carries the trust thesis: *the system knows what it doesn't know; a person stays accountable.* Margin note: human-in-the-loop thresholds, audit trail.
5. **07:51 — It's posted.** Into the accounting system the client already uses; green "posted" stamp. Margin note: integration through existing ERP/accounting APIs — no new tool for the team. Attach here (brief, prose): the objection-killer "we connect and extend what you already run."
6. **End of month — the quiet report.** A small summary artifact (invoices processed, exceptions escalated, hours returned to the team) labeled *illustrative scenario*. Narration: this is what production means — running, watched, boring in the best way.

**After the spine (kept light, structurally varied):**
- **"Other things that take this journey"** — one compact passage + inline artifact chips (a customer email, a support ticket, a contract, a stack of receipts) mapping to the three service areas in prose — explicitly NOT a card grid.
- **"How an engagement runs"** — Assess / Build / Operate adapted from c1, presented as a continuation of the timeline device (Week 0 / Weeks 1–2 / then ongoing), as ruled rows, not cards.
- **Readiness-check module** — "Would a system like this hold up in your business? Eight questions, two minutes." Compact panel per shared spec.
- **Close** — honest-disqualification sentence + "Book a discovery call" + email line, set as quiet typography on the same paper (no dark band). Footer per shared rules.

**Aesthetic — "paperwork, annotated by hand":** warm paper `#F7F5F1`, ink `#1A1E22`, document artifacts on white with soft realistic shadows. Two semantic accents: **pen blue** `#2149B8` for annotations/margin notes (the human/engineering hand) and **stamp red** `#B3261E` strictly for the exception flag, plus a **posted green** `#1E7A46` for the resolution stamp — each color means something, none is decoration. Type: editorial serif display (Newsreader) for narration headings, quiet humanist sans (Public Sans) for body, IBM Plex Mono for timestamps/annotations/field labels. Motion: stations reveal subtly on scroll and the station-4 flag→approval→stamp beat is the one orchestrated moment; everything renders complete under `prefers-reduced-motion` / no JS.

---

# Candidate 7 — "The working memo"
**File:** `candidates/c7-memo.html`

**Concept:** The homepage is a typeset working document, not a marketing page. It reads like the firm's actual thinking, published. No hero, no bands, no cards — one continuous document on one background, structured by numbered sections, hairline rules, and a margin of sidenotes.

**Document header (replaces hero):** A formal memo block — "KENTRO AI LABS — WORKING MEMO" · Subject: *What we build, how we engage, and what it costs to find out* · July 2026 · Version 1.0 · Prepared for prospective clients · Reading time ≈ 6 minutes. A quiet "Book a discovery call" link sits in the header block and repeats in §6 — no floating buttons.

**Navigation:** Slim sticky table of contents (left rail on desktop, collapsible at top on mobile) with scroll-spy highlighting. Mono, small.

**Sections (main column ~65ch, plain English; superscript-keyed technical sidenotes in the right margin):**
- **§1 The problem we keep seeing.** Most AI initiatives stall between a convincing demo and a system anyone relies on (adapt c1/c2 diagnosis). Includes two or three of c4's recognizable situations woven into prose.
- **§2 What we build.** The three areas in prose paragraphs — document processing, assistants and agentic workflows grounded in the client's data and systems, team enablement — each with named example builds inline and 1–2 technical sidenotes. Engineering-depth sentence (15+ years across distributed systems, data-intensive backends, cloud on GCP and AWS, ML platforms) belongs here as substantiation.
- **§3 How we work.** Method commitments from c2 (evaluation before launch, traceable runs, rollback, client ownership) written as numbered clauses.
- **§4 What an engagement looks like, and what it costs to find out.** Assess / Build / Operate from c1 as memo clauses or a simple ruled definition list (no cards): shape, duration, deliverables, "stop after any stage," fixed prices agreed in writing; discovery call free.
- **§5 Whether this is worth doing at all.** The honesty section: sometimes the answer is no, and the criteria we use to say so (adapt c4 + c1 disqualification copy).
- **§6 How to reach us.** Two sentences + the mailto CTA + hello@kentrolabs.ai. Signed "— The Kentro AI Labs team" (anonymous, consistent).
- **Appendix A — A self-check.** The compact readiness module, framed as a memo appendix ("Eight questions we would ask on the first call. Score yourself first if you like.").
- **Appendix B — Plain-English glossary (optional, if length allows).** Six to eight terms (agent, agentic workflow, RAG, evaluation set, human-in-the-loop, inference cost) each defined in one owner-readable sentence — a small dual-audience gift that demonstrates the firm can explain things.
- **Document footer:** revision line ("v1.0 — first public edition") above the standard site footer links.

**Aesthetic — "a document you'd keep":** single continuous off-white `#FCFBF8`, near-black text, hairline rules only; sidenotes smaller and gray with **oxblood** `#7A2430` superscript markers and links — the one accent, used only for reference apparatus and links. Type: Literata (body and headings — a long-form reading serif) + IBM Plex Mono for the ToC, labels, and document furniture. No imagery at all; the typography is the design. Motion: essentially none (scroll-spy highlight and sidenote hover emphasis only).

---

## SHARED RULES (unchanged from round 1, restated as binding)

1. Anonymous firm — "we / our team," no names, bios, photos. No invented client logos, testimonials, case studies, or client-attributed metrics. Illustrative scenarios clearly labeled (C6's labeling spec above). Team experience framed honestly as prior anonymized work.
2. Professional register: complete sentences, measured confidence, technical specificity, no hype vocabulary, sentence case. Write out "and" in headings (no ampersand glyphs).
3. "Kentro AI Labs" wordmark; © 2026 Kentro AI Labs Inc; domain kentrolabs.ai.
4. Primary CTA: `mailto:hello@kentrolabs.ai?subject=Discovery%20call` (readiness module may append tier to the subject).
5. One self-contained HTML file per candidate; inline CSS/JS; Google Fonts the only external resource (preconnect + single stylesheet link); works from file:// and any static host.
6. Head: title, ~150-char meta description, canonical `https://kentrolabs.ai/`, OG tags, `lang="en"`, viewport, inline SVG data-URI favicon in the candidate's palette.
7. Quality floor: responsive to 360px with zero horizontal scroll (test grids and rails); visible `:focus-visible`; `prefers-reduced-motion` respected; WCAG AA contrast; semantic heading order; skip link; in-page anchors only (no dead links).
8. Footer: © 2026 Kentro AI Labs Inc · Agent K → `/products/agent-k` · Privacy → `/kentro/privacy` · Terms → `/kentro/terms` · Support → `/kentro/support` · hello@kentrolabs.ai.
