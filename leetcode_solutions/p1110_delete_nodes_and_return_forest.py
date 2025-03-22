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
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        def dfs(node: Optional[TreeNode], trees: List[TreeNode], to_delete: set[int]):
            if node.left:
                node.left = dfs(node.left, trees, to_delete)
            if node.right:
                node.right = dfs(node.right, trees, to_delete)
            if node.val in to_delete:
                if node.left:
                    trees.append(node.left)
                if node.right:
                    trees.append(node.right)
                return None
            return node

        d = to_delete[0]
        to_delete = set(to_delete)
        trees = []
        dfs(TreeNode(d, root), trees, to_delete)
        return trees


class Solution1:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        def postorder(node, ans, to_delete):
            if node.left and postorder(node.left, ans, to_delete):
                node.left = None

            if node.right and postorder(node.right, ans, to_delete):
                node.right = None

            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return True

            return False

        ans = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            ans.append(root)
        postorder(root, ans, to_delete)

        return ans


class Solution2:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def dfs(n, new):
            if not n:
                return
            deleted = n.val in to_delete
            if new and not deleted:
                ans.append(n)
            n.left = dfs(n.left, deleted)
            n.right = dfs(n.right, deleted)
            return None if deleted else n

        dfs(root, True)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def list_to_tree(nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        nums = iter(nums)
        root = TreeNode(next(nums))
        bfs = deque([root])
        try:
            while bfs:
                node = bfs.popleft()
                val = next(nums)
                if val:
                    node.left = TreeNode(val)
                    bfs.append(node.left)
                val = next(nums)
                if val:
                    node.right = TreeNode(val)
                    bfs.append(node.right)
        except StopIteration:
            pass
        return root

    @staticmethod
    def tree_to_list(root: Optional[TreeNode]) -> List[int]:
        ans = []
        bfs = deque([root])
        while bfs:
            node = bfs.popleft()
            if node:
                ans.append(node.val)
                bfs.append(node.left)
                bfs.append(node.right)
            else:
                ans.append(None)
        while ans[-1] is None:
            ans.pop()
        return ans

    def assertTreesEqual(self, trees1: List[List[int]], trees2: List[TreeNode]):
        self.assertEqual(len(trees1), len(trees2))
        trees1 = set(map(tuple, trees1))
        trees2 = set(tuple(self.tree_to_list(t)) for t in trees2)
        self.assertSetEqual(trees1, trees2)

    def test_delNodes_1(self):
        print("Test delNodes 1... ", end="")
        root = [1, 2, 3, 4, 5, 6, 7]
        to_delete = [3, 5]
        expected = [[1, 2, None, 4], [6], [7]]
        root = self.list_to_tree(root)
        self.assertTreesEqual(expected, self.sol.delNodes(root, to_delete))
        print("OK")

    def test_delNodes_2(self):
        print("Test delNodes 2... ", end="")
        root = [1, 2, 4, None, 3]
        to_delete = [3]
        expected = [[1, 2, 4]]
        root = self.list_to_tree(root)
        self.assertTreesEqual(expected, self.sol.delNodes(root, to_delete))
        print("OK")


if __name__ == "__main__":
    unittest.main()
