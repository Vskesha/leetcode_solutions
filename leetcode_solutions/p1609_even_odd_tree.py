# Definition for a binary tree node.
from collections import deque
from functools import wraps
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def isEvenOddTree(self, root: Optional[List]) -> bool:
            root = self.list2tree(root)
            return self.original.isEvenOddTree(root)

        def list2tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            vals = iter(nums)
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

    return Wrapper


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque([root])
        level = -1
        inf = float("inf")

        while bfs:
            prev = inf
            for _ in range(len(bfs)):
                node = bfs.popleft()
                if not node:
                    continue
                if (node.val % 2) * 2 - 1 == level:
                    return False
                if node.val * level < prev:
                    bfs.append(node.left)
                    bfs.append(node.right)
                else:
                    return False
                prev = node.val * level
            level = -level

        return True


class Solution2:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque([root])
        level = 0
        inf = float("inf")

        while bfs:
            if level:
                prev = inf
                for _ in range(len(bfs)):
                    node = bfs.popleft()
                    if node.val % 2 == 1:
                        return False
                    if node.val < prev:
                        if node.left:
                            bfs.append(node.left)
                        if node.right:
                            bfs.append(node.right)
                    else:
                        return False
                    prev = node.val
            else:
                prev = 0
                for _ in range(len(bfs)):
                    node = bfs.popleft()
                    if node.val % 2 == 0:
                        return False
                    if node.val > prev:
                        if node.left:
                            bfs.append(node.left)
                        if node.right:
                            bfs.append(node.right)
                    else:
                        return False
                    prev = node.val
            level = 1 - level

        return True


def test():
    null = None
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert (
        sol.isEvenOddTree(root=[1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2])
        is True
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.isEvenOddTree(root=[5, 4, 2, 3, 3, 7]) is False
    print("OK")

    print("Test 3... ", end="")
    assert sol.isEvenOddTree(root=[5, 9, 1, 3, 5, 7]) is False
    print("OK")


if __name__ == "__main__":
    test()
