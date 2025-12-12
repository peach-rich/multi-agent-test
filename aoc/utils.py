from __future__ import annotations

from typing import Iterable


def lines(text: str) -> list[str]:
    """Split into non-empty lines (trailing newline ok)."""
    return [ln for ln in text.splitlines() if ln != ""]


def ints(text: str) -> list[int]:
    """Parse one integer per non-empty line."""
    return [int(x) for x in lines(text)]


def chunks(text: str) -> list[str]:
    """Split on blank lines."""
    parts = text.strip("\n").split("\n\n")
    return [p for p in parts if p != ""]


def sliding_window(seq: Iterable[int], n: int) -> list[tuple[int, ...]]:
    """Materialize length-n sliding windows."""
    xs = list(seq)
    return [tuple(xs[i : i + n]) for i in range(0, max(0, len(xs) - n + 1))]
