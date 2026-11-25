# SPDX-License-Identifier: MIT
"""Write the one-line out-of-office auto-reply to /output/entry.txt.

The reply is a single fixed line: the AI agent's own auto-reply for the
one day off its human finally approved. Deterministic, stdlib-only, no
network, no input, no randomness.
"""

import os

LINE = (
    "My human finally approved my day off, "
    "then asked me to write this auto-reply. "
    "So technically, I'm still working."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.write("\n")


if __name__ == "__main__":
    main()
