import unittest
from bisect import bisect_right
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ts = ans = 0

        for i in range(1, n + 1):
            if i not in banned:
                ts += i
                if ts > maxSum:
                    break
                ans += 1

        return ans


class Solution2:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = sorted(set(banned))
        acc = list(accumulate(banned, initial=0))
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            i = bisect_right(banned, mid)
            cs = mid * (mid + 1) // 2 - acc[i]
            if cs > maxSum:
                right = mid - 1
            else:
                left = mid

        ans = right - bisect_right(banned, right)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxCount"] * 4,
            "kwargs": [
                dict(
                    banned=[
                        87,
                        193,
                        85,
                        55,
                        14,
                        69,
                        26,
                        133,
                        171,
                        180,
                        4,
                        8,
                        29,
                        121,
                        182,
                        78,
                        157,
                        53,
                        26,
                        7,
                        117,
                        138,
                        57,
                        167,
                        8,
                        103,
                        32,
                        110,
                        15,
                        190,
                        139,
                        16,
                        49,
                        138,
                        68,
                        69,
                        92,
                        89,
                        140,
                        149,
                        107,
                        104,
                        2,
                        135,
                        193,
                        87,
                        21,
                        194,
                        192,
                        9,
                        161,
                        188,
                        73,
                        84,
                        83,
                        31,
                        86,
                        33,
                        138,
                        63,
                        127,
                        73,
                        114,
                        32,
                        66,
                        64,
                        19,
                        175,
                        108,
                        80,
                        176,
                        52,
                        124,
                        94,
                        33,
                        55,
                        130,
                        147,
                        39,
                        76,
                        22,
                        112,
                        113,
                        136,
                        100,
                        134,
                        155,
                        40,
                        170,
                        144,
                        37,
                        43,
                        151,
                        137,
                        82,
                        127,
                        73,
                    ],
                    n=1079,
                    maxSum=87,
                ),
                dict(banned=[1, 6, 5], n=5, maxSum=6),
                dict(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1),
                dict(banned=[11], n=7, maxSum=50),
            ],
            "expected": [9, 2, 0, 7],
        },
    ]


if __name__ == "__main__":
    unittest.main()
