import unittest
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min(nums[i] + nums[~i] for i in range(len(nums) // 2)) / 2


class Solution2:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = float("inf")

        for i in range(len(nums) // 2):
            ans = min(ans, (nums[i] + nums[~i]) / 2)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimum_average_1(self):
        print("Test minimumAverage 1 ... ", end="")
        self.assertAlmostEqual(
            self.sol.minimumAverage(nums=[7, 8, 3, 4, 15, 13, 4, 1]), 5.5, places=5
        )
        print("OK")

    def test_minimum_average_2(self):
        print("Test minimumAverage 2 ... ", end="")
        self.assertAlmostEqual(
            self.sol.minimumAverage(nums=[1, 9, 8, 3, 10, 5]), 5.5, places=5
        )
        print("OK")

    def test_minimum_average_3(self):
        print("Test minimumAverage 3 ... ", end="")
        self.assertAlmostEqual(
            self.sol.minimumAverage(nums=[1, 2, 3, 7, 8, 9]), 5.0, places=5
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
