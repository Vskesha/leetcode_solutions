import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        vals = Counter(nums).values()
        mx = max(vals)
        return sum(x for x in vals if x == mx)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxFrequencyElements"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 2, 3, 1, 4]),
                dict(nums=[1, 2, 3, 4, 5]),
            ],
            "expected": [4, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_max_frequency_elements():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]) == 4
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.maxFrequencyElements(nums=[1, 2, 3, 4, 5]) == 5
#     print("OK")


# if __name__ == "__main__":
#     test_max_frequency_elements()
