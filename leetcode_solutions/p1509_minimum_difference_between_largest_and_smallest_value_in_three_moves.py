import unittest
from heapq import heappop, heappush, heappushpop, nlargest, nsmallest
from operator import sub
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return min(map(sub, sorted(nlargest(4, nums)), nsmallest(4, nums)))


class Solution1:
    def minDifference(self, nums: List[int]) -> int:
        return min(
            a - b
            for a, b in zip(sorted(nlargest(4, nums)), nsmallest(4, nums))
        )


class Solution2:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        nums = iter(nums)
        mins, maxs = [], []

        for _ in range(4):
            val = next(nums)
            heappush(mins, -val)
            heappush(maxs, val)

        for val in nums:
            heappushpop(mins, -val)
            heappushpop(maxs, val)

        mins.sort(reverse=True)
        return min(heappop(maxs) + m for m in mins)


class Solution3:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        return min(nums[i - 4] - nums[i] for i in range(4))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_difference_1(self):
        print("Test minDifference 1... ", end="")
        self.assertEqual(self.sol.minDifference(nums=[5, 3, 2, 4]), 0)
        print("OK")

    def test_min_difference_2(self):
        print("Test minDifference 2... ", end="")
        self.assertEqual(self.sol.minDifference(nums=[1, 5, 0, 10, 14]), 1)
        print("OK")

    def test_min_difference_3(self):
        print("Test minDifference 3... ", end="")
        self.assertEqual(self.sol.minDifference(nums=[3, 100, 20]), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()
