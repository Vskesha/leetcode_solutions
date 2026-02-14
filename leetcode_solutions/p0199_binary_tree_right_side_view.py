import unittest
from collections import deque
from functools import wraps
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        row = deque([root] if root else [])

        while row:
            for _ in range(len(row)):
                curr = row.popleft()
                if curr.left:
                    row.append(curr.left)
                if curr.right:
                    row.append(curr.right)
            ans.append(curr.val)

        return ans


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans

        row = [root]

        while row:
            ans.append(row[-1].val)
            nrow = []
            for node in row:
                if node.left:
                    nrow.append(node.left)
                if node.right:
                    nrow.append(node.right)
            row = nrow

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = cls.solution_decorator(Solution)()

    @classmethod
    def solution_decorator(cls, class_):
        @wraps(class_, updated=())
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.original = class_(*args, **kwargs)

            def rightSideView(self, root: List[int]) -> List[int]:
                root = self.list_to_tree(root)
                return self.original.rightSideView(root)

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

        return Wrapper

    def test_right_side_view_1(self):
        print("Test rightSideView 1... ", end="")
        null = None
        self.assertEqual(
            self.sol.rightSideView(root=[1, 2, 3, null, 5, null, 4]), [1, 3, 4]
        )
        print("OK")

    def test_right_side_view_2(self):
        print("Test rightSideView 2... ", end="")
        null = None
        self.assertEqual(
            self.sol.rightSideView(root=[1, null, 3]),
            [1, 3],
        )
        print("OK")

    def test_right_side_view_3(self):
        print("Test rightSideView 3... ", end="")
        self.assertEqual(
            self.sol.rightSideView(root=[]),
            [],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
