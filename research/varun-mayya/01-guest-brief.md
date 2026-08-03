# Guest brief — Varun Mayya
_Researched 2026-08-03 · Version **V1** · Research score **7/10**_
_New channel · Language: Hinglish · Angle: not yet chosen — three candidates at the end._

## Collection summary

| Source | Window | Items | Status |
|---|---|---|---|
| YouTube search (2 queries) | all-time | 80 → **61 relevant** | ok |
| His own channel, newest | May 2025 – Jul 2026 | **40** | ok |
| Full transcripts | — | **10 (129,384 words)** | ok |
| Instagram | 30 d | **0** — blocked twice, 2 actors | FAILED |
| X / Twitter | 60 d | **not attempted** | skipped by design |
| YouTube comments | — | **not attempted** | skipped by design |

**Cost: $0.47** — YouTube search $0.316 · channel pull $0.156 · Instagram attempts $0.003 ·
**all 10 transcripts $0.00**.

*Skips were deliberate, carried over from the Ritesh run: X and LinkedIn return
placeholder items on Apify's free tier, and comments were the worst return per rupee.
Instagram genuinely failed here — `apify/instagram-post-scraper` and
`apify/instagram-scraper` both returned "Request got blocked". It matters less for this
guest than it would for most: **41 of 61 relevant videos are on his own channel**, so
YouTube is where he actually publishes his thinking.*

Transcripts analyzed:

| Appearance | Date | Length | Words |
|---|---|---|---|
| WTF is ChatGPT (Nikhil Kamath, Ep #4) | 2023-05-14 | 2:28:40 | 26,965 |
| Mundhe Banni Podcast | 2026-02-07 | 2:04:20 | 22,677 |
| Bad Decisions Studio | 2024-10-29 | 1:23:50 | 18,729 |
| Guide to Scaling A Startup with Zero Funding (KATA 1) | 2025-12-21 | 1:18:41 | 15,572 |
| 10 Projects I've Built | 2026-06-27 | 0:43:03 | 10,036 |
| Best Skill to Learn in 2026 | 2026-02-17 | 0:41:06 | 8,325 |
| How Distribution Can 10x Your Luck (KATA 10) | 2026-07-16 | 0:39:23 | 7,217 |
| 5 Apps I Built With AI to Run My 500-Person Company | 2026-07-06 | 0:30:10 | 7,099 |
| Reacting To Your Feedback On Unleash The Avatar | 2026-06-30 | 0:31:32 | 6,802 |
| How Simplifying Everything Makes You Rich | 2026-07-26 | 0:28:50 | 5,962 |

---

## 1. The central tension ⭐ — read this first

His channel teaches AI leverage: automate everything, five apps replace a team, agents do
the work. The reality underneath it is the opposite shape.

> "We have **500 employees** now and we absolutely need a CFO."
> — Best Skill to Learn in 2026, 2026-02-17 [32:00] [V]

> "We are now sitting at close to **500 employees**. Last month we did **a billion views**
> across all our channels, ourselves and our customers."
> — Mundhe Banni Podcast, 2026-02-07 [53:26] [V]

> "Yes, we're working on a Souls-like, technically a Sekiro-like. **It's a 40-man team.**"
> — 10 Projects I've Built, 2026-06-27 [31:14] [V]

The man best known in India for "AI can run your company" is running a **500-person
headcount business**, hiring an expensive CFO, and staffing a **40-person** game studio.

That is not hypocrisy and shouldn't be framed as a gotcha — it is the most interesting
unexplained thing about him, and **the count appears only 3 times across 129,384 words**.
Nobody has asked him to reconcile it. This is the episode.

## 2. Core themes (by transcript frequency)

| Theme | Mentions across 10 appearances |
|---|---|
| Automation / agents / n8n | **67** |
| Prompting, how to actually use AI | **47** |
| Scenes (his product) | **33** |
| Dropping out / college | **26** |
| Avalon Labs origin | **18** |
| Unleash The Avatar (game) | **13** — all since Jun 2026 |
| KATA framework series | 5 |
| **500-person company** | **3** ⚠️ |
| India vs Silicon Valley | 3 |

The gap between row 1 and the second-to-last row is the whole opportunity.

## 3. Signature frameworks

| Framework | What it is | Freshness |
|---|---|---|
| **KATA series** | numbered lesson series (KATA 1–10+), his flagship teaching format — scaling with zero funding, risk-taking, distribution, hiring | **circulating** — it is his own catalogue, so recapping it adds nothing |
| Automate-anything / n8n workflows | agent-and-workflow tutorials | **commodity** — 67 mentions; the single most saturated thing he does |
| Prompting discipline ("99% of you prompt AI wrong") | how to actually instruct models | **commodity** |
| Distribution as luck multiplier | KATA 10, 2026-07-16 | circulating |
| **Kora** — custom C++ combat system for the game | built from scratch, with an internal AI documentation interface so new C++ engineers can query it | **fresh** ⭐ — barely explained anywhere |
| **EOS / AOS Labs** | his system for bringing young builders in; commercialized, incl. work with Bangalore police | **fresh** ⭐ |

## 4. Unfinished threads ⭐

Note on method: the usual verbal seams ("long story short", "that's another video")
returned **zero hits**. His own-channel content is scripted and produced, so it does not
leave conversational loose ends. Everything below comes from things stated once and
dropped, not from hedges.

| # | Thread | Quote | Where |
|---|---|---|---|
| 1 | **The 500 people** | "We have 500 employees now and we absolutely need a CFO" | bestskill2026 [32:00] |
| 2 | **A billion views in one month** | "Last month we did a billion views across all our channels, ourselves and our customers" | mundhebanni [53:26] |
| 3 | **The game he wanted to build since 2008** | "remember that game project from 2008? That thing that I always wanted to do from 2007, 2008? Now it's a mature version of [him] trying it" | 10projects [31:14] |
| 4 | **Viral in China** | "it's gone super viral in China" — an Indian Souls-like finding a Chinese audience | 10projects [31:14] |
| 5 | **The legacy line** ⭐ | "EOS is the thing that hopefully I will be known for after I pass away" | 10projects [40:56] |
| 6 | **Kora + AI documentation** | "we have our own combat system built from scratch, called Kora… new C++ engineers can ask any query in real time" | 5apps [20:49] |
| 7 | **The Scenes pivot** | rooms of 200–500 people, Tanmay Bhat once drew ~1,000, "but we didn't make any money. Ultimately I had to take this hard call to pivot to B2B to survive" | 10projects [05:57] |

Thread 5 is the strongest single question in this brief. A 30-something founder naming
what he wants to be remembered for, in passing, in a listicle video, is an entire segment
nobody has opened.

## 5. Kill list — do not ask

| Beat | Why it's dead |
|---|---|
| "How should people use AI / prompting basics" | 47 mentions; his channel *is* this |
| "Which AI tools do you use", n8n workflows, automation tutorials | 67 mentions; the most saturated topic he has |
| "Will AI take our jobs" | already done at scale on Nikhil Kamath's *WTF is ChatGPT* (1.17M views, 2:28:40) and its dedicated clip *"Jobs AI Will Replace In India"* (160k) |
| College dropout story | 26 mentions |
| Avalon Labs founding story | 18 mentions |
| Anything from KATA 1–10 | it is his own published catalogue — a viewer can watch it free |

**Competitive note.** His long-form is already owned: Nikhil Kamath (1.17M), Bad Decisions
Studio (198k), Mundhe Banni (2h04m, Feb 2026). A new channel repeating "AI + automation
with Varun Mayya" is competing directly against those and against **his own channel**,
which publishes better-produced versions of the same material every week.

## 6. Recent delta (Jun–Jul 2026)

- **Unleash The Avatar** — Bollywood Souls-like, gameplay trailer 2026-06-23 (228k views),
  40-person team, viral in China, custom engine work [V]
- **"Reacting To Your Feedback On Unleash The Avatar"** (2026-06-30) — he is now running a
  public feedback loop on a game, a very different posture from tutorial content [V]
- **"5 Apps I Built With AI to Run My 500-Person Company"** (2026-07-06) [V]
- **"10 Projects I've Built and 1 Thing I Learned From Each"** (2026-06-27) [V]
- **"How Simplifying Everything Makes You Rich"** (2026-07-26) — most recent upload [V]
- Now interviewing global tech leaders: Demis Hassabis (2026-02-19), Nothing CEO
  (2026-03-21), Meta AI Chief (2026-02-26) [V]

## 7. Landmines

| Topic | Handling |
|---|---|
| Scenes' failure to monetise | he discusses it openly himself — usable, but frame as decision-making, not failure |
| Employee count vs. AI-leverage message | the core question, but ask it with genuine curiosity; framed as a gotcha it closes the conversation |
| Bangalore police work | commercial//government client — let him set the boundary |
| Auto-caption name errors | transcripts render him as "Arun Maya" in places. **Verify every name and number against a primary source before the host says it aloud** |

## 8. Candidate angles — pick one before questions are written

**A. "The 500-Person AI Company"** ⭐ *recommended*
The man teaching AI leverage runs 500 people and a 40-person game studio. What did AI
actually replace, what did it not, and where does headcount still win? Unique to him,
almost no supply, and directly useful to every founder watching.

**B. "Why the AI guy is building a video game"**
A Souls-like from India, viral in China, a custom C++ engine, a 2008 teenage ambition
finally attempted. The freshest material, strong visuals, but narrower in usefulness.

**C. "What he wants to be remembered for"**
Built on the EOS legacy line. The most personal and least covered, but riskiest — it
depends entirely on him being willing to go there.

---

## Honest self-assessment

**Research score: 7/10.**

Strong: 129k words across 10 appearances covering 2023–2026, a recent delta that runs to
last week, and a central tension backed by three direct quotes rather than a hunch.

Missing:
1. **Instagram: zero**, blocked on two actors. Web-search fallback not run.
2. **X/Twitter and comments not attempted** — deliberate, but they remain unknowns rather
   than confirmed dead ends for this guest specifically.
3. **Stage 2B topic research not started**, so the content-supply gap is argued from his
   own catalogue rather than the market's.
4. **The 500-employee figure is his own claim**, repeated twice by him and verified nowhere
   independently. Tagged [V] as "he said it", **not** as "it is true" — the host should
   attribute it out loud, not assert it.
5. **51 of 61 relevant videos untranscribed** — free, so pure upside.

**To reach 9/10:** independent verification of headcount and the billion-views claim,
Stage 2B, and the Instagram fallback. Cost: near zero — the remaining work is mostly free.
