from __future__ import annotations

from bisect import bisect_left, bisect_right


def _parse_ranges(text: str) -> list[tuple[int, int]]:
    # Accept wrapped inputs (newlines/spaces) even though the real input is one line.
    raw = "".join(ch for ch in text if not ch.isspace())
    if not raw:
        return []
    out: list[tuple[int, int]] = []
    for part in raw.split(","):
        if not part:
            continue
        a_str, b_str = part.split("-", 1)
        a = int(a_str)
        b = int(b_str)
        if a > b:
            a, b = b, a
        out.append((a, b))
    return out


def _invalid_ids_up_to(max_n: int) -> tuple[list[int], list[int]]:
    """
    Invalid ID definition: a sequence of digits repeated twice, e.g. 55, 6464, 123123.

    Generate all such numbers <= max_n. Since max_n in the puzzle input is ~10 digits,
    this is small (<= 111,109 candidates up to 10 digits).
    Returns (sorted_ids, prefix_sums).
    """
    if max_n < 11:
        return ([], [0])

    max_digits = len(str(max_n))
    max_k = max_digits // 2

    ids: list[int] = []
    for k in range(1, max_k + 1):
        lo = 10 ** (k - 1)
        hi = 10**k - 1
        pow10 = 10**k
        for r in range(lo, hi + 1):
            n = r * pow10 + r
            if n > max_n:
                break
            ids.append(n)

    prefix = [0]
    s = 0
    for n in ids:
        s += n
        prefix.append(s)
    return ids, prefix


def solve_part1(text: str) -> int:
    ranges = _parse_ranges(text)
    if not ranges:
        return 0

    max_b = max(b for _, b in ranges)
    invalids, pref = _invalid_ids_up_to(max_b)

    total = 0
    for a, b in ranges:
        i = bisect_left(invalids, a)
        j = bisect_right(invalids, b)
        total += pref[j] - pref[i]
    return total


def solve_part2(text: str):
    raise NotImplementedError
