import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(index + 1)
            else:
                nums[index] = -nums[index]

        return res


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for n in nums:
            if n in seen:
                seen.remove(n)
                ans.append(n)
            else:
                seen.add(n)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findDuplicates"] * 3,
            "kwargs": [
                dict(nums=[4, 3, 2, 7, 8, 2, 3, 1]),
                dict(nums=[1, 1, 2]),
                dict(nums=[1]),
            ],
            "expected": [[2, 3], [1], []],
            "assert_methods": ["assertSameNumbers"] * 3,
        },
    ]

    def assertSameNumbers(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(len(set(actual)), len(actual))
        self.assertSetEqual(set(actual), set(expected))


if __name__ == "__main__":
    unittest.main()
