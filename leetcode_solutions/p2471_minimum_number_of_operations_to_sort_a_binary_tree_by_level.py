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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def swaps(row) -> int:
            srt = sorted(range(len(row)), key=row.__getitem__)
            visited = [False] * len(row)
            res = 0

            for i, si in enumerate(srt):
                if not visited[i]:
                    visited[i] = True
                    while not visited[si]:
                        res += 1
                        visited[si] = True
                        si = srt[si]

            return res

        ans = 0
        q = deque([root])

        while q:
            row = [node.val for node in q]
            ans += swaps(row)
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return ans


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
            "class_methods": ["minimumOperations"] * 3,
            "kwargs": [
                dict(
                    root=array_to_tree(
                        [1, 4, 3, 7, 6, 8, 5, null, null, null, null, 9, null, 10]
                    )
                ),
                dict(root=array_to_tree([1, 3, 2, 7, 6, 5, 4])),
                dict(root=array_to_tree([1, 2, 3, 4, 5, 6])),
            ],
            "expected": [3, 3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
