import math
import unittest
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def num_of_ways(arr: list) -> int:
            n = len(arr)
            if n < 3:
                return 1

            left_arr, right_arr, root = [], [], arr[0]
            for i in range(1, n):
                if arr[i] < root:
                    left_arr.append(arr[i])
                else:
                    right_arr.append(arr[i])

            left_ways = num_of_ways(left_arr)
            right_ways = num_of_ways(right_arr)
            combs = math.comb(n - 1, len(left_arr))

            return combs * left_ways * right_ways % 1000000007

        return num_of_ways(nums) - 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_num_of_ways_1(self):
        print("Test numOfWays 1... ", end="")
        self.assertEqual(self.sol.numOfWays(nums=[2, 1, 3]), 1)
        print("OK")

    def test_num_of_ways_2(self):
        print("Test numOfWays 2... ", end="")
        self.assertEqual(self.sol.numOfWays(nums=[3, 4, 5, 1, 2]), 5)
        print("OK")

    def test_num_of_ways_3(self):
        print("Test numOfWays 3... ", end="")
        self.assertEqual(self.sol.numOfWays(nums=[1, 2, 3]), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()
