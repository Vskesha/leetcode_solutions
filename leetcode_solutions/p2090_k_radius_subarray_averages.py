import unittest
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        el = k * 2 + 1
        ws = sum(nums[: el - 1])

        for i in range(k, len(nums) - k):
            ws += nums[i + k]
            res[i] = ws // el
            ws -= nums[i - k]

        return res


class Solution2:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n

        if k * 2 >= n:
            return result

        li = k * 2 + 1
        curr_sum = sum(nums[: li - 1])
        for i in range(k, n - k):
            curr_sum += nums[i + k]
            result[i] = curr_sum // li
            curr_sum -= nums[i - k]

        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_get_averages_1(self):
        print("Test getAverages 1... ", end="")
        self.assertEqual(
            self.sol.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3),
            [-1, -1, -1, 5, 4, 4, -1, -1, -1],
        )
        print("OK")

    def test_get_averages_2(self):
        print("Test getAverages 2... ", end="")
        self.assertEqual(
            self.sol.getAverages(nums=[100000], k=0),
            [100000],
        )
        print("OK")

    def test_get_averages_3(self):
        print("Test getAverages 3... ", end="")
        self.assertEqual(
            self.sol.getAverages(nums=[8], k=100000),
            [-1],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
