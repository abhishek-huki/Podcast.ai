#!/usr/bin/env python3
"""Turn a brief, question sheet, or runsheet into a PDF the host can read on a phone.

    python brief_to_pdf.py research/ritesh-agarwal/01-guest-brief.md
    python brief_to_pdf.py research/<slug>/05-runsheet.md --landscape

Markdown is the working format, but nobody reads markdown thirty minutes before a
recording. The PDF is the thing that actually gets opened, so the styling here is
tuned for reading on a phone: generous line height, tables that do not overflow, and
page breaks that never split a question from its follow-up.

Needs the `markdown` package (pip install markdown) and a Chromium binary. It looks
for Chromium in PLAYWRIGHT_BROWSERS_PATH, then the usual system locations.
"""

import argparse
import glob
import os
import subprocess
import sys
import tempfile

CSS = """
@page { size: A4; margin: 16mm 14mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Roboto, "Noto Sans", "Noto Sans Devanagari", sans-serif;
       font-size: 10.5pt; line-height: 1.55; color: #1a1a1a; margin: 0; }
h1 { font-size: 21pt; margin: 0 0 2mm; border-bottom: 2px solid #1a1a1a; padding-bottom: 2mm; }
h2 { font-size: 14pt; margin: 8mm 0 2mm; padding-top: 1mm; border-top: 1px solid #ddd; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 5mm 0 1mm; break-after: avoid; }
p, li { orphans: 2; widows: 2; }
em { color: #555; }
blockquote { margin: 2mm 0 2mm 3mm; padding: 1mm 0 1mm 4mm; border-left: 3px solid #bbb;
             color: #333; font-style: italic; break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0; font-size: 9pt;
        table-layout: fixed; break-inside: avoid; }
th, td { border: 1px solid #ccc; padding: 1.6mm 2mm; text-align: left; vertical-align: top;
         word-wrap: break-word; overflow-wrap: anywhere; }
th { background: #f2f2f2; font-weight: 600; }
tr:nth-child(even) td { background: #fafafa; }
code { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 8.8pt;
       background: #f0f0f0; padding: 0.4mm 1mm; border-radius: 2px; }
hr { border: none; border-top: 1px solid #ddd; margin: 6mm 0; }
strong { font-weight: 650; }
ul, ol { padding-left: 6mm; margin: 2mm 0; }
"""


def find_chromium():
    pw = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    hits = sorted(glob.glob(os.path.join(pw, "chromium-*/chrome-linux/chrome")))
    for c in hits + ["/usr/bin/chromium", "/usr/bin/chromium-browser",
                     "/usr/bin/google-chrome",
                     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
        if os.path.exists(c):
            return c
    sys.exit("No Chromium found. Set PLAYWRIGHT_BROWSERS_PATH or install Chrome.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("markdown_file")
    ap.add_argument("--out", help="output path (default: same name, .pdf)")
    ap.add_argument("--landscape", action="store_true", help="for wide runsheets")
    args = ap.parse_args()

    try:
        import markdown
    except ImportError:
        sys.exit("pip install markdown")

    src = open(args.markdown_file, encoding="utf-8").read()
    body = markdown.markdown(src, extensions=["tables", "fenced_code", "sane_lists"])
    title = os.path.basename(args.markdown_file).rsplit(".", 1)[0]
    css = CSS + ("\n@page { size: A4 landscape; }" if args.landscape else "")
    html = (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>{title}</title><style>{css}</style></head><body>{body}</body></html>")

    out = args.out or args.markdown_file.rsplit(".", 1)[0] + ".pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(html)
        tmp = fh.name

    cmd = [find_chromium(), "--headless", "--no-sandbox", "--disable-gpu",
           "--no-pdf-header-footer", "--virtual-time-budget=10000",
           f"--print-to-pdf={os.path.abspath(out)}", f"file://{tmp}"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    os.unlink(tmp)

    if not os.path.exists(out):
        sys.exit(f"PDF not produced.\n{res.stderr[-800:]}")
    print(f"{out}  ({os.path.getsize(out) // 1024} KB)")


if __name__ == "__main__":
    main()
