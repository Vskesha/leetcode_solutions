import test


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} --> {self.next} '

    def __repr__(self):
        return f'{self.val} --> {self.next} '


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


def reverse_k_groups(head, k):
    result = prev = ListNode()
    i, dummy, end = 0, None, head
    while head:
        curr = head
        head = head.next
        curr.next = dummy
        dummy = curr
        i += 1
        if i == k:
            prev.next = curr
            prev = end
            i, dummy, end = 0, None, head
    while dummy:
        curr = dummy
        dummy = dummy.next
        curr.next = head
        head = curr
    prev.next = head
    return result.next


def reverse_k_groups3(head, k):
    prev = result = ListNode()
    sub = []
    while head:
        sub.append(head)
        head = head.next
        if len(sub) == k:
            for node in reversed(sub):
                prev.next = node
                prev = node
            prev.next = head
            sub = []
    return result.next


def reverse_k_groups1(head, k):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    new_order = []
    for i in range(0, len(result), k):
        sub = result[i:i + k]
        new_order += reversed(sub) if len(sub) == k else sub

    nxt = None
    for val in reversed(new_order):
        node = ListNode(val, nxt)
        nxt = node

    return nxt


def reverse_k_groups2(head, k):
    prev = result = ListNode()
    prev.next = curr = head
    while True:
        values = []
        for _ in range(k):
            try:
                values.append(curr.val)
                curr = curr.next
            except AttributeError:
                break
        else:
            for val in reversed(values):
                node = ListNode(val)
                prev.next = node
                prev = node
            prev.next = curr
            continue
        break
    return result.next


if __name__ == '__main__':
    test.assert_equals(from_linked_list(reverse_k_groups(head=to_linked_list([1, 2, 3, 4, 5]), k=2)), [2, 1, 4, 3, 5])
    test.assert_equals(from_linked_list(reverse_k_groups(head=to_linked_list([1, 2, 3, 4, 5]), k=3)), [3, 2, 1, 4, 5])
