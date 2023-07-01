# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode()
        ad = 0
        while l1 or l2 or ad:
            curr.next = ListNode()
            curr = curr.next
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            curr.val, ad = divmod(d1 + d2 + ad, 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


def main():
    sol = Solution()
    l1 = curr = ListNode(2)
    curr.next = ListNode(4)
    curr = curr.next
    curr.next = ListNode(3)
    l2 = curr = ListNode(5)
    curr.next = ListNode(6)
    curr = curr.next
    curr.next = ListNode(4)
    result = sol.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next


if __name__ == '__main__':
    main()
