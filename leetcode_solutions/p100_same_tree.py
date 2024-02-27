import inspect
from collections import deque
from functools import wraps
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_from_list(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrap = cls(*args, **kwargs)

        def isSameTree(self, p: list[int], q: list[int]) -> bool:
            p = self.tree_from_arr(p)
            q = self.tree_from_arr(q)
            return self.wrap.isSameTree(p, q)

        @staticmethod
        def tree_from_arr(arr: list[int]) -> Optional[TreeNode]:
            if not arr:
                return None
            arr = iter(arr)
            root = TreeNode(next(arr))
            bfs = deque([root])
            while bfs:
                node = bfs.popleft()
                val = next(arr, None)
                if val is not None:
                    node.left = TreeNode(val)
                    bfs.append(node.left)
                val = next(arr, None)
                if val is not None:
                    node.right = TreeNode(val)
                    bfs.append(node.right)
            return root

    return Wrapper


@make_tree_from_list
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs1 = deque([p])
        bfs2 = deque([q])

        while bfs1 and bfs2:
            a = bfs1.popleft()
            b = bfs2.popleft()
            if (a and not b) or (b and not a) or (a and b and a.val != b.val):
                return False
            if a:
                bfs1.append(a.left)
                bfs1.append(a.right)
            if b:
                bfs2.append(b.left)
                bfs2.append(b.right)

        return True


@make_tree_from_list
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs1 = deque([p])
        bfs2 = deque([q])

        while bfs1 and bfs2:
            a = bfs1.popleft()
            b = bfs2.popleft()
            if (a and not b) or (b and not a) or (a and b and a.val != b.val):
                return False
            if a:
                bfs1.append(a.left)
                bfs1.append(a.right)
            if b:
                bfs2.append(b.left)
                bfs2.append(b.right)
        return True


@make_tree_from_list
class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True
        if (p is None) ^ (q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test():
    sol = Solution()
    # print(type(sol))
    # print(dir(sol))
    # print(inspect.signature(sol.isSameTree))

    print("Test 1... ", end="")
    assert sol.isSameTree(p=[1, 2, 3], q=[1, 2, 3]) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.isSameTree(p=[1, 2], q=[1, None, 2]) is False
    print("OK")

    print("Test 3... ", end="")
    assert sol.isSameTree(p=[1, 2, 1], q=[1, 1, 2]) is False
    print("OK")


if __name__ == "__main__":
    test()
