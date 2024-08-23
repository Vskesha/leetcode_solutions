import unittest
from bisect import bisect_left
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countKConstraintSubstrings(
        self, s: str, k: int, queries: List[List[int]]
    ) -> List[int]:
        starts, total, sbstr, st = [], [0], 0, 0
        cnt = {"1": 0, "0": 0}
        for i, ch in enumerate(s):
            cnt[ch] += 1
            while cnt["0"] > k and cnt["1"] > k:
                cnt[s[st]] -= 1
                st += 1
            sbstr += i - st + 1
            total.append(sbstr)
            starts.append(st)

        acst = list(accumulate(starts, initial=0))
        answer = []
        for li, ri in queries:
            tot = total[ri + 1] - total[li]
            bi = min(bisect_left(starts, li), ri + 1)
            if bi > li:
                tot += acst[bi] - acst[li] - li * (bi - li)
            answer.append(tot)

        return answer


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countKConstraintSubstrings"] * 3,
            "kwargs": [
                dict(s="0001111", k=2, queries=[[0, 6]]),
                dict(s="010101", k=1, queries=[[0, 5], [1, 4], [2, 3]]),
                dict(
                    s="000",
                    k=1,
                    queries=[[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]],
                ),
            ],
            "expected": [[26], [15, 9, 3], [1, 3, 6, 1, 3, 1]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
