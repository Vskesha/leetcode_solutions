from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == p or node == q:
                return node
            lt = dfs(node.left) if node.left else None
            rt = dfs(node.right) if node.right else None
            return node if lt and rt else lt if lt else rt

        return dfs(root)


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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


def test():
    sol = Solution()
    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.right = TreeNode(3)

    print('Test 1 ... ', end='')
    assert sol.lowestCommonAncestor(root, root.left.right, root.left.left.left) == root.left
    print('ok')


if __name__ == '__main__':
    test()

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
