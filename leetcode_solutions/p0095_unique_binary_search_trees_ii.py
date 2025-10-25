# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:

        def trees(vals: list):

            if not vals:
                return [None]

            if len(vals) == 1:
                return [TreeNode(vals[0])]

            ans_list = []
            for i, val in enumerate(vals):
                lefts = vals[:i]
                rights = vals[i + 1 :]
                for left in trees(lefts):
                    for right in trees(rights):
                        ans_list.append(TreeNode(val, left, right))

            return ans_list

        values = list(range(1, n + 1))
        return trees(values)


def main():
    sol = Solution()
    sol.generateTrees(n=3)
    sol.generateTrees(n=1)
    sol.generateTrees(n=4)


if __name__ == "__main__":
    main()
