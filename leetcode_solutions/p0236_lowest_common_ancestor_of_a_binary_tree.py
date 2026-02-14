import unittest
from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


class Solution0:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if node == p or node == q:
                return node
            lt = dfs(node.left) if node.left else None
            rt = dfs(node.right) if node.right else None
            return node if lt and rt else lt if lt else rt

        return dfs(root)


class Solution1:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.first = []
        self.second = []

        def dfs(track):
            curr = track[-1]
            # print(curr.val)
            if curr in (p, q):
                if self.first:
                    self.second = track.copy()
                    raise StopIteration
                else:
                    self.first = track.copy()

            if curr.left:
                track.append(curr.left)
                dfs(track)
                track.pop()
            if curr.right:
                track.append(curr.right)
                dfs(track)
                track.pop()

        try:
            dfs([root])
        except StopIteration:
            pass

        prev = None
        for n1, n2 in zip(self.first, self.second):
            if n1 is not n2:
                break
            prev = n1
        return prev


class Solution2:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        stack = []
        parent = defaultdict(TreeNode)
        res = []
        stack.append([root, 0])
        while stack:
            t = stack.pop()
            node = t[0]
            level = t[1]
            if node.val in [p.val, q.val]:
                res.append([node, level])
            if node.right:
                stack.append([node.right, level + 1])
                parent[node.right] = node
            if node.left:
                stack.append([node.left, level + 1])
                parent[node.left] = node
        p, pl = res[0][0], res[0][1]
        q, ql = res[1][0], res[1][1]
        if pl > ql:
            for i in range(pl - ql):
                p = parent[p]
        elif pl < ql:
            for i in range(ql - pl):
                q = parent[q]
        while p.val != q.val:
            p = parent[p]
            q = parent[q]
        return p


class Solution3:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node) -> bool:
            if not node:
                return False
            lf = dfs(node.left)
            rt = dfs(node.right)
            if self.lca:
                return True
            if lf and rt:
                self.lca = node
                return True
            if lf or rt:
                if node is p or node is q:
                    self.lca = node
                return True
            return node is p or node is q

        dfs(root)
        return self.lca


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def get_tree_and_nodes(
        self, root: List[int], p: int, q: int
    ) -> (TreeNode, TreeNode, TreeNode):
        vals = iter(root)
        root_node = TreeNode(next(vals))
        q_node, p_node = None, None
        queue = deque([root_node])

        try:
            while queue:
                node = queue.popleft()
                if node.val == p:
                    p_node = node
                if node.val == q:
                    q_node = node
                val = next(vals)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                val = next(vals)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        except StopIteration:
            return root_node, p_node, q_node

    def test_lowest_common_ancestor1(self):
        print("Test lowestCommonAncestor 1... ", end="")
        null = None
        root, p, q = self.get_tree_and_nodes(
            root=[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p=5, q=1
        )
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 3)
        print("OK")

    def test_lowest_common_ancestor2(self):
        print("Test lowestCommonAncestor 2... ", end="")
        null = None
        root, p, q = self.get_tree_and_nodes(
            root=[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p=5, q=4
        )
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 5)
        print("OK")

    def test_lowest_common_ancestor3(self):
        print("Test lowestCommonAncestor 3... ", end="")
        root, p, q = self.get_tree_and_nodes(root=[1, 2], p=1, q=2)
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()

# [-1, 0, 3, -2, 4, null, null, 8]
#
#                     1
#                    / \
#                   /   \
#                  /     \
#                 0       3
#                / \     / \
#              -2   4   n   n
#              /
#             8
