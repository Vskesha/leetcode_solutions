from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        self.original_serialize = instance.serialize
        self.original_deserialize = instance.deserialize
        instance.serialize = self.serialize
        instance.deserialize = self.deserialize
        return instance

    def serialize(self, root: Optional[List]) -> str:
        root = self.list2tree(root)
        return self.original_serialize(root)

    def deserialize(self, data: str) -> Optional[List]:
        result = self.original_deserialize(data)
        return self.tree2list(result)

    @staticmethod
    def list2tree(nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        vals = iter(nums)
        root = TreeNode(next(vals))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root

    @staticmethod
    def tree2list(root: Optional[TreeNode]) -> List:
        arr = []
        if not root:
            return arr

        arr.append(root)
        i = li = 0

        while i < len(arr):
            node = arr[i]
            if node is not None:
                arr.append(node.left)
                arr.append(node.right)
                arr[i] = node.val
                li = i
            i += 1

        return arr[: li + 1]


@CodecDecorator
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        i = 0
        li = 0
        res = [root]

        while i < len(res):
            node = res[i]
            if node is not None:
                res.append(node.left)
                res.append(node.right)
                res[i] = node.val
                li = i
            i += 1

        return " ".join(str(k) for k in res[: li + 1])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        lst = [None if k == "None" else int(k) for k in data.split()]

        vals = iter(lst)
        root = TreeNode(next(vals))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


def test_codec():
    codec = Codec()
    null = None

    print("Test 1... ", end="")
    root = [1, 2, 3, null, null, 4, 5]
    assert codec.deserialize(codec.serialize(root=root)) == root
    print("OK")

    print("Test 2... ", end="")
    root = []
    assert codec.deserialize(codec.serialize(root=root)) == root
    print("OK")


if __name__ == "__main__":
    test_codec()
