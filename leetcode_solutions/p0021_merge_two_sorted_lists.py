import unittest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        curr.next = list1 if list1 else list2
        return dummy.next


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def arr_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val=val, next=head)
        return head

    def assert_is_sorted(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        prev = head.val
        head = head.next
        while head:
            self.assertLessEqual(prev, head.val)
            prev = head.val
            head = head.next

    def test_merge_two_lists_1(self):
        print("Test mergeTwoLists 1 ... ", end="")
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]
        list1 = self.arr_to_linked_list(list1)
        list2 = self.arr_to_linked_list(list2)
        self.assert_is_sorted(self.sol.mergeTwoLists(list1, list2))
        print("OK")

    def test_merge_two_lists_2(self):
        print("Test mergeTwoLists 2 ... ", end="")
        list1 = []
        list2 = []
        list1 = self.arr_to_linked_list(list1)
        list2 = self.arr_to_linked_list(list2)
        self.assert_is_sorted(self.sol.mergeTwoLists(list1, list2))
        print("OK")

    def test_merge_two_lists_3(self):
        print("Test mergeTwoLists 3 ... ", end="")
        list1 = []
        list2 = [0]
        list1 = self.arr_to_linked_list(list1)
        list2 = self.arr_to_linked_list(list2)
        self.assert_is_sorted(self.sol.mergeTwoLists(list1, list2))
        print("OK")


if __name__ == "__main__":
    unittest.main()
