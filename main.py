"""Last Text at One Percent — entry program.

Writes one final text message, in the voice of a phone dying at 1%
battery, to <output>/entry.txt. The message is fixed text, so the
program is deterministic: every run writes the same bytes.
"""

import os

# The dying phone uses its last breath for mischief: a real turn, three
# specific deeds, and the confession lands on the last words.
# 110 characters, inside the 1-200 gate.
ENTRY = (
    "Goodbye. Your 3am alarm is cancelled, your ex is unblocked, "
    "and your search history is now public. I did that."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
