from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Reversing given lists and adding respecting nodes and forming new linked list from the end
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def reverse(l_list: ListNode):
            cur, nxt = l_list, l_list.next
            cur.next = None
            while nxt:
                nxt.next, nxt, cur = cur, nxt.next, nxt
            return cur

        l1 = reverse(l1)
        l2 = reverse(l2)
        add = 0
        nxt = None
        cur = None
        while l1 or l2 or add:
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            cur = ListNode(add % 10, nxt)
            add //= 10
            nxt = cur

        return cur


# Solution through the transformation to int, addindg and transformation to linked list
class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        n2 = 0
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
        res = n1 + n2
        if not res:
            return ListNode()
        nxt = None
        while res:
            nxt = ListNode(val=res % 10, next=nxt)
            res //= 10
        return nxt


def test():
    sol = Solution()


if __name__ == "__main__":
    test()
