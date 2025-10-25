import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        ln1, ln2 = len(nums1), len(nums2)
        res = []

        while i < ln1 and j < ln2:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < ln1:
            res.append(nums1[i])
            i += 1
        while j < ln2:
            res.append(nums2[j])
            j += 1

        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["mergeArrays"] * 2,
            "kwargs": [
                dict(
                    nums1=[[1, 2], [2, 3], [4, 5]],
                    nums2=[[1, 4], [3, 2], [4, 1]],
                ),
                dict(nums1=[[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]]),
            ],
            "expected": [
                [[1, 6], [2, 3], [3, 2], [4, 6]],
                [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]],
            ],
            "assert_methods": ["assertSameIdValues"] * 2,
        },
    ]

    def assertSameIdValues(
        self, actual: List[List[int]], expected: List[List[int]]
    ) -> None:
        self.assertEqual(len(actual), len(expected))
        for act, exp in zip(actual, expected):
            self.assertListEqual(act, exp)


if __name__ == "__main__":
    unittest.main()
