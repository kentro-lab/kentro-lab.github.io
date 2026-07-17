# Kentro AI Labs — Website v2: Strategy & Build Roadmap

This is our shared plan. We work through it **one step at a time**, and confirm each step's output before moving to the next. This file is the source of truth for decisions; each step also produces its own deliverable file in `strategy/`.

---

## New direction (decided by Ali, 2026-07-16)

- **Audience:** non-technical SMB owners — mainly *small* businesses. We are not selling to engineers.
- **Positioning:** a **boutique AI lab**. Core differentiator = **highly customizable solutions**, tailored to each business, versus one-size-fits-all SaaS.
- **Offer:** 3 solutions today (exact naming confirmed in Step 1).
- **Niche:** target one to three **non-regulated** verticals that have (a) a large enough market, (b) clear pain points our solutions solve, (c) low regulatory burden. We deliberately **avoid heavily regulated spaces** (healthcare, finance/banking, legal, accounting) to sidestep the SOC2 / HIPAA certification cost. Candidate verticals (e.g. construction, realtors, others) get evaluated, not assumed.
- **Communicate value through diagrams and stories**, not jargon.
- **Firm stays anonymous** (no founder name/photo) unless Ali says otherwise.

## Candidate verdicts from round 1 + 2 (captured for content reuse)

| Candidate | Verdict | Where its content goes |
|---|---|---|
| **C1 Blueprint** | Liked | Primary source for the homepage offer / productized clarity |
| **C2 Field Notes** | Good but too "scary" for non-technical buyers | Park the dark/technical aesthetic |
| **C3 Diagnostic** | Good content, wrong for homepage | → secondary **self-guide page or blog post** (readiness check) |
| **C4 Warm Counsel** | "What we build" liked, but felt disconnected | Reuse "what we build"; fix the connective tissue |
| **C5 Ledger** | Rejected | **Deleted** |
| **C6 Follow-the-invoice** | Nice, wrong for homepage | → **blog post or part of a solutions page** (story format) |
| **C7 Memo** | Has everything but too dense, no clear message | Lesson: one sharp message, less texture |

## Visual references (Ali)

- **freshworks.com** — approachable SMB SaaS; benefit-led, friendly, not intimidating.
- **servicenow.com** — polished enterprise workflow platform.
- **temporal.io** — clean, modern, workflow / durable-execution (technical but beautifully built).
- **crewai.com/open-source** — agent-framework aesthetic.
- **across.ai** — agentic AI.

*Tension to resolve:* the references lean modern/technical, but our voice must stay non-technical. We borrow their **polish and workflow-visual language**, not their developer voice. (Addressed in Step 5.)

---

## The plan — one step at a time

Each step: a deliverable, then a checkpoint where Ali confirms before we continue.

- [~] **Step 1 — Positioning and the 3 solutions.** Draft complete in `strategy/positioning.md`, awaiting Ali's confirmation. Decided so far: differentiator = *custom AI, trained on your business, that works alongside your team — not generic ChatGPT/Copilot*. Solutions (Read→Answer→Do): **1. Document processing** ("Paperwork, handled."), **2. AI assistants** ("an assistant that knows your business"), **3. AI agents** (framed as an "AI teammate" that does the routine work).
- [x] **Step 2 — Niche / ICP selection.** DONE. **Primary: construction and the trades** (anchored by Agent K proof). **Adjacent: home / field services** (shared owner profile). Realtors + accountants excluded (regulation). Scoring grounded in Coresignal market-size data. → `strategy/niches.md`
- [~] **Step 3 — Solutions, with value stories and diagrams.** Draft in `strategy/solutions.md`, awaiting Ali's review. **Decided: block diagrams** (boxes and arrows), each with a plain-language line. Three solutions framed for construction: (1) invoice → extract → match to PO → post/flag; (2) your project data → assistant → sourced answer; (3) trigger → chase-and-collect lien-waiver loop → file/flag exceptions. Human-in-control step highlighted in each. Agent K = the proof point.
- [x] **Step 4 — Homepage message and content architecture.** DONE. **Hero line A** ("The paperwork, the questions, the chasing — handled."), **lead with construction**, **relief-from-pain-points** tone. 9-section flow (hero → reality → 3 solutions with block diagrams → why different → Agent K proof → how we work → CTA). Sitemap locked (launch = home + 3 solution pages + how-we-work + book; fast-follow = readiness check, blog, about). → `strategy/homepage-copy.md`
- [x] **Step 5 — Visual design direction.** DONE. Core idea **"the friendly blueprint."** Confirmed: **safety-orange** accent, **Space Grotesk** display + **Inter** body, **NO monospace** (uppercase letter-spaced Inter labels instead), aligned to the **existing Kentro design system** (Inter + charcoal/gray neutrals; orange replaces the old blue). Light not dark. Block-diagram-as-blueprint is the signature, with a highlighted orange "a person stays in control" node. → `strategy/design-direction.md`
- [x] **Step 6 — Build the homepage.** DONE. `candidates/v2-home.html` built (Opus) from the four strategy docs — 9 sections, 4 inline-SVG blueprint diagrams (hero + 3 solutions) each with the orange human-in-control node, Kentro neutrals + orange, Space Grotesk + Inter, no monospace, Agent K as sole proof.
- [x] **Step 7 — Verify and refine.** DONE (Fable, browser). Desktop + mobile (390px) verified: no horizontal overflow, diagrams legible on both and reflow cleanly, 8 discovery-call mailto CTAs, no-monospace confirmed, human-node consistent across all 4 diagrams, one dark section only. Minor polish noted: "JOB BUDGET" chip slightly clipped at a card edge. Screenshots in `research/screenshots-candidates/v2-*.png`. Awaiting Ali's review.
- [ ] **Step 7 — Verify and refine.** Browser test at desktop + mobile, screenshots, accessibility, iterate together.
- [~] **Step 8 — Secondary pages (fast-follow).** In progress. **DONE:** homepage promoted to `index.html` (replacing the old ship-log page); three solution pages built at `/solutions/{document-processing,ai-assistants,ai-agents}/`, pixel-consistent siblings, each with its blueprint diagram, the document-processing page carrying the C6 "follow one invoice" deep-dive; homepage "Learn more" links wired to them; dead readiness teaser removed. Also fixed: the diagram chip clip (viewBox widened) and a scroll-reveal bug across all pages (threshold 0.2→0 + a position-based scroll/resize failsafe so content can never stay invisible). All verified desktop + mobile, no overflow, no dead links. **STILL TODO:** readiness check tool page, blog (C6 story as first article), About page.
- Nothing committed/pushed — staged locally for Ali's review (no PR requested).

## Open questions (resolved as we reach them)

1. Exact names and scope of the 3 solutions — **Step 1**.
2. Which niche(s), and confirm the "avoid regulated" constraint — **Step 2**.
3. Keep the firm anonymous (no founder identity)? Assumed **yes** unless changed.
