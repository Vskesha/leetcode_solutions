import unittest
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs1 = deque([p])
        bfs2 = deque([q])

        while bfs1 and bfs2:
            a = bfs1.popleft()
            b = bfs2.popleft()
            if (a and not b) or (b and not a) or (a and b and a.val != b.val):
                return False
            if a:
                bfs1.append(a.left)
                bfs1.append(a.right)
            if b:
                bfs2.append(b.left)
                bfs2.append(b.right)

        return True


class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs1 = deque([p])
        bfs2 = deque([q])

        while bfs1 and bfs2:
            a = bfs1.popleft()
            b = bfs2.popleft()
            if (a and not b) or (b and not a) or (a and b and a.val != b.val):
                return False
            if a:
                bfs1.append(a.left)
                bfs1.append(a.right)
            if b:
                bfs2.append(b.left)
                bfs2.append(b.right)
        return True


class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True
        if (p is None) ^ (q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def tree_from_list(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        bfs = deque([root])

        while bfs:
            node = bfs.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                bfs.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                bfs.append(node.right)

        return root

    def test_is_same_tree_1(self):
        print("Test isSameTree 1... ", end="")
        self.assertTrue(
            self.sol.isSameTree(
                p=self.tree_from_list([1, 2, 3]), q=self.tree_from_list([1, 2, 3])
            )
        )
        print("OK")

    def test_is_same_tree_2(self):
        print("Test isSameTree 2... ", end="")
        self.assertFalse(
            self.sol.isSameTree(
                p=self.tree_from_list([1, 2]), q=self.tree_from_list([1, None, 2])
            )
        )
        print("OK")

    def test_is_same_tree_3(self):
        print("Test isSameTree 3... ", end="")
        self.assertFalse(
            self.sol.isSameTree(
                p=self.tree_from_list([1, 2, 1]), q=self.tree_from_list([1, 1, 2])
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
