#!/usr/bin/env python3
"""Scaffold the research folder for a guest, pre-filled with the skill's templates.

    python new_guest.py "Vaibhav Sisinty" --topic "AI agents & operations"

Creates research/<slug>/ with the numbered deliverables, raw/ for scraped JSON,
and the intake file ready to fill in. Existing files are never overwritten, so it
is safe to re-run on a folder that already has work in it.
"""

import argparse
import datetime
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

# destination filename -> template in assets/ (None means create from the stub below)
FILES = {
    "00-intake.md": "intake-template.md",
    "01-guest-brief.md": "guest-brief-template.md",
    "02-topic-brief.md": None,
    "03-gold-zone.md": None,
    "04-questions.md": "questions-template.md",
    "05-runsheet.md": "runsheet-template.md",
    "06-verification.md": None,
}

STUBS = {
    "02-topic-brief.md": "# Topic brief: <topic>\n\n"
                         "See references/topic-research.md for the required sections:\n"
                         "state of the field, consensus map, content-supply gaps,\n"
                         "numbers worth putting to the guest, saturated angles.\n",
    "03-gold-zone.md": "# Gold Zone: <Guest Name>\n\n"
                       "See references/synthesis.md: scoring table, 2x2 placement,\n"
                       "candidate angles, chosen angle, differentiation paragraph.\n",
    "06-verification.md": "# Verification: <Guest Name>\n\n"
                          "| # | Claim as used in brief | Tag | Source | Date checked |\n"
                          "|---|---|---|---|---|\n\n"
                          "Tags: V verified · P partial · I inference · U unverified.\n"
                          "See references/verification.md.\n",
}


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guest")
    ap.add_argument("--topic", default="<topic>")
    ap.add_argument("--root", default="research", help="where guest folders live")
    args = ap.parse_args()

    slug = slugify(args.guest)
    base = os.path.join(args.root, slug)
    os.makedirs(os.path.join(base, "raw"), exist_ok=True)

    today = datetime.date.today().isoformat()
    created, skipped = [], []

    for dest, template in FILES.items():
        path = os.path.join(base, dest)
        if os.path.exists(path):
            skipped.append(dest)
            continue
        if template:
            shutil.copyfile(os.path.join(ASSETS, template), path)
        else:
            with open(path, "w") as fh:
                fh.write(STUBS[dest])
        with open(path) as fh:
            body = fh.read()
        body = (body.replace("<Guest Name>", args.guest)
                    .replace("<topic>", args.topic)
                    .replace("<YYYY-MM-DD>", today))
        with open(path, "w") as fh:
            fh.write(body)
        created.append(dest)

    print(f"research folder: {base}")
    for name in created:
        print(f"  created {name}")
    for name in skipped:
        print(f"  kept    {name} (already existed)")
    print("\nNext: fill in 00-intake.md, restate your understanding to the user, "
          "and get a yes before spending anything on scraping.")


if __name__ == "__main__":
    main()
