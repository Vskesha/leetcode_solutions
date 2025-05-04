import unittest
from functools import wraps
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def doubleIt(self, head: Optional[List]) -> Optional[List]:
            head = self.arr2linkedlist(head)
            res = self.original.doubleIt(head)
            return self.linkedlist2arr(res)

        def arr2linkedlist(self, arr: Optional[List]) -> Optional[ListNode]:
            head = None
            for n in reversed(arr):
                head = ListNode(val=n, next=head)
            return head

        def linkedlist2arr(self, head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


@sol_decorator
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev = dummy
        while head:
            ad, head.val = divmod(head.val * 2, 10)
            prev.val += ad
            prev = head
            head = head.next

        return dummy if dummy.val else dummy.next

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["doubleIt"] * 2,
            "kwargs": [
                dict(head=[1, 8, 9]),
                dict(head=[9, 9, 9]),
            ],
            "expected": [[3, 7, 8], [1, 9, 9, 8]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_double_it():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.doubleIt(head=[1, 8, 9]) == [3, 7, 8]
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.doubleIt(head=[9, 9, 9]) == [1, 9, 9, 8]
#     print("OK")


# if __name__ == "__main__":
#     test_double_it()
