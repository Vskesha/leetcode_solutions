import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def gen_sum():
            dp = [0]
            while True:
                ldp = len(dp)
                for i in range(1, 10):
                    for j in range(ldp):
                        dp.append(i + dp[j])
                        yield dp[-1]

        it = gen_sum()
        cnt = Counter(next(it) for _ in range(n))
        mv = max(cnt.values())
        return sum(v == mv for v in cnt.values())


class Solution2:
    def countLargestGroup(self, n: int) -> int:
        dp = [0]
        ldp = 1
        while ldp <= n:
            if len(dp) > n:
                break
            for i in range(1, 10):
                for j in range(ldp):
                    dp.append(i + dp[j])
            ldp = len(dp)

        cnt = Counter(dp[1 : n + 1])
        mv = max(cnt.values())
        return sum(v == mv for v in cnt.values())


class Solution3:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter(sum(int(d) for d in str(k)) for k in range(1, n + 1))
        ans = mv = 0
        for v in cnt.values():
            if v > mv:
                mv = v
                ans = 1
            elif v == mv:
                ans += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countLargestGroup"] * 2,
            "kwargs": [
                dict(n=13),
                dict(n=2),
            ],
            "expected": [4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
