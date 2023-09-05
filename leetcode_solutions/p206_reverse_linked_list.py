# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur, nxt = head, head.next
        cur.next = None
        while nxt:
            nxt.next, nxt, cur = cur, nxt.next, nxt
        return cur


def main():
    sol = Solution()


if __name__ == '__main__':
    main()
