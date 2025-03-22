import unittest
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} --> {self.next} "


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = prev = ListNode()
        i, dummy, end = 0, None, head
        while head:
            curr = head
            head = head.next
            curr.next = dummy
            dummy = curr
            i += 1
            if i == k:
                prev.next = curr
                prev = end
                i, dummy, end = 0, None, head
        while dummy:
            curr = dummy
            dummy = dummy.next
            curr.next = head
            head = curr
        prev.next = head
        return result.next


class Solution2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = result = ListNode()
        sub = []
        while head:
            sub.append(head)
            head = head.next
            if len(sub) == k:
                for node in reversed(sub):
                    prev.next = node
                    prev = node
                prev.next = head
                sub = []
        return result.next


class Solution3:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = []
        while head:
            result.append(head.val)
            head = head.next

        new_order = []
        for i in range(0, len(result), k):
            sub = result[i : i + k]
            new_order += reversed(sub) if len(sub) == k else sub

        nxt = None
        for val in reversed(new_order):
            node = ListNode(val, nxt)
            nxt = node

        return nxt


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = result = ListNode()
        prev.next = curr = head
        while True:
            values = []
            for _ in range(k):
                try:
                    values.append(curr.val)
                    curr = curr.next
                except AttributeError:
                    break
            else:
                for val in reversed(values):
                    node = ListNode(val)
                    prev.next = node
                    prev = node
                prev.next = curr
                continue
            break
        return result.next


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def array_to_linkedlist(self, arr: List) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    def assertEqualLinkedList(self, ll1: Optional[ListNode], ll2: Optional[ListNode]):
        while ll1 and ll2:
            self.assertEqual(ll1.val, ll2.val)
            ll1, ll2 = ll1.next, ll2.next
        self.assertIsNone(ll1)
        self.assertIsNone(ll2)

    def test_reverse_k_group_1(self):
        print("Test reverseKGroup 1... ", end="")
        self.assertEqualLinkedList(
            self.sol.reverseKGroup(head=self.array_to_linkedlist([1, 2, 3, 4, 5]), k=2),
            self.array_to_linkedlist([2, 1, 4, 3, 5]),
        )
        print("OK")

    def test_reverse_k_group_2(self):
        print("Test reverseKGroup 2... ", end="")
        self.assertEqualLinkedList(
            self.sol.reverseKGroup(head=self.array_to_linkedlist([1, 2, 3, 4, 5]), k=3),
            self.array_to_linkedlist([3, 2, 1, 4, 5]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
