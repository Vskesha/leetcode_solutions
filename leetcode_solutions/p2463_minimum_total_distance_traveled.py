import unittest
from collections import deque
from functools import cache
from itertools import accumulate
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.sort()
        factory.sort()
        thla = list(accumulate((h for _, h in factory), initial=0))

        @cache
        def dp(rl, fi, thl) -> int:
            if rl == 0:
                return 0
            if thl <= thla[fi]:
                return dp(rl, fi - 1, thla[fi])
            rp = robot[rl - 1]
            fp = factory[fi][0]
            if rp >= fp:
                return dp(rl - 1, fi, thl - 1) + rp - fp
            if fi == 0:
                return sum(fp - rp for rp in robot[:rl])
            if thla[fi] < rl:
                return dp(rl - 1, fi, thl - 1) + fp - rp
            return min(
                dp(rl - 1, fi, thl - 1) + fp - rp, dp(rl, fi - 1, thla[fi])
            )

        ans = dp(len(robot), len(factory) - 1, thla[-1])
        return ans


class Solution1:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.sort()
        factory.sort()
        factory = [p for p, h in factory for _ in range(h)]
        lf, lr = len(factory) + 1, len(robot) + 1
        dp = [0] * lf

        for i in range(1, lr):
            ndp = [inf] * lf
            for j in range(i, lf):
                ndp[j] = min(
                    ndp[j - 1], dp[j - 1] + abs(robot[i - 1] - factory[j - 1])
                )
            dp = ndp

        return dp[-1]


class Solution2:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.sort()
        factory.sort()
        factory = [p for p, h in factory for _ in range(h)]

        @cache
        def dp(rl, fl) -> int:
            if not rl:
                return 0
            if not fl:
                return inf
            return min(
                dp(rl, fl - 1),
                dp(rl - 1, fl - 1) + abs(robot[rl - 1] - factory[fl - 1]),
            )

        return dp(len(robot), len(factory))


class Solution3:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][-1] = inf
        for j in range(n - 1, -1, -1):
            prefix = 0
            qq = deque([(m, 0)])
            for i in range(m - 1, -1, -1):
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i + factory[j][1]:
                    qq.popleft()
                while qq and qq[-1][1] >= dp[i][j + 1] - prefix:
                    qq.pop()
                qq.append((i, dp[i][j + 1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumTotalDistance"] * 2,
            "kwargs": [
                dict(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]),
                dict(robot=[1, -1], factory=[[-2, 1], [2, 1]]),
            ],
            "expected": [4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
