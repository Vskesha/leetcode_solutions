from collections import deque
from functools import wraps
from typing import Optional


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

        def sumEvenGrandparent(self, root: list) -> int:
            root = self.list_to_tree(root)
            return self.original.sumEvenGrandparent(root)

        @staticmethod
        def list_to_tree(arr: list) -> Optional[TreeNode]:
            if not arr:
                return None

            arr = iter(arr)
            root = TreeNode(next(arr))
            q = deque([root])

            while q:
                node = q.popleft()
                val = next(arr, None)
                if val:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = next(arr, None)
                if val:
                    node.right = TreeNode(val)
                    q.append(node.right)

            return root

    return Wrapper


@sol_decorator
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, po, gpo) -> int:
            if not node:
                return 0

            no = node.val % 2
            return dfs(node.left, no, po) + dfs(node.right, no, po) + (0 if gpo else node.val)

        return dfs(root, 1, 1)


@sol_decorator
class Solution1:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, p_even, gp_even) -> int:
            if not node:
                return 0

            n_even = not node.val % 2
            return dfs(node.left, n_even, p_even) + dfs(node.right, n_even, p_even) + (node.val if gp_even else 0)

        return dfs(root, False, False)


@sol_decorator
class Solution2:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        even = root.val % 2 == 0
        lft = root.left
        if lft:
            res += self.sumEvenGrandparent(lft)
            if even:
                if lft.left:
                    res += lft.left.val
                if lft.right:
                    res += lft.right.val

        rht = root.right
        if rht:
            res += self.sumEvenGrandparent(rht)
            if even:
                if rht.left:
                    res += rht.left.val
                if rht.right:
                    res += rht.right.val

        return res


@sol_decorator
class Solution3:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, pe, gpe) -> int:
            if not node:
                return 0

            ne = 1 - node.val % 2
            return dfs(node.left, ne, pe) + dfs(node.right, ne, pe) + gpe * node.val

        return dfs(root, 0, 0)


def test():
    null = None
    sol = Solution()
    print(sol)

    print('Test 1... ', end='')
    assert sol.sumEvenGrandparent(root=[6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]) == 18
    print('OK')

    print('Test 2... ', end='')
    assert sol.sumEvenGrandparent(root=[1]) == 0
    print('OK')


if __name__ == '__main__':
    test()
