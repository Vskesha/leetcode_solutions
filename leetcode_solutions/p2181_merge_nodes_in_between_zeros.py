import unittest
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast:
            sm = 0
            while fast.val:
                sm += fast.val
                fast = fast.next
            fast = fast.next
            slow.next.val = sm
            slow = slow.next
        slow.next = fast
        return head.next


class Solution2:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head.next
        while slow:
            fast = fast.next
            if fast.val:
                slow.val += fast.val
            else:
                slow.next = fast = fast.next
                slow = fast
        return head.next


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def array_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val=val, next=head)
        return head

    def assertLinkedListEqual(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        while l1 and l2:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        self.assertIsNone(l1)
        self.assertIsNone(l2)

    def test_merge_nodes_1(self):
        print("Test mergeNodes 1 ... ", end="")
        head = [0, 3, 1, 0, 4, 5, 2, 0]
        output = [4, 11]
        self.assertLinkedListEqual(
            self.sol.mergeNodes(self.array_to_linked_list(head)),
            self.array_to_linked_list(output),
        )
        print("OK")

    def test_merge_nodes_2(self):
        print("Test mergeNodes 2 ... ", end="")
        head = [0, 1, 0, 3, 0, 2, 2, 0]
        output = [1, 3, 4]
        self.assertLinkedListEqual(
            self.sol.mergeNodes(self.array_to_linked_list(head)),
            self.array_to_linked_list(output),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
