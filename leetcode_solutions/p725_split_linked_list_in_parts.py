from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        if k > size:
            while curr:
                res.append(curr)
                curr.next, curr = None, curr.next
            res += [None] * (k - size)
        else:
            num = size // k - 1
            fst = size % k
            for i in range(k):
                res.append(curr)
                for _ in range(num + (i < fst)):
                    curr = curr.next
                curr.next, curr = None, curr.next
        return res


class Solution2:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        if k > size:
            while curr:
                res.append(curr)
                curr.next, curr = None, curr.next
            res += [None] * (k - size)
        else:
            for i in range(k, 0, -1):
                res.append(curr)
                count = (size - 1) // i + 1
                size -= count
                for _ in range(count - 1):
                    curr = curr.next
                curr.next, curr = None, curr.next
        return res


def test():
    sol = Solution()


if __name__ == '__main__':
    test()
