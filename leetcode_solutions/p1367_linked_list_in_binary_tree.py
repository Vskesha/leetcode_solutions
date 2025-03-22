import unittest
from collections import deque
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.include(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def include(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.include(head.next, root.left) or self.include(head.next, root.right)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None
        vals = iter(arr)
        root = TreeNode(next(vals))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isSubPath"] * 3,
            "kwargs": [
                dict(
                    head=array_to_linked_list([4, 2, 8]),
                    root=array_to_tree(
                        [
                            1,
                            4,
                            4,
                            null,
                            2,
                            2,
                            null,
                            1,
                            null,
                            6,
                            8,
                            null,
                            null,
                            null,
                            null,
                            1,
                            3,
                        ]
                    ),
                ),
                dict(
                    head=array_to_linked_list([1, 4, 2, 6]),
                    root=array_to_tree(
                        [
                            1,
                            4,
                            4,
                            null,
                            2,
                            2,
                            null,
                            1,
                            null,
                            6,
                            8,
                            null,
                            null,
                            null,
                            null,
                            1,
                            3,
                        ]
                    ),
                ),
                dict(
                    head=array_to_linked_list([1, 4, 2, 6, 8]),
                    root=array_to_tree(
                        [
                            1,
                            4,
                            4,
                            null,
                            2,
                            2,
                            null,
                            1,
                            null,
                            6,
                            8,
                            null,
                            null,
                            null,
                            null,
                            1,
                            3,
                        ]
                    ),
                ),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
