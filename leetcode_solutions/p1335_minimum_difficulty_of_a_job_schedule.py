from functools import cache
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = list(accumulate(jobDifficulty, func=max))
        for day in range(1, d):
            stack = []
            curr = [inf] * n
            for i in range(day, n):
                curr[i] = dp[i - 1] + jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    curr[i] = min(
                        curr[i], curr[j] + jobDifficulty[i] - jobDifficulty[j]
                    )
                if stack:
                    curr[i] = min(curr[i], curr[stack[-1]])
                stack.append(i)
            dp = curr
        return dp[-1]


class Solution1:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        prev = [float("inf")] * n
        curr = [float("inf")] * n
        for day in range(d):
            stack = []
            for i in range(day, n):
                if i == 0:
                    curr[i] = jobDifficulty[0]
                else:
                    curr[i] = prev[i - 1] + jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    curr[i] = min(
                        curr[i], curr[j] + jobDifficulty[i] - jobDifficulty[j]
                    )
                if stack:
                    curr[i] = min(curr[i], curr[stack[-1]])
                stack.append(i)
            prev, curr = curr, prev
        return prev[-1]


class Solution2:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ljd = len(jobDifficulty)
        if ljd < d:
            return -1

        dp = list(accumulate(jobDifficulty, func=max))

        for di in range(1, d):
            ndp = [inf] * ljd
            for i in range(di, ljd):
                mx = 0
                for j in range(i, di - 1, -1):  # di, i + 1
                    mx = max(mx, jobDifficulty[j])
                    ndp[i] = min(ndp[i], dp[j - 1] + mx)
            dp = ndp
        return dp[-1]


class Solution3:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ljd = len(jobDifficulty)
        if ljd < d:
            return -1

        @cache
        def dp(i, d) -> int:
            if d == 1:
                return max(jobDifficulty[:i])
            mx = 0
            ans = inf
            d -= 1
            for j in range(i - 1, d - 1, -1):
                mx = max(mx, jobDifficulty[j])
                ans = min(ans, dp(j, d) + mx)
            return ans

        return dp(ljd, d)


class Solution4:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ljd = len(jobDifficulty)
        if ljd < d:
            return -1

        @cache
        def dp(i, d) -> int:
            if d == 1:
                return max(jobDifficulty[:i])
            d -= 1
            return min(dp(j, d) + max(jobDifficulty[j:i]) for j in range(d, i))

        return dp(ljd, d)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
    print("OK")

    print("Test 2... ", end="")
    assert sol.minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1
    print("OK")

    print("Test 3... ", end="")
    assert sol.minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3
    print("OK")

    print("Test 4... ", end="")
    assert sol.minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3) == 15
    print("OK")


if __name__ == "__main__":
    test()
