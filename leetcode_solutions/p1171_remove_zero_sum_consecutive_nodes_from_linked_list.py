from functools import wraps
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def removeZeroSumSublists(self, head: Optional[List]) -> Optional[List]:
            head = self.arr2linkedlist(head)
            removed = self.original.removeZeroSumSublists(head)
            return self.linkedlist2arr(removed)

        @staticmethod
        def arr2linkedlist(arr: Optional[List]) -> Optional[ListNode]:
            head = None
            for val in reversed(arr):
                head = ListNode(val, head)
            return head

        @staticmethod
        def linkedlist2arr(head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sums = {0: dummy}
        total = 0

        while head:
            total += head.val
            sums[total] = head
            head = head.next

        head = dummy
        total = 0
        while head:
            total += head.val
            if sums[total] is not head:
                head.next = sums[total].next
            head = head.next

        return dummy.next


class Solution2:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tot = 0
        sums = {tot: dummy}

        while head:
            tot += head.val
            if tot in sums:
                prev = sums[tot]
                prev.next = head.next
                head = dummy.next
                tot = 0
                sums = {tot: dummy}
            else:
                sums[tot] = head
                head = head.next

        return dummy.next


def test_remove_zero_sum_sublists():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.removeZeroSumSublists(head=[1, 2, -3, 3, 1]) == [3, 1]
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeZeroSumSublists(head=[1, 2, 3, -3, 4]) == [1, 2, 4]
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeZeroSumSublists(head=[1, 2, 3, -3, -2]) == [1]
    print("OK")


if __name__ == "__main__":
    test_remove_zero_sum_sublists()
