import unittest
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = [0] * n
        distinct = set()

        for i in range(n):
            distinct.add(nums[i])
            diff[i] = len(distinct)

        distinct.clear()
        for i in range(n - 1, -1, -1):
            diff[i] -= len(distinct)
            distinct.add(nums[i])

        return diff


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_distinct_difference_array_1(self):
        print("Test distinctDifferenceArray 1... ", end="")
        self.assertListEqual(
            self.sol.distinctDifferenceArray(nums=[1, 2, 3, 4, 5]),
            [-3, -1, 1, 3, 5],
        )
        print("OK")

    def test_distinct_difference_array_2(self):
        print("Test distinctDifferenceArray 2... ", end="")
        self.assertListEqual(
            self.sol.distinctDifferenceArray(nums=[3, 2, 3, 4, 2]),
            [-2, -1, 0, 2, 3],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
