import unittest
from itertools import groupby
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diffs = [a - b for a, b in zip(nums, target)]
        ans = 0

        for neg, gr in groupby(diffs, key=lambda x: x < 0):
            prev = 0
            for g in map(abs, gr):
                if g > prev:
                    ans += g - prev
                prev = g

        return ans


class Solution2:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diffs = [a - b for a, b in zip(nums, target)]
        ans = 0
        neg = False
        prev = 0

        for d in diffs:
            if d == 0:
                prev = 0
                continue
            elif d > 0:
                if neg:
                    ans += d
                    neg = False
                else:
                    ans += max(0, d - prev)
                prev = d
            else:
                d = -d
                if neg:
                    ans += max(0, d - prev)
                else:
                    ans += d
                    neg = True
                prev = d

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimumOperations_1(self):
        print("Test minimumOperations 1... ", end="")
        self.assertEqual(
            2,
            self.sol.minimumOperations(nums=[3, 5, 1, 2], target=[4, 6, 2, 4]),
        )
        print("OK")

    def test_minimumOperations_2(self):
        print("Test minimumOperations 2... ", end="")
        self.assertEqual(
            5, self.sol.minimumOperations(nums=[1, 3, 2], target=[2, 1, 4])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
