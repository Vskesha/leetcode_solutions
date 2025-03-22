import unittest
from collections import Counter, defaultdict
from itertools import combinations
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        lm = len(str(max(nums)))
        cnt = Counter(nums)
        freq = defaultdict(list)
        for x, v in cnt.items():
            nn = str(x).zfill(lm)
            freq[nn].append((nn, v))
            s = list(nn)
            for j in range(1, lm):
                for k in range(j):
                    if s[j] != s[k]:
                        s[j], s[k] = s[k], s[j]
                        cand = "".join(s)
                        freq[cand].append((nn, v))
                        s[j], s[k] = s[k], s[j]
        ans = Counter()
        for _, vk in freq.items():
            for x1, v1 in vk:
                ans[(x1, x1)] = v1 * (v1 - 1) // 2
            for (x1, v1), (x2, v2) in combinations(vk, 2):
                ans[(x1, x2)] = v1 * v2
        return sum(ans.values())


class Solution2:
    def countPairs(self, nums: List[int]) -> int:
        lm = len(str(max(nums)))
        cnt = Counter(nums)
        freq = defaultdict(list)
        for x, v in cnt.items():
            freq[x].append((x, v))
            s = list(str(x).zfill(lm))
            for j in range(lm):
                for k in range(j + 1, lm):
                    if s[j] != s[k]:
                        s[j], s[k] = s[k], s[j]
                        cand = int("".join(s))
                        freq[cand].append((x, v))
                        s[j], s[k] = s[k], s[j]
        ans = Counter()
        for x, v in freq.items():
            for x1, v1 in v:
                ans[x1, x1] = v1 * (v1 - 1) // 2
            for (x1, v1), (x2, v2) in combinations(v, 2):
                ans[x1, x2] = v1 * v2
        return sum(ans.values())


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPairs"] * 2,
            "kwargs": [
                dict(nums=[1023, 2310, 2130, 213]),
                dict(nums=[1, 10, 100]),
            ],
            "expected": [4, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
