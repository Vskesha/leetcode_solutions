from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        self.original_getAllElements = instance.getAllElements
        instance.getAllElements = self.getAllElements
        return instance

    def getAllElements(self, root1: List[int], root2: List[int]) -> List[int]:
        root1 = self.list_to_tree(root1)
        root2 = self.list_to_tree(root2)
        return self.original_getAllElements(root1, root2)  # noqa

    def list_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
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


@SolDecorator
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def to_list(node) -> None:
            if not node:
                return
            to_list(node.left)
            arr.append(node.val)
            to_list(node.right)

        arr = []
        to_list(root1)
        to_list(root2)

        return sorted(arr)


@SolDecorator
class Solution1:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def to_list(node) -> list:
            if not node:
                return []
            return to_list(node.left) + [node.val] + to_list(node.right)

        list1, list2 = to_list(root1), to_list(root2)
        l1, l2 = len(list1), len(list2)
        i, j = 0, 0

        res = []
        while i < l1 and j < l2:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        while i < l1:
            res.append(list1[i])
            i += 1

        while j < l2:
            res.append(list2[j])
            j += 1

        return res


@SolDecorator
class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def tree_gen(node):
            if node.left:
                yield from tree_gen(node.left)
            yield node.val
            if node.right:
                yield from tree_gen(node.right)

        vals1 = tree_gen(root1) if root1 else iter([None])
        vals2 = tree_gen(root2) if root2 else iter([None])

        res = []
        a, b = next(vals1), next(vals2)
        while a is not None and b is not None:
            if a < b:
                res.append(a)
                a = next(vals1, None)
            else:
                res.append(b)
                b = next(vals2, None)

        while a is not None:
            res.append(a)
            a = next(vals1, None)

        while b is not None:
            res.append(b)
            b = next(vals2, None)

        return res


def test_get_all_elements():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.getAllElements(root1=[2, 1, 4], root2=[1, 0, 3]) == [
        0,
        1,
        1,
        2,
        3,
        4,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.getAllElements(root1=[1, null, 8], root2=[8, 1]) == [1, 1, 8, 8]
    print("OK")


if __name__ == "__main__":
    test_get_all_elements()
