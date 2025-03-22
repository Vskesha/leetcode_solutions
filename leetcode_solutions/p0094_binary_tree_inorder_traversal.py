from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol_decorator(cls):
    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def inorderTraversal(self, root: Optional[List[int]]) -> List[int]:
            root = self.list2tree(root)
            return self.original.inorderTraversal(root)

        @staticmethod
        def list2tree(arr: Optional[List[int]]) -> Optional[TreeNode]:
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


@sol_decorator
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans


@sol_decorator
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root
        while curr:
            while curr.left:
                lf = curr.left
                while lf.right:
                    lf = lf.right
                lf.right = curr
                curr.left, curr = None, curr.left
            ans.append(curr.val)
            curr = curr.right
        return ans


@sol_decorator
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node:
                inorder(node.left)
                ans.append(node.val)
                inorder(node.right)
        ans = []
        inorder(root)
        return ans


def test():
    null = None
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.inorderTraversal(root=[1, null, 2, 3]) == [1, 3, 2]
    print('OK')

    print('Test 2... ', end='')
    assert sol.inorderTraversal(root=[]) == []
    print('OK')

    print('Test 3... ', end='')
    assert sol.inorderTraversal(root=[1]) == [1]
    print('OK')


if __name__ == '__main__':
    test()
