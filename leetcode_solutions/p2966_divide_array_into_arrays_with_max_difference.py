import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        ln = len(nums)

        for i in range(0, ln, 3):
            if nums[i + 2] - nums[i] > k:
                return []

        return [nums[i : i + 3] for i in range(0, ln, 3)]


class Solution2:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        ans = []
        for i in range(0, ln, 3):
            if nums[i] + k >= nums[i + 2]:
                ans.append(nums[i : i + 3])
            else:
                return []
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["divideArray"] * 3,
            "kwargs": [
                dict(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2),
                dict(nums=[2, 4, 2, 2, 5, 2], k=2),
                dict(
                    nums=[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11],
                    k=14,
                ),
            ],
            "expected": [
                ([[1, 1, 3], [3, 4, 5], [7, 8, 9]], 2),
                ([], 2),
                (
                    [
                        [2, 2, 12],
                        [4, 8, 5],
                        [5, 9, 7],
                        [7, 8, 5],
                        [5, 9, 10],
                        [11, 12, 2],
                    ],
                    14,
                ),
            ],
            "assert_methods": ["assertMaxDiffIsLessEqual"] * 3,
        },
    ]

    def assertMaxDiffIsLessEqual(self, result: List[List[int]], expected: int) -> None:
        expected_list, expected_diff = expected
        self.assertEqual(len(result), len(expected_list))
        for res, exp in zip(result, expected_list):
            self.assertEqual(len(res), 3)
            self.assertEqual(len(exp), 3)
            self.assertLessEqual(max(res) - min(res), expected_diff)


if __name__ == "__main__":
    unittest.main()

# def test_diff(arr: List[List[int]], k: int) -> bool:
#     for sarr in arr:
#         if max(sarr) - min(sarr) > k:
#             return False
#     return True


# def test():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert test_diff(sol.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2), k=2)
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert test_diff(sol.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3), k=3)
#     print("OK")


# if __name__ == "__main__":
#     test()
