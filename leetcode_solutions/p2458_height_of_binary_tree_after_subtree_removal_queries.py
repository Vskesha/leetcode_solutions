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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def ldfs(node, ch):
            if not node:
                return
            hts[node.val] = self.cmh
            self.cmh = max(self.cmh, ch)
            ldfs(node.left, ch + 1)
            ldfs(node.right, ch + 1)

        def rdfs(node, ch):
            if not node:
                return
            hts[node.val] = max(hts[node.val], self.cmh)
            self.cmh = max(self.cmh, ch)
            rdfs(node.right, ch + 1)
            rdfs(node.left, ch + 1)

        hts = {root.val: 0}
        self.cmh = 0
        ldfs(root, 0)
        self.cmh = 0
        rdfs(root, 0)

        return [hts[n] for n in queries]


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

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["treeQueries"] * 2,
            "kwargs": [
                dict(
                    root=array_to_tree(
                        [1, 3, 4, 2, null, 6, 5, null, null, null, null, null, 7]
                    ),
                    queries=[4],
                ),
                dict(
                    root=array_to_tree([5, 8, 9, 2, 1, 3, 7, 4, 6]),
                    queries=[3, 2, 4, 8],
                ),
            ],
            "expected": [
                [2],
                [3, 2, 3, 2],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
