import unittest
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not (self or other):
            return True
        if not (self and other):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(k - 1):
            fast = fast.next

        kth = fast
        fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.val, kth.val = kth.val, slow.val

        return head


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def array_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        if not arr:
            return None

        head = None
        for val in reversed(arr):
            head = ListNode(val=val, next=head)

        return head

    def test_swap_nodes_1(self):
        print("Test swapNodes 1... ", end="")
        self.assertEqual(
            self.sol.swapNodes(head=self.array_to_linked_list([1, 2, 3, 4, 5]), k=2),
            self.array_to_linked_list([1, 4, 3, 2, 5]),
        )
        print("OK")

    def test_swap_nodes_2(self):
        print("Test swapNodes 2... ", end="")
        self.assertEqual(
            self.sol.swapNodes(
                head=self.array_to_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), k=5
            ),
            self.array_to_linked_list([7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
