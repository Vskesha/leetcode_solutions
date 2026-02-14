import unittest
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return (
                n1.val == n2.val
                and dfs(n1.left, n2.right)
                and dfs(n1.right, n2.left)
            )

        return dfs(root.left, root.right)


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(n1, n2):
            if n1 and n2:
                return (
                    n1.val == n2.val
                    and dfs(n1.left, n2.right)
                    and dfs(n1.right, n2.left)
                )
            if n1 or n2:
                return False
            return True

        return dfs(root.left, root.right)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def list_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        q = deque([root])

        while q:
            node = q.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)

        return root

    def test_is_symmetric_1(self):
        print("Test isSymmetric 1... ", end="")
        self.assertTrue(
            self.sol.isSymmetric(self.list_to_tree([1, 2, 2, 3, 4, 4, 3]))
        )
        print("OK")

    def test_is_symmetric_2(self):
        print("Test isSymmetric 2... ", end="")
        null = None
        self.assertFalse(
            self.sol.isSymmetric(
                self.list_to_tree([1, 2, 2, null, 3, null, 3])
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
