import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}
        free_indices = SortedList()
        ans = [0] * len(rains)

        for i, lake in enumerate(rains):
            if lake:
                ans[i] = -1
                if lake in full_lakes:
                    idx = full_lakes[lake]
                    if not free_indices or idx > free_indices[-1]:
                        return []
                    free_idx = free_indices.bisect_left(idx)
                    ans[free_indices.pop(free_idx)] = lake
                full_lakes[lake] = i
            else:
                free_indices.add(i)
        for idx in free_indices:
            ans[idx] = 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["avoidFlood"] * 4,
            "kwargs": [
                dict(rains=[0, 1, 1]),
                dict(rains=[1, 2, 3, 4]),
                dict(rains=[1, 2, 0, 0, 2, 1]),
                dict(rains=[1, 2, 0, 1, 2]),
            ],
            "expected": [[], [-1, -1, -1, -1], [-1, -1, 2, 1, -1, -1], []],
            "assert_methods": ["assertListEqual"] * 4,
        },
    ]


if __name__ == "__main__":
    unittest.main()
