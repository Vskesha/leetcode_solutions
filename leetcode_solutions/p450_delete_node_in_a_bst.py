from collections import deque
from functools import wraps
from typing import Optional, List


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

        def deleteNode(self, root: Optional[List], key: int) -> Optional[List]:
            root = self.list2tree(root)
            result = self.original.deleteNode(root, key)
            return self.tree2list(result)

        def list2tree(self, arr: Optional[List]) -> Optional[TreeNode]:
            if not arr:
                return None

            vals = iter(arr)
            root = TreeNode(next(vals))
            que = deque([root])

            while que:
                node = que.popleft()
                val = next(vals, None)
                if val is not None:
                    node.left = TreeNode(val)
                    que.append(node.left)
                val = next(vals, None)
                if val is not None:
                    node.right = TreeNode(val)
                    que.append(node.right)

            return root

        def tree2list(self, root: Optional[TreeNode]) -> Optional[List]:
            arr = []
            if not root:
                return arr

            arr.append(root)
            i = 0

            while i < len(arr):
                node = arr[i]
                if node is not None:
                    arr.append(node.left)
                    arr.append(node.right)
                    arr[i] = node.val
                i += 1

            while arr[-1] is None:
                arr.pop()

            return arr

    return Wrapper


@sol_decorator
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        return root


@sol_decorator
class Solution2:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def del_node(node, parent, key, dir):
            if not node:
                return
            elif node.val > key:
                del_node(node.left, node, key, "left")
            elif node.val < key:
                del_node(node.right, node, key, "right")
            elif node.left and node.right:
                repl = node.right
                while repl.left:
                    repl = repl.left
                node.val = repl.val
                del_node(node.right, node, repl.val, "right")
            else:
                setattr(parent, dir, node.left or node.right)

        dummy = TreeNode(left=root)
        del_node(root, dummy, key, "left")
        return dummy.left


def test_delete_node():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.deleteNode(root=[5, 3, 6, 2, 4, null, 7], key=3) == [
        5,
        4,
        6,
        2,
        null,
        null,
        7,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.deleteNode(root=[5, 3, 6, 2, 4, null, 7], key=0) == [
        5,
        3,
        6,
        2,
        4,
        null,
        7,
    ]
    print("OK")

    print("Test 3... ", end="")
    assert sol.deleteNode(root=[], key=0) == []
    print("OK")


if __name__ == "__main__":
    test_delete_node()
