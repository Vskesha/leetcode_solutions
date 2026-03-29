import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = [0] * n
        curr = 1

        for i in range(n):
            if not ans[i]:
                if curr > 26:
                    return ""
                ans[i] = curr
                curr += 1
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        ans[j] = ans[i]
            lcp[i].append(0)
        lcp.append([0] * (n + 1))

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (ans[i] != ans[j] and lcp[i][j]) or (
                    ans[i] == ans[j] and lcp[i][j] != lcp[i + 1][j + 1] + 1
                ):
                    return ""

        return "".join(chr(96 + val) for val in ans)


class Solution2:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = [0] * n
        curr = 1

        for i in range(n):
            if not ans[i]:
                if curr > 26:
                    return ""
                ans[i] = curr
                curr += 1
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        ans[j] = ans[i]
            lcp[i].append(0)
        lcp.append([0] * (n + 1))

        if any(
            (ans[i] != ans[j] and lcp[i][j])
            or (ans[i] == ans[j] and lcp[i][j] != lcp[i + 1][j + 1] + 1)
            for i in range(n - 1, -1, -1)
            for j in range(n - 1, -1, -1)
        ):
            return ""

        return "".join(chr(96 + val) for val in ans)


class Solution3:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = [0] * n
        ans[0] = 1
        mx = 1
        mxi = 1

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        for i in range(1, n):
            for j in range(i):
                if lcp[i][j] != lcp[j][i]:
                    return ""

                if not lcp[i][j]:
                    continue

                if i + lcp[i][j] > n:
                    return ""

                mxi = max(mxi, i)
                for k in range(mxi, i + lcp[i][j]):
                    ans[k] = ans[j - i + k]
                mxi = max(mxi, i + lcp[i][j])

            if ans[i] == 0:
                mx += 1
                if mx > 26:
                    return ""
                ans[i] = mx
                mxi = i + 1

        for j in range(n - 1, -1, -1):
            if lcp[n - 1][j] != int(ans[n - 1] == ans[j]):
                return ""
        for i in range(n - 2, -1, -1):
            if lcp[i][n - 1] != int(ans[i] == ans[n - 1]):
                return ""
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if ans[i] == ans[j]:
                    if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                        return ""
                elif lcp[i][j]:
                    return ""

        return "".join(chr(96 + n) for n in ans)


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findTheString"] * 3,
            "kwargs": [
                dict(
                    lcp=[
                        [4, 0, 2, 0],
                        [0, 3, 0, 1],
                        [2, 0, 2, 0],
                        [0, 1, 0, 1],
                    ]
                ),
                dict(
                    lcp=[
                        [4, 3, 2, 1],
                        [3, 3, 2, 1],
                        [2, 2, 2, 1],
                        [1, 1, 1, 1],
                    ]
                ),
                dict(
                    lcp=[
                        [4, 3, 2, 1],
                        [3, 3, 2, 1],
                        [2, 2, 2, 1],
                        [1, 1, 1, 3],
                    ]
                ),
            ],
            "expected": ["abab", "aaaa", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()
