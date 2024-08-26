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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = self.postorderTraversal(root.left)
        ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)
        return ans


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
            "class_methods": ["postorderTraversal"] * 3,
            "kwargs": [
                dict(root=arr_to_tree([1, null, 2, 3])),
                dict(root=arr_to_tree([])),
                dict(root=arr_to_tree([1])),
            ],
            "expected": [[3, 2, 1], [], [1]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == '__main__':
    unittest.main()
