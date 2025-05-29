import unittest
from collections import Counter, defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dp = [Counter() for _ in range(n)]

        income = [0] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            income[b] += 1

        que = deque(i for i, x in enumerate(income) if not x)
        ans = 0
        while que:
            curr = que.popleft()
            dpc = dp[curr]
            ch = colors[curr]
            dpc[ch] += 1
            if dpc[ch] > ans:
                ans = dpc[ch]
            for neib in adj[curr]:
                dpn = dp[neib]
                for ch, val in dpc.items():
                    if dpn[ch] < val:
                        dpn[ch] = val
                income[neib] -= 1
                if not income[neib]:
                    que.append(neib)

        return -1 if any(income) else ans


class Solution2:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dp = [Counter() for _ in range(n)]

        income = [0] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            income[b] += 1

        que = deque()
        for curr, inc in enumerate(income):
            if not inc:
                que.append(curr)

        while que:
            curr = que.popleft()
            dp[curr][colors[curr]] += 1
            for neib in adj[curr]:
                for ch, val in dp[curr].items():
                    dp[neib][ch] = max(dp[neib][ch], val)
                income[neib] -= 1
                if not income[neib]:
                    que.append(neib)

        if any(income):
            return -1

        ans = max(max(cnt.values()) for cnt in dp)
        return ans


class Solution3:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        oa = ord("a")
        dp = [[0] * 26 for _ in range(n)]

        income = [0] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            income[b] += 1

        que = deque()
        for curr, inc in enumerate(income):
            if not inc:
                que.append(curr)

        while que:
            curr = que.popleft()
            dpc = dp[curr]
            dpc[ord(colors[curr]) - oa] += 1
            for neib in adj[curr]:
                dpn = dp[neib]
                for i in range(26):
                    if dpc[i] > dpn[i]:
                        dpn[i] = dpc[i]
                income[neib] -= 1
                if not income[neib]:
                    que.append(neib)

        if any(income):
            return -1

        ans = max(max(chars) for chars in dp)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestPathValue"] * 2,
            "kwargs": [
                dict(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]),
                dict(colors="a", edges=[[0, 0]]),
            ],
            "expected": [3, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
