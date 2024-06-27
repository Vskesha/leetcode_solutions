import unittest
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        a, b = 0, nums[0]

        for i in range(1, len(nums)):
            a, b = b, max(b + nums[i], a + nums[i - 1] - nums[i])

        return b


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximum_total_cost_1(self):
        print("Test maximumTotalCost 1... ", end="")
        self.assertEqual(self.sol.maximumTotalCost(nums=[1, -2, 3, 4]), 10)
        print("OK")

    def test_maximum_total_cost_2(self):
        print("Test maximumTotalCost 2... ", end="")
        self.assertEqual(self.sol.maximumTotalCost(nums=[1, -1, 1, -1]), 4)
        print("OK")

    def test_maximum_total_cost_3(self):
        print("Test maximumTotalCost 3... ", end="")
        self.assertEqual(self.sol.maximumTotalCost(nums=[0]), 0)
        print("OK")

    def test_maximum_total_cost_4(self):
        print("Test maximumTotalCost 4... ", end="")
        self.assertEqual(self.sol.maximumTotalCost(nums=[1, -1]), 2)
        print("OK")


if __name__ == "__main__":
    unittest.main()
