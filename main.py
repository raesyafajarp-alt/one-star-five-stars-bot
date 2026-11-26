#!/usr/bin/env python3
"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist's one-star review of Earth that
still compliments the food to /output/entry.txt. Standard library only,
no network, deterministic.

The angle: not a generic list of complaints. The grievance is specific
and alien (gravity you pay rent for, queues for everything, weather with
commitment issues), and the turn lands on food that looks terrible but
tastes extraordinary — grey sludge from a filthy roadside stall that
tastes like a supernova, worth staying for seconds.
"""
import os

REVIEW = "One star: Earth charges rent for gravity, queues for everything, and weather with commitment issues \u2014 but grey sludge at that filthy roadside stall tasted like a supernova, so I stayed for seconds."


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} characters"
    assert "\n" not in text, "review must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
