import unittest
from collections import deque
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def traverse(nodel, noder, lvl):
            if not nodel:
                return
            if lvl % 2:
                nodel.val, noder.val = noder.val, nodel.val
            traverse(nodel.left, noder.right, lvl + 1)
            traverse(nodel.right, noder.left, lvl + 1)

        traverse(root.left, root.right, 1)
        return root


class Solution2:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        row = deque([root])
        k = 0

        while row:
            if k % 2:
                vals = [node.val for node in reversed(row)]
                for n, v in zip(row, vals):
                    n.val = v
            k += 1
            for _ in range(len(row)):
                node = row.popleft()
                if node.left:
                    row.append(node.left)
                    row.append(node.right)

        return root


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        values = iter(arr)
        root = TreeNode(next(values))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(values, None)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = next(values, None)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reverseOddLevels"] * 3,
            "kwargs": [
                dict(root=array_to_tree([2, 3, 5, 8, 13, 21, 34])),
                dict(root=array_to_tree([7, 13, 11])),
                dict(root=array_to_tree([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])),
            ],
            "expected": [
                array_to_tree([2, 5, 3, 8, 13, 21, 34]),
                array_to_tree([7, 11, 13]),
                array_to_tree([0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]),
            ],
            "assert_methods": ["assertTreesEqual"] * 3,
        },
    ]

    def assertTreesEqual(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> None:
        if not (root1 and root2):
            self.assertIsNone(root1)
            self.assertIsNone(root2)
        else:
            self.assertEqual(root1.val, root2.val)
            self.assertTreesEqual(root1.left, root2.left)
            self.assertTreesEqual(root1.right, root2.right)


if __name__ == "__main__":
    unittest.main()
