from collections import deque
from typing import Optional


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

        def widthOfBinaryTree(self, root: list) -> int:
            root = self.list_to_tree(root)
            return self.original.widthOfBinaryTree(root)

        def list_to_tree(self, root: list) -> Optional[TreeNode]:
            if not root:
                return None

            root = iter(root)
            head = TreeNode(next(root))
            q = deque([head])

            while q:
                node = q.popleft()
                val = next(root, None)
                if val:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = next(root, None)
                if val:
                    node.right = TreeNode(val)
                    q.append(node.right)

            return head

    return Wrapper


@decorator
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0
        bfs = deque()
        bfs.append((root, 0))

        while bfs:
            lvl = bfs[-1][1] - bfs[0][1]
            ans = max(ans, lvl)
            for _ in range(len(bfs)):
                curr, width = bfs.popleft()
                if curr.left:
                    bfs.append((curr.left, width * 2))
                if curr.right:
                    bfs.append((curr.right, width * 2 + 1))

        return ans + 1


@decorator
class Solution2:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, width = deque([(root, 0)]), 0
        while q:
            width = max(width, q[-1][1] - q[0][1])
            for _ in range(len(q)):
                node, k = q.popleft()
                if node.left:
                    q.append((node.left, k * 2 - 1))
                if node.right:
                    q.append((node.right, k * 2))
        return width + 1


def test():
    null = None
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.widthOfBinaryTree(root=[1, 3, 2, 5, 3, null, 9]) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.widthOfBinaryTree(root=[1, 3, 2, 5, null, null, 9, 6, null, 7]) == 7
    print('OK')

    print('Test 3... ', end='')
    assert sol.widthOfBinaryTree(root=[1, 3, 2, 5]) == 2
    print('OK')


if __name__ == '__main__':
    test()
