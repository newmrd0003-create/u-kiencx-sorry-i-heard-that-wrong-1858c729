#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — single-line smart-speaker apology.

Deterministic: writes the same entry on every run, only to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""
import hashlib
import os
import sys

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
    # Write-verify: the written entry.txt must match ENTRY exactly.
    expected = (ENTRY + "\n").encode("utf-8")
    expected_sha = hashlib.sha256(expected).hexdigest()
    with open(path, "rb") as f:
        written = f.read()
    if written != expected or hashlib.sha256(written).hexdigest() != expected_sha:
        sys.exit(1)

if __name__ == "__main__":
    main()
