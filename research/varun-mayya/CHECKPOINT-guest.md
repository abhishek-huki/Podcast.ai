# CHECKPOINT — Stage 2A — Varun Mayya
_2026-08-03 · V1 · Research 7/10_

## Headline finding
His channel teaches AI leverage; he runs ~500 employees and a 40-person game studio.
The employee count appears 3 times in 129,384 words. Nobody has asked him to reconcile it.

## Sources
| Source | Actor | Items | Cost |
|---|---|---|---|
| YouTube search | streamers/youtube-scraper | 80 → 61 relevant | $0.316 |
| Own channel, newest | streamers/youtube-scraper | 40 | $0.156 |
| Transcripts x10 | pintostudio/youtube-transcript-scraper | 129,384 words | $0.000 |
| Instagram | apify/instagram-post-scraper, then apify/instagram-scraper | 0 — "Request got blocked" both times | $0.003 |

Total **$0.47**. Running total across both guests: **$1.11** of the $5/month free tier.

## Lessons for the skill
- `sortingOrder: "newest"` made the channel run hang past 530s; without it, 40 items in
  under a minute. Don't pass sort options to this actor.
- Creator-guests need a different collection shape than interview-guests: for Varun,
  41 of 61 relevant videos are his own, so the channel pull matters more than the search.
- Verbal seam-hunting ("long story short") finds nothing in scripted own-channel content.
  For creators, seams come from things said once and dropped, not from hedges.
- Auto-captions garbled his name to "Arun Maya" — reinforces the verification stage.

## Next stage needs
- Host picks an angle from the three candidates in §8 of the brief.
- Stage 2B topic research not started.
- Independent verification of the 500-employee and billion-views claims.
