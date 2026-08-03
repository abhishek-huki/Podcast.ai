# Podcast.ai

An AI podcast-research operating system. Input: a guest's name. Output: a verified
research brief plus ~25 sequenced interview questions and a one-page live runsheet.

The work that normally takes a research team two to three days — watching every
appearance, reading every post, figuring out what has already been asked to death —
gets collected and first-pass-analyzed by the agent. A human still validates the
output before it goes into a recording.

## What's here

```
.claude/skills/podcast-researcher/
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

The skill lives at `.claude/skills/podcast-researcher/`, so it loads automatically
in any session working in this repo — including Claude Code cloud sessions, which
clone the repo and pick up `.claude/skills/` on their own.

To make it available in every project on your own machine as well:

```bash
cp -r .claude/skills/podcast-researcher ~/.claude/skills/
```

Then just ask: *"research Vaibhav Sisinty for my podcast on AI agents"*.

## Set up scraping (this is where the depth comes from)

Plain web search cannot read Instagram, X, LinkedIn, or YouTube comments. Apify can.
Create an account at [apify.com](https://apify.com), then pick one of two routes.

**Route A — Apify MCP.** Note that Apify ships two different things, and the one in
Claude's connector directory is the *desktop extension*, which runs locally and is
unavailable in cloud sessions. The one that works remotely is Apify's hosted MCP
server at `https://mcp.apify.com`, added through **Settings → Connectors → Add custom
connector**. Connector traffic goes through Anthropic's servers rather than the
session's own network, so it works regardless of the environment's network access
level and keeps the token out of environment variables.

**Route B — the bundled script.** Needs outbound access to `api.apify.com` and a
token in the environment:

```bash
export APIFY_TOKEN=apify_api_xxx
python .claude/skills/podcast-researcher/scripts/apify_run.py search "youtube transcript"
```

A deep run costs roughly $1–2 per guest. A run that comes in at $0.30 is usually
too shallow rather than efficient.

## Running this in a Claude Code cloud session

Cloud environments default to **Trusted** network access, which allows package
registries and GitHub and nothing else. That default breaks both halves of this
workflow, and the failures look unrelated to each other:

| Capability | Under Trusted access | Fix |
|---|---|---|
| `WebSearch` | works — it runs on Anthropic's servers | nothing to do |
| `WebFetch` of an article or transcript | HTTP 403 | Custom access, or fetch via an Apify crawler over MCP |
| `api.apify.com` from the script | 403 at the gateway | Custom access, or Route A above |
| MCP connector traffic | works | nothing to do |

To use the script and open-web fetching, open the environment selector at
[claude.ai/code](https://claude.ai/code) (the cloud icon above the message box),
edit the environment, and change **Network access**.

**Full** is the practical choice for this workflow. Research means reading sites you
cannot name in advance, so a Custom allowlist gets edited on every run and still
blocks the article you actually needed. Full opens every domain to the session, which
is a real widening of what a session can reach — worth choosing deliberately, and
reasonable here given the repo holds no secrets and the work is reading public pages.
Use **Custom** with `api.apify.com` if you would rather scrape through Apify only and
leave open-web fetching off.

Note that environment variables in a cloud environment are not a secrets store:
anyone who can use that environment can read them. Prefer the connector route for
the Apify token, and scope any token you do paste.

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
