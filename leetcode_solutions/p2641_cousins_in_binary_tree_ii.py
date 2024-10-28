import unittest
from collections import deque
from typing import Optional, List

from leetcode_solutions._test_meta import TestMeta


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0

        row = [root]
        while True:
            nrow, sums = [], []
            for node in row:
                sums.append(0)
                if node.left:
                    nrow.append(node.left)
                    sums[-1] += node.left.val
                if node.right:
                    nrow.append(node.right)
                    sums[-1] += node.right.val
            if not nrow:
                break
            sm = sum(sums)
            for node, chs in zip(row, sums):
                chs = sm - chs
                if node.left:
                    node.left.val = chs
                if node.right:
                    node.right.val = chs
            row = nrow

        return root


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def arr_to_tree(arr: List[int]) -> Optional[TreeNode]:
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
            "class_methods": ["replaceValueInTree"] * 4,
            "kwargs": [
                dict(root=arr_to_tree([5, 4, 9, 1, 10, null, 7])),
                dict(root=arr_to_tree([3, 1, 2])),
                dict(root=arr_to_tree([33, 37, 42, null, null, null, 46])),
                dict(
                    root=arr_to_tree(
                        [
                            763,
                            111,
                            229,
                            null,
                            334,
                            145,
                            null,
                            null,
                            338,
                            674,
                            null,
                            513,
                            193,
                            366,
                            null,
                            365,
                            null,
                            600,
                            null,
                            null,
                            null,
                            null,
                            null,
                            65,
                            926,
                            null,
                            null,
                            null,
                            607,
                        ]
                    )
                ),
            ],
            "expected": [
                arr_to_tree([0, 0, 0, 7, 7, null, 11]),
                arr_to_tree([0, 0, 0]),
                arr_to_tree([0, 0, 0, null, null, null, 0]),
                arr_to_tree(
                    [
                        0,
                        0,
                        0,
                        null,
                        145,
                        334,
                        null,
                        null,
                        674,
                        338,
                        null,
                        366,
                        366,
                        706,
                        null,
                        600,
                        null,
                        365,
                        null,
                        null,
                        null,
                        null,
                        null,
                        0,
                        0,
                        null,
                        null,
                        null,
                        0,
                    ]
                ),
            ],
            "assert_methods": ["assertTreesEqual"] * 4,
        },
    ]

    def assertTreesEqual(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> None:
        if root1 and root2:
            self.assertEqual(root1.val, root2.val)
            self.assertTreesEqual(root1.left, root2.left)
            self.assertTreesEqual(root1.right, root2.right)
        else:
            self.assertIsNone(root1)
            self.assertIsNone(root2)


if __name__ == "__main__":
    unittest.main()
