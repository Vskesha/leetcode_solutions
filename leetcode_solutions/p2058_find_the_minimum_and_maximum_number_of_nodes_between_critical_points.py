import unittest
from itertools import pairwise
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals = []
        i = 0
        prev = head.val
        head = head.next

        while head.next:
            nxt = head.next
            if (prev < head.val > nxt.val) or (prev > head.val < nxt.val):
                criticals.append(i)
            prev = head.val
            head = nxt
            i += 1

        if len(criticals) < 2:
            return [-1, -1]

        min_dist = min(b - a for a, b in pairwise(criticals))
        max_dist = criticals[-1] - criticals[0]
        return [min_dist, max_dist]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def array_to_list(self, head: List[int]) -> Optional[ListNode]:
        linked_list = None
        for val in reversed(head):
            linked_list = ListNode(val=val, next=linked_list)
        return linked_list

    def test_nodes_between_critical_points_1(self):
        print("Test nodesBetweenCriticalPoints 1... ", end="")
        self.assertListEqual(
            self.sol.nodesBetweenCriticalPoints(self.array_to_list(head=[3, 1])),
            [-1, -1],
        )
        print("OK")

    def test_nodes_between_critical_points_2(self):
        print("Test nodesBetweenCriticalPoints 2... ", end="")
        self.assertListEqual(
            self.sol.nodesBetweenCriticalPoints(
                self.array_to_list(head=[5, 3, 1, 2, 5, 1, 2])
            ),
            [1, 3],
        )
        print("OK")

    def test_nodes_between_critical_points_3(self):
        print("Test nodesBetweenCriticalPoints 3... ", end="")
        self.assertListEqual(
            self.sol.nodesBetweenCriticalPoints(
                self.array_to_list(head=[1, 3, 2, 2, 3, 2, 2, 2, 7])
            ),
            [3, 3],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
