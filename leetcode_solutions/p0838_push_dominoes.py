import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = []
        prev = "L"
        dots = 0

        for d in dominoes + "R":
            if d == ".":
                dots += 1
                continue

            if d == "R":
                if prev == "R":
                    ans.append("R" * (dots + 1))
                else:
                    ans.append("." * dots)
            elif prev == "L":
                ans.append("L" * (dots + 1))
            else:
                d2 = dots // 2 + 1
                mid = "." * (dots % 2)
                ans.append("R" * d2 + mid + "L" * d2)

            dots = 0
            prev = d

        return "".join(ans)


class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        ans = []
        prev = "L"
        dots = 0

        for d in dominoes:
            if d == ".":
                dots += 1
                continue

            if d == "L":
                if prev == "L":
                    ans.append("L" * (dots + 1))
                else:
                    dots2 = dots // 2 + 1
                    ans.append("R" * dots2 + "." * (dots % 2) + "L" * dots2)
            elif prev == "R":
                ans.append("R" * (dots + 1))
            else:
                ans.append("." * dots)

            dots = 0
            prev = d

        if prev == "R":
            ans.append("R" * (dots + 1))
        else:
            ans.append("." * dots)

        ans = "".join(ans)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["pushDominoes"] * 2,
            "kwargs": [
                dict(dominoes="RR.L"),
                dict(dominoes=".L.R...LR..L.."),
            ],
            "expected": ["RR.L", "LL.RR.LLRRLL.."],
        },
    ]


if __name__ == "__main__":
    unittest.main()
