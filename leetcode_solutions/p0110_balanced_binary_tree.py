import unittest
from typing import Optional

from leetcode_solutions._test_meta import TestMeta
from leetcode_solutions.utils.array_to_binary_tree import array_to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_height = is_balanced(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = is_balanced(node.right)
            if not right_balanced:
                return False, 0

            if abs(left_height - right_height) > 1:
                return False, 0

            return True, max(left_height, right_height) + 1

        result = is_balanced(root)[0]
        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isBalanced"] * 3,
            "kwargs": [
                dict(root = array_to_binary_tree([3,9,20,null,null,15,7])),
                dict(root = array_to_binary_tree([1,2,2,3,3,null,null,4,4])),
                dict(root = array_to_binary_tree([])),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()
