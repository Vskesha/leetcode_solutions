import unittest
from math import inf

from leetcode_solutions._test_meta import TestMeta


class ListNode:
    def __init__(self, key="", val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next, self.next.prev = self.next, self.prev

    def insert_after(self, other):
        nxt = other.next
        other.next = self
        self.prev = other
        self.next = nxt
        nxt.prev = self

    def move_forward(self):
        prv = self.prev
        nxt = self.next
        self.next = nxt.next
        nxt.next.prev = self
        prv.next = nxt
        nxt.prev = prv
        nxt.next = self
        self.prev = nxt

    def __repr__(self) -> str:
        return f"ListNode({self.key}, {self.val})"


class AllOne:

    def __init__(self):
        self.head = ListNode(val=-inf)
        self.tail = ListNode(val=inf, prev=self.head)
        self.head.next = self.tail
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val += 1
            while node.val > node.next.val:
                node.move_forward()
        else:
            node = ListNode(key=key, val=1)
            node.insert_after(self.head)
            self.nodes[key] = node

    def dec(self, key: str) -> None:
        node = self.nodes[key]
        if node.val == 1:
            node.remove()
            del self.nodes[key]
        else:
            node.val -= 1
            while node.val < node.prev.val:
                node.prev.move_forward()

    def getMaxKey(self) -> str:
        return self.tail.prev.key

    def getMinKey(self) -> str:
        return self.head.next.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": AllOne,
            "class_methods": [
                "inc",
                "inc",
                "getMaxKey",
                "getMinKey",
                "inc",
                "getMaxKey",
                "getMinKey",
            ],
            "args": [["hello"], ["hello"], [], [], ["leet"], [], []],
            "expected": [null, null, "hello", "hello", null, "hello", "leet"],
        },
        {
            "class": AllOne,
            "class_methods": [
                "inc",
                "inc",
                "inc",
                "inc",
                "inc",
                "inc",
                "getMaxKey",
                "inc",
                "dec",
                "getMaxKey",
                "dec",
                "inc",
                "getMaxKey",
                "inc",
                "inc",
                "dec",
                "dec",
                "dec",
                "dec",
                "getMaxKey",
                "inc",
                "inc",
                "inc",
                "inc",
                "inc",
                "inc",
                "getMaxKey",
                "getMinKey",
            ],
            "args": [
                ["hello"],
                ["world"],
                ["leet"],
                ["code"],
                ["ds"],
                ["leet"],
                [],
                ["ds"],
                ["leet"],
                [],
                ["ds"],
                ["hello"],
                [],
                ["hello"],
                ["hello"],
                ["world"],
                ["leet"],
                ["code"],
                ["ds"],
                [],
                ["new"],
                ["new"],
                ["new"],
                ["new"],
                ["new"],
                ["new"],
                [],
                [],
            ],
            "expected": [
                null,
                null,
                null,
                null,
                null,
                null,
                "leet",
                null,
                null,
                "ds",
                null,
                null,
                "hello",
                null,
                null,
                null,
                null,
                null,
                null,
                "hello",
                null,
                null,
                null,
                null,
                null,
                null,
                "new",
                "hello",
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
