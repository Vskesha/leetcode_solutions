import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        d = iter(range(1, 10))
        stack = []
        pattern += "I"
        ans = [0] * len(pattern)

        for i, op in enumerate(pattern):
            if op == "D":
                stack.append(i)
            else:
                ans[i] = next(d)
                while stack:
                    ans[stack.pop()] = next(d)

        return "".join(map(str, ans))


class Solution2:
    def smallestNumber(self, pattern: str) -> str:
        def dfs(i) -> bool:
            if i == lp:
                return True

            if pattern[i] == "I":
                rng = range(seq[-1] + 1, 10)
            else:
                rng = range(1, seq[-1])

            for n in rng:
                if taken[n]:
                    continue
                seq.append(n)
                taken[n] = True
                if dfs(i + 1):
                    return True
                taken[n] = False
                seq.pop()

            return False

        taken = [False] * 10
        seq = []
        lp = len(pattern)

        for n in range(1, 10):
            seq.append(n)
            taken[n] = True
            if dfs(0):
                break
            taken[n] = False
            seq.pop()

        return "".join(map(str, seq))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestNumber"] * 2,
            "kwargs": [
                dict(pattern="IIIDIDDD"),
                dict(pattern="DDD"),
            ],
            "expected": ["123549876", "4321"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
