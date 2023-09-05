from itertools import zip_longest


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


def to_linked_list(us_list: list) -> ListNode:
    next_val = None
    for x in reversed(us_list):
        node = ListNode(x, next_val)
        next_val = node
    return next_val


def from_linked_list(linked_list: ListNode) -> list:
    result = []
    while linked_list:
        result.append(linked_list.val)
        linked_list = linked_list.next
    return result


def add_two_numbers_linked_list(l1: ListNode, l2: ListNode) -> ListNode:
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


def add_two_numbers_list(l1: list, l2: list) -> list:
    result, n = [], 0
    for a, b in zip_longest(l1, l2, fillvalue=0):
        s = a + b + n
        result.append(s % 10)
        n = s // 10
    if n:
        result.append(n)
    return result


if __name__ == '__main__':
    print(add_two_numbers_list([2, 4, 3], [5, 6, 4]))
    print(add_two_numbers_list([0], [0]))
    print(add_two_numbers_list([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

    l1, l2 = to_linked_list([2, 4, 3]), to_linked_list([5, 6, 4])
    print(add_two_numbers_linked_list(l1, l2))
    l1, l2 = to_linked_list([0]), to_linked_list([0])
    print(add_two_numbers_linked_list(l1, l2))
    l1, l2 = to_linked_list([9, 9, 9, 9, 9, 9, 9]), to_linked_list([9, 9, 9, 9])
    print(add_two_numbers_linked_list(l1, l2))

    l1, l2 = to_linked_list([2, 4, 3]), to_linked_list([5, 6, 4])
    print(from_linked_list(add_two_numbers_linked_list(l1, l2)))
    l1, l2 = to_linked_list([0]), to_linked_list([0])
    print(from_linked_list(add_two_numbers_linked_list(l1, l2)))
    l1, l2 = to_linked_list([9, 9, 9, 9, 9, 9, 9]), to_linked_list([9, 9, 9, 9])
    print(from_linked_list(add_two_numbers_linked_list(l1, l2)))
