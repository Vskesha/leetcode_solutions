from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        while curr:
            curr.next, curr = Node(curr.val, curr.next), curr.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head.next
        while curr.next:
            curr.next, curr = curr.next.next, curr.next.next

        return head.next


class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        nodes = []
        curr = head
        i = 0
        while curr:
            curr.index = i
            nodes.append(Node(curr.val))
            curr = curr.next
            i += 1

        nodes.append(None)
        curr = head
        i = 0
        while curr:
            nodes[i].next = nodes[i + 1]
            if curr.random:
                nodes[i].random = nodes[curr.random.index]
            curr = curr.next
            i += 1

        return nodes[0]
