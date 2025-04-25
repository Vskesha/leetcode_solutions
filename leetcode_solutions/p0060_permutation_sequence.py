import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(d) for d in range(1, n + 1)]
        ans = []
        p = 1
        for m in range(1, n):
            p *= m

        for m in range(n - 1, 0, -1):
            i = (k - 1) // p
            ans.append(arr.pop(i))
            k %= p
            p //= m

        ans.append(arr.pop())
        res = "".join(ans)
        return res


class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(d) for d in range(1, n + 1)]
        ans = ""
        p = 1

        for m in range(1, n):
            p *= m

        for m in range(n - 1, 0, -1):
            i = (k - 1) // p
            ans += arr.pop(i)
            k %= p
            p //= m

        return ans + arr.pop()


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getPermutation"] * 3,
            "kwargs": [
                dict(n=3, k=3),
                dict(n=4, k=9),
                dict(n=3, k=1),
            ],
            "expected": ["213", "2314", "123"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
