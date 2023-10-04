from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        i = 0
        while head:
            ans.append(0)
            v = head.val
            while stack and stack[-1][0] < v:
                _, idx = stack.pop()
                ans[idx] = v
            stack.append((v, i))
            i += 1
            head = head.next
        return ans


def test():
    sol = Solution()


if __name__ == '__main__':
    test()
