import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def calculate(x):
            return 0 if x < 0 else x * (x - 1) // 2

        return (
            calculate(n + 2)
            - 3 * calculate(n + 1 - limit)
            + 3 * calculate(n - 2 * limit)
            - calculate(n - 3 * limit - 1)
        )


class Solution2:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        mv = min(n + 1, limit + 1, max(0, n - limit))
        for n1 in range(max(0, n - 2 * limit), mv):
            ans += 2 * limit - n + n1 + 1
        for n1 in range(mv, min(n, limit) + 1):
            ans += n - n1 + 1
        return ans


class Solution3:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        mv = min(n + 1, limit + 1, max(0, n - limit))
        return sum(
            2 * limit - n + n1 + 1 for n1 in range(max(0, n - 2 * limit), mv)
        ) + sum(n - n1 + 1 for n1 in range(mv, min(n, limit) + 1))


class Solution4:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0

        for i in range(max(0, n - limit * 2), min(limit, n) + 1):
            rem = n - i
            min_qty = max(0, rem - limit)
            max_qty = min(rem, limit)
            ans += max_qty - min_qty + 1

        return ans


class Solution5:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(
            min(n - n1, limit) - max(0, n - n1 - limit) + 1
            for n1 in range(max(0, n - 2 * limit), min(n, limit) + 1)
        )


class Solution6:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for n1 in range(max(0, n - 2 * limit), min(n, limit) + 1):
            ans += min(n - n1, limit) - max(0, n - n1 - limit) + 1
        return ans


class Solution7:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for n1 in range(max(0, n - 2 * limit), min(n, limit) + 1):
            lf = n - n1
            n2max = min(lf, limit)
            n2min = max(0, lf - limit)
            total = n2max - n2min + 1
            ans += total
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["distributeCandies"] * 2,
            "kwargs": [
                dict(n=5, limit=2),
                dict(n=3, limit=3),
            ],
            "expected": [3, 10],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1 ... ', end='')
#     assert sol.distributeCandies(n=5, limit=2) == 3
#     print('OK')
#
#     print('Test 1 ... ', end='')
#     assert sol.distributeCandies(n=3, limit=3) == 10
#     print('OK')


# if __name__ == '__main__':
#     test()
