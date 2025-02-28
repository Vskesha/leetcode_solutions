import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = list(map(int, reversed(num1)))
        n2 = list(map(int, reversed(num2)))
        ans = [0] * (len(num1) + len(num2))

        for i1, d1 in enumerate(n1):
            for i2, d2 in enumerate(n2):
                ans[i1 + i2] += d1 * d2
        for ai in range(len(ans) - 1):
            ans[ai + 1] += ans[ai] // 10
            ans[ai] %= 10

        ans = "".join(str(d) for d in reversed(ans)).lstrip("0")
        return ans


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = list(map(int, reversed(num1)))
        n2 = list(map(int, reversed(num2)))

        ans = [0] * (len(num1) + len(num2))
        for i2, d2 in enumerate(n2):
            for i1, d1 in enumerate(n1):
                ci = i1 + i2
                ans[ci] += d1 * d2
                while ans[ci] > 9:
                    ad, ans[ci] = divmod(ans[ci], 10)
                    ci += 1
                    ans[ci] += ad

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        ans = "".join(str(d) for d in reversed(ans))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["multiply"] * 2,
            "kwargs": [
                dict(num1="2", num2="3"),
                dict(num1="123", num2="456"),
            ],
            "expected": ["6", "56088"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
