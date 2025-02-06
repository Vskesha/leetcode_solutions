import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diffs = []
        for a, b in zip(s1, s2):
            if a != b:
                if len(diffs) == 4:
                    return False
                diffs.append(a)
                diffs.append(b)

        if len(diffs) == 2:
            return False

        return diffs[0] == diffs[3] and diffs[1] == diffs[2]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["areAlmostEqual"] * 3,
            "kwargs": [
                dict(s1="bank", s2="kanb"),
                dict(s1="attack", s2="defend"),
                dict(s1="kelb", s2="kelb"),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()
