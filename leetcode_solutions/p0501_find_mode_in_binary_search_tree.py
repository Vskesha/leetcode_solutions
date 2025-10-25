from collections import Counter
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        max_streak, curr_streak, curr_number, ans = 0, 0, 0, []

        while root:
            if root.left:
                friend = root.left
                while friend.right:
                    friend = friend.right
                friend.right = root
                root.left, root = None, root.left
            else:
                num = root.val
                if num == curr_number:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_number = num
                if curr_streak == max_streak:
                    ans.append(num)
                elif curr_streak > max_streak:
                    ans = [num]
                    max_streak = curr_streak
                root = root.right

        return ans


class Solution1:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        count = Counter()
        dfs(root)

        ans, mf = [], max(count.values())
        for el, fr in count.items():
            if fr == mf:
                ans.append(el)

        return ans


class Solution2:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        count = Counter()
        dfs(root)
        ans, mf = [], 0
        for el, fr in count.items():
            if fr == mf:
                ans.append(el)
            elif fr > mf:
                mf = fr
                ans = [el]

        return ans


class Solution3:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()

        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        mc = count.most_common()
        mf = mc[0][1]
        ans = []
        for el, fr in mc:
            if fr == mf:
                ans.append(el)
            else:
                break
        return ans


class Solution4:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        count = Counter()
        stack = [root]
        while stack:
            curr = stack.pop()
            count[curr.val] += 1
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        ans, mf = [], max(count.values())
        for el, fr in count.items():
            if fr == mf:
                ans.append(el)

        return ans


class Solution5:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(node, sl):
            if not node:
                return
            inorder(node.left, sl)
            sl.append(node.val)
            inorder(node.right, sl)

        sl = []
        inorder(root, sl)

        mf, cf, pn, ans = 0, 0, sl[0], []
        for n in sl:
            cf = cf + 1 if n == pn else 1
            pn = n
            if cf == mf:
                ans.append(n)
            elif cf > mf:
                ans = [n]
                mf = cf

        return ans


class Solution6:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if node.val == aux[2]:
                aux[1] += 1
            else:
                aux[1] = 1
                aux[2] = node.val

            if aux[1] == aux[0]:
                ans.append(node.val)
            elif aux[1] > aux[0]:
                ans.clear()
                ans.append(node.val)
                aux[0] = aux[1]

            inorder(node.right)

        aux = [0, 0, 0]  # max_streak, curr_streak, curr_number
        ans = []
        inorder(root)

        return ans


def test():
    sol = Solution()


if __name__ == "__main__":
    test()
