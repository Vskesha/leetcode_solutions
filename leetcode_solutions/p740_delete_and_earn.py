import unittest
from itertools import groupby
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = b = prev = 0
        for n, gr in groupby(sorted(nums)):
            sm = sum(gr)
            a, b = b, max(b, a + sm) if n == prev else b + sm
            prev = n + 1
        return b


class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = b = prev = 0
        for n, gr in groupby(sorted(nums)):
            a, b = b, max(b, sum(gr) + (a if n == prev else b))
            prev = n + 1
        return b


class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev = -1
        dp = [0, 0]

        for n, gr in groupby(sorted(nums)):
            val = len(list(gr)) * n
            if n == prev:
                dp.append(max(dp[-1], val + dp[-2]))
            else:
                dp.append(dp[-1] + val)
            prev = n + 1

        return dp[-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_delete_and_earn_1(self):
        print("Test deleteAndEarn 1... ", end="")
        self.assertEqual(self.sol.deleteAndEarn(nums=[3, 4, 2]), 6)
        print("OK")

    def test_delete_and_earn_2(self):
        print("Test deleteAndEarn 2... ", end="")
        self.assertEqual(self.sol.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]), 9)
        print("OK")


if __name__ == "__main__":
    unittest.main()
