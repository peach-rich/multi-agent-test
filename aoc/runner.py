from __future__ import annotations

import argparse
import importlib
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
        return path.read_text(encoding="utf-8")

    if input_path == "-":
        import sys

        return sys.stdin.read()

    return Path(input_path).read_text(encoding="utf-8")


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
    p.add_argument("--part", type=int, choices=[1, 2], default=1)
    p.add_argument(
        "--input",
        dest="input_path",
        default=None,
        help="Path to input file. Use '-' to read stdin. Defaults to inputs/<year>/dayDD.txt",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    target = RunTarget(year=args.year, day=args.day)
    mod = _load_module(target.module_path)
    text = _read_text(args.input_path, target.default_input_path)

    solver = _pick_solver(mod, args.part)
    result = solver(text)
    print(result)
    return 0
