from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        self.original_distributeCoins = instance.distributeCoins
        instance.distributeCoins = self.distributeCoins
        return instance

    def distributeCoins(self, root: Optional[List]) -> int:
        root = self.list2tree(root)
        return self.original_distributeCoins(root)

    def list2tree(self, arr: Optional[List]) -> Optional[TreeNode]:
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


@SolDecorator
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            bl = dfs(node.left)
            br = dfs(node.right)
            self.ans += abs(bl) + abs(br)
            return bl + br + node.val - 1

        dfs(root)
        return self.ans


@SolDecorator
class Solution2:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            ml, bl = dfs(node.left)
            mr, br = dfs(node.right)

            b = bl + br + node.val - 1
            m = ml + mr + abs(bl) + abs(br)
            return m, b

        return dfs(root)[0]


def test_distribute_coins():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.distributeCoins(root=[3, 0, 0]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.distributeCoins(root=[0, 3, 0]) == 3
    print("OK")


if __name__ == "__main__":
    test_distribute_coins()
