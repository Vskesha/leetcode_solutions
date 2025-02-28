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


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        row = deque([root])

        while row:
            ans.append(max(n.val for n in row))
            for _ in range(len(row)):
                node = row.popleft()
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)

        return ans


class Solution1:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        bfs = deque([(root, 1)])

        while bfs:
            node, idx = bfs.popleft()

            if not node:
                continue

            if idx == len(ans):
                ans[-1] = max(ans[-1], node.val)
            else:
                ans.append(node.val)

            bfs.append((node.left, idx + 1))
            bfs.append((node.right, idx + 1))

        return ans


class Solution2:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        bfs = deque([(root, 1)])

        while bfs:
            node, idx = bfs.popleft()
            if idx == len(ans):
                ans[-1] = max(ans[-1], node.val)
            else:
                ans.append(node.val)
            if node.left:
                bfs.append((node.left, idx + 1))
            if node.right:
                bfs.append((node.right, idx + 1))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional[TreeNode]:
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
            "class_methods": ["largestValues"] * 2,
            "kwargs": [
                dict(root=array_to_tree([1, 3, 2, 5, 3, null, 9])),
                dict(root=array_to_tree([1, 2, 3])),
            ],
            "expected": [[1, 3, 9], [1, 3]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
