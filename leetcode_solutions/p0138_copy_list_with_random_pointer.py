from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def decorator(cls):
    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def copyRandomList(self, head: list) -> list[int]:
            head = self.list_to_linked_list(head)
            result = self.original.copyRandomList(head)
            result = self.linked_list_to_list(result)
            return result

        @staticmethod
        def list_to_linked_list(array: list) -> "Optional[Node]":

            nodes = []
            for val, _ in array:
                nodes.append(Node(val))

            nodes.append(None)
            for i in range(len(array)):
                nodes[i].next = nodes[i + 1]
                if array[i][1] is not None:
                    nodes[i].random = nodes[array[i][1]]

            return nodes[0]

        @staticmethod
        def linked_list_to_list(head: "Optional[Node]") -> list:
            if not head:
                return []

            curr = head
            i = 0
            while curr:
                curr.index = i
                i += 1
                curr = curr.next

            curr = head
            ans = []
            while curr:
                ans.append(
                    [curr.val, curr.random.index if curr.random else None]
                )
                curr = curr.next

            curr = head
            while curr:
                delattr(curr, "index")
                curr = curr.next

            return ans

    return Wrapper


@decorator
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        curr = head

        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        hc = copy = Node(0)
        curr = head
        while curr:
            curr.next, copy.next = curr.next.next, curr.next
            curr = curr.next
            copy = copy.next

        return hc.next


@decorator
class Solution2:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
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


def test():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    for a, b in zip(
        sol.copyRandomList(
            head=[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
        ),
        [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]],
    ):
        assert a == b
    print("OK")

    print("Test 2... ", end="")
    for a, b in zip(
        sol.copyRandomList(head=[[1, 1], [2, 1]]), [[1, 1], [2, 1]]
    ):
        assert a == b
    print("OK")

    print("Test 3... ", end="")
    for a, b in zip(
        sol.copyRandomList(head=[[3, null], [3, 0], [3, null]]),
        [[3, null], [3, 0], [3, null]],
    ):
        assert a == b
    print("OK")


if __name__ == "__main__":
    test()
