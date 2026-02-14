from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        curr = dummy = ListNode(0, head)

        for i in range(left - 1):
            curr = curr.next

        end1, end2 = curr, curr.next
        prev, curr = end2, end2.next

        for i in range(right - left):
            curr.next, prev, curr = prev, curr, curr.next

        end1.next = prev
        end2.next = curr

        return dummy.next
