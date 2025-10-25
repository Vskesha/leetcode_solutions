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

        def tree2str(self, root: list) -> str:
            root = self.list2tree(root)
            return self.original.tree2str(root)

        def list2tree(self, arr: list) -> Optional[TreeNode]:
            if not arr:
                return None

            arr = iter(arr)
            root = TreeNode(next(arr))
            st, i = [root], 0

            while i < len(st):
                curr = st[i]
                val = next(arr, None)
                if val:
                    curr.left = TreeNode(val)
                    st.append(curr.left)
                val = next(arr, None)
                if val:
                    curr.right = TreeNode(val)
                    st.append(curr.right)
                i += 1

            return root

    return Wrapper


@sol_decorator
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = str(root.val)
        if root.right:
            if root.left:
                res += f"({self.tree2str(root.left)})"
            else:
                res += "()"
            res += f"({self.tree2str(root.right)})"
        elif root.left:
            res += f"({self.tree2str(root.left)})"
        return res


@sol_decorator
class Solution2:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = str(root.val)
        if root.left or root.right:
            res += f"({self.tree2str(root.left)})"
        if root.right:
            res += f"({self.tree2str(root.right)})"
        return res


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.tree2str(root=[1, 2, 3, 4]) == "1(2(4))(3)"
    print("OK")

    print("Test 2... ", end="")
    assert sol.tree2str(root=[1, 2, 3, null, 4]) == "1(2()(4))(3)"
    print("OK")


if __name__ == "__main__":
    test()
