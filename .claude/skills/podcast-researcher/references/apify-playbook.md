# Apify playbook

Plain web search cannot see inside Instagram, X, LinkedIn, or YouTube comments.
Apify runs "Actors" (hosted scrapers) that can. This file covers access, actor
selection, inputs, cost control, and what to do when a scraper fails.

## Contents
- [Two ways to reach Apify](#two-ways-to-reach-apify)
- [Choosing an actor](#choosing-an-actor)
- [Known-good starting points](#known-good-starting-points)
- [Typical inputs](#typical-inputs)
- [Cost control](#cost-control)
- [When a scraper fails](#when-a-scraper-fails)
- [Data hygiene](#data-hygiene)

## Two ways to reach Apify

**A. Apify connector (preferred in Claude apps).** One-time setup by the user:
1. Create an account at apify.com and open the Console.
2. Settings → API & Integrations → copy the personal API token.
3. In Claude, open Settings → Connectors, add the Apify connector, paste the token.
4. Approve the tools when first used.

Once connected, actors can be searched and run directly as tool calls.

**B. Script fallback (any terminal).** Export the token and use the bundled script:

```bash
export APIFY_TOKEN=apify_api_xxx

# find an actor
python scripts/apify_run.py search "instagram scraper"

# run one and save the dataset
python scripts/apify_run.py run apify/instagram-scraper \
  --input '{"directUrls":["https://instagram.com/handle"],"resultsLimit":30}' \
  --out research/<slug>/raw/instagram.json
```

The script polls until the run finishes, downloads the dataset, and prints the run's
actual USD cost. Use `--dry-run` to see the request without spending anything.

## Choosing an actor

Actor IDs and quality change over time, so **search the store at run time rather than
trusting any hardcoded list** — including the one below. Search, then pick using:

- **Maintainer** — official `apify/*` actors are the safest default.
- **Recent runs / users** — a popular, actively used actor is usually maintained.
- **Pricing model** — prefer per-result or pay-per-event over long compute runs.
- **Input schema fit** — if it needs a login/cookie, skip it; use public-data actors.

Try the smallest possible run first (5–10 results) to confirm the shape of the output
before pulling the full window.

## Known-good starting points

These IDs were confirmed to exist in the store on 2026-08-03. Existing is not the
same as working for your case, so still run one small test before the full pull.

| Need | Actor to try first | Notes |
|---|---|---|
| Instagram posts | `apify/instagram-scraper` | `directUrls` + `resultsLimit`; use `resultsType: "posts"` |
| Instagram single-profile posts | `apify/instagram-post-scraper` | lighter/cheaper for post-only pulls |
| Instagram comments | `apify/instagram-comment-scraper` | if audience signal on IG matters |
| X / Twitter posts | `apidojo/tweet-scraper` | the most fragile platform; expect retries |
| YouTube search + video metadata | `streamers/youtube-scraper` | good for finding appearances |
| YouTube transcripts | `pintostudio/youtube-transcript-scraper` | many competitors exist; test cheap first |
| YouTube comments | `streamers/youtube-comments-scraper` | or `apidojo/youtube-comments-scraper` |
| LinkedIn profile posts | `harvestapi/linkedin-profile-posts` | see the LinkedIn note below |
| LinkedIn post search | `harvestapi/linkedin-post-search` | finds posts mentioning the guest |
| Any website / newsletter | `apify/website-content-crawler` | clean markdown from arbitrary sites |
| Google results at scale | `apify/google-search-scraper` | when built-in web search isn't enough |

## Typical inputs

Instagram profile posts:
```json
{"directUrls": ["https://www.instagram.com/<handle>/"],
 "resultsType": "posts", "resultsLimit": 30}
```

X/Twitter by handle, last 60 days:
```json
{"twitterHandles": ["<handle>"], "maxItems": 50, "sort": "Latest",
 "start": "2026-06-01"}
```

YouTube appearances (search rather than channel, since guest appearances live on
*other people's* channels):
```json
{"searchQueries": ["<guest full name> podcast", "<guest full name> interview"],
 "maxResults": 25, "dateFilter": "year"}
```

Website / newsletter:
```json
{"startUrls": [{"url": "https://<site>/blog"}], "maxCrawlPages": 25,
 "crawlerType": "cheerio"}
```

Adjust to whatever the actor's own input schema says — schemas differ and change.

## Cost control

- Agree a per-guest budget in Stage 0; ~$1–2 buys a deep run at 2026 pricing.
- A shallow demo-grade run lands near $0.30. If the total comes in far under budget,
  that is usually evidence the research is too thin, not that it was efficient.
- Cap every run with `resultsLimit` / `maxItems`. Uncapped social scrapers can run
  for a long time and bill for it.
- Record actual spend per run in the stage checkpoint so the host learns the real
  cost per episode.

## When a scraper fails

Failure is normal on social platforms. Escalate in this order:

1. **Retry with different input** — full URL instead of handle, smaller limit,
   different sort order.
2. **Try a different actor** for the same platform.
3. **Fall back to web search** — `site:linkedin.com/posts <name>`,
   `site:x.com <handle>`, cached and syndicated copies. Label the resulting data
   *partial, via web search* in the brief.
4. **Declare the gap.** Write it in the checkpoint and in the quality self-score.
   A named gap is recoverable; a silent one poisons the brief.

LinkedIn specifically: a maintained family of actors does exist (`harvestapi/*`
covers profile posts, post search, comments, and reactions), so LinkedIn is worth a
real attempt rather than being written off. It is still the platform most likely to
return thin or empty results, so test with a small pull, and keep the
`site:linkedin.com/posts <name>` web-search fallback ready.

## Data hygiene

- Save raw JSON per source under `research/<slug>/raw/`, one file per platform, so a
  later stage can re-analyze without re-paying.
- Keep the source URL and post date on every item — the brief needs them for citation.
- Public data only. Do not scrape private accounts, use logged-in sessions, or pull
  personal contact information; the goal is understanding a public professional
  persona, not building a dossier on a private individual.
- Delete or archive raw dumps once the episode is recorded if the host prefers.
