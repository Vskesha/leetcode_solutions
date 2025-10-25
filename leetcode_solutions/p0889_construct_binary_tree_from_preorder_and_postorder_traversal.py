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
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:

        def constr(prfr, prto, psfr, psto) -> Optional[TreeNode]:
            if prfr >= prto:
                return None

            node = TreeNode(preorder[prfr])
            if prto - prfr > 1:
                i = postorder.index(preorder[prfr + 1], psfr) + 1
                els = i - psfr
                node.left = constr(prfr + 1, prfr + els + 1, psfr, psfr + els)
                node.right = constr(prfr + els + 1, prto, psfr + els, psto - 1)

            return node

        return constr(0, len(preorder), 0, len(postorder))


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

            left_val = next(values, None)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)

            right_val = next(values, None)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)

        return root

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["constructFromPrePost"] * 2,
            "kwargs": [
                dict(
                    preorder=[1, 2, 4, 5, 3, 6, 7],
                    postorder=[4, 5, 2, 6, 7, 3, 1],
                ),
                dict(preorder=[1], postorder=[1]),
            ],
            "expected": [
                array_to_tree([1, 2, 3, 4, 5, 6, 7]),
                array_to_tree([1]),
            ],
            "assert_methods": ["assertSamePrePost"] * 2,
        },
    ]

    def assertSamePrePost(
        self, actual: Optional[TreeNode], expected: Optional[TreeNode]
    ) -> None:
        self.assertListEqual(self.preorder(actual), self.preorder(expected))
        self.assertListEqual(self.postorder(actual), self.postorder(expected))

    def preorder(self, root: Optional[TreeNode]):
        ans = []
        if root:
            ans.append(root.val)
            ans.extend(self.preorder(root.left))
            ans.extend(self.preorder(root.right))
        return ans

    def postorder(self, root: Optional[TreeNode]):
        ans = []
        if root:
            ans.extend(self.postorder(root.left))
            ans.extend(self.postorder(root.right))
            ans.append(root.val)
        return ans


if __name__ == "__main__":
    unittest.main()
