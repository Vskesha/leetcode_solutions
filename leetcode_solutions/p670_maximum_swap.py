import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumSwap(self, num: int) -> int:
        sn = list(str(num))
        lsn = len(sn)

        mch = [("", 0)] * lsn
        mch[-1] = (sn[-1], lsn - 1)
        for i in range(lsn - 2, -1, -1):
            if sn[i] > mch[i + 1][0]:
                mch[i] = (sn[i], i)
            else:
                mch[i] = mch[i + 1]

        for i in range(lsn - 1):
            if sn[i] != mch[i][0]:
                j = mch[i + 1][1]
                sn[i], sn[j] = sn[j], sn[i]
                return int("".join(sn))

        return num


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumSwap"] * 2,
            "kwargs": [
                dict(num=2736),
                dict(num=9973),
            ],
            "expected": [7236, 9973],
        },
    ]


if __name__ == "__main__":
    unittest.main()
