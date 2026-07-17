# Step 3 — The Three Solutions, with Block Diagrams and Value Stories

Status: **draft for Ali's review.** Framed for the primary niche (construction and the trades) and the adjacent (home / field services). Each solution has: the problem in the owner's words, how it works in plain language, a **block diagram** (boxes and arrows), the before→after value, and what makes it custom. These become the "what we build" backbone of the homepage.

**Confirmed inputs (Ali, 2026-07-16):** integrations = QuickBooks / Sage / Foundation (accounting), Procore / Buildertrend (PM), plus email and spreadsheets · proof = Agent K (a voice-and-text photo-logging and issue-tracking app used on job sites) plus honestly anonymized team experience · doc priorities = subcontractor/supplier invoices, POs, lien waivers · assistant user = office/admin staff · agent showcase = collecting lien waivers and compliance docs from subcontractors.

**The through-line across all three:** the AI does the work, a **person stays in control of the exceptions**, and everything is **built around your business** — your POs, your project data, your subs. That is the "works with you, not a generic bot" differentiator, made concrete.

The block diagrams below are drawn in ASCII to show structure and get the logic approved. In the build (Step 6) each becomes a clean, styled diagram — boxes, arrows, one highlighted "a person decides" step.

---

## 1. Document processing — *Paperwork, handled.*

**The problem (owner's words):** "Every sub and supplier sends invoices a different way — email, a photo, a paper slip. My office manager retypes each one into QuickBooks, matches it to the right PO and job, and chases down the ones that look wrong. It eats hours, and things still slip through — we've paid the wrong amount more than once."

**How it works (plain):** The system reads each invoice however it arrives, pulls out the vendor, amount, and line items, checks it against your purchase orders and job budgets, and posts it straight into your accounting system — flagging only the ones that don't match for your admin to approve.

**Block diagram:**
```
  Invoice arrives          AI reads it              Checks it                 Result
  email · photo · PDF  ──▶ extracts vendor,   ──▶   matches against    ──┬──▶ MATCHES ──────▶ Posts to QuickBooks
  · paper                  amount, line items       your PO and         │
                           (+ a confidence score)   job budget          └──▶ DOESN'T MATCH ──▶ Flags for your admin
                                                                                                      │ approve
                                                                                                      ▼
                                                                                                    Posts
```
*Diagram spec for build: 4 stages left→right; the "Checks it" node branches into a clean path (auto-post) and an exception path (human approve → post). Highlight the "Flags for your admin" node as the human-in-control step.*

**The value (before → after):**
- Before: hours of manual data entry, invoices matched by hand, overbillings caught late or not at all.
- After: invoices posted automatically, every one checked against the PO, exceptions caught before they're paid, your admin's hours given back.

**Custom to you:** built around your document types, your POs, your chart of accounts, and your job-costing — not a generic OCR tool.

---

## 2. AI assistants — *An assistant that actually knows your business.*

**The problem (owner's words):** "My office staff spend half their day answering the same questions — what's the status of the Elm Street job, what did we quote for that change, what's the spec on those windows. The answer is always buried in an email, a plan, or somebody's head. People wait, or they guess wrong."

**How it works (plain):** An assistant trained on your own project documents and history — plans, specs, contracts, schedules, past jobs, pricing — that answers questions instantly, with the source. Because it knows *your* jobs, not the internet, the answer is right and you can see where it came from.

**Block diagram:**
```
   YOUR project data                                          Instant, sourced answer
   plans · specs · contracts  ───trained into───▶             "Andersen A-Series,
   schedules · past jobs · pricing        │                    per approved RFI-14"
                                          ▼                     + the document
                                   ┌─────────────┐                    ▲
                    Question ────▶ │ AI ASSISTANT│ ───answers from────┘
        "What's the spec on the    │ knows YOUR  │      your own records
         third-floor windows?"     │ business    │
                                   └─────────────┘
```
*Diagram spec for build: your-data node feeds the central assistant; a question flows in, a sourced answer flows out. Emphasize "knows YOUR business, not the internet" on the central node.*

**The value (before → after):**
- Before: constant interruptions, digging through email and plans, wrong answers, delays and rework.
- After: anyone gets an instant, correct, sourced answer — office staff stop being the bottleneck, mistakes drop.

**Custom to you:** grounded in your project records; answers in your terms; and (adjacent niche) for home/field services it becomes the assistant that answers customer calls and booking questions 24/7 — a missed call is a missed job.

---

## 3. AI agents — *An AI teammate that does the routine work.*

**The problem (owner's words):** "Before I can pay a sub or bill a client, I need signed lien waivers and current insurance certs from everyone. Tracking who's missing what, chasing them down, checking the paperwork, filing it — it's a whole day of nagging, every pay cycle. Miss one and it holds up a payment or puts us at risk."

**How it works (plain):** A teammate agent that runs the whole loop: it checks which subcontractors are missing a signed lien waiver or a current insurance certificate, requests it from each one, follows up until they respond, validates what comes back, files it, and updates your system — handing you only the exceptions that need a person.

**Block diagram:**
```
  Trigger              Agent checks          Requests           Collects &
  payment run    ──▶   who's missing   ──▶   from each    ──▶   validates
  or new sub           docs                  sub                waiver / cert
                           ▲                                        │
                           │                                        ▼
                           └──── follows up ◀──── not valid / no reply
                                 until done
                                                              valid │
                                                                    ▼
                                              Files it · updates your system ·
                                              flags only the exceptions for you
```
*Diagram spec for build: a left→right multi-step flow with a visible follow-up LOOP back to the request step, resolving into "files it + flags exceptions." Highlight the loop (persistence) and the final "flags exceptions for you" (human-in-control) nodes.*

**The value (before → after):**
- Before: a full day of manual chasing every pay cycle, missed documents, delayed payments, compliance exposure.
- After: the loop runs itself, documents get collected and filed, you handle only the exceptions — a recurring chore turned into a background process.

**Custom to you:** built around your subs, your document requirements, and your payment schedule; and the same pattern extends to other trades workflows — quote follow-ups, subcontractor onboarding, scheduling and dispatch for field-services businesses.

---

## How this proves out, and how it maps to the homepage

- **Proof, not claims:** Kentro already ships **Agent K** — a voice-and-text photo-logging and issue-tracking app used on real job sites. It's the evidence that we build and run production AI in construction, which lets the three solutions above read as "things this firm actually does," not aspirations. (Named as proof; the firm stays anonymous.)
- **The Read → Answer → Do spine holds:** solution 1 understands what comes in, solution 2 answers what people ask, solution 3 does the work that follows — a story a non-technical owner can follow top to bottom.
- **They stack:** a construction business can start with invoices (1), add an assistant on that same project information (2), and grow into agents that run whole compliance and scheduling loops (3). Start small, expand as trust grows.
- **Homepage use:** each solution becomes a block — plain headline, the block diagram, one or two lines of value — under a "what we build" section, with the "works with you / you stay in control / built for your business" theme carried throughout. The longer "follow the invoice" narrative (old C6) becomes a deeper solution or story page, not the homepage.

## Open items carried forward

- Exact homepage ordering and how much of each solution shows on the homepage vs a solution page → Step 4 (content architecture).
- Visual treatment of the diagrams (colors, the highlighted human step, motion) → Step 5 (design direction).
