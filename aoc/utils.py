from __future__ import annotations

import re
from typing import Iterable, TypeVar


def lines(text: str) -> list[str]:
    """Split into non-empty lines (trailing newline ok)."""
    return [ln for ln in text.splitlines() if ln != ""]


def ints(text: str) -> list[int]:
    """Parse one integer per non-empty line."""
    return [int(x) for x in lines(text)]


def extract_ints(text: str) -> list[int]:
    """Extract all integers (including negative) from text using regex."""
    return [int(x) for x in re.findall(r"-?\d+", text)]


def chunks(text: str) -> list[str]:
    """Split on blank lines."""
    parts = text.strip("\n").split("\n\n")
    return [p for p in parts if p != ""]


T = TypeVar("T")


def sliding_window(seq: Iterable[T], n: int) -> list[tuple[T, ...]]:
    """Materialize length-n sliding windows."""
    xs = list(seq)
    return [tuple(xs[i : i + n]) for i in range(0, max(0, len(xs) - n + 1))]


def grid(text: str) -> list[list[str]]:
    """Parse text into a 2D grid of characters."""
    return [list(line) for line in lines(text)]


def neighbors_4(row: int, col: int) -> list[tuple[int, int]]:
    """Get 4-directional neighbors (up, down, left, right)."""
    return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]


def neighbors_8(row: int, col: int) -> list[tuple[int, int]]:
    """Get 8-directional neighbors (including diagonals)."""
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]


def in_bounds(grid_data: list[list[T]], row: int, col: int) -> bool:
    """Check if a position is within grid bounds."""
    return 0 <= row < len(grid_data) and 0 <= col < len(grid_data[0])


def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
