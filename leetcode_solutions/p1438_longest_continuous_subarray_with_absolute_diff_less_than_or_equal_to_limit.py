import unittest
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        stmin, stmax = deque(), deque()
        prev = -1
        ans = 0

        for i, n in enumerate(nums):
            while stmax and stmax[-1][0] <= n:
                stmax.pop()
            stmax.append((n, i))

            while stmin and stmin[-1][0] >= n:
                stmin.pop()
            stmin.append((n, i))

            while stmax[0][0] - stmin[0][0] > limit:
                if stmax[0][1] < stmin[0][1]:
                    prev = stmax.popleft()[1]
                else:
                    prev = stmin.popleft()[1]

            ans = max(ans, i - prev)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_longest_subarray_1(self):
        print("Test longestSubarray_1 ... ", end="")
        self.assertEqual(self.sol.longestSubarray(nums=[8, 2, 4, 7], limit=4), 2)
        print("OK")

    def test_longest_subarray_2(self):
        print("Test longestSubarray_2 ... ", end="")
        self.assertEqual(self.sol.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5), 4)
        print("OK")

    def test_longest_subarray_3(self):
        print("Test longestSubarray_3 ... ", end="")
        self.assertEqual(
            self.sol.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0), 3
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
