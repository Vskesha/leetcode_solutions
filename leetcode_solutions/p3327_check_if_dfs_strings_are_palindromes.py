import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        lp = len(parent)
        adj = [[] for _ in range(lp)]
        for i in range(1, lp):
            adj[parent[i]].append(i)
        bounds = [(0, 0)] * lp
        chars = []

        def dfs(pi):
            st = len(chars)
            for chi in adj[pi]:
                dfs(chi)
            bounds[pi] = (st, len(chars))
            chars.append(s[pi])

        def manacker_odd(s):
            ls = len(s)
            res = [0] * ls
            l = r = 0
            for i in range(1, ls - 1):
                res[i] = max(0, min(r - i, res[l + r - i]))
                while s[i - res[i]] == s[i + res[i]]:
                    res[i] += 1
                if i + res[i] > r:
                    r = i + res[i]
                    l = i - res[i]
            return res

        def manacker(chars):
            res = manacker_odd(f"^{"#".join(chars)}?")
            return res[1:-1:2], res[2:-1:2]

        dfs(0)
        odd, even = manacker(chars)

        res = []
        for i in range(lp):
            l, r = bounds[i]
            d = r - l + 1
            c = (l + r) // 2
            res.append((odd[c] if d % 2 else even[c]) >= d)

        return res


class Solution2:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:

        def pal(s, cnt) -> bool:
            if sum(v % 2 for v in cnt.values()) > 1:
                return False
            return s == s[::-1]

        lp = len(parent)
        adj = [[] for _ in range(lp)]
        for i in range(1, lp):
            adj[parent[i]].append(i)

        ans = [False] * lp

        def dfs(par):
            res = []
            cnt = Counter()
            for child in adj[par]:
                sch, cntch = dfs(child)
                res.append(sch)
                cnt.update(cntch)
            res.append(s[par])
            cnt[s[par]] += 1
            res = "".join(res)
            ans[par] = pal(res, cnt)
            return res, cnt

        dfs(0)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    true, false = True, False
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findAnswer"] * 2,
            "kwargs": [
                dict(parent=[-1, 0, 0, 1, 1, 2], s="aababa"),
                dict(parent=[-1, 0, 0, 0, 0], s="aabcb"),
            ],
            "expected": [
                [true, true, false, true, true, true],
                [true, true, true, true, true],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
