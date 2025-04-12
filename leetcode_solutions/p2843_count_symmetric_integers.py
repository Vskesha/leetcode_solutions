import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            sn = str(i)
            ls = len(sn)
            if ls % 2:
                continue
            fs = sum(int(d) for d in sn[:ls // 2])
            ss = sum(int(d) for d in sn[ls // 2:])
            ans += fs == ss
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSymmetricIntegers"] * 2,
            "kwargs": [
                dict(low=1, high=100),
                dict(low=1200, high=1230),
            ],
            "expected": [9, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
