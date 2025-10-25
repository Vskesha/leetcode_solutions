import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            if height[left] < height[right]:
                ans = max(ans, height[left] * (right - left))
                curr_height = height[left]
                left += 1
                while left < right and height[left] <= curr_height:
                    left += 1
            else:
                ans = max(ans, height[right] * (right - left))
                curr_height = height[right]
                right -= 1
                while left < right and height[right] <= curr_height:
                    right -= 1

        return ans


class Solution1:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            if height[l] < height[r]:
                ans = max(ans, height[l] * (r - l))
                l += 1
            else:
                ans = max(ans, height[r] * (r - l))
                r -= 1

        return ans


class Solution2:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            if height[left] < height[right]:
                ans = max(ans, height[left] * (right - left))
                left += 1
            else:
                ans = max(ans, height[right] * (right - left))
                right -= 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxArea"] * 3,
            "kwargs": [
                dict(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]),
                dict(height=[1, 1]),
                dict(height=[4, 3, 2, 1]),
            ],
            "expected": [49, 1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
