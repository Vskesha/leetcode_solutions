class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = set()
        return self.traverse(root, nums, k)

    def traverse(self, node, nums, k):
        if node is None:
            return False
        if k - node.val in nums:
            return True
        nums.add(node.val)
        return self.traverse(node.left, nums, k) or self.traverse(node.right, nums, k)


def main():
    sol = Solution


if __name__ == '__main__':
    main()