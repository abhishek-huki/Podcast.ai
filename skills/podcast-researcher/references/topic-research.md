# Topic and market intelligence

The guest tells you what one person thinks. This stage tells you what the *world*
currently thinks, what it already knows, and what it is still confused about. Without
it, you cannot tell whether a guest's idea is fresh or three months stale.

## Contents
- [What to gather](#what-to-gather)
- [The consensus map](#the-consensus-map)
- [The content-supply gap map](#the-content-supply-gap-map)
- [Reddit and forums](#reddit-and-forums)
- [Output format](#output-format)

## What to gather

Run this independently of the guest research — deliberately don't anchor on the
guest's framing, or you'll only find evidence that they're right.

| Source | What you're looking for |
|---|---|
| News, last 90 days | launches, funding, regulation, incidents, reversals |
| Long-form analysis pieces | the serious arguments, not the headlines |
| Existing frameworks in circulation | what's already been named and taught |
| Practitioner discussion (Reddit, HN, X, Discord recaps) | where real users disagree with the marketing |
| Top-ranking explainers on the core topic | what a beginner will find in 10 seconds of searching |
| Competing podcasts on the same topic | which angles are saturated |
| Data points and benchmarks | numbers the host can put to the guest |

Prefer primary sources and dated material. For a fast-moving field, anything older
than 6 months needs a reason to be included.

## The consensus map

Write down what "everyone says" right now, in 5–8 bullet points, and for each one note:

- **How settled is it?** (contested / emerging consensus / accepted)
- **Who disagrees, and on what grounds?**
- **What does the guest say about it?** (agrees / disagrees / silent)

The interesting questions come from the rows where the guest disagrees with the
consensus, or where the guest is silent on something that has become important.

## The content-supply gap map

For each subtopic the audience clearly cares about, rate:

- **Demand** — search interest, comment requests, how often the question recurs
- **Supply** — how much good, specific, credible material already exists
- **Gap** = high demand + low supply

Be specific about *what kind* of supply is missing. Usually the pattern is: plenty of
"what is X" content, almost nothing on "how to actually run X at scale, with numbers,
after the initial excitement". Name the missing shape precisely, because that shape
becomes the episode's promise.

Sources of demand signal, in rough order of reliability:
1. Recurring questions in comments on the guest's and competitors' videos
2. Practitioner forum threads with high engagement and no good answer
3. Search-suggest and related-question patterns
4. What competing podcasts keep booking guests to talk about

## Reddit and forums

Indexed Reddit and forum threads are reachable via search, and they are the best
source of unvarnished practitioner opinion. Two caveats worth stating in the brief:
search only surfaces indexed threads, and deep comment chains often need a dedicated
scraper to read properly. If forum evidence is thin, say so rather than generalizing
from three comments.

## Output format

Write `02-topic-brief.md`:

```markdown
# Topic brief: <topic>
_Researched <date>. Sources: N articles, M discussions._

## State of the field (last 90 days)
- <development> — <why it matters> [source, date]

## Consensus map
| Belief | Settledness | Dissenters | Guest's position |

## Content-supply gaps
| Subtopic | Demand evidence | Existing supply | Gap shape |

## Numbers worth putting to the guest
| Claim | Number | Source | Date |

## Saturated angles (do not build the episode here)
- <angle> — already covered by <who>, <when>
```

The "numbers worth putting to the guest" table is disproportionately useful during
recording: concrete figures force specific answers and break generic monologues.
