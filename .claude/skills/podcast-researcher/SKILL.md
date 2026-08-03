---
name: podcast-researcher
description: End-to-end podcast guest research and interview design. Give it a guest name (and optionally a topic) and it runs deep guest intelligence (website, web, Instagram, X, LinkedIn, YouTube appearances, transcripts, comments via Apify), separate topic/market research, finds the "Gold Zone" where the guest's unique knowledge meets an unmet audience demand, and produces a verified research brief plus ~25 sequenced interview questions with follow-ups and a live runsheet. Use this skill whenever the user mentions podcast prep, interview prep, guest research, "questions to ask <person>", show notes planning, briefing a host, or researching a person before recording or a long-form conversation — even if they only say "research this guest" or "prep me for my interview with X".
---

# Podcast Researcher

Turn one guest name into a complete, verified, interview-ready brief.

The job here is not "generate 25 questions". A model can do that from memory in ten
seconds and the result is the same generic list the guest has already answered on
forty other shows. The job is to **find what nobody has asked this guest yet, and
what the audience is actually starving to hear** — and that only comes from real
research, honestly assessed, iterated more than once.

## What good output looks like

A host reads the brief 30 minutes before recording and walks in knowing:
- what this guest uniquely knows that almost nobody else can explain
- which questions are dead on arrival because the guest has answered them 20 times
- which threads the guest started publicly and never finished
- how their public position has shifted, and what to ask about that shift
- 25 questions ordered so a beginner and an expert both stay hooked for 2 hours
- exactly which claims in the brief are verified vs. inferred

If the brief could have been written without doing the research, it failed.

## Operating principles

**Research is the hard part; everything else is downstream.** Synthesis, structuring,
and question writing are things the model is naturally good at. Collection is where
runs fail — social platforms are not readable by plain web search. Spend effort and
tool calls there.

**Never treat the first output as final.** Run V1 → critique → V2 → critique → V3.
Each critique is a written, specific gap list ("X/Twitter returned 4 posts, need 30+;
top-commented videos not analyzed"), not a vibe. Most of the value appears in V2/V3.

**Checkpoint after every stage.** Long research runs lose context. After each stage,
write a checkpoint file (see `assets/checkpoint-template.md`) recording what was
learned, which sources worked, which failed, and what the next stage needs. If the
conversation degrades, resume from the checkpoint instead of restarting.

**Separate what you saw from what you concluded.** Every factual claim in the brief
carries a source URL and a date. Anything inferred is labelled as inference. In the
original demo the model confidently got the host's own name wrong — a brief that
mixes verified and invented facts is worse than no brief, because the host says it
out loud on camera.

**The human owns the edit.** Suggestions that the host finds useless (e.g. comment
analysis, contradiction questions) get dropped from that show's SOP, not defended.
Capture those preferences — see "Learning from feedback" at the end.

## Stage 0 — Intake and restate

Collect from the user (ask only for what's missing; sensible defaults are fine):

| Field | Default if not given |
|---|---|
| Guest name + any handles/URLs | resolve by search, confirm identity with the user |
| Topic / angle | derive from guest's recent work |
| Episode length | 90–120 min |
| Audience level | mixed: beginner → advanced in one episode |
| Language / delivery style | match the user's own language, including Hinglish |
| Host's previous episodes on this topic | ask — needed for the kill list |
| No-go areas | ask — personal life, legal matters, sponsor conflicts |
| Budget for scraping | roughly 1–2 USD per guest |

Then **state back what you understood before doing any work**: what kind of episode
this is, what the output must contain, and what would make it fail. Get a yes.
This one question catches most wasted runs — it is cheap to ask and expensive to skip.

Write the answers to `research/<guest-slug>/00-intake.md`
(template: `assets/intake-template.md`).

## Stage 1 — Research plan and approval

Draft the source list and per-source date windows, then ask the user two questions
before spending money: *is anything missing that would give this show an unfair
advantage?* and *is any of this a waste of time for your format?*

Default windows: Instagram 30 days, X/Twitter 60 days, LinkedIn 60 days, YouTube
appearances 12 months, launches/news 6 months, foundational work — no limit.

Full source list, per-platform extraction targets, and the signals to pull out of
each transcript: **read `references/guest-research.md`**.
Apify setup, actor selection, cost control, and fallbacks when a scraper fails:
**read `references/apify-playbook.md`**.

## Stage 2A — Guest intelligence

Collect, then extract. Collection without extraction is just a pile of posts.

From everything gathered, produce these seven artifacts (details and formats in
`references/guest-research.md`):

1. **Core themes** — what they keep coming back to, in their own words
2. **Signature frameworks** — named models they teach, and whether each is now commodity
3. **Kill list** — questions answered to death; never ask these
4. **Unfinished threads** — ideas raised publicly and never explained (highest-value seam)
5. **Evolution / contradictions** — how their position moved and when
6. **Recent delta** — what changed in the last 30–90 days that no existing interview covers
7. **Landmines** — sensitive areas, disputes, things to route around or handle carefully

Then **self-assess honestly**: which sources returned thin data, what the run cost,
and whether this is deep enough to build a 2-hour masterclass on. If any source is
thin, that is a V2 task, not a footnote. Score against
`references/quality-rubric.md` and go deeper until the guest research scores 8+.

Checkpoint. Write `research/<guest-slug>/CHECKPOINT-guest.md`.

## Stage 2B — Topic and market intelligence

The guest is only half the episode. Research the topic independently:
current state of the field, the last 90 days of news, prevailing consensus,
existing frameworks in circulation, what practitioners argue about, and where
the good explanations simply don't exist yet.

Method, sources, and how to build the consensus map and content-supply-gap map:
**read `references/topic-research.md`**.

Checkpoint. Write `research/<guest-slug>/CHECKPOINT-topic.md`.

## Stage 3 — Synthesis: find the Gold Zone

Cross two axes:

- **Guest uniqueness** — what can *this* guest explain that few others credibly can?
- **Content-supply gap** — what does the audience clearly want where good material is scarce?

The intersection is the Gold Zone and it becomes the episode's spine. Everything
high-uniqueness but well-supplied is a repeat; everything in-demand but not unique
to the guest is a waste of the booking.

Scoring method, the 2×2, and how to turn the Gold Zone into 3–5 candidate episode
angles the user picks from: **read `references/synthesis.md`**.

Present the angles and let the user choose before writing questions. Question
generation on the wrong angle wastes the entire run.

## Stage 4 — Structure and 25 questions

Questions are sequenced as a learning arc, not a list — context → the guest's prior
beliefs → what changed → the tension worth pressing on → concrete examples →
step-by-step frameworks → advanced implementation → predictions and risks →
what the viewer does tomorrow morning.

Every question ships with: why it's being asked, what the guest will probably say,
the follow-up that gets past the canned answer, and a rough time allocation.

Full arc, question quality bar, follow-up ladders, rescue kit for short answers,
and the one-page live runsheet: **read `references/question-design.md`**.

## Stage 5 — Verification (do not skip)

Before delivery, verify every name, number, date, company, title, and quoted claim
against a source. Mark each as VERIFIED (with link) or UNVERIFIED. Anything that
stays unverified either gets cut or gets phrased as a question to the guest rather
than a statement by the host.

Checklist and the confidence-labelling scheme: **read `references/verification.md`**.

## Stage 6 — Deliverables

Write all of these to `research/<guest-slug>/`:

| File | What it is |
|---|---|
| `00-intake.md` | brief spec agreed in Stage 0 |
| `01-guest-brief.md` | the seven guest artifacts, with sources |
| `02-topic-brief.md` | consensus map + content gaps |
| `03-gold-zone.md` | 2×2, chosen angle, rationale |
| `04-questions.md` | 25 sequenced questions + follow-ups + timings |
| `05-runsheet.md` | one page the host holds during recording |
| `06-verification.md` | fact table with VERIFIED/UNVERIFIED status |
| `raw/` | raw scraped JSON, one file per source |
| `CHECKPOINT-*.md` | stage checkpoints |

Templates for the briefs, runsheet, and checkpoints live in `assets/`.

## Stage 7 — Score and iterate

Score the final package against `references/quality-rubric.md`, state the score
plainly, and list exactly what a higher score would require. Then do that work
rather than shipping a 7/10 with a note. Only stop when the rubric clears 8+ or
the user says it's good enough.

Be honest in self-assessment: a self-score is a planning tool for finding the next
gap, not a grade to defend. Inflating it destroys the only mechanism that makes
V2 and V3 better than V1.

## Learning from feedback

After the episode (or after the user reviews the brief), ask what to change:
questions that landed, questions that died, sections never used, sources that
were worth it. Then update this skill's references — kill list rules, which
platforms to bother with, question style, what to stop producing.

Record show-specific preferences in `references/show-profile.md` (create it on
first run) so the next guest starts from the host's accumulated taste rather
than from scratch. A skill that never absorbs feedback stays a template; one
that does becomes an experienced researcher.

## Tools

- **Apify** for social platforms — MCP connector if configured, otherwise
  `scripts/apify_run.py` with an `APIFY_TOKEN`. See `references/apify-playbook.md`.
- **Web search / fetch** for the open web, news, and indexed discussion.
- `scripts/new_guest.py <guest name>` scaffolds the output folder and copies templates.

Check tool access *before* promising a deep run, because the failure is silent
otherwise: in a sandboxed environment (Claude Code cloud sessions default to
**Trusted** network access), `WebSearch` works but `WebFetch` and direct calls to
`api.apify.com` return 403. An Apify MCP connector still works there, since connector
traffic does not use the session's network — and an Apify web-crawler actor can then
fetch pages that `WebFetch` cannot reach. If neither route is available, say so up
front and scope the run to what search snippets alone can support, rather than
producing a brief that looks complete but rests on almost no data.

Scraping is rate-limited and costs money: pull public data only, respect the
per-guest budget agreed in Stage 0, and report actual spend in each checkpoint.
