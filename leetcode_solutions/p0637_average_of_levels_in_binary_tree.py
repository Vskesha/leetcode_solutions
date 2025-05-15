import unittest
from collections import deque
from functools import wraps
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol_decorator(cls):

    @wraps(cls, updated=())
    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def averageOfLevels(self, root: Optional[List[int]]) -> List[float]:
            root = self.list2tree(root)
            return self.original.averageOfLevels(root)

        @staticmethod
        def list2tree(arr: Optional[List[int]]) -> Optional[TreeNode]:
            if not arr:
                return None

            vals = iter(arr)
            root = TreeNode(next(vals))
            que = deque([root])

            while que:
                curr = que.popleft()
                val = next(vals, None)
                if val:
                    curr.left = TreeNode(val)
                    que.append(curr.left)
                val = next(vals, None)
                if val:
                    curr.right = TreeNode(val)
                    que.append(curr.right)

            return root

    return Wrapper


@sol_decorator
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        ans = []
        bfs = deque([root])
        while bfs:
            t, n = 0, len(bfs)
            for _ in range(n):
                curr = bfs.popleft()
                t += curr.val
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            ans.append(t / n)

        return ans


@sol_decorator
class Solution2:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        ans = []
        row = [root]
        while row:
            total = 0
            nrow = []
            for node in row:
                total += node.val
                if node.left:
                    nrow.append(node.left)
                if node.right:
                    nrow.append(node.right)
            ans.append(total / len(row))
            row = nrow

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["averageOfLevels"] * 2,
            "kwargs": [
                dict(root=[3, 9, 20, null, null, 15, 7]),
                dict(root=[3, 9, 20, 15, 7]),
            ],
            "expected": [
                [3.00000, 14.50000, 11.00000],
                [3.00000, 14.50000, 11.00000],
            ],
            "assert_methods": ["assertAlmostEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     null = None
#     sol = Solution()
#
#     print('Test 1... ', end='')
#     assert sol.averageOfLevels(root=[3, 9, 20, null, null, 15, 7]) == [3.00000, 14.50000, 11.00000]
#     print('OK')
#
#     print('Test 2... ', end='')
#     assert sol.averageOfLevels(root=[3, 9, 20, 15, 7]) == [3.00000, 14.50000, 11.00000]
#     print('OK')


# if __name__ == '__main__':
#     test()
