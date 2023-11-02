from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):  # sum, qty, total
            if not node:
                return 0, 0, 0
            sl, ql, tl = dfs(node.left)
            sr, qr, tr = dfs(node.right)
            s = sl + sr + node.val
            q = ql + qr + 1
            t = tl + tr + int(s // q == node.val)
            return s, q, t

        return dfs(root)[2]


class Solution1:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):  # sum, qty, total
            if not node:
                return [0, 0, 0]
            ret = []
            for a, b in zip(dfs(node.left), dfs(node.right)):
                ret.append(a + b)
            ret[0] += node.val
            ret[1] += 1
            ret[2] += ret[0] // ret[1] == node.val
            return ret

        return dfs(root)[2]


class Solution2:

    def __init__(self):
        self.ans = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):  # sum, qty
            if not node:
                return [0, 0]
            res = [a + b for a, b in zip(dfs(node.left), dfs(node.right))]
            res[0] += node.val
            res[1] += 1
            self.ans += res[0] // res[1] == node.val
            return res

        dfs(root)
        return self.ans


def test():
    sol = Solution()


if __name__ == '__main__':
    test()
