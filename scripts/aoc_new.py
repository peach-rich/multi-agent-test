from __future__ import annotations

import argparse
from pathlib import Path


TEST_TEMPLATE = """import unittest

from aoc.years.y{year} import day{day:02d}


class TestDay{day:02d}(unittest.TestCase):
    EXAMPLE = \"\"\"\"\"\"
    
    def test_part1_example(self):
        result = day{day:02d}.solve_part1(self.EXAMPLE)
        self.assertEqual(result, None)  # TODO: Add expected value
    
    def test_part2_example(self):
        result = day{day:02d}.solve_part2(self.EXAMPLE)
        self.assertEqual(result, None)  # TODO: Add expected value


if __name__ == "__main__":
    unittest.main()
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="python scripts/aoc_new.py",
        description="Create scaffolding for a new Advent of Code day",
    )
    p.add_argument("year", type=int, help="AoC year (e.g., 2025)")
    p.add_argument("day", type=int, help="AoC day (1-25)")
    args = p.parse_args(argv)

    # Validate inputs
    if args.year < 2015:
        raise SystemExit("Year must be 2015 or later")
    if not 1 <= args.day <= 25:
        raise SystemExit("Day must be between 1 and 25")

    # Create year directory structure
    year_dir = Path("aoc") / "years" / f"y{args.year}"
    year_dir.mkdir(parents=True, exist_ok=True)
    (year_dir / "__init__.py").touch(exist_ok=True)

    # Create day module from template
    day_mod = year_dir / f"day{args.day:02d}.py"
    if not day_mod.exists():
        template = (Path("aoc") / "templates" / "day.py").read_text(encoding="utf-8")
        day_mod.write_text(template, encoding="utf-8")
        print(f"Created: {day_mod}")
    else:
        print(f"Already exists: {day_mod}")

    # Create input file
    input_dir = Path("inputs") / str(args.year)
    input_dir.mkdir(parents=True, exist_ok=True)
    input_file = input_dir / f"day{args.day:02d}.txt"
    if not input_file.exists():
        input_file.touch(exist_ok=True)
        print(f"Created: {input_file}")
    else:
        print(f"Already exists: {input_file}")

    # Create test file
    test_file = Path("tests") / f"test_day{args.day:02d}.py"
    if not test_file.exists():
        test_content = TEST_TEMPLATE.format(year=args.year, day=args.day)
        test_file.write_text(test_content, encoding="utf-8")
        print(f"Created: {test_file}")
    else:
        print(f"Already exists: {test_file}")

    print(f"\nReady to solve! Run with:")
    print(f"  python -m aoc {args.year} {args.day}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
