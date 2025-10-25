import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxDiff(self, num: int) -> int:
        snum = str(num)
        for d in snum:
            if d != "9":
                mxn = int(snum.replace(d, "9"))
                break
        else:
            return int("8" * len(snum))

        if snum[0] != "1":
            return mxn - int(snum.replace(snum[0], "1"))

        for d in snum:
            if d != "0" and d != "1":
                return mxn - int(snum.replace(d, "0"))

        return mxn - int(snum)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxDiff"] * 3,
            "kwargs": [
                dict(num=555),
                dict(num=9),
                dict(num=123456),
            ],
            "expected": [888, 8, 820000],
        },
    ]


if __name__ == "__main__":
    unittest.main()
