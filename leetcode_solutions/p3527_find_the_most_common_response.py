import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = Counter(w for r in responses for w in set(r))
        mv = max(cnt.values())
        return min(w for w, c in cnt.items() if c == mv)


class Solution2:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = Counter()

        for resp in responses:
            for dr in set(resp):
                cnt[dr] += 1

        mc, mr = 0, ""
        for resp, val in cnt.items():
            if val > mc:
                mc = val
                mr = resp
            elif val == mc and resp < mr:
                mr = resp

        return mr


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findCommonResponse"] * 2,
            "kwargs": [
                dict(
                    responses=[
                        ["good", "ok", "good", "ok"],
                        ["ok", "bad", "good", "ok", "ok"],
                        ["good"],
                        ["bad"],
                    ]
                ),
                dict(
                    responses=[
                        ["good", "ok", "good"],
                        ["ok", "bad"],
                        ["bad", "notsure"],
                        ["great", "good"],
                    ]
                ),
            ],
            "expected": ["good", "bad"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
