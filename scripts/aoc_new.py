from __future__ import annotations

import argparse
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python scripts/aoc_new.py")
    p.add_argument("year", type=int)
    p.add_argument("day", type=int)
    args = p.parse_args(argv)

    year_dir = Path("aoc") / "years" / f"y{args.year}"
    year_dir.mkdir(parents=True, exist_ok=True)
    (year_dir / "__init__.py").touch(exist_ok=True)

    day_mod = year_dir / f"day{args.day:02d}.py"
    if not day_mod.exists():
        template = (Path("aoc") / "templates" / "day.py").read_text(encoding="utf-8")
        day_mod.write_text(template, encoding="utf-8")

    input_dir = Path("inputs") / str(args.year)
    input_dir.mkdir(parents=True, exist_ok=True)
    input_file = input_dir / f"day{args.day:02d}.txt"
    input_file.touch(exist_ok=True)

    print(f"Created/verified: {day_mod}")
    print(f"Created/verified: {input_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
