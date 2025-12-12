import unittest

from aoc.years.y2025 import day01


class TestDay01Template(unittest.TestCase):
    def test_part1_sums_ints(self):
        self.assertEqual(day01.solve_part1("1\n2\n3\n"), 6)

    def test_part2_doubles_sum(self):
        self.assertEqual(day01.solve_part2("1\n2\n3\n"), 12)


if __name__ == "__main__":
    unittest.main()
