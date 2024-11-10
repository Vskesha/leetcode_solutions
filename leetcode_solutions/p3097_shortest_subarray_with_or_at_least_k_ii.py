import unittest
from collections import Counter
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ors = {}
        ans = inf

        for i, n in enumerate(nums):
            ors = {or_ | n: pi for or_, pi in ors.items()}
            ors[n] = i
            for or_, pi in ors.items():
                if or_ >= k:
                    ans = min(ans, i - pi + 1)

        return ans if ans < inf else -1


class Solution2:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if not k:
            return 1
        ln = len(nums)
        sti = eni = 0
        bits = Counter()
        ans = ln + 1

        def total(bits):
            ans = sum(pow(2, k) for k, v in bits.items() if v)
            return ans

        while eni < ln:
            while eni < ln and total(bits) < k:
                for i, b in enumerate(bin(nums[eni])[::-1]):
                    if b == "1":
                        bits[i] += 1
                eni += 1

            while total(bits) >= k:
                ans = min(ans, eni - sti)
                for i, b in enumerate(bin(nums[sti])[::-1]):
                    if b == "1":
                        bits[i] -= 1
                sti += 1

        return -1 if ans > ln else ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumSubarrayLength"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3], k=2),
                dict(nums=[2, 1, 8], k=10),
                dict(nums=[1, 2], k=0),
            ],
            "expected": [1, 3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
