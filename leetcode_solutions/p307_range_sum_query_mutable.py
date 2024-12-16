import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class TreeNode:
    def __init__(self, li, ri, val=0, left=None, right=None):
        self.li = li
        self.ri = ri
        self.val = val
        self.left = left
        self.right = right


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * (len(nums))
        self.itree = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def update(self, index: int, val: int) -> None:
        d = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.itree):
            self.itree[i] += d
            i += i & (-i)

    def sum_till(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self.itree[i]
            i -= i & (-i)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        sr = self.sum_till(right + 1)
        sl = self.sum_till(left)
        return sr - sl


class NumArray1:
    def __init__(self, nums: List[int]):
        self.root = self.create_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int, node=None) -> None:
        node = node or self.root

        if node.li == node.ri:
            node.val = val
            return

        if index > node.left.ri:
            self.update(index, val, node.right)
        else:
            self.update(index, val, node.left)

        node.val = node.left.val + node.right.val

    def sumRange(self, left: int, right: int, node=None) -> int:
        node = node or self.root

        if node.ri < left or node.li > right:
            return 0

        if node.ri <= right and node.li >= left:
            return node.val

        return self.sumRange(left, right, node.left) + self.sumRange(
            left, right, node.right
        )

    def create_tree(self, nums, li, ri) -> TreeNode:
        node = TreeNode(li=li, ri=ri)

        if li == ri:
            node.val = nums[li]
            return node

        mid = (li + ri) // 2
        node.left = self.create_tree(nums, li, mid)
        node.right = self.create_tree(nums, mid + 1, ri)
        node.val = node.left.val + node.right.val

        return node


class NumArray2:
    def __init__(self, nums: List[int]):
        self.root = self.create_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def upd(node):
            if node.li == node.ri:
                node.val = val
                return

            if index > node.left.ri:
                upd(node.right)
            else:
                upd(node.left)

            node.val = node.left.val + node.right.val

        upd(self.root)

    def sumRange(self, left: int, right: int) -> int:
        def sumr(node) -> int:
            if node.ri < left or node.li > right:
                return 0

            if node.ri <= right and node.li >= left:
                return node.val

            return sumr(node.left) + sumr(node.right)

        return sumr(self.root)

    def create_tree(self, nums, li, ri) -> TreeNode:
        node = TreeNode(li=li, ri=ri)

        if li == ri:
            node.val = nums[li]
            return node

        mid = (li + ri) // 2
        node.left = self.create_tree(nums, li, mid)
        node.right = self.create_tree(nums, mid + 1, ri)
        node.val = node.left.val + node.right.val

        return node


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": NumArray,
            "cls_init_args": [[1, 3, 5]],
            "class_methods": ["sumRange", "update", "sumRange"],
            "args": [[0, 2], [1, 2], [0, 2]],
            "expected": [9, null, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()


# def test_num_array():
#     null = None
#     commands = ["NumArray", "sumRange", "update", "sumRange"]
#     params = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
#     output = [null, 9, null, 8]
#     na = NumArray(*params[0])
#     for i in range(1, len(commands)):
#         print(f"Test {i}... ", end="")
#         res = getattr(na, commands[i])(*params[i])
#         assert res == output[i]
#         print("OK")
#
#
# if __name__ == "__main__":
#     test_num_array()
