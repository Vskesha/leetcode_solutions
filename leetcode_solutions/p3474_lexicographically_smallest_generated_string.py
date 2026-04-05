import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        # process the case of 'T'
        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    s[j], fixed[j] = c, True

        # process the case of 'F'
        for i, ch in enumerate(str1):
            if ch == "F":
                # check if there are already different characters
                if any(str2[j - i] != s[j] for j in range(i, i + m)):
                    continue

                # find the first modifiable position
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = "b"
                        break
                else:
                    return ""

        return "".join(s)


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["generateString"] * 3,
            "kwargs": [
                dict(str1="TFTF", str2="ab"),
                dict(str1="TFTF", str2="abc"),
                dict(str1="F", str2="d"),
            ],
            "expected": ["ababa", "", "a"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
