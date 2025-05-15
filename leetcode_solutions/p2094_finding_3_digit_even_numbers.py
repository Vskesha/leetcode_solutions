import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ds = sorted(cnt)
        first = [d for d in ds if d]
        even = [d for d in ds if d % 2 == 0]
        ans = []

        for a in first:
            cnt[a] -= 1
            for b in ds:
                if cnt[b]:
                    cnt[b] -= 1
                    for c in even:
                        if cnt[c]:
                            ans.append(a * 100 + b * 10 + c)
                    cnt[b] += 1
            cnt[a] += 1

        return ans


class Solution1:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(map(str, digits))
        return [n for n in range(100, 1000, 2) if Counter(str(n)) <= cnt]


class Solution2:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()

        for i, d1 in enumerate(digits):
            if d1 == 0:
                continue
            d1 *= 100
            for j, d2 in enumerate(digits):
                if j == i:
                    continue
                d2 *= 10
                for k, d3 in enumerate(digits):
                    if d3 % 2 or k == i or k == j:
                        continue
                    ans.add(d1 + d2 + d3)

        return sorted(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findEvenNumbers"] * 3,
            "kwargs": [
                dict(digits=[2, 1, 3, 0]),
                dict(digits=[2, 2, 8, 8, 2]),
                dict(digits=[3, 7, 5]),
            ],
            "expected": [
                [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
                [222, 228, 282, 288, 822, 828, 882],
                [],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
