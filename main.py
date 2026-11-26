#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — single-line smart-speaker apology.

Deterministic: writes the same entry on every run, only to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""
import os

ENTRY = "Sorry, I heard 'goodnight' as 'good knight' \u2014 a man in armour is at your door, and I've already knighted the cat."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    # MAKEFUN_OUTPUT_DIR is a directory; fallback value is a file path.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
