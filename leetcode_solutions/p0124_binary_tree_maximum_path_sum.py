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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1000, 0
            lans, lsum = dfs(node.left)
            rans, rsum = dfs(node.right)
            ans = max([lans, rans, lsum + rsum + node.val])
            sum_ = max(0, node.val + max(lsum, rsum))
            return ans, sum_

        ret = dfs(root)[0]
        return ret


class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val

        def dfs(node) -> int:
            if not node:
                return 0
            lsum = dfs(node.left)
            rsum = dfs(node.right)

            self.ans = max(self.ans, lsum + rsum + node.val)

            return max(0, node.val + max(lsum, rsum))

        dfs(root)
        return self.ans


def list_to_tree(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    nums = iter(nums)
    val = next(nums)
    if not val:
        return None
    head = TreeNode(val)
    bfs = deque([head])
    try:
        while bfs:
            node = bfs.popleft()
            val = next(nums)
            if val:
                node.left = TreeNode(val)
                bfs.append(node.left)
            val = next(nums)
            if val:
                node.right = TreeNode(val)
                bfs.append(node.right)
    except StopIteration:
        pass
    return head


def test():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    root = [1, 2, 3]
    assert sol.maxPathSum(list_to_tree(root)) == 6
    print("OK")

    print("Test 2... ", end="")
    root = [-10, 9, 20, null, null, 15, 7]
    assert sol.maxPathSum(list_to_tree(root)) == 42
    print("OK")


if __name__ == "__main__":
    test()
