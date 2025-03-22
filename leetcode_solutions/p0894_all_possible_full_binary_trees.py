from collections import defaultdict, deque
from functools import lru_cache
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []

        trees = defaultdict(list)
        trees[1].append(TreeNode())

        for total_len in range(3, n + 1, 2):
            for left_len in range(1, total_len, 2):
                right_len = total_len - left_len - 1
                for ltree in trees[left_len]:
                    for rtree in trees[right_len]:
                        trees[total_len].append(TreeNode(val=0, left=ltree, right=rtree))

        return trees[n]


class Solution2:
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


def test(n, out, sol):
    all_possible = sol.allPossibleFBT(n)
    assert len(all_possible) == len(out)
    for tree in all_possible:
        exist = False
        for t in out:
            if t == to_list(tree):
                exist = True
                break
        assert exist


def main():
    sol = Solution()
    null = None

    print('Test 1... ', end='')
    test(n=3, out=[[0, 0, 0]], sol=sol)
    print('OK')

    print('Test 1... ', end='')
    test(n=7,
         out=[[0, 0, 0, null, null, 0, 0, null, null, 0, 0], [0, 0, 0, null, null, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, null, null, null, null, 0, 0], [0, 0, 0, 0, 0, null, null, 0, 0]], sol=sol)
    print('OK')


if __name__ == '__main__':
    main()
