from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        this = self
        while this and other:
            if this.val != other.val:
                return False
            this = this.next
            other = other.next
        return this is None and other is None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head = head.next
        return head


def arr2linkedlist(arr: Optional[List]) -> Optional[ListNode]:
    head = None
    for val in reversed(arr):
        head = ListNode(val, head)
    return head


def test_middle_node():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.middleNode(
        head=arr2linkedlist([1, 2, 3, 4, 5])
    ) == arr2linkedlist([3, 4, 5])
    print("OK")

    print("Test 2... ", end="")
    assert sol.middleNode(
        head=arr2linkedlist([1, 2, 3, 4, 5, 6])
    ) == arr2linkedlist([4, 5, 6])
    print("OK")


if __name__ == "__main__":
    test_middle_node()
