import math
import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ls = len(s)
        ans = list(map(int, s))
        digits = tuple(int(d) for d in s * 2)

        shifts = [0] * 10
        for digit in range(10):
            values = {(digit + a * i) % 10 for i in range(10)}
            shifts[digit] = digit - min(values)

        step = math.gcd(ls, b)
        for i in range(0, ls, step):
            diffs = [
                shifts[digits[i]] * (step % 2),
                shifts[digits[i + 1]]
            ]
            for j in range(i, i + ls):
                digit = (digits[j] - diffs[(j - i) % 2]) % 10
                if digit != ans[j - i]:
                    if digit < ans[j - i]:
                        ans = [
                            (digits[j] - diffs[(j - i) % 2]) % 10
                            for j in range(i, i + ls)
                        ]
                    break

        ans = "".join(map(str, ans))
        return ans


class Solution2:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ls = len(s)
        ans = list(map(int, s))
        digits = tuple(int(d) for d in s * 2)

        shifts = [0] * 10
        for digit in range(10):
            values = {(digit + a * i) % 10 for i in range(10)}
            shifts[digit] = digit - min(values)

        def get_ans(i, diffs):
            answer = []
            for j in range(i, i + ls):
                digit = (digits[j] - diffs[(j - i) % 2]) % 10
                answer.append(digit)
            return answer

        step = math.gcd(ls, b)
        for i in range(0, ls, step):
            diffs = [
                shifts[digits[i]] * (step % 2),
                shifts[digits[i + 1]]
            ]
            for j in range(i, i + ls):
                digit = (digits[j] - diffs[(j - i) % 2]) % 10
                if digit != ans[j - i]:
                    if digit < ans[j - i]:
                        ans = get_ans(i, diffs)
                    break

        ans = "".join(map(str, ans))
        return ans

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findLexSmallestString"] * 5,
            "kwargs": [
                dict(s = "863376891476", a = 4, b = 9),
                dict(s = "43987654", a = 7, b = 3),
                dict(s = "5525", a = 9, b = 2),
                dict(s = "74", a = 5, b = 1),
                dict(s = "0011", a = 4, b = 2),
            ],
            "expected": ["005790033890", "00553311", "2050", "24", "0011"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
