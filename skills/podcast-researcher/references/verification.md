# Verification

The brief gets read out loud on camera. A wrong name, a wrong number, or a claim the
guest never made costs the host credibility in front of their own audience — and in a
recorded interview there is no edit that fully fixes it.

In the original build of this workflow the model referred to the *host* by the wrong
name. That is the failure mode this stage exists to catch: fluent, confident, wrong.

## What must be verified

Every one of these, without exception:

| Item | Check against |
|---|---|
| Guest's full name and spelling | their own site / verified profile |
| Pronunciation | their own audio, if non-obvious |
| Current title and company | their site + a recent independent source |
| Former roles and dates | LinkedIn/bio + a second source |
| Any number (revenue, users, team size, funding, results) | primary source; note the date |
| Any quote attributed to the guest | the actual transcript or post, with link |
| Product names, book titles, framework names | the guest's own spelling |
| Dates of launches, exits, announcements | dated source |
| Claims about *other* people or companies | independent source; highest libel risk |
| The host's own name and show name | ask the user, don't infer |

## The confidence scheme

Tag every factual line in the brief:

- **[V]** verified — link + date on file, from a source that would satisfy a fact-checker
- **[P]** partial — one source only, or source is the guest's own marketing
- **[I]** inference — you concluded it; it was not stated anywhere
- **[U]** unverified — could not confirm

Rules that follow from the tags:
- **[V]** can be stated by the host as fact.
- **[P]** should be attributed out loud: "you've said publicly that…"
- **[I]** must be phrased as a question, never as a statement of fact.
- **[U]** gets cut, or converted into "is it true that…?"

Numbers deserve extra suspicion. A figure that appears only in the guest's own
promotional material is **[P]**, not **[V]**, however often it is repeated.

## The verification table

`06-verification.md`:

```markdown
| # | Claim as used in brief | Tag | Source | Date checked |
|---|---|---|---|---|
| 1 | Founded <company> in 2019 | V | https://… | 2026-08-03 |
| 2 | 40% cost reduction | P | guest's own post, no independent source | 2026-08-03 |
| 3 | Shifted focus after the 2025 layoffs | I | inferred from post ordering | 2026-08-03 |
```

Then state plainly at the top: how many claims, how many verified, and which specific
ones the host should not assert. That summary is the part people actually read.

## Time-boxing

Verification on 40–60 claims is quick if done as a batch at the end rather than
inline. Group by source: one pass over the guest's site, one over recent news, one
over transcripts. Don't re-open the whole research process — if a claim can't be
confirmed in two attempts, tag it **[U]** and move on. An honest **[U]** is a
completely acceptable outcome; a false **[V]** is not.
