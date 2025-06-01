import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        seen1, seen2 = set(), set()
        edges.append(-1)

        while node1 not in seen1 and node2 not in seen2:
            seen1.add(node1)
            seen2.add(node2)
            if node1 in seen2:
                if node2 in seen1:
                    return min(node1, node2)
                return node1
            if node2 in seen1:
                return node2
            node1 = edges[node1]
            node2 = edges[node2]

        while node1 not in seen1:
            seen1.add(node1)
            if node1 in seen2:
                return node1
            node1 = edges[node1]

        while node2 not in seen2:
            seen2.add(node2)
            if node2 in seen1:
                return node2
            node2 = edges[node2]

        return -1


class Solution2:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        edges.append(-1)
        seen1, seen2 = set(), set()

        for _ in range(len(edges)):
            seen1.add(node1)
            seen2.add(node2)
            if node1 in seen2:
                if node2 in seen1:
                    return min(node1, node2)
                return node1
            if node2 in seen1:
                return node2
            node1 = edges[node1]
            node2 = edges[node2]

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["closestMeetingNode"] * 2,
            "kwargs": [
                dict(edges=[2, 2, 3, -1], node1=0, node2=1),
                dict(edges=[1, 2, -1], node1=0, node2=2),
            ],
            "expected": [2, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
