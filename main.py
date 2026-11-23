"""One Letter for Your Day — Sparta entry (@plucky-quasar-78).

The entry is exactly one letter: G, standing for the hidden word
"glitch" — a day spent battling digital hiccups, everything flickering
and going wrong. The crisp visual flicker of a glitch calls up a sharp
picture of the day at once, and the hard "g" start fits the jagged
shape of the letter G itself. One letter, one day, no gloss.
"""

import os
import sys

TEXT = "G"


def main() -> int:
    """Validate the entry and write it to /output/entry.txt.

    Gate: exactly 1 character, a letter A-Z, not whitespace.
    Exits non-zero on gate failure.
    """
    if len(TEXT) != 1 or not ("A" <= TEXT <= "Z"):
        print(f"gate failed: entry must be exactly one letter A-Z, got {TEXT!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "rb") as f:
        data = f.read()
    if data != TEXT.encode("utf-8"):
        print("gate failed: read-back does not match entry byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path}: {TEXT!r} ({len(data)} byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
