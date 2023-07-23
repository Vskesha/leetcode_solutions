from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []

        self.ans = []

        def tree_from_comb(comb):
            new = [TreeNode() for _ in range(n)]
            i = 0
            j = 1
            while j < n:
                if comb[i]:
                    new[i].left = new[j]
                    j += 1
                    new[i].right = new[j]
                    j += 1
                i += 1
            self.ans.append(new[0])

        def create_combs(comb, i, total):
            if total == n:
                tree_from_comb(comb)
                return

            if i < total - 1:
                create_combs(comb, i + 1, total)
            comb[i] = 1
            create_combs(comb, i + 1, total + 2)
            comb[i] = 0

        comb = [0] * n
        create_combs(comb, 0, 1)
        return self.ans

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
