import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0

        for key, val in cnt.items():
            key += 1
            ans += ((val - 1) // key + 1) * key

        return ans


class Solution2:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = {}
        ans = 0

        for n in answers:
            if n in cnt and cnt[n]:
                cnt[n] -= 1
            else:
                ans += n + 1
                cnt[n] = n

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numRabbits"] * 2,
            "kwargs": [
                dict(answers=[1, 1, 2]),
                dict(answers=[10, 10, 10]),
            ],
            "expected": [5, 11],
        },
    ]


if __name__ == "__main__":
    unittest.main()
