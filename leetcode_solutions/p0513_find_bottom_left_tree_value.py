# Definition for a binary tree node.
from collections import deque
from functools import wraps
from typing import List, Optional


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

        def findBottomLeftValue(self, root: Optional[List]) -> int:
            root = self.list2tree(root)
            return self.original.findBottomLeftValue(root)

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


@sol_decorator
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])
        ans = root.val
        while bfs:
            ans = bfs[0].val
            for _ in range(len(bfs)):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return ans


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findBottomLeftValue(root=[2, 1, 3]) == 1
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.findBottomLeftValue(root=[1, 2, 3, 4, null, 5, 6, null, null, 7])
        == 7
    )
    print("OK")


if __name__ == "__main__":
    test()
