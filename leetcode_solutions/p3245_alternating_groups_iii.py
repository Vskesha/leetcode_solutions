import unittest
from collections import Counter
from itertools import pairwise
from typing import List


class Solution:
    def numberOfAlternatingGroups(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        lc = len(colors)
        ends = [i for i in range(lc - 1) if colors[i] == colors[i + 1]]
        if colors[0] == colors[-1]:
            ends.append(lc - 1)
        groups = Counter(cv - pv for pv, cv in pairwise(ends))
        groups[ends[0] + lc - ends[-1]] += 1
        pass


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numberOfAlternatingGroups_1(self):
        print("Test numberOfAlternatingGroups 1... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[0, 1, 1, 0, 1], queries=[[2, 1, 0], [1, 4]]
            ),
            [2],
        )
        print("OK")

    def test_numberOfAlternatingGroups_2(self):
        print("Test numberOfAlternatingGroups 2... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[1, 0, 1, 0, 1, 1], queries=[[1, 3], [2, 3, 0], [1, 5]]
            ),
            [2, 0],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
