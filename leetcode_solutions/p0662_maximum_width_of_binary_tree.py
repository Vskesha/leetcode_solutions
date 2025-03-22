import unittest
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        bfs = deque()
        bfs.append((root, 0))

        while bfs:
            lvl = bfs[-1][1] - bfs[0][1]
            ans = max(ans, lvl)
            for _ in range(len(bfs)):
                curr, width = bfs.popleft()
                if curr.left:
                    bfs.append((curr.left, width * 2))
                if curr.right:
                    bfs.append((curr.right, width * 2 + 1))

        return ans + 1


class Solution2:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, width = deque([(root, 0)]), 0
        while q:
            width = max(width, q[-1][1] - q[0][1])
            for _ in range(len(q)):
                node, k = q.popleft()
                if node.left:
                    q.append((node.left, k * 2 - 1))
                if node.right:
                    q.append((node.right, k * 2))
        return width + 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def list_to_tree(root: List[int]) -> Optional[TreeNode]:
        if not root:
            return None

        values = iter(root)
        root = TreeNode(next(values))
        q = deque([root])

        while q:
            node = q.popleft()
            val = next(values, None)
            if val:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(values, None)
            if val:
                node.right = TreeNode(val)
                q.append(node.right)

        return root

    def test_width_of_binary_tree_1(self):
        print("Test widthOfBinaryTree 1... ", end="")
        root = self.list_to_tree(root=[1, 3, 2, 5, 3, None, 9])
        self.assertEqual(
            self.sol.widthOfBinaryTree(root=root),
            4,
        )
        print("OK")

    def test_width_of_binary_tree_2(self):
        print("Test widthOfBinaryTree 2... ", end="")
        root = self.list_to_tree(root=[1, 3, 2, 5, 3, None, 9])
        self.assertEqual(
            self.sol.widthOfBinaryTree(root=root),
            4,
        )
        print("OK")

    def test_width_of_binary_tree_3(self):
        print("Test widthOfBinaryTree 3... ", end="")
        root = self.list_to_tree(root=[1, 3, 2, 5])
        self.assertEqual(
            self.sol.widthOfBinaryTree(root=root),
            2,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
