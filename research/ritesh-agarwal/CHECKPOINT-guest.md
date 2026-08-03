# CHECKPOINT — Stage 2A guest intelligence — Ritesh Agarwal
_2026-08-03 · Version V1_

## What was learned
- The founder-journey angle is saturated: parents (62 mentions), Thiel (38), SIM cards
  (26), Odisha (21), Kota (13) across four transcripts. Dedicated clips exist for several.
- The unexplored seam sits inside the same angle: **capital**. SoftBank/Masayoshi appears
  once across 61k words, while he states "capital is more an outcome rather than the
  input" without ever arguing it.
- Raj Shamani's channel already published this exact angle in 2022 (610k views).

## Sources that worked
| Source | Actor | Items | Cost |
|---|---|---|---|
| YouTube search pass 1 | streamers/youtube-scraper | 30 (noisy) | $0.116 |
| YouTube search pass 2 | streamers/youtube-scraper | 75 | $0.284 |
| Transcripts x4 | pintostudio/youtube-transcript-scraper | 61,155 words | $0.000 |

## Sources that failed or were skipped
| Source | What happened | Recoverable? |
|---|---|---|
| X / LinkedIn / Instagram | never attempted this pass | yes — actors exist, budget remains |
| YouTube comments | never attempted | yes |
| Pass-1 search precision | 30 results, only ~7 actually Ritesh | fixed by quoting the name in pass 2 |

## Lessons for the skill
- Quote the guest's name in YouTube search queries; unquoted queries return other people.
- Hindi auto-captions break English keyword analysis silently — run both alphabets.
- Item count is a bad thinness test; transcripts arrive as one item. Fixed in apify_run.py.

## Score
Research **6/10** · Questions n/a · Integrity n/a
To gain 2 points: run the three social actors, pull top-50 comments on the two biggest
videos, transcribe 4-6 more appearances (free) including Nikhil Kamath's.

## Next stage needs
- Host identity confirmation (is this Raj Shamani's show?) — changes the kill list.
- No-go decision on the personal/relationship thread.
- Stage 2B topic research not started.

---

# CHECKPOINT — V2 — 2026-08-03

## What changed
- Transcripts 4 → 13 (61k → 149k words). All free.
- Instagram: 30 posts, Apr–Jul 2026. Best source in the whole run for recent delta.
- Comments: 120 sampled. Low yield, but produced one cross-source insight.
- X/Twitter and LinkedIn: failed. Declared, not hidden.
- Host confirmed: this is a NEW channel, so no own-show kill list, but the
  differentiation bar is higher. Personal/relationship thread dropped on instruction.

## Cost ledger
YouTube search $0.400 · comments $0.160 · Instagram $0.076 · X $0.004 · LinkedIn $0.0001
· transcripts $0.000 → **total $0.64** of the $5/month free tier.

## Lessons for the skill
- On Apify's free tier X/Twitter is effectively unavailable: two actors returned
  `noResults` markers and billing notices instead of posts. Plan around it.
- Instagram captions beat every other social source for recent delta on this guest.
- Comments were the worst return per rupee; make them opt-in, not default.
- Cross-referencing comment complaints against Instagram product launches produced the
  single best question in the brief. Worth making that cross-source pass explicit.

## Score
Research **8/10** · Questions n/a · Integrity n/a
To reach 9: web-search fallbacks for X/LinkedIn, transcribe the Nikhil Kamath episode,
run Stage 2B. Cost under $0.10.
