# Kentro homepage redesign — research & build progress

**Task:** Research small AI/agent-focused consulting firms (from the local Coresignal company dataset + their live websites), keep up to 20 high-quality samples, then design and build **5 distinct homepage candidates** for kentrolabs.ai to choose from.

**Model assignments:** Fable = planning, design directions, final judgment · Sonnet = database search + initial ranking + web validation · Opus = final ranking/selection + implementation.

## Deliverables

1. `research/` — **permanent** research data (extraction pools, ranked shortlists, per-site validation notes, full-page screenshots of kept samples). Not to be deleted.
2. `research/dossier.md` — the ≤20 kept firms with credibility/quality notes and selection reasons.
3. `research/service-taxonomy.md` — side product per Ali: a synthesized list of **service categories and niches** observed across the researched firms, as input for deciding Kentro's own service menu.
4. `candidates/` — 5 distinct homepage builds to choose from.

## Stage status

| # | Stage | Who | Status |
|---|---|---|---|
| 0 | Prep: brief deleted, research dirs created, duckdb/jq verified | Fable | ✅ done |
| 1 | Database extraction (3 keyword sweeps over Coresignal companies) | Sonnet | ✅ done |
| 2 | Dedupe + initial ranking → top ~70 | Sonnet | ✅ done |
| 3 | Website validation (domain/areas/credibility via live sites) | Sonnet | ✅ done — 27/70 passed |
| 4 | Visual QA (Chrome) + final ranking → ≤20 kept samples | Opus | ✅ done — 20 selected |
| 5 | Walk shortlist → 5 design + content directions | Fable | ✅ done |
| 6 | Build 5 homepage candidates in `candidates/` | Opus ×5 | ✅ done |
| 7 | Final judgment + ranked presentation to Ali | Fable | ✅ done |
| 8 | Round 2: structural redesign after layout-authenticity feedback | Fable plan · Opus ×2 build | ✅ done — c6 + c7 built and verified |

## Stage 0 — Prep (done)

- `kentro-ai-labs-website-brief.md` deleted per instruction (research-driven redesign; brief intentionally not used).
- Created `research/` (pools, shortlists, dossier, screenshots) and `candidates/` (the 5 builds). Both untracked; nothing committed.
- Dataset: `~/workspace/data/coresignal/linkedin/clean_company/202606/partition_by_column=united_states/*.json.gz` (~40M US companies, ~19 GB), queried via DuckDB.
- Carry-over constraints for the final builds: anonymous firm, no fabricated proof, CTA → hello@kentrolabs.ai, static self-contained HTML, footer legal links.

## Stage 1 — Database extraction

_Three parallel Sonnet sweeps with different keyword families; results land in `research/pool-*.json`._

- `ai-ml-consulting` — AI/ML/data-science consulting keywords → **300 kept** (~2,007 raw matches; exact-employees 1–50 used over stale size_range buckets)
- `agentic-llm` — agentic/LLM/generative-AI + consulting signals → **300 kept** (~8,008 raw; 'llm' tightened to word-boundary regex to kill 'fulfillment/Hollywood' noise; staffing/recruiting deprioritized)
- `ai-studio-boutique` — AI studios/labs/applied-AI boutiques → **300 kept** (5,768 raw; penalized staffing-heavy descriptions)

Pools saved: `research/pool-*.json` (kept permanently).

## Stage 2 — Dedupe + initial ranking (done)

**877 unique firms** after dedupe (by company_id/domain). Scored 0–10 on: AI/agents-consulting core business, boutique scale (1–50, sweet spot 2–25), description specificity, credibility hints (founded year, followers). Full scored list: `research/shortlist-initial.json`.

⚠️ Caveat noted: scores saturated at the top (many 10.0s with near-templated reasons) — the DB fields alone don't differentiate well past a point. Treating stage 2 as a recall filter; real precision comes from stage 3 (live-site validation) and stage 4 (visual QA).

**Top 70 advanced to website validation:**

| Firm | Website |
|---|---|
| 2two2 Consulting | http://2two2consulting.com |
| 4sight AI | https://4sightai.com |
| AI Leadership Institute | https://skool.com/aili/about |
| Alive Studios.AI | https://alivestudios.ai |
| Anveshi.ai | https://anveshi.ai |
| Anyon Consulting | https://anyonconsulting.com |
| BAY6.AI | https://bay6.ai |
| Beige Bananas | https://beigebananas.com/ |
| CO/AI | http://getcoai.com |
| Cocoon AI | https://cocoon-ai.com |
| Crimson Sage Global LLC | http://crimsonsageglobal.com |
| EXRwebflow | https://exrwebflow.com |
| EaaS AI | http://eaaservice.com |
| Elucidate AI | https://elucidate.ai |
| Enso Labs | https://ensolabs.ai |
| Execucom AI | https://execucom.co |
| Fintechy | https://fintechy.net |
| FirmAdapt | https://firmadapt.com |
| Frontier Foundry | https://frontierfoundry.com |
| GenAI Protos | https://genaiprotos.com |
| Global Technology Partners | https://globaltechnologypartners.com |
| Grace & Cronos | https://graceandcronos.com |
| GreenData Ventures | https://greendata.io |
| HelloAgentic | https://helloagentic.ai |
| Human Pilots AI | https://humanpilots.ai |
| ISW Consulting | https://isw.consulting |
| InitializeAI | https://initializeai.com |
| InnovatiCS | https://innovatics.ai |
| Intellivon | https://intellivon.com |
| Intellus | https://www.intellus.build |
| Knova AI | https://knova.us |
| Lexim AI | https://lexim.ai |
| Metricoid Technology Solutions | https://metricoidtech.com |
| N5R.AI | http://n5r.ai |
| Neferdata | https://neferdata.com |
| NeoLumin | https://neolumin.com |
| Netwise Consultancy Services | https://netwiseconsultancy.com |
| NeuraNx.ai | https://neuranx.ai |
| NewWave AI Partners LLC. | https://newwavepartners.ai |
| Nexyom | https://nexyom.com |
| OmbuLabs.ai | https://ombulabs.ai |
| Oori Data LLC | https://oori.dev |
| Opinosis Analytics | https://opinosis-analytics.com |
| OptimaNova AI | https://optimanova.ai |
| Pandatron | https://pandatron.ai |
| Pi R-Square Solutions LLC | https://pirsquaresolutions.com |
| Premier Strategy Consulting | https://premier-strategy.com |
| Purple AI Lab | https://purpleallab.com |
| QuantFi | https://quantfi.us |
| Remoder | https://remoder.com |
| Sense7ai | https://sense7ai.com |
| Sentia+ | https://sentia.website |
| Tessera Analytics | https://tessera-analytics.ai |
| The International Social Impact Institute® | https://internationalsocialimpactinstitute.com |
| Tico AI | https://ticoai.net |
| aallie | https://aallie.com |
| adaptAI Inc. | https://adaptai.com |
| aiChemist | https://aichemist.agency |
| CoreAi Consulting | https://coreaiconsulting.com |
| Dynapt | https://dynapt.com |
| Evren AI | https://evrenai.com |
| GoGloby | https://gogloby.com |
| Hexaa | https://thehexaa.ai |
| Nimbusnext | https://nimbusnext.com |
| Pure Math AI | https://puremath.ai |
| Rytsense Technologies | https://rytsensetech.com |
| SimplAI | https://simplai.ai |
| Soothsayer Analytics | https://soothsayeranalytics.com |
| WhiteBox | https://whiteboxml.com |
| Cake Studio AI | https://cakestudio.ai |


## Stage 3 — Website validation (done)

70 sites fetched and judged by one Sonnet agent each. **27 passed** (reachable + confirmed small AI/agents consultancy + credibility ≥3 + site quality ≥3). Failure breakdown: 3 unreachable · 24 reachable but not actually AI-consulting firms (SaaS products, Skool course communities, staffing, generic dev shops) · 16 confirmed-but-below-bar (template sites, thin credibility). Full per-site verdicts incl. service categories + niches: `research/validation.json` (permanent; feeds the service-taxonomy deliverable).

**27 advancing to Opus visual QA** (Q = site quality /5, C = credibility /5):

| Firm | Website | Q | C | Validator note (truncated) |
|---|---|---|---|---|
| FirmAdapt | https://firmadapt.com | 5 | 4 | Highly distinctive design with custom SVG diagrams, a serif/mono type pairing, and an unusually product-like free diagnostic tool (8-lens company scan… |
| HelloAgentic | https://helloagentic.ai | 5 | 4 | Exceptionally sharp, non-templated positioning and copy (Blueprint/Build/Operate framing, explicit dev-shop-vs-Big-4 comparison, live unit-economics d… |
| Frontier Foundry | https://frontierfoundry.com | 4 | 5 | Polished, content-rich Next.js/Astro site with named founder (ex-FDIC CIO), real case studies, industry-specific pages, glossary, media appearances, a… |
| Anveshi.ai | https://anveshi.ai | 4 | 4 | Distinctive, consistent mountaineering/expedition metaphor carried through copy and structure (Basecamp/Route Map/Ascent, 12-Objective Transformation … |
| Beige Bananas | https://beigebananas.com/ | 4 | 4 | Distinctive, non-templated brand voice ("Intelligence is the new inventory", "Built with Love") with a clear productized service menu and quantified i… |
| Cocoon AI | https://cocoon-ai.com | 4 | 4 | Named founders (CEO/CTO) with LinkedIn profiles, real address, structured data, distinct 'five engagement shapes' productized offer framing, and a dif… |
| Enso Labs | https://ensolabs.ai | 4 | 4 | Polished modern Next.js site with tight, specific copy (named engagement tiers like "2-week AI Audit", vertical-specific service pages, an insights/bl… |
| Fintechy | https://fintechy.net | 4 | 4 | Well-structured Next.js site with detailed schema.org markup, transparent pricing tiers ($150K-$400K pilots), a clear four-phase engagement methodolog… |
| GenAI Protos | https://genaiprotos.com | 4 | 4 | Modern Next.js site with specific, non-templated copy (named solutions like 'Chat-with-Jira', concrete metrics like '2-4 week MVPs', '20-30% faster de… |
| Grace & Cronos | https://graceandcronos.com | 4 | 4 | Strong, non-templated copy with a named proprietary methodology (Leverage Index™), a structured 4-phase engagement model, and interactive elements (le… |
| Human Pilots AI | https://humanpilots.ai | 4 | 4 | Confident, differentiated copy built around a named proprietary framework (ARC) and a clear 3-stage engagement model, plus case studies with specific … |
| InitializeAI | https://initializeai.com | 4 | 4 | Deep, well-structured IA with named methodology ("AI Execution Gap"), interactive tools (scorecard, ROI calculator), 6+ case studies, and extensive ve… |
| Sense7ai | https://sense7ai.com | 4 | 4 | Custom Next.js build with polished typography (Inter + Cormorant Garamond mix), clear regulated-industry positioning, named service tiers, case studie… |
| Evren AI | https://evrenai.com | 4 | 4 | Polished Next.js site with strong structured content (schema.org markup, FAQ, named services, founder letter, named case study with iSeedoc/HIPAA tele… |
| Hexaa | https://thehexaa.ai | 4 | 4 | Distinctive, specific copy (named example invoices, confidence-threshold mechanics, '47+ engagements') avoids generic AI-agency boilerplate; clean mod… |
| WhiteBox | https://whiteboxml.com | 4 | 4 | Clean, well-structured Webflow site with a clear 5-step methodology narrative, named named case studies with real client (Vodafone) and quantified pro… |
| Execucom AI | https://execucom.co | 4 | 3 | Clean modern Next.js site with a distinctive gradient hero, a clear branded 3-step methodology (AIT Method, AI Strategy Roadmap trademarked), and shar… |
| BAY6.AI | https://bay6.ai | 3 | 4 | Polished, professional enterprise positioning with a distinctive 'Think6' framework and named vertical products, but it's WordPress/Elementor-built wi… |
| Elucidate AI | https://elucidate.ai | 3 | 4 | Named founders, real case studies (Airvantage, Huduma Credit), client logos, and concrete metrics ($800M+ decisions, 15% KPI lift) give strong credibi… |
| NeoLumin | https://neolumin.com | 3 | 4 | Solid, professional WordPress site with real named case studies (bank, non-profit, coaching client, trade association) with quantified outcomes and ma… |
| OmbuLabs.ai | https://ombulabs.ai | 3 | 4 | Legitimate, well-established firm (founded 2011, ~15-person named team, real case studies including Snapchat) with a clear productized service menu, b… |
| Opinosis Analytics | https://opinosis-analytics.com | 3 | 4 | Standard WordPress/Astra template with generic stock-style hero imagery, but content is substantive and specific (named founder with credentials, book… |
| GoGloby | https://gogloby.com | 3 | 4 | Content is substantive and specific with named enterprise clients (Zillow, GitLab, Hasbro, Tata), quantified claims, and named testimonials, giving st… |
| Soothsayer Analytics | https://soothsayeranalytics.com | 3 | 4 | Content is substantive with named solutions (AuGENT, ESG Analytics), real case studies, blog, podcast, and industry pages, signaling a genuine establi… |
| 4sight AI | https://4sightai.com | 3 | 3 | Site is a Next.js build with animated number counters and a broad, somewhat scattered product/service portfolio (police AI, news AI, finance co-pilot,… |
| GreenData Ventures | https://greendata.io | 3 | 3 | Clean modern Next.js build with a coherent "grind to generativity" narrative and a clearly laid-out service menu, but no named clients, case studies, … |
| aiChemist | https://aichemist.agency | 3 | 3 | Clear, specific offer-driven copy with a distinct "diagnose before you build" positioning, ROI calculator, and concrete pricing — stronger content tha… |

## Stage 4 — Visual QA + final selection (done)

All 27 sites rendered in Chrome (5 sequential Opus batches), full-page screenshots in `research/screenshots/`. Final Opus selector (high effort) read both the visual reports and `research/validation.json`, picked **20 benchmarks** for positioning diversity (technical-led, vertical-specialist, enablement-led, productized-offer-led), wrote `research/dossier.md`. Machine-readable: `research/final-selection.json`.

**Selected 20 (ranked):**

1. **Hexaa** — https://thehexaa.ai  
   Highest-craft editorial system in the set (serif-italic-in-sans, live invoice-UI hero mock, volume-slider ROI calculator) that reads as authored, not templated.
2. **Enso Labs** — https://ensolabs.ai  
   Dark editorial art direction a studio would sign, with a live LangGraph terminal as proof-of-shipping and a 'no vanity metrics' proof-grid framing.
3. **GoGloby** — https://gogloby.com  
   Best risk-reversal in the batch ($3M liability + 120-day guarantee) plus recognizable client logos and a sharp production-without-risk niche thesis.
4. **Frontier Foundry** — https://frontierfoundry.com  
   Highest-credibility firm (real gov logos, ex-FDIC-CIO founder) that teaches category-owning framing ('three-part sovereignty test') and bespoke technical diagram art.
5. **HelloAgentic** — https://helloagentic.ai  
   Master class in productized fixed-shape offers, contrarian thesis ('a demo is not a system'), and building trust via unit-economics transparency with zero client logos.
6. **Grace & Cronos** — https://graceandcronos.com  
   Interaction-led content: clickable Leverage Map, named methodology, and a productized 30-day assessment with a week-by-week deliverable timeline.
7. **InitializeAI** — https://initializeai.com  
   The definitive diagnostic-as-lead-magnet playbook: hero scorecard UI, free Gap Score, ROI calculator, and named downloadable toolkits per step.
8. **Beige Bananas** — https://beigebananas.com/  
   Strongest brand personality in the set (rotating hero verb, LaTeX 'equation' graphic) and anonymized-but-specific testimonials that keep credibility without named clients.
9. **Human Pilots AI** — https://humanpilots.ai  
   Best enablement/advisory positioning: verbatim board-anxiety pain cards, the ARC framework, and sticky reframes on a restrained Squarespace build.
10. **FirmAdapt** — https://firmadapt.com  
   Most product-like top-of-funnel — a free type-your-domain 8-lens scan and a whole suite of free micro-tools driving the funnel, with a HUD/telemetry aesthetic.
11. **WhiteBox** — https://whiteboxml.com  
   Model for logo-led trust (DoD/Vodafone/Carrefour) and demoing real work via an embedded live forecasting data-viz, in a high-craft minimal dark style.
12. **Evren AI** — https://evrenai.com  
   Warm serif-on-peach palette that breaks the cold-navy AI-site default, plus an AEO-aware FAQ written for buyers and AI assistants.
13. **Elucidate AI** — https://elucidate.ai  
   SLA-tied, dated, vertical-tagged case studies and a bespoke 3D data-mesh hero show how to make metrics read as real, not vanity.
14. **aiChemist** — https://aichemist.agency  
   Closest peer to a small SMB shop: transparent fixed-price roadmap CTA, hero ROI calculator anchored to price, and a full trust-without-logos playbook.
15. **Cocoon AI** — https://cocoon-ai.com  
   Excellent 'meet you where you are' diagnostic self-selector routing felt problems to named service tiers, plus honesty about when AI is the wrong call.
16. **Anveshi.ai** — https://anveshi.ai  
   Sustained single-metaphor branding (Sherpa expedition), humanist counter-positioning, and per-vertical GEO hooks — plus a cautionary hero-contrast failure.
17. **GreenData Ventures** — https://greendata.io  
   Teaches how a young firm borrows credibility: quantified industry proof-point carousel and an 'AI Entourage' partner network in place of client logos.
18. **Execucom AI** — https://execucom.co  
   Sharp objection-handling FAQ (verbatim buyer fears) and motive-tuned audience-segment cards speaking to three buyers on one page.
19. **GenAI Protos** — https://genaiprotos.com  
   Concrete-offering patterns: industry-tagged Solution cards as mini case studies and named productized accelerators framed as buyable IP.
20. **Sense7ai** — https://sense7ai.com  
   Regulated-vertical positioning with radical-honesty trust copy ('certs earned, not claimed') and response-time SLAs stated in the CTA.

**Dropped 7:**

- **Fintechy** — Polished but generic dark Next.js agency template with no distinctive typographic or color POV; its trust-bar and 7-day-assessment ideas are already better shown by higher-ranked picks.
- **BAY6.AI** — Reads as a product/platform company on a default dark-mode AI-startup template with no case studies or metrics; positioning is off-axis and design isn't distinctive.
- **NeoLumin** — Busy, template-driven WordPress/Elementor build (vq2) that visibly duplicates its hero block — a build error, not a benchmark; its case studies are its only asset and don't outweigh weak design.
- **OmbuLabs.ai** — Legitimate firm with real clients (Snapchat) but a visually generic light agency template (vq2) whose lessons (personable About, open-source trust) are minor and covered elsewhere.
- **Opinosis Analytics** — Substantive founder-led content but a formulaic blue-gradient WordPress template (vq2) with a mid-page rendering gap; unremarkable as a design or content benchmark.
- **Soothsayer Analytics** — Credible established firm but dated, stock-heavy 'AI-slop' imagery and cluttered mega-menu (vq2); its quantified-outcome band is better demonstrated by GoGloby/WhiteBox.
- **4sight AI** — Generic AI-slop hero (stock robot, spinning buzzword wheel) collapsing into text walls (vq2); nothing to learn except what to avoid.

## Stage 5 — Fable walkthrough → design directions (done)

Read `research/dossier.md` in full; personally viewed screenshot crops of Hexaa, Enso Labs, HelloAgentic, FirmAdapt, Evren AI, Beige Bananas to calibrate. Wrote two deliverables:

- **`research/service-taxonomy.md`** — normalized service categories (strategy/roadmap and custom agents are the crowded center; IDP under-supplied; fractional leadership + operate retainers are how small firms build recurring revenue; construction nearly empty — relevant given Agent K) and niches by frequency (healthcare 10, finserv 9, manufacturing 4 …), plus the observed conversion ladder (free diagnostic → fixed-price entry → build → retainer).
- **`research/design-directions.md`** — full specs for 5 candidates, each betting on a different conversion mechanism, trust playbook, and aesthetic:
  1. **Blueprint** — productized fixed-shape offers (Assess/Build/Operate), positioning matrix; near-white + hot orange restraint.
  2. **Field Notes** — dark editorial studio, § markers, animated terminal proof-of-craft; Fraunces italic + amber.
  3. **Diagnostic** — interactive 8-lens "AI Production-Readiness Check" (client-side, instant score routing to services); HUD blue-teal + serif.
  4. **Warm Counsel** — SMB-owner humanist, buyer-situation self-selector cards; cream/peach/coral + Fraunces.
  5. **Ledger** — radical-honesty ledger ("what we'll claim / what we won't claim yet"), engagement spec-sheet, SLA; Swiss grid + deep green.

All five share hard rules: anonymity, zero fabricated proof, professional voice, mailto CTA, single-file static HTML, 360px responsive, reduced-motion, footer legal links.

## Stage 6 — Building 5 candidates (running)

Five parallel Opus agents, one per candidate, each implementing its spec from `research/design-directions.md` into `candidates/c*.html`. Browser verification deferred to stage 7 (Fable) to avoid contention.

## Stage 7 — Fable final judgment (done)

All five candidates verified in the browser at 1440px and 390px (screenshots: `research/screenshots-candidates/`). Checks: no horizontal overflow at 390px (one bug found and fixed — C5's hero grid never collapsed on mobile, blowing out the page; fixed with a one-line media-query override), C3's interactive readiness check tested end-to-end (correct score, tier, weak-lens routing, and prefilled mailto subject/body), copyright years, footer links, and mailto CTAs verified across all five.

**Fable ranking (for the site's job: trust-confirmation for warm leads, dual audience, must not read generic):**

1. **C1 Blueprint** — best overall fit. The fixed-shape engagements plus the freelancer/Kentro/big-consultancy matrix answer the two questions every warm lead has ("what am I buying, why you"), and the restrained paper-and-orange craft reads premium to both audiences. Least adventurous visually — its only real weakness.
2. **C5 Ledger** — the most differentiated trust strategy in the set; the honesty ledger and term-sheet spec table are disarming and memorable. Slightly austere for non-technical owners. Note: it cites Agent K by name inside the ledger ("we operate our own production AI product") — a deliberate, honest extension beyond the footer-only convention; flagged for Ali's call.
3. **C2 Field Notes** — strongest pure art direction (editorial dark, serif italics, credible terminal simulation). Speaks most powerfully to technical buyers; least approachable for SMB owners.
4. **C3 Diagnostic** — the readiness check is a genuine lead-gen asset and it works flawlessly; as the homepage it subordinates services to the tool, and the HUD look is tonally the riskiest. Strong candidate to live on as a standalone page regardless of the winner.
5. **C4 Warm Counsel** — warmest and most owner-friendly, disciplined contrast, good self-selector; softest technical-credibility signaling for the technical-team audience.

Cross-pollination notes: C3's check could become a `/readiness` page under any winner; C5's ledger section could merge into C1; C2's field-notes section is a natural "Insights" seed.

**Awaiting Ali's pick.** View locally: `python3 -m http.server` → `/candidates/c{1..5}-*.html`. Winner replaces `/index.html`; nothing committed yet.

## Stage 8 — Round 2: structural redesign (running)

**Owner feedback on round 1:** all five candidates (and most benchmarks) share the same skeleton — hero → alternating bands → three-card grid → numbered process cards → dark CTA band — which reads as AI-generated regardless of skin. c5-ledger strongly disliked (dropped). Content of c1–c4 liked. Requirement: genuinely different layouts (without breaking UI/UX fundamentals), serving both tech-savvy and non-tech-savvy buyers.

**Owner decisions (via questions):** build layouts A + B · industry-neutral (no construction wedge; Agent K stays footer-only) · c3 readiness check becomes a compact embedded module.

**Spec:** `research/design-directions-v2.md`. Key moves: an explicit BANNED-PATTERNS list (the round-1 skeleton elements); dual audience handled by annotation layers (margin notes / sidenotes) instead of a segregated "for technical teams" band; content recycled from c1 (engagement shapes), c2 (method/honesty), c3 (lenses + scoring), c4 (situation copy).

- **C6 "Follow the invoice"** (`candidates/c6-invoice.html`) — the page is one labeled-illustrative worked example: an invoice arrives at 07:42 and the scroll follows it through extraction → checks → human exception → posting → month-end report, with services/engagement attached to stations; paper-and-annotation aesthetic (Newsreader/Public Sans/Plex Mono; pen blue, stamp red, posted green).
- **C7 "The working memo"** (`candidates/c7-memo.html`) — the page is a typeset working document: memo header, sticky ToC, numbered sections, Tufte-style technical sidenotes, engagement terms as memo clauses, readiness check as Appendix A, optional plain-English glossary; Literata + Plex Mono, oxblood reference accent.

Two Opus builders launched in parallel; Fable browser judgment to follow (same verification protocol as stage 7).

### Stage 8 verification + judgment (Fable, done)

Both round-2 candidates verified in the browser (screenshots in `research/screenshots-candidates/`): zero horizontal overflow at 390px; readiness modules tested end-to-end on both (c6: 5/8 → Piloting; c7: 2/8 → Exploring; correct tier-carrying mailtos); c6's scroll-reveal confirmed working on real scroll (initial blank full-page capture was a screenshot artifact — six stations reveal correctly and render complete under reduced-motion/no-JS); c7's 10 sidenotes have accessible inline fallbacks.

**Judgment vs the authenticity bar:** both pass the "could this section live on a generic consultancy site?" test — no banned skeleton patterns present. c6 leads by a nose (the recurring annotated invoice makes the firm's work self-evident to both audiences); c7 is the most human-authored page of the whole project (typeset memo, sidenotes, glossary). They pair naturally: one as homepage, the other as a secondary page (/how-we-work as "the memo", or the walkthrough as its own page).

**Awaiting Ali's pick between c6, c7, or a pairing.** Nothing committed.
