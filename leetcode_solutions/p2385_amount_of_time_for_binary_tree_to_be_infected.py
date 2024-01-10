from collections import deque
from functools import wraps
from typing import List, Optional


# Definition for a binary tree node.
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

        def amountOfTime(self, root: Optional[List], start: int) -> int:
            root = self.list2tree(root)
            return self.original.amountOfTime(root, start)

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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        bfs = deque()

        def to_graph(node: TreeNode, neibs: List):
            if node.left:
                neibs.append(node.left)
                to_graph(node.left, [node])
            if node.right:
                neibs.append(node.right)
                to_graph(node.right, [node])
            node.neibs = neibs
            if node.val == start:
                bfs.append(node)

        to_graph(root, [])
        visited = set(bfs)
        ans = -1

        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                for neib in curr.neibs:
                    if neib not in visited:
                        bfs.append(neib)
                        visited.add(neib)
            ans += 1

        return ans


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.amountOfTime(root=[1, 5, 3, null, 4, 10, 6, 9, 2], start=3) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.amountOfTime(root=[1], start=1) == 0
    print("OK")


if __name__ == "__main__":
    test()
