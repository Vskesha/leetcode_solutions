import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val

    def __str__(self):
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
        return str(res)


class SolutionDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        self.original_addTwoNumbers = instance.addTwoNumbers
        instance.addTwoNumbers = self.addTwoNumbers
        return instance

    def addTwoNumbers(self, l1: List, l2: List) -> List:
        l1 = self.arr_to_linked_list(l1)
        l2 = self.arr_to_linked_list(l2)
        result = self.original_addTwoNumbers(l1, l2)  # noqa
        return self.linked_list_to_arr(result)  # noqa

    @staticmethod
    def arr_to_linked_list(arr: List) -> Optional[ListNode]:
        head = None
        for n in reversed(arr):
            head = ListNode(n, head)
        return head

    @staticmethod
    def linked_list_to_arr(head: Optional[ListNode]) -> List:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr


@SolutionDecorator
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = curr = ListNode()
        over = 0
        while l1 or l2 or over:
            s = over
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            curr.next = ListNode()
            curr = curr.next
            over, curr.val = divmod(s, 10)
        return first.next


@SolutionDecorator
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode()
        add = 0

        while add or l1 or l2:
            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0
            add, val = divmod(a1 + a2 + add, 10)
            curr.next = ListNode(val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_add_two_numbers1(self):
        print("Test addTwoNumbers 1 ... ", end="")
        self.assertListEqual(
            self.sol.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]), [7, 0, 8]
        )
        print("OK")

    def test_add_two_numbers2(self):
        print("Test addTwoNumbers 2 ... ", end="")
        self.assertListEqual(self.sol.addTwoNumbers(l1=[0], l2=[0]), [0])
        print("OK")

    def test_add_two_numbers3(self):
        print("Test addTwoNumbers 3 ... ", end="")
        self.assertListEqual(
            self.sol.addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]),
            [8, 9, 9, 9, 0, 0, 0, 1],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
