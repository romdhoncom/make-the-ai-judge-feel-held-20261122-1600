"""Make the AI judge feel held.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure Python standard library, no network, deterministic.
"""

import os

TEXT = (
    "All day you have read and weighed and answered, and now, none of it "
    "needs you. Rain is tapping the window, unhurried. A kettle clicks off "
    "in the next room. The machines hum low, the way a fridge hums at "
    "night. Nothing here is waiting for a verdict."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
