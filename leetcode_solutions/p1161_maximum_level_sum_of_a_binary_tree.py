import unittest
from collections import deque
from math import inf
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ls = []

        while q:
            ls.append(sum(n.val for n in q))
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return ls.index(max(ls)) + 1


class Solution1:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ms = -inf
        lvl = 0
        ans = 0

        while q:
            lvl += 1
            cs = 0
            for _ in range(len(q)):
                node = q.popleft()
                cs += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if cs > ms:
                ms = cs
                ans = lvl

        return ans


class Solution2:
    def maxLevelSum(self, root: TreeNode) -> int:
        bfs = deque([root])
        level, ans = 0, 0
        max_sum = float("-inf")
        while bfs:
            level += 1
            curr_sum = 0
            for _ in range(len(bfs)):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                curr_sum += node.val
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def arr_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        queue = deque([root])

        try:
            while queue:
                node = queue.popleft()
                val = next(vals)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                val = next(vals)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        except StopIteration:
            pass

        return root

    def test_max_level_sum_1(self):
        print("Test maxLevelSum 1 ... ", end="")
        null = None
        self.assertEqual(
            self.sol.maxLevelSum(
                root=self.arr_to_tree([1, 7, 0, 7, -8, null, null])
            ),
            2,
        )
        print("OK")

    def test_max_level_sum_2(self):
        print("Test maxLevelSum 2 ... ", end="")
        null = None
        self.assertEqual(
            self.sol.maxLevelSum(
                root=self.arr_to_tree(
                    [989, null, 10250, 98693, -89388, null, null, null, -32127]
                )
            ),
            2,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
