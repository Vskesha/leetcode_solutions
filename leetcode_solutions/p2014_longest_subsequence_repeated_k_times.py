import unittest
from collections import Counter, deque

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        chars = [ch for ch, freq in cnt.items() if freq >= k]
        chars.sort(reverse=True)
        que = deque(chars)
        ans = ""

        while que:
            cur = que.popleft()
            if len(cur) > len(ans):
                ans = cur
            for ch in chars:
                can = cur + ch
                it = iter(s)
                if all(c in it for c in can * k):
                    que.append(can)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestSubsequenceRepeatedK"] * 3,
            "kwargs": [
                dict(s="letsleetcode", k=2),
                dict(s="bb", k=2),
                dict(s="ab", k=2),
            ],
            "expected": ["let", "b", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()
