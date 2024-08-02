import unittest
from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        fr, ans, st = Counter(), 0, 0
        for i, n in enumerate(nums):
            fr[n] += 1
            while fr[n] > k:
                fr[nums[st]] -= 1
                st += 1
            ans = max(ans, i - st + 1)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maxSubarrayLength_1(self):
        print("Test maxSubarrayLength 1... ", end="")
        self.assertEqual(
            6,
            self.sol.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2),
        )
        print("OK")

    def test_maxSubarrayLength_2(self):
        print("Test maxSubarrayLength 2... ", end="")
        self.assertEqual(
            2,
            self.sol.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1),
        )
        print("OK")

    def test_maxSubarrayLength_3(self):
        print("Test maxSubarrayLength 3... ", end="")
        self.assertEqual(
            4,
            self.sol.maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
