import unittest

from aoc.years.y2025 import day02


class TestDay02(unittest.TestCase):
    def test_example(self):
        # Wrapped for readability, but solver should accept whitespace/newlines.
        sample = """
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
        1698522-1698528,446443-446449,38593856-38593862,565653-565659,
        824824821-824824827,2121212118-2121212124
        """
        self.assertEqual(day02.solve_part1(sample), 1227775554)


if __name__ == "__main__":
    unittest.main()
