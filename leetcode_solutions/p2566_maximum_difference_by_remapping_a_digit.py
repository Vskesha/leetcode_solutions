import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minMaxDifference(self, num: int) -> int:
        snum = str(num)
        for ch in snum:
            if ch != "9":
                return int(snum.replace(ch, "9")) - int(
                    snum.replace(snum[0], "0")
                )
        else:
            return num


class Solution2:
    def minMaxDifference(self, num: int) -> int:
        snum = str(num)
        for ch in snum:
            if ch != "9":
                fnn = ch
                break
        else:
            return num
        return int(snum.replace(fnn, "9")) - int(snum.replace(snum[0], "0"))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minMaxDifference"] * 2,
            "kwargs": [
                dict(num=11891),
                dict(num=90),
            ],
            "expected": [99009, 99],
        },
    ]


if __name__ == "__main__":
    unittest.main()
