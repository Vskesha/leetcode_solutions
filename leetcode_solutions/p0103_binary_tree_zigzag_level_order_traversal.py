from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def decorator(cls):

    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def zigzagLevelOrder(self, root: List[int]) -> List[List[int]]:
            root = self.list_to_tree(root)
            return self.original.zigzagLevelOrder(root)

        def list_to_tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            nums = iter(nums)
            root = TreeNode(next(nums))
            que = deque([root])

            while que:
                curr = que.popleft()
                val = next(nums, None)
                if val:
                    curr.left = TreeNode(val)
                    que.append(curr.left)
                val = next(nums, None)
                if val:
                    curr.right = TreeNode(val)
                    que.append(curr.right)

            return root

    return Wrapper


@decorator
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        que = deque([root])
        backward = False

        while que:
            row = []
            for _ in range(len(que)):
                curr = que.popleft()
                row.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            if backward:
                row = row[::-1]
            ans.append(row)
            backward = not backward

        return ans


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    for a, b in zip(
        sol.zigzagLevelOrder(root=[3, 9, 20, null, null, 15, 7]),
        [[3], [20, 9], [15, 7]],
    ):
        assert a == b
    print("ok")

    print("Test 2... ", end="")
    for a, b in zip(sol.zigzagLevelOrder(root=[1]), [[1]]):
        assert a == b
    print("ok")

    print("Test 3... ", end="")
    for a, b in zip(sol.zigzagLevelOrder(root=[]), []):
        assert a == b
    print("ok")


if __name__ == "__main__":
    test()
