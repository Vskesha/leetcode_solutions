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
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodes = {}
        parents = {}

        for parent, child, is_left in descriptions:
            if child not in nodes:
                nodes[child] = TreeNode(child)
            child_node = nodes[child]
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            parent_node = nodes[parent]
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            parents[child] = parent

        head = descriptions[0][0]
        while head in parents:
            head = parents[head]

        return nodes[head]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def list_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
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

    def assertEqualTrees(
        self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]
    ):
        def dfs_equal_trees(
            node1: Optional[TreeNode], node2: Optional[TreeNode]
        ) -> bool:
            if node1 and node2:
                return (
                    node1.val == node2.val
                    and dfs_equal_trees(node1.left, node2.left)
                    and dfs_equal_trees(node1.right, node2.right)
                )
            return not (node1 or node2)

        self.assertTrue(dfs_equal_trees(tree1, tree2))

    def test_create_binary_tree_1(self):
        print("Test createBinaryTree 1... ", end="")
        result_tree = self.sol.createBinaryTree(
            descriptions=[
                [20, 15, 1],
                [20, 17, 0],
                [50, 20, 1],
                [50, 80, 0],
                [80, 19, 1],
            ]
        )
        expected_tree = self.list_to_tree([50, 20, 80, 15, 17, 19])
        self.assertEqualTrees(result_tree, expected_tree)
        print("OK")

    def test_create_binary_tree_2(self):
        print("Test createBinaryTree 2... ", end="")
        null = None
        result_tree = self.sol.createBinaryTree(
            descriptions=[[1, 2, 1], [2, 3, 0], [3, 4, 1]]
        )
        expected_tree = self.list_to_tree([1, 2, null, null, 3, 4])
        self.assertEqualTrees(result_tree, expected_tree)
        print("OK")


if __name__ == "__main__":
    unittest.main()
