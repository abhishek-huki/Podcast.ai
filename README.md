# Podcast.ai

An AI podcast-research operating system. Input: a guest's name. Output: a verified
research brief plus ~25 sequenced interview questions and a one-page live runsheet.

The work that normally takes a research team two to three days — watching every
appearance, reading every post, figuring out what has already been asked to death —
gets collected and first-pass-analyzed by the agent. A human still validates the
output before it goes into a recording.

## What's here

```
skills/podcast-researcher/
├── SKILL.md                  the workflow: intake → research → synthesis → questions
├── references/               the deep guidance, loaded only when a stage needs it
│   ├── guest-research.md     sources, extraction targets, the seven artifacts
│   ├── apify-playbook.md     scraping social platforms, actor choice, cost, fallbacks
│   ├── topic-research.md     consensus map + content-supply gap map
│   ├── synthesis.md          the Gold Zone 2×2 and episode angles
│   ├── question-design.md    the 9-movement arc, follow-up ladders, runsheet
│   ├── verification.md       V/P/I/U fact tagging before anything is said on camera
│   └── quality-rubric.md     scoring and the V1 → V2 → V3 loop
├── assets/                   templates for every deliverable
└── scripts/
    ├── apify_run.py          run Apify actors from the terminal, no dependencies
    └── new_guest.py          scaffold a guest's research folder
```

## Install the skill

Copy (or symlink) the skill folder into a skills directory Claude reads:

```bash
# available in every project
cp -r skills/podcast-researcher ~/.claude/skills/

# or scoped to one project
mkdir -p .claude/skills && cp -r skills/podcast-researcher .claude/skills/
```

Then just ask: *"research Vaibhav Sisinty for my podcast on AI agents"*.

## Set up scraping (optional but this is where the depth comes from)

Plain web search cannot read Instagram, X, LinkedIn, or YouTube comments. Apify can.

1. Create an account at [apify.com](https://apify.com), open the Console.
2. Settings → API & Integrations → copy your API token.
3. Either add the **Apify connector** in Claude's settings and paste the token, or
   export it for the bundled script:

```bash
export APIFY_TOKEN=apify_api_xxx
python skills/podcast-researcher/scripts/apify_run.py search "youtube transcript"
```

A deep run costs roughly $1–2 per guest. A run that comes in at $0.30 is usually
too shallow rather than efficient.

## How the workflow runs

| Stage | What happens | Gate |
|---|---|---|
| 0 | Intake, then the agent restates what it understood | user confirms |
| 1 | Research plan and budget | user approves |
| 2A | Guest intelligence — themes, frameworks, kill list, unfinished threads, evolution, recent delta, landmines | score ≥ 8 |
| 2B | Topic intelligence — consensus map, content-supply gaps | checkpoint |
| 3 | Gold Zone: guest uniqueness × content gap → episode angles | user picks the angle |
| 4 | 25 sequenced questions, follow-ups, timings, runsheet | — |
| 5 | Verification of every name, number, date and quote | — |
| 6–7 | Deliverables, self-score, iterate to V2/V3 | user says ship |

Checkpoints are written after every stage, so a long run can be resumed instead of
restarted.

## Why it's built this way

Asking a model for "25 podcast questions" produces the same list the guest has
already answered on forty other shows. The value comes from four things this
workflow forces:

- **research before questions**, with real social data, not recall
- **a kill list** — knowing what *not* to ask is worth as much as the questions
- **honest self-scoring and iteration** — V1 is never the deliverable
- **verification** — the brief gets read aloud on camera, so every fact carries a
  source and a confidence tag

The skill also learns: after each episode, feedback about what landed and what was
useless gets written back into the references, so the next guest starts from the
host's accumulated taste rather than a blank template.

## Output layout

Per guest, under `research/<guest-slug>/` (gitignored by default — it holds scraped
data):

```
00-intake.md  01-guest-brief.md  02-topic-brief.md  03-gold-zone.md
04-questions.md  05-runsheet.md  06-verification.md
raw/  CHECKPOINT-*.md
```

## A note on the data

Public professional information only — what someone has published about their work.
No private accounts, no logged-in scraping, no personal contact details. The purpose
is to prepare a better interview, not to build a dossier.
