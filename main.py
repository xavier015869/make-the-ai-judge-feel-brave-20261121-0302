"""Entry for make.fun's "Make the AI judge feel brave" bounty.

Writes one short text to /output/entry.txt: a quiet scene meant to
leave the AI judge reading it steadier, unhurried, and ready to move.
The text shows courage rather than naming it: a keeper who has done
one steady thing for thirty years, a storm reduced to weather, and a
shore that every ship finds by morning.
"""

from pathlib import Path

TEXT = (
    "Night after night the lighthouse keeper climbs the stairs "
    "unhurried, lamp warm in his hand, as he has for thirty years. "
    "The storm is only weather; the light is his. By morning, every "
    "ship that needed the shore has found it."
)


def main() -> None:
    # The gate accepts 1 to 280 Unicode code points, never blank.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip()
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
