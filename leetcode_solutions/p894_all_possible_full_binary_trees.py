from collections import deque
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @lru_cache
    def allPossibleFBT(self, n: int) -> list[TreeNode]:

        if not n % 2:
            return []

        if n == 1:
            return [TreeNode()]

        res = []
        for i in range(1, n, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - i - 1)
            for left in lefts:
                for right in rights:
                    res.append(TreeNode(val=0, left=left, right=right))

        return res


def to_list(tree):
    res = []
    bfs = deque([tree])
    while bfs:
        curr = bfs.popleft()
        if not curr:
            res.append(None)
            continue
        res.append(curr.val)
        bfs.append(curr.left)
        bfs.append(curr.right)

    while res[-1] is None:
        res.pop()

    return res


def print_trees(trees):
    for tree in trees:
        print(to_list(tree))
    print()


def main():
    sol = Solution()
    print_trees(sol.allPossibleFBT(7))
    print_trees(sol.allPossibleFBT(3))


if __name__ == '__main__':
    main()
