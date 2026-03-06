import unittest
from typing import Optional

from leetcode_solutions._test_meta import TestMeta
from leetcode_solutions.utils import TreeNode, array_to_binary_tree


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, parent_value, leaf_values):
            curr = parent_value * 2 + node.val

            if not (node.left or node.right):
                leaf_values.append(curr)
                return

            if node.left:
                dfs(node.left, curr, leaf_values)
            if node.right:
                dfs(node.right, curr, leaf_values)

        lvals = []
        dfs(root, 0, lvals)
        return sum(lvals)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sumRootToLeaf"] * 2,
            "kwargs": [
                dict(root=array_to_binary_tree([1, 0, 1, 0, 1, 0, 1])),
                dict(root=array_to_binary_tree([0])),
            ],
            "expected": [22, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
