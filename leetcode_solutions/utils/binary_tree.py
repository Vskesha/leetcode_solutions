from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_binary_tree(arr: Optional[List]) -> TreeNode:
    if not arr:
        return None

    vals = iter(arr)
    root = TreeNode(next(vals))
    queue = deque()
    queue.append(root)

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
