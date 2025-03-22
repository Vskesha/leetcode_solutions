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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, suffix):
            ch = chr(node.val + 97)
            suffix = ch + suffix

            if node.left:
                if node.right:
                    left = dfs(node.left, suffix)
                    right = dfs(node.right, suffix)
                    if left + suffix < right + suffix:
                        return left + ch
                    else:
                        return right + ch
                else:
                    return dfs(node.left, suffix) + ch
            else:
                if node.right:
                    return dfs(node.right, suffix) + ch
                else:
                    return ch

        return dfs(root, "")


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def list_to_tree(arr: Optional[List]) -> TreeNode:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        q = deque([root])
        while q:
            node = q.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)

        return root

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestFromLeaf"] * 3,
            "kwargs": [
                dict(root=list_to_tree([0, 1, 2, 3, 4, 3, 4])),
                dict(root=list_to_tree([25, 1, 3, 1, 3, 0, 2])),
                dict(root=list_to_tree([2, 2, 1, null, 1, 0, null, 0])),
            ],
            "expected": ["dba", "adz", "abc"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
