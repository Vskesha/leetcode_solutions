from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        def postorder(node, ans, to_delete):
            if node.left and postorder(node.left, ans, to_delete):
                node.left = None

            if node.right and postorder(node.right, ans, to_delete):
                node.right = None

            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return True

            return False

        ans = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            ans.append(root)
        postorder(root, ans, to_delete)

        return ans


class Solution2:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def dfs(n, new):
            if not n:
                return
            deleted = n.val in to_delete
            if new and not deleted:
                ans.append(n)
            n.left = dfs(n.left, deleted)
            n.right = dfs(n.right, deleted)
            return None if deleted else n

        dfs(root, True)
        return ans


def list_to_tree(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    nums = iter(nums)
    root = TreeNode(next(nums))
    bfs = deque([root])
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
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    ans = []
    bfs = deque([root])
    while bfs:
        node = bfs.popleft()
        if node:
            ans.append(node.val)
            bfs.append(node.left)
            bfs.append(node.right)
        else:
            ans.append(None)
    while ans[-1] is None:
        ans.pop()
    return ans


def test_del_nodes():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    root = [1, 2, 3, 4, 5, 6, 7]
    to_delete = [3, 5]
    trees = sol.delNodes(root=list_to_tree(root), to_delete=to_delete)
    res = [tree_to_list(tree) for tree in trees]
    assert res == [[1, 2, null, 4], [6], [7]]
    print("OK")

    print("Test 2... ", end="")
    root = [1, 2, 4, null, 3]
    to_delete = [3]
    trees = sol.delNodes(root=list_to_tree(root), to_delete=to_delete)
    res = [tree_to_list(tree) for tree in trees]
    assert res == [[1, 2, 4]]
    print("OK")


if __name__ == "__main__":
    test_del_nodes()
