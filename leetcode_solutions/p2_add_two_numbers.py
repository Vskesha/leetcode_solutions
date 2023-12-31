from itertools import zip_longest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val

    def __str__(self):
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
        return str(res)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = curr = ListNode()
        over = 0
        while l1 or l2 or over:
            s = over
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            curr.next = ListNode()
            curr = curr.next
            over, curr.val = divmod(s, 10)
        return first.next

    def add_two_numbers_list(self, l1: list, l2: list) -> list:
        result, n = [], 0
        for a, b in zip_longest(l1, l2, fillvalue=0):
            s = a + b + n
            result.append(s % 10)
            n = s // 10
        if n:
            result.append(n)
        return result

    def to_linked_list(self, us_list: list) -> ListNode:
        next_val = None
        for x in reversed(us_list):
            node = ListNode(x, next_val)
            next_val = node
        return next_val

    def from_linked_list(self, linked_list: ListNode) -> list:
        result = []
        while linked_list:
            result.append(linked_list.val)
            linked_list = linked_list.next
        return result


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.from_linked_list(sol.addTwoNumbers(sol.to_linked_list([2, 4, 3]), sol.to_linked_list([5, 6, 4]))) == [7, 0, 8]
    print('ok\nTest 2 ... ', end='')
    assert sol.from_linked_list(sol.addTwoNumbers(sol.to_linked_list([0]), sol.to_linked_list([0]))) == [0]
    print('ok\nTest 3 ... ', end='')
    assert sol.from_linked_list(sol.addTwoNumbers(sol.to_linked_list([9, 9, 9, 9, 9, 9, 9]), sol.to_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
    print('ok')


if __name__ == '__main__':
    test()
