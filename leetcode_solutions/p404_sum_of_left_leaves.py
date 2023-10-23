from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            if not (node.left or node.right):
                return node.val if is_left else 0

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left) -> int:
            if not node:
                return 0
            return (node.val if is_left and not node.left and not node.right else 0) + dfs(node.left, True) + dfs(
                node.right, False)

        return dfs(root, False)


def to_binary_tree(tree_list: list):
    head = TreeNode(tree_list[0])
    dq = deque([head])
    i = 1
    while i < len(tree_list):
        curr = dq.popleft()
        if tree_list[i]:
            curr.left = TreeNode(tree_list[i])
            dq.append(curr.left)
        i += 1
        if tree_list[i]:
            curr.right = TreeNode(tree_list[i])
            dq.append(curr.right)
        i += 1
    return head


def main():
    null = None
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.sumOfLeftLeaves(to_binary_tree([3, 9, 20, null, null, 15, 7])) == 24
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.sumOfLeftLeaves(to_binary_tree([1])) == 0
    print('ok')


if __name__ == '__main__':
    main()
