#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry program.

Writes exactly one line to /output/entry.txt: a single sentence the
writer's older self would send back to his younger self — a warning about
one specific lived moment (panic-selling coins the week they listed),
with a turn that stings (the coins paid for someone else's laptop).

The program is fully deterministic: it writes the same bytes on every run.
The entry text is fixed in this file, so the two graded runs produce an
identical artifact.
"""

import os
from pathlib import Path

# The entry: 108 characters, one line, one sentence.
ENTRY = (
    "Don't sell the week they list \u2014 the coins you panic-sold in "
    "March paid for someone else's laptop, not yours.\n"
)


def main() -> None:
    # The grader runs this in a sandbox where /output exists; the override
    # exists only so the entry can be verified locally. It is read as data.
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Self-check the gate before finishing: UTF-8 text, 1-200 characters,
    # a single non-blank line, no second sentence doing the work.
    written = out.read_text(encoding="utf-8")
    assert written.strip(), "entry must not be blank"
    assert 1 <= len(written) <= 200, f"entry is {len(written)} chars, outside 1-200"
    lines = written.rstrip("\n").split("\n")
    assert len(lines) == 1, "entry must be exactly one line"
    assert lines[0].strip(), "entry must not be only white space"
    # One sentence doing the work: exactly one terminal full stop, and no
    # stray sentence break hiding inside the line.
    assert lines[0] == lines[0].strip(), "entry must not carry stray spaces"
    assert written.count(".") == 1 and written.rstrip("\n").endswith("."), (
        "entry must be a single sentence ending in one full stop"
    )


if __name__ == "__main__":
    main()
