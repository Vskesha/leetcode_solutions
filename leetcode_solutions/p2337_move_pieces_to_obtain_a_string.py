import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        st = [(i, ch) for i, ch in enumerate(start) if ch != "_"]
        tg = [(i, ch) for i, ch in enumerate(target) if ch != "_"]
        if len(st) != len(tg):
            return False
        for (si, sc), (ti, tc) in zip(st, tg):
            if sc != tc:
                return False
            if sc == "R" and ti < si:
                return False
            if sc == "L" and si < ti:
                return False
        return True


class Solution1:
    def canChange(self, start: str, target: str) -> bool:
        st = [(i, ch) for i, ch in enumerate(start) if ch != "_"]
        tg = [(i, ch) for i, ch in enumerate(target) if ch != "_"]
        if len(st) != len(tg):
            return False
        for (si, sc), (ti, tc) in zip(st, tg):
            if sc != tc or (sc == "R" and ti < si) or (sc == "L" and si < ti):
                return False
        return True


class Solution2:
    def canChange(self, start: str, target: str) -> bool:
        ls = len(start)
        i = j = 0
        while True:
            while i < ls and start[i] == "_":
                i += 1
            while j < ls and target[j] == "_":
                j += 1
            if i == ls or j == ls:
                return i == j
            if start[i] != target[j]:
                return False
            elif start[i] == "R":
                if j < i:
                    return False
            elif i < j:
                return False
            i += 1
            j += 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canChange"] * 4,
            "kwargs": [
                dict(start="_L__R__R_", target="L______RR"),
                dict(start="R_L_", target="__LR"),
                dict(start="_R", target="R_"),
                dict(start="_L__R__R_L", target="L______RR_"),
            ],
            "expected": [True, False, False, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
