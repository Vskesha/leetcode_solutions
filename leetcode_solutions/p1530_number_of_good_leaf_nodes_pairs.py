import unittest
from collections import deque
from itertools import accumulate
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node: Optional[TreeNode], d: int) -> List[int]:
            if not (node.left or node.right):
                dists = [0] * (d + 1)
                dists[1] = 1
                return dists

            if not (node.left and node.right):
                dists = dfs(node.left or node.right, d)
                dists[1:] = dists[:-1]
                return dists

            dists = dfs(node.left, d)
            rdists = dfs(node.right, d)
            acc_rdist = list(accumulate(rdists))
            self.pairs += sum(dists[i] * acc_rdist[~i] for i in range(1, d))
            for i in range(d, 0, -1):
                dists[i] = dists[i - 1] + rdists[i - 1]

            return dists

        self.pairs = 0
        dfs(root, distance)
        return self.pairs


class Solution1:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node: Optional[TreeNode], distance: int) -> List[int]:
            if not (node.left or node.right):
                distances = [0] * (distance + 1)
                distances[1] = 1
                return distances

            if not (node.left and node.right):
                distances = dfs(node.left or node.right, distance)
                for i in range(distance, 0, -1):
                    distances[i] = distances[i - 1]
                return distances

            distances_left = dfs(node.left, distance)
            distances_right = dfs(node.right, distance)
            acc_distances_right = list(accumulate(distances_right))
            for i in range(1, distance):
                self.pairs += distances_left[i] * acc_distances_right[~i]
            for i in range(distance, 0, -1):
                distances_left[i] = distances_left[i - 1] + distances_right[i - 1]

            return distances_left

        self.pairs = 0
        dfs(root, distance)
        return self.pairs


class Solution2:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node: Optional[TreeNode], distance: int) -> tuple[int, List]:
            if not (node.left or node.right):
                distances = [0] * (distance + 1)
                distances[1] = 1
                return 0, distances

            if not (node.left and node.right):
                pairs, distances = dfs(node.left or node.right, distance)
                for i in range(distance, 0, -1):
                    distances[i] = distances[i - 1]
                distances[0] = 0
                return pairs, distances

            pairs_left, distances_left = dfs(node.left, distance)
            pairs_right, distances_right = dfs(node.right, distance)
            pairs_left += pairs_right
            for i in range(distance + 1):
                for j in range(distance - i + 1):
                    pairs_left += distances_left[i] * distances_right[j]
            for i in range(distance, 0, -1):
                distances_left[i] = distances_left[i - 1] + distances_right[i - 1]
            distances_left[0] = 0

            return pairs_left, distances_left

        ans = dfs(root, distance)[0]
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

    def test_countPairs_1(self):
        print("Test countPairs 1... ", end="")
        root = [1, 2, 3, None, 4]
        distance = 3
        root = self.arr_to_tree(root)
        self.assertEqual(1, self.sol.countPairs(root, distance))
        print("OK")

    def test_countPairs_2(self):
        print("Test countPairs 2... ", end="")
        root = [1, 2, 3, 4, 5, 6, 7]
        distance = 3
        root = self.arr_to_tree(root)
        self.assertEqual(2, self.sol.countPairs(root, distance))
        print("OK")

    def test_countPairs_3(self):
        print("Test countPairs 3... ", end="")
        null = None
        root = [7, 1, 4, 6, null, 5, 3, null, null, null, null, null, 2]
        distance = 3
        root = self.arr_to_tree(root)
        self.assertEqual(1, self.sol.countPairs(root, distance))
        print("OK")


if __name__ == "__main__":
    unittest.main()
