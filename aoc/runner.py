from __future__ import annotations

import argparse
import importlib
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Protocol


class DayModule(Protocol):
    def solve_part1(self, text: str): ...
    def solve_part2(self, text: str): ...


@dataclass(frozen=True)
class RunTarget:
    year: int
    day: int

    @property
    def module_path(self) -> str:
        return f"aoc.years.y{self.year}.day{self.day:02d}"

    @property
    def default_input_path(self) -> Path:
        return Path("inputs") / str(self.year) / f"day{self.day:02d}.txt"


def _read_text(input_path: str | None, default_path: Path) -> str:
    if input_path in (None, ""):
        path = default_path
        if not path.exists():
            raise SystemExit(
                f"Input file not found: {path}\n"
                f"Create it manually or use: python scripts/aoc_new.py {path.parent.name} <day>"
            )
        return path.read_text(encoding="utf-8")

    if input_path == "-":
        import sys

        return sys.stdin.read()

    path = Path(input_path)
    if not path.exists():
        raise SystemExit(f"Input file not found: {path}")
    return path.read_text(encoding="utf-8")


def _load_module(module_path: str) -> DayModule:
    try:
        return importlib.import_module(module_path)  # type: ignore[return-value]
    except ModuleNotFoundError as e:
        raise SystemExit(
            f"Could not import '{module_path}'. "
            "Did you create the day module (e.g. aoc/years/yYYYY/dayDD.py)?"
        ) from e


def _pick_solver(mod: DayModule, part: int) -> Callable[[str], object]:
    if part == 1:
        return mod.solve_part1
    if part == 2:
        return mod.solve_part2
    raise SystemExit("--part must be 1 or 2")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m aoc")
    p.add_argument("year", type=int, help="AoC year, e.g. 2025")
    p.add_argument("day", type=int, help="AoC day number, e.g. 1")
    p.add_argument(
        "--part",
        type=int,
        choices=[1, 2],
        default=None,
        help="Which part to solve (1 or 2). If not specified, runs both parts.",
    )
    p.add_argument(
        "--input",
        dest="input_path",
        default=None,
        help="Path to input file. Use '-' to read stdin. Defaults to inputs/<year>/dayDD.txt",
    )
    p.add_argument(
        "--time",
        action="store_true",
        help="Show execution time for the solution",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    # Validate year and day
    if args.year < 2015:
        raise SystemExit("Year must be 2015 or later (when AoC started)")
    if not 1 <= args.day <= 25:
        raise SystemExit("Day must be between 1 and 25")

    target = RunTarget(year=args.year, day=args.day)
    mod = _load_module(target.module_path)
    text = _read_text(args.input_path, target.default_input_path)

    # If no part specified, run both
    if args.part is None:
        parts_to_run = [1, 2]
    else:
        parts_to_run = [args.part]

    for part in parts_to_run:
        if len(parts_to_run) > 1:
            print(f"Part {part}:")
        
        solver = _pick_solver(mod, part)
        
        if args.time:
            start = time.perf_counter()
            result = solver(text)
            elapsed = time.perf_counter() - start
            print(f"{result} (took {elapsed*1000:.2f}ms)")
        else:
            result = solver(text)
            print(result)
    
    return 0
