import unittest
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        res = []
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        if k > size:
            while curr:
                res.append(curr)
                curr.next, curr = None, curr.next
            res += [None] * (k - size)
        else:
            num = size // k - 1
            fst = size % k
            for i in range(k):
                res.append(curr)
                for _ in range(num + (i < fst)):
                    curr = curr.next
                curr.next, curr = None, curr.next
        return res


class Solution2:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        res = []
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        if k > size:
            while curr:
                res.append(curr)
                curr.next, curr = None, curr.next
            res += [None] * (k - size)
        else:
            for i in range(k, 0, -1):
                res.append(curr)
                count = (size - 1) // i + 1
                size -= count
                for _ in range(count - 1):
                    curr = curr.next
                curr.next, curr = None, curr.next
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
        head = None
        for v in reversed(arr):
            head = ListNode(v, head)
        return head

    exp1 = []
    for arr in [[1], [2], [3], [], []]:
        exp1.append(array_to_linked_list(arr))
    exp2 = []
    for arr in [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]:
        exp2.append(array_to_linked_list(arr))
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["splitListToParts"] * 2,
            "kwargs": [
                dict(head=array_to_linked_list([1, 2, 3]), k=5),
                dict(head=array_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), k=3),
            ],
            "expected": [exp1, exp2],
            "assert_methods": ["assertListOfLinkedListsEqual"] * 2,
        },
    ]

    def assertListOfLinkedListsEqual(self, lists1: List[ListNode], lists2: List[ListNode]):
        self.assertEqual(len(lists1), len(lists2))
        for head1, head2 in zip(lists1, lists2):
            self.assertLinkedListEqual(head1, head2)

    def assertLinkedListEqual(self, head1: ListNode, head2: ListNode):
        while head1 and head2:
            self.assertEqual(head1.val, head2.val)
            head1 = head1.next
            head2 = head2.next
        self.assertIsNone(head1)
        self.assertIsNone(head2)

if __name__ == "__main__":
    unittest.main()
