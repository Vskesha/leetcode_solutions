from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolDecor:
    def __init__(self, original):
        self.original = original

    def __call__(self, *args, **kwargs):
        instance = self.original(*args, **kwargs)
        self.originalAddOneRow = instance.addOneRow
        instance.addOneRow = self.addOneRow
        return instance

    def addOneRow(
        self, root: Optional[List], val: int, depth: int
    ) -> Optional[List]:
        root = self.arr_to_tree(root)
        result = self.originalAddOneRow(root, val, depth)
        return self.tree_to_arr(result)

    def arr_to_tree(self, arr: Optional[List]) -> TreeNode:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        queue = deque()
        queue.append(root)

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

    def tree_to_arr(self, root: Optional[TreeNode]) -> List:
        arr = [root]
        i = 0
        while i < len(arr):
            node = arr[i]
            if node is None:
                i += 1
                continue
            arr.append(node.left)
            arr.append(node.right)
            arr[i] = node.val
            i += 1

        while arr[-1] is None:
            arr.pop()

        return arr


@SolDecor
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val, left=root)
            return new_root

        def dfs(node, lvl):
            if not node:
                return
            if lvl == depth:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
                return
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 2)
        return root


def test_add_one_row():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.addOneRow(root=[4, 2, 6, 3, 1, 5], val=1, depth=2) == [
        4,
        1,
        1,
        2,
        null,
        null,
        6,
        3,
        1,
        5,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.addOneRow(root=[4, 2, null, 3, 1], val=1, depth=3) == [
        4,
        2,
        null,
        1,
        1,
        3,
        null,
        null,
        1,
    ]
    print("OK")


if __name__ == "__main__":
    test_add_one_row()
