import unittest
from collections import deque
from itertools import pairwise
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"Node(val={self.val})"


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        row = [root]

        while row:
            for a, b in pairwise(row):
                a.next = b

            nrow = []
            for node in row:
                if node.left:
                    nrow.append(node.left)
                if node.right:
                    nrow.append(node.right)

            row = nrow

        return root


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def list_to_tree(arr: List[int]) -> Optional[Node]:
        if not arr:
            return None

        vals = iter(arr)
        root = Node(val=next(vals))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = Node(val=val)
                queue.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = Node(val=val)
                queue.append(node.right)

        return root

    @staticmethod
    def get_rows(root: Optional[Node]) -> List[int]:
        if not root:
            return []

        row = [root]
        rows = []

        while row:
            nrow = []
            for node in row:
                if node.left:
                    nrow.append(node.left)
                if node.right:
                    nrow.append(node.right)
                rows.append(node.val)
            rows.append(None)
            row = nrow

        return rows

    def test_connect_1(self):
        print("Test connect 1 ... ", end="")
        null = None
        root = [1, 2, 3, 4, 5, null, 7]
        self.assertListEqual(
            self.get_rows(self.sol.connect(root=self.list_to_tree(root))),
            [1, None, 2, 3, None, 4, 5, 7, None],
        )
        print("OK")

    def test_connect_2(self):
        print("Test connect 2 ... ", end="")
        root = []
        self.assertListEqual(
            self.get_rows(self.sol.connect(root=self.list_to_tree(root))), []
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
