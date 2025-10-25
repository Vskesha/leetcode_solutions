# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = curr = ListNode(-200, head)
        while curr.next and curr.next.val < x:
            curr = curr.next
        last, sec = curr, curr.next
        while curr.next:
            if curr.next.val < x:
                curr.next, last.next = curr.next.next, curr.next
                last = last.next
            else:
                curr = curr.next
        last.next = sec
        return dummy.next


class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = smaller = ListNode()
        second = bigger = ListNode()

        while head:
            if head.val < x:
                smaller.next, head = head, head.next
                smaller = smaller.next
            else:
                bigger.next, head = head, head.next
                bigger = bigger.next

        bigger.next = None
        smaller.next = second.next
        return new_head.next


def main():
    sol = Solution()
    head = ListNode(
        1,
        ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None))))),
    )
    sol.partition(head, 3)


if __name__ == "__main__":
    main()
