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

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node1, node2) -> bool:
            if not (node1 and node2):
                return not (node1 or node2)
            if node1.val != node2.val:
                return False
            ans = dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            if ans:
                return True
            ans = dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            return ans

        return dfs(root1, root2)


class Solution2:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2) -> bool:
            return (
                not (node1 or node2)
                if not (node1 and node2)
                else node1.val == node2.val
                and (
                    dfs(node1.left, node2.left)
                    and dfs(node1.right, node2.right)
                    or dfs(node1.left, node2.right)
                    and dfs(node1.right, node2.left)
                )
            )

        return dfs(root1, root2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def list_to_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        que = deque([root])
        while que:
            node = que.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                que.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                que.append(node.right)

        return root

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["flipEquiv"] * 3,
            "kwargs": [
                dict(
                    root1=list_to_tree([1, 2, 3, 4, 5, 6, null, null, null, 7, 8]),
                    root2=list_to_tree(
                        [1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7]
                    ),
                ),
                dict(root1=list_to_tree([]), root2=list_to_tree([])),
                dict(root1=list_to_tree([]), root2=list_to_tree([1])),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
