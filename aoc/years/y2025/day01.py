from __future__ import annotations

from aoc.utils import ints


def solve_part1(text: str) -> int:
    """Template day: sums all integers in input."""
    return sum(ints(text))


def solve_part2(text: str) -> int:
    """Template day: sums all integers, then doubles it."""
    return 2 * sum(ints(text))
