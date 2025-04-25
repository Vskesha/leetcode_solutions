import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0

        for i in range(max(0, n - limit * 2), min(limit, n) + 1):
            rem = n - i
            min_qty = max(0, rem - limit)
            max_qty = min(rem, limit)
            ans += max_qty - min_qty + 1

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
