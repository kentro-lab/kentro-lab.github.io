# Step 5 — Visual Design Direction

Status: **draft for Ali's review.** The visual language for the build — grounded in the five reference sites (screenshots in `strategy/reference-shots/`), tuned to a non-technical construction/trades owner. This is the brief the homepage build (Step 6) follows.

---

## The core idea: "the friendly blueprint"

A construction owner trusts things that are **built, solid, and clearly drawn**. Our signature device — the block diagram — is literally a **blueprint**: precise boxes and arrows on a light drafting-paper background, warm and legible, never cold or techy. The diagram is both the "workflow visual language" of the reference sites *and* authentic to construction. That's the ownable idea: **AI, drawn like a blueprint.**

**Light, not dark.** Three of the five references (Temporal, ServiceNow, Across) are dark — exactly the quality you flagged as "scary" on C2. So we go **light and warm** (Freshworks, CrewAI), and borrow the *structural craft* of the dark ones (grids, mono labels, workflow panels) without their cold surface.

## What we borrow from each reference (grounded in the screenshots)

- **CrewAI** → the whole **block-diagram-as-hero** system: labeled boxes, connecting arrows, small satellite chips, a dotted-grid card, one warm accent. This is our signature reference.
- **Freshworks** → warm light background, a big confident headline with one emphasized word, a simple "trusted by / we ship our own product" line, generous whitespace.
- **ServiceNow** → the **two-tone headline** (accent-colored key word beside dark text), a punchy relief-led message, and **checkmark value lists**.
- **Temporal** → a **subtle structural grid** in the background (reads as blueprint drafting).
- **Across** → **bold, heavy display weight** and emphasis-bolding of key words in the subhead.

## Palette — Kentro neutrals + safety orange

Built on the **existing Kentro design system** — the charcoal-and-gray neutrals already used on the Agent K and legal pages — so the homepage feels of a piece with the rest of the site. The one deliberate change: the accent moves from the old blue (`#2563EB`) to **safety orange**, distinctive against all five references (none is orange) and native to construction without hard-hat cliché.

| Token | Hex | Role | Source |
|---|---|---|---|
| `--white` | `#FFFFFF` | page base, cards, diagram surfaces | Kentro |
| `--surface` | `#F9FAFB` | alternating section tint, chip fills | Kentro |
| `--ink` | `#101828` | headings, body, diagram boxes | Kentro primary |
| `--ink-2` | `#475467` | secondary text | Kentro secondary |
| `--line` | `#E4E7EC` | hairlines and the blueprint dot-grid | Kentro border |
| `--orange` | `#E0562A` | primary accent — CTAs, arrows, emphasized headline word, the highlighted "a person stays in control" node | new (replaces blue) |
| `--orange-deep` | `#B8451E` | hover / pressed | new |

One accent, Kentro's own neutrals underneath. Discipline over decoration.

## Typography

Anchored to the Kentro design system — **Inter is already the Kentro typeface** — with Space Grotesk added for display character. **No monospace anywhere:** monospace reads as "code" to people outside software, and this audience is non-technical.

- **Display — Space Grotesk (600–700).** Geometric, sturdy, "built" — clearly not the generic Inter-everywhere SaaS look. The emphasized hero word is set in `--orange` (the ServiceNow two-tone move).
- **Body — Inter (400–600).** The existing Kentro body font; neutral, highly readable.
- **Labels / eyebrows / diagram tags — Inter, small, UPPERCASE, letter-spaced (~0.08em), medium weight.** This gives the small "drafting label" texture without monospace.

## The signature: the block-diagram system

Every solution gets one, and one lives in the hero. Consistent rules so they read as a family:

- **Container:** a rounded card (`--white`) on `--paper`, with a faint `--line` **dot-grid** background (the blueprint surface).
- **Step boxes:** solid `--ink` fill, white text, small radius — the main flow, left → right.
- **The human-in-control node:** filled `--orange` with a small person/badge mark — the one highlighted box in every diagram, making "a person stays in control" visible at a glance. This is the recurring trust signal.
- **Arrows:** `--orange`, clean, with clear direction; a **loop-back arrow** where the workflow repeats (solution 3's follow-up loop).
- **Satellite chips:** small `--surface` rounded chips with a `--line` border and **small uppercase letter-spaced labels** (e.g. "YOUR POs", "QUICKBOOKS", "YOUR PROJECT DATA") — the "built around your business" inputs, like CrewAI's memory/tools/knowledge chips.
- **Caption:** a one-line plain-language sentence under each diagram so a non-technical owner reads it effortlessly.

Hero diagram: a simple three-node blueprint — **your business → custom AI → your team** — establishing the device immediately, with the AI node in ink and a person badge on "your team."

## Layout

- Clean, warm, generous — Freshworks/CrewAI calibre. Max width ~1200px. Whitespace and hairlines carry rhythm; **avoid heavy alternating color bands** (the round-1 template tell). Mostly `--paper` with occasional `--white` cards and one deeper ink section for the Agent K proof (a single, purposeful dark moment — proof, not the whole page).
- **Hero:** headline + subhead + two CTAs on the left, the hero blueprint diagram on the right (stacks on mobile).
- **Solutions:** each is a row — heading + value + checkmark points on one side, its blueprint diagram on the other, alternating sides down the page for rhythm.
- **Sturdy, grounded feel:** confident type sizes, solid buttons (`--orange` primary, ink outline secondary), squared-but-slightly-rounded corners (built, not bubbly).

## Motion

Calm and minimal — this audience wants trust, not flash. Diagram arrows and boxes fade/draw in once on scroll; the orange human-in-control node gets a single gentle pulse on first view. Everything renders complete and static under `prefers-reduced-motion`. No parallax, no autoplay, no particle fields.

## Quality floor (carried into the build)

Responsive to 360px with no horizontal scroll (diagrams reflow to vertical stacks on mobile); visible `:focus-visible`; `prefers-reduced-motion` honored; WCAG AA contrast (orange text only at large sizes or on ink; body stays ink on paper); semantic headings; single self-contained HTML file; Google Fonts the only external resource.

## What this hands to Step 6 (build)

A complete brief: light "drafting paper" palette with safety-orange accent, Space Grotesk / Inter / IBM Plex Mono, a clean SMB-SaaS layout, and the **blueprint block-diagram system** as the signature — hero diagram plus one per solution, each with the highlighted human-in-control node. Copy and section flow come from `strategy/homepage-copy.md`.

## Confirmed (Ali, 2026-07-16)

- Accent = **safety orange** ✓
- Display = **Space Grotesk** ✓
- **No monospace** ✓ — labels use uppercase letter-spaced Inter instead
- Align to the **existing Kentro design system** (Inter + the charcoal/gray neutrals; orange replaces the old blue accent) ✓
