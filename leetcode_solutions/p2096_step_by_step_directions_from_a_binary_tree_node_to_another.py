import unittest
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        self.start_path = self.dest_path = None

        def get_path(sp, dp):
            i = 0
            for a, b in zip(sp, dp):
                if a != b:
                    break
                i += 1
            sp = "U" * (len(sp) - i)
            dp = "".join(dp[i:])
            return sp + dp

        def dfs(node, path) -> str:
            if not node:
                return ""
            if node.val == startValue:
                if self.dest_path is not None:
                    return get_path(path, self.dest_path)
                self.start_path = path.copy()
            elif node.val == destValue:
                if self.start_path is not None:
                    return get_path(self.start_path, path)
                self.dest_path = path.copy()

            path.append("L")
            left = dfs(node.left, path)
            path.pop()
            if left:
                return left

            path.append("R")
            right = dfs(node.right, path)
            path.pop()
            return right

        return dfs(root, [])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def arr_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
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

    def test_getDirections_1(self):
        print("Test getDirections 1... ", end="")
        null = None
        self.assertEqual(
            "UURL",
            self.sol.getDirections(
                root=self.arr_to_tree(arr=[5, 1, 2, 3, null, 6, 4]),
                startValue=3,
                destValue=6,
            ),
        )
        print("OK")

    def test_getDirections_2(self):
        print("Test getDirections 2... ", end="")
        self.assertEqual(
            "L",
            self.sol.getDirections(
                root=self.arr_to_tree(arr=[2, 1]),
                startValue=2,
                destValue=1,
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
