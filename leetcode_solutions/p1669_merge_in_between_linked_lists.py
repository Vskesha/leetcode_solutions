# Definition for singly-linked list.
from functools import wraps
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def mergeInBetween(
            self, list1: List, a: int, b: int, list2: List
        ) -> List:
            list1 = self.arr2linkedlist(list1)
            list2 = self.arr2linkedlist(list2)
            result_linked_list = self.original.mergeInBetween(
                list1, a, b, list2
            )
            return self.linkedlist2arr(result_linked_list)

        def arr2linkedlist(self, arr: Optional[List]) -> Optional[ListNode]:
            head = None
            for val in reversed(arr):
                head = ListNode(val, head)
            return head

        def linkedlist2arr(self, head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        a1 = list1
        for _ in range(a - 1):
            a1 = a1.next
        b1 = a1
        for _ in range(b - a + 2):
            b1 = b1.next
        a1.next = list2
        while a1.next:
            a1 = a1.next
        a1.next = b1
        return list1


def test_merge_in_between():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.mergeInBetween(
        list1=[10, 1, 13, 6, 9, 5], a=3, b=4, list2=[1000000, 1000001, 1000002]
    ) == [10, 1, 13, 1000000, 1000001, 1000002, 5]
    print("OK")

    print("Test 2... ", end="")
    assert sol.mergeInBetween(
        list1=[0, 1, 2, 3, 4, 5, 6],
        a=2,
        b=5,
        list2=[1000000, 1000001, 1000002, 1000003, 1000004],
    ) == [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
    print("OK")


if __name__ == "__main__":
    test_merge_in_between()
