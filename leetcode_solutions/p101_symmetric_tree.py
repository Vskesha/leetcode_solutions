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

        def isSymmetric(self, root: Optional[list]) -> bool:
            root = self.list2tree(root)
            return self.original.isSymmetric(root)

        def list2tree(self, arr: Optional[List[int]]) -> Optional[TreeNode]:
            if not arr:
                return None

            vals = iter(arr)
            root = TreeNode(next(vals))
            q = deque([root])

            while q:
                node = q.popleft()
                val = next(vals, None)
                if val:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = next(vals, None)
                if val:
                    node.right = TreeNode(val)
                    q.append(node.right)

            return root

    return Wrapper


@sol_decorator
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and dfs(n1.left, n2.right) and dfs(n1.right, n2.left)

        return dfs(root.left, root.right)
    

@sol_decorator
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(n1, n2):
            if n1 and n2:
                return n1.val == n2.val and dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
            if n1 or n2:
                return False
            return True

        return dfs(root.left, root.right)


def test():
    null = None
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.isSymmetric(root=[1, 2, 2, 3, 4, 4, 3]) is True
    print('OK')

    print('Test 2... ', end='')
    assert sol.isSymmetric(root=[1, 2, 2, null, 3, null, 3]) is False
    print('OK')


if __name__ == '__main__':
    test()
