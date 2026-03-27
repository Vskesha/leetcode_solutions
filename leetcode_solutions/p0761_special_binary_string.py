import unittest
from itertools import pairwise

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        mnt = [0]
        h = 0

        for d in s:
            h += 1 if d == "1" else -1
            mnt.append(h)

        def dfs(sti, eni, mnt):
            if eni - sti < 2:
                return

            lvl = mnt[sti]
            inds = [i for i in range(sti, eni) if mnt[i] == lvl]

            sbmnts = []
            for i, j in pairwise(inds):
                dfs(i + 1, j, mnt)
                sbmnts.append(mnt[i + 1 : j])

            if len(sbmnts) > 1:
                sbmnts.sort(reverse=True)
                i = sti + 1
                for sbmnt in sbmnts:
                    for h in sbmnt:
                        mnt[i] = h
                        i += 1
                    mnt[i] = lvl
                    i += 1

        dfs(0, len(mnt), mnt)

        ans = "".join("1" if b > a else "0" for a, b in pairwise(mnt))
        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["makeLargestSpecial"] * 2,
            "kwargs": [
                dict(s="11011000"),
                dict(s="10"),
            ],
            "expected": ["11100100", "10"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
