from collections import deque
from typing import List, Optional


def tree_to_list_decorator(cls):

    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def findTarget(self, root: list[int], k: int) -> bool:
            root = self.list_to_tree(root)
            return self.original.findTarget(root, k)

        def list_to_tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            nums = iter(nums)
            root = TreeNode(next(nums))
            q = deque([root])
            while q:
                node = q.popleft()
                val = next(nums, None)
                if val:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = next(nums, None)
                if val:
                    node.right = TreeNode(val)
                    q.append(node.right)

            return root

    return Wrapper


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@tree_to_list_decorator
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def flatten(root, vals):
            if not root:
                return
            flatten(root.left, vals)
            vals.append(root.val)
            flatten(root.right, vals)

        vals = []
        flatten(root, vals)
        l, r = 0, len(vals) - 1

        while l < r:
            sm = vals[l] + vals[r]
            if sm < k:
                l += 1
            elif sm > k:
                r -= 1
            else:
                return True

        return False


@tree_to_list_decorator
class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        return self.traverse(root, nums, k)

    def traverse(self, node, nums, k):
        if node is None:
            return False
        if k - node.val in nums:
            return True
        nums.add(node.val)
        return self.traverse(node.left, nums, k) or self.traverse(
            node.right, nums, k
        )


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findTarget(root=[5, 3, 6, 2, 4, null, 7], k=9) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.findTarget(root=[5, 3, 6, 2, 4, null, 7], k=28) is False
    print("OK")


if __name__ == "__main__":
    test()
