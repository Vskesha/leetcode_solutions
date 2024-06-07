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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, m):
            if node.left:
                dfs(node.left, m)
                dfs(node.right, m)
                node.val = min(node.left.val, node.right.val)
            elif node.val == m:
                node.val = float("inf")

        dfs(root, root.val)
        return root.val if root.val < float("inf") else -1


class Solution2:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, m):
            if node.left:
                return min(dfs(node.left, m), dfs(node.right, m))
            elif node.val == m:
                return float("inf")
            else:
                return node.val

        ans = dfs(root, root.val)
        return ans if ans < float("inf") else -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def list_to_tree(self, root: List[int]) -> Optional[TreeNode]:
        if not root:
            return None

        vals = iter(root)
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

    def test_find_second_minimum_value1(self):
        print("Test findSecondMinimumValue 1 ... ", end="")
        null = None
        self.assertEqual(
            self.sol.findSecondMinimumValue(
                root=self.list_to_tree(root=[2, 2, 5, null, null, 5, 7])
            ),
            5,
        )
        print("OK")

    def test_find_second_minimum_value2(self):
        print("Test findSecondMinimumValue 2 ... ", end="")
        self.assertEqual(
            self.sol.findSecondMinimumValue(root=self.list_to_tree(root=[2, 2, 2])), -1
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
