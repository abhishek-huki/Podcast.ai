#!/usr/bin/env python3
"""Run Apify actors and save their datasets, without leaving the terminal.

Use this when the Apify connector isn't configured. Needs only stdlib and an
APIFY_TOKEN environment variable (Apify Console -> Settings -> API & Integrations).

    export APIFY_TOKEN=apify_api_xxx

    # find an actor for a platform
    python apify_run.py search "instagram scraper"

    # inspect an actor's input schema before spending anything
    python apify_run.py info apify/instagram-scraper

    # run it and save the dataset
    python apify_run.py run apify/instagram-scraper \
        --input '{"directUrls":["https://instagram.com/handle"],"resultsLimit":30}' \
        --out research/guest/raw/instagram.json

    # or read the input from a file, and check the request first
    python apify_run.py run apidojo/tweet-scraper --input @tweets.json --dry-run

Actor IDs and pricing change; always `search` before trusting a hardcoded ID.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.apify.com/v2"


def token():
    tok = os.environ.get("APIFY_TOKEN")
    if not tok:
        sys.exit("APIFY_TOKEN is not set. Get one from Apify Console -> Settings -> API.")
    return tok


def request(method, path, params=None, body=None, timeout=120):
    params = dict(params or {})
    params["token"] = token()
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = resp.read().decode()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()[:500]
        sys.exit(f"Apify {method} {path} failed: HTTP {exc.code}\n{detail}")
    except urllib.error.URLError as exc:
        sys.exit(f"Could not reach api.apify.com: {exc.reason}\n"
                 "If you are inside a sandbox or corporate proxy, outbound access to "
                 "api.apify.com may be blocked by network policy — check that first, "
                 "before assuming the token is wrong.")
    return json.loads(payload) if payload else {}


def actor_path(actor_id):
    """apify/instagram-scraper -> apify~instagram-scraper (the API's URL form)."""
    return actor_id.replace("/", "~")


def load_input(raw):
    if not raw:
        return {}
    if raw.startswith("@"):
        with open(raw[1:]) as fh:
            return json.load(fh)
    return json.loads(raw)


def cmd_search(args):
    result = request("GET", "/store", {"search": args.query, "limit": args.limit})
    data = result.get("data", result)
    items = data.get("items", data) if isinstance(data, dict) else data
    if not items:
        print("No actors matched. Try broader terms.")
        return
    for item in items:
        actor = f"{item.get('username')}/{item.get('name')}"
        stats = item.get("stats", {}) or {}
        pricing = (item.get("currentPricingInfo") or {}).get("pricingModel", "?")
        print(f"{actor:<50} runs30d={stats.get('totalRuns30Days', '?'):<8} "
              f"users={stats.get('totalUsers', '?'):<8} pricing={pricing}")
        title = item.get("title")
        if title:
            print(f"    {title}")


def cmd_info(args):
    result = request("GET", f"/acts/{actor_path(args.actor)}")
    data = result.get("data", {})
    print(f"{data.get('username')}/{data.get('name')} — {data.get('title', '')}")
    print(f"description: {(data.get('description') or '')[:400]}")
    versions = data.get("versions") or []
    if versions:
        schema = versions[-1].get("sourceFiles") or []
        for f in schema:
            if f.get("name", "").endswith("INPUT_SCHEMA.json"):
                print("\ninput schema:")
                print((f.get("content") or "")[:3000])
                return
    print("\nNo input schema found in the API response; check the actor's store page.")


def cmd_run(args):
    actor_input = load_input(args.input)
    if args.dry_run:
        print(f"POST /acts/{actor_path(args.actor)}/runs")
        print(json.dumps(actor_input, indent=2))
        return

    started = request("POST", f"/acts/{actor_path(args.actor)}/runs", body=actor_input)
    run_id = started["data"]["id"]
    print(f"run {run_id} started; polling (max {args.max_wait}s)…", file=sys.stderr)

    deadline = time.time() + args.max_wait
    status, run = "READY", started["data"]
    while time.time() < deadline:
        run = request("GET", f"/actor-runs/{run_id}")["data"]
        status = run.get("status")
        if status not in ("READY", "RUNNING"):
            break
        time.sleep(args.poll)
    else:
        print(f"still {status} after {args.max_wait}s — abort or resume with:\n"
              f"  python {sys.argv[0]} fetch {run_id} --out {args.out}", file=sys.stderr)
        return

    save_dataset(run, args.out, args.limit)


def cmd_fetch(args):
    run = request("GET", f"/actor-runs/{args.run_id}")["data"]
    save_dataset(run, args.out, args.limit)


def save_dataset(run, out, limit):
    status = run.get("status")
    cost = run.get("usageTotalUsd")
    dataset_id = run.get("defaultDatasetId")
    if status != "SUCCEEDED":
        print(f"run finished with status {status}"
              f"{' — no dataset' if not dataset_id else ''}", file=sys.stderr)
    if not dataset_id:
        return

    items = request("GET", f"/datasets/{dataset_id}/items",
                    {"format": "json", "clean": "true", "limit": limit})
    if not isinstance(items, list):
        items = items.get("data", items)

    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "w") as fh:
            json.dump(items, fh, indent=2, ensure_ascii=False)
        print(f"{len(items)} items -> {out}", file=sys.stderr)
    else:
        json.dump(items, sys.stdout, indent=2, ensure_ascii=False)

    if cost is not None:
        print(f"cost: ${cost:.4f} — record this in the stage checkpoint", file=sys.stderr)
    if len(items) < 10:
        print("WARNING: thin pull (<10 items). Treat as a failed source: retry with "
              "different input, try another actor, or declare the gap.", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("search", help="find actors in the Apify store")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("info", help="show an actor's description and input schema")
    p.add_argument("actor")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("run", help="run an actor and save its dataset")
    p.add_argument("actor", help="e.g. apify/instagram-scraper")
    p.add_argument("--input", default="{}", help="JSON string, or @path/to/file.json")
    p.add_argument("--out", help="where to write the dataset (default: stdout)")
    p.add_argument("--limit", type=int, default=1000, help="max dataset items to fetch")
    p.add_argument("--max-wait", type=int, default=600, help="seconds to poll")
    p.add_argument("--poll", type=int, default=5, help="seconds between polls")
    p.add_argument("--dry-run", action="store_true", help="print the request, spend nothing")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("fetch", help="download the dataset of an earlier run")
    p.add_argument("run_id")
    p.add_argument("--out")
    p.add_argument("--limit", type=int, default=1000)
    p.set_defaults(func=cmd_fetch)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
