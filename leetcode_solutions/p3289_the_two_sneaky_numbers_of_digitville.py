import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v == 2]


class Solution2:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        for n in nums:
            if n in seen:
                ans.append(n)
            else:
                seen.add(n)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getSneakyNumbers"] * 3,
            "kwargs": [
                dict(nums=[0, 1, 1, 0]),
                dict(nums=[0, 3, 2, 1, 3, 2]),
                dict(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]),
            ],
            "expected": [[0, 1], [2, 3], [4, 5]],
            "assert_methods": ["assertSameSneakyNumbers"] * 3,
        },
    ]

    def assertSameSneakyNumbers(self, sn1: List[int], sn2: List[int]) -> None:
        self.assertListEqual(sorted(sn1), sorted(sn2))


if __name__ == "__main__":
    unittest.main()
