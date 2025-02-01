import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        def ops(ss: str):
            ls = len(ss)
            ss = sorted(ss)
            op = sum(ord(ss[~i]) - ord(ss[i]) for i in range(ls // 2))
            rs = ss[(ls - 1) // 2] * ls
            return op, rs

        def chars(sti: int, ss: str, dps: List[str]):
            while True:
                for ch in ss:
                    yield ch
                sti += len(ss)
                if sti >= len(dps):
                    break
                ss = dps[sti]

        n = len(caption)
        if n < 3:
            return ""
        if n < 6:
            return ops(caption)[1]

        dp = [inf] * n
        dps = [""] * n

        for i in range(n - 3, n - 6, -1):
            dp[i], dps[i] = ops(caption[i:])

        for i in range(n - 6, -1, -1):
            dp[i], dps[i] = ops(caption[i : i + 3])
            dp[i] += dp[i + 3]
            for ln in (4, 5):
                op, rs = ops(caption[i : i + ln])
                nop = dp[i + ln] + op
                if dp[i] > nop:
                    dp[i] = nop
                    dps[i] = rs
                elif dp[i] == nop:
                    for a, b in zip(chars(i, dps[i], dps), chars(i, rs, dps)):
                        if a == b:
                            continue
                        if b < a:
                            dps[i] = rs
                        break

        ans = "".join(chars(0, dps[0], dps))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minCostGoodCaption"] * 5,
            "kwargs": [
                dict(caption="ylrtdmm"),
                dict(caption="owsjeo"),
                dict(caption="cdcd"),
                dict(caption="aca"),
                dict(caption="bc"),
            ],
            "expected": ["rrrrmmm", "sssjjj", "cccc", "aaa", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()
