import unittest
from itertools import product
from typing import List, Set

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if n[i] == '0' else '0' for i, n in enumerate(nums))


class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i, n in enumerate(nums):
            ans.append("1" if n[i] == "0" else "0")

        return "".join(ans)

class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def expected_for(nums: List[str]) -> Set[str]:
        res = set()
        for prod in product("01", repeat=len(nums)):
            res.add("".join(prod))
        return res - set(nums)

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findDifferentBinaryString"] * 3,
            "kwargs": [
                dict(nums = ["01","10"]),
                dict(nums = ["00","01"]),
                dict(nums = ["111","011","001"]),
            ],
            "expected": [
                expected_for(["01","10"]),
                expected_for(["00", "01"]),
                expected_for(["111", "011", "001"]),
            ],
            "assert_methods": ["assert_distinct_binary"] * 3,
        },
    ]

    def assert_distinct_binary(self, result: str, expected: Set[str]) -> None:
        self.assertIn(result, expected)


if __name__ == "__main__":
    unittest.main()
