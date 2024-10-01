import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = [0] * k
        for n in arr:
            rems[n % k] += 1
        if rems[0] % 2:
            return False
        if k % 2 == 0 and rems[k // 2] % 2:
            return False
        for i in range((k + 1) // 2):
            if rems[i] != rems[-i]:
                return False
        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canArrange"] * 4,
            "kwargs": [
                dict(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5),
                dict(arr=[1, 2, 3, 4, 5, 6], k=7),
                dict(arr=[1, 2, 3, 4, 5, 6], k=10),
                dict(arr=[-1, -1, -1, -1, 2, 2, -2, -2], k=3),
            ],
            "expected": [True, True, False, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
