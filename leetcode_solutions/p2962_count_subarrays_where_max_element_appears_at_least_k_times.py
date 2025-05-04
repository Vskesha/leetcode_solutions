import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx, ln = max(nums), len(nums)
        ids = [i for i in range(ln) if nums[i] == mx]
        li = len(ids) + 1
        if li <= k:
            return 0
        ids.append(ln)
        ans = 0
        for i, j in zip(range(li), range(k, li)):
            ans += (ids[i] + 1) * (ids[j] - ids[j - 1])
        return ans
class Solution2:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        mn = max(nums)
        ln = len(nums)
        inds = [i for i in range(ln) if nums[i] == mn]
        inds.append(ln)
        for i in range(k, len(inds)):
            ans += (inds[i] - inds[i - 1]) * (inds[i - k] + 1)
        return ans


class Solution3:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        mn = max(nums)
        inds = [i for i, n in enumerate(nums) if n == mn]
        li = len(inds)
        if li < k:
            return 0
        inds.append(len(nums))
        for si, ei in zip(range(li), range(k - 1, li)):
            ans += (inds[si] + 1) * (inds[ei + 1] - inds[ei])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubarrays"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 2, 3, 3], k=2),
                dict(nums=[1, 4, 2, 1], k=3),
            ],
            "expected": [6, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()


# def test_count_subarrays():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.countSubarrays(nums=[1, 3, 2, 3, 3], k=2) == 6
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.countSubarrays(nums=[1, 4, 2, 1], k=3) == 0
#     print("OK")

# if __name__ == "__main__":
#     test_count_subarrays()
