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


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.nodes

    def dfs(self, node: TreeNode, val: int) -> None:
        if node:
            self.nodes.add(val)
            self.dfs(node.left, val * 2 + 1)
            self.dfs(node.right, val * 2 + 2)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null, false, true = None, False, True

    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        values = iter(arr)
        root = TreeNode(next(values))
        q = deque([root])

        while q:
            node = q.popleft()
            val = next(values, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(values, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)

        return root


    test_cases = [
        {
            "class": FindElements,
            "cls_init_args": [array_to_tree([-1, null, -1])],
            "class_methods": ["find", "find"],
            "args": [[1], [2]],
            "expected": [false, true],
        },
        {
            "class": FindElements,
            "cls_init_args": [array_to_tree([-1, -1, -1, -1, -1])],
            "class_methods": ["find", "find", "find"],
            "args": [[1], [3], [5]],
            "expected": [true, true, false],
        },
        {
            "class": FindElements,
            "cls_init_args": [array_to_tree([-1, null, -1, -1, null, -1])],
            "class_methods": ["find", "find", "find", "find"],
            "args": [[2], [3], [4], [5]],
            "expected": [true, false, false, true],
        },
    ]


if __name__ == "__main__":
    unittest.main()
