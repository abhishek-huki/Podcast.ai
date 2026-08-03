# Guest intelligence

Everything about extracting what *this specific person* thinks, teaches, repeats,
avoids, and has recently changed their mind about.

## Contents
- [Source list and date windows](#source-list-and-date-windows)
- [Per-platform extraction targets](#per-platform-extraction-targets)
- [Transcript analysis: the signals that matter](#transcript-analysis-the-signals-that-matter)
- [The seven artifacts](#the-seven-artifacts)
- [Identity disambiguation](#identity-disambiguation)
- [Common failure modes](#common-failure-modes)

## Source list and date windows

Tier 1 — always do these:

| Source | Window | Why |
|---|---|---|
| Personal site / about / bio | current | canonical titles, spellings, current role |
| Web search: name + recent news | 6 months | launches, funding, partnerships, controversies |
| Top 5–10 YouTube/podcast appearances | 12 months | the actual substance of what they say |
| Transcripts of the 3 most substantive appearances | — | frameworks, phrasing, repeated stories |
| Most-viewed appearance ever | no limit | this is the ceiling to beat |
| X/Twitter posts | 60 days | fastest-moving signal of current thinking |
| LinkedIn posts | 60 days | professional positioning, launches |
| Instagram posts + captions | 30 days | what they're promoting right now |

Tier 2 — do these when the guest is prolific or the topic is fast-moving:

| Source | Window | Why |
|---|---|---|
| Comments on 2 biggest videos (top ~50 each) | — | what the audience keeps asking for |
| Newsletter / blog archive | 6 months | long-form positions not in video |
| Books, courses, talks | no limit | signature frameworks in their fullest form |
| Their company's product/pricing/changelog pages | 6 months | what they actually built vs. what they say |
| Their co-founders'/team's public posts | 90 days | fills gaps when the guest posts little |
| Other podcasts' episodes with them, last 6 months | — | dedupe: don't repeat a rival show |

Comment analysis is genuinely useful for validating audience demand, but some hosts
find it noise. Offer it, mark it optional, and drop it permanently if the host says
it wasn't useful.

## Per-platform extraction targets

Don't just save posts. For each platform pull out the specific thing it's good for:

**YouTube appearances** — which host, which format, what got covered, what the guest
said that they don't say elsewhere, where the conversation got cut short. Note the
view counts: the top performer tells you what the market rewards from this guest.

**YouTube comments** — recurring requests ("wish they'd asked about X"), confusion
points, disagreement with the guest, and praise for specific segments. Cluster into
themes; report as "N of 50 comments asked for X", not as anecdotes.

**X/Twitter** — hot takes, threads, replies, arguments. This is where positions are
sharpest and most current. Aim for 30+ posts; 4 posts is a failed pull, not a result.

**LinkedIn** — announcements, hiring, launches, longer professional essays. LinkedIn
scraping is the least reliable of the platforms; if the actor fails, fall back to web
search of `site:linkedin.com/posts <name>` and label the data as partial.

**Instagram** — current promotions, events, tone, and what they're proud of. Captions
matter more than images for research purposes.

**Website / newsletter** — the guest's own framing of their expertise, in their own
structure. Good source for framework names and exact terminology.

## Transcript analysis: the signals that matter

Collecting a transcript is worthless without extraction. From each transcript pull:

1. **Signature frameworks** — named, numbered, or repeated mental models. Note the
   exact name they use, because the host should use their vocabulary.
2. **Stories told more than once** — across two or more appearances, this is their
   set piece. It will come out again unless the host explicitly routes around it.
3. **Questions they've answered repeatedly** — feeds the kill list directly.
4. **Incomplete thoughts** — "there's a whole other thing about X, but that's for
   another day". These are the seams. Mark timestamp and exact phrasing.
5. **Excitement spikes** — where their energy jumps, where they interrupt the host to
   keep going. The episode should be built on these.
6. **Hedges and deflections** — where they avoid specifics. Sometimes sensitive,
   sometimes just unexplored. Distinguish the two before turning it into a question.
7. **Concrete numbers** — revenue, team size, timelines, results. These anchor
   follow-ups and are also the highest-risk facts to get wrong; log sources.
8. **Statements with dates** — needed later to detect evolution and contradictions.

## The seven artifacts

Each of these goes in `01-guest-brief.md`.

### 1. Core themes
5–8 themes with 2–3 supporting quotes each, with source + date. Order by how often
and how recently they appear.

### 2. Signature frameworks
For each: name, one-line summary, where they teach it, and a commodity rating —
*fresh* (barely explained anywhere), *circulating* (other creators repeat it), or
*commodity* (fully saturated). Commodity frameworks must not become episode segments;
they can be a 60-second recap at most.

### 3. Kill list
10–20 specific questions to avoid, each with evidence of where it was already
answered. Include questions asked by the host's own previous episodes — repeating
your own show is worse than repeating someone else's.

### 4. Unfinished threads
The highest-value output of this whole stage. Each entry: the thread, exact quote,
where and when it was said, and why it was never finished (out of scope / cut off /
avoided). These convert almost directly into questions.

### 5. Evolution and contradictions
A short timeline of the guest's public position on 2–4 key issues. Frame as evolution,
not "gotcha" — the useful question is *what changed in the world, or in your thinking?*
If the host has said they don't want confrontational questions, keep the analysis but
convert the questions to curiosity framing.

### 6. Recent delta
What is new in the last 30–90 days that existing interviews cannot possibly cover:
new launches, new opinions, reversals, new experiments. This is the freshness that
makes the episode worth recording now instead of linking to an old one.

### 7. Landmines
Legal matters, disputes, personal topics, sponsor conflicts, ongoing controversies,
and anything the guest's team flagged. State clearly whether each is *avoid entirely*
or *approach carefully with this framing*.

## Identity disambiguation

Before spending money on scraping, confirm you have the right person: match the
handle to the bio, the bio to the topic, and the topic to what the user described.
Common names produce expensive research on the wrong human. If confidence is below
certain, show the user the candidate profiles and ask.

Also lock in: exact legal/professional name spelling, current title, current company,
and pronunciation if non-obvious. The host will say all of these on camera.

## Common failure modes

- **Thin pull reported as success.** 4 tweets is a failure. Say so, retry with a
  different actor, and log the gap in the checkpoint.
- **Summarizing instead of extracting.** "Talks about AI a lot" is not an artifact.
- **Stale data presented as current.** Always attach dates; a 2-year-old position
  stated as current is how briefs embarrass hosts.
- **Believing the guest's own bio.** Bios inflate. Cross-check claimed numbers
  against independent sources and mark unverifiable ones.
- **Skipping the kill list** because the questions "seem good". They seem good
  precisely because forty other hosts also thought so.
