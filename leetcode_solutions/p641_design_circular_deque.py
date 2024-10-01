import unittest
from collections import deque

from leetcode_solutions._test_meta import TestMeta


class ListNode:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        nxt = self.head.next
        node = ListNode(val=value, prev=self.head, next=nxt)
        self.head.next = nxt.prev = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        prv = self.tail.prev
        node = ListNode(val=value, prev=prv, next=self.tail)
        self.tail.prev = prv.next = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.val if self.size else -1

    def getRear(self) -> int:
        return self.tail.prev.val if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


class MyCircularDeque2:

    def __init__(self, k: int):
        self.dq = deque()
        self.ms = k

    def insertFront(self, value: int) -> bool:
        if len(self.dq) == self.ms:
            return False
        self.dq.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) == self.ms:
            return False
        self.dq.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.dq:
            return False
        self.dq.popleft()
        return True

    def deleteLast(self) -> bool:
        if not self.dq:
            return False
        self.dq.pop()
        return True

    def getFront(self) -> int:
        return self.dq[0] if self.dq else -1

    def getRear(self) -> int:
        return self.dq[-1] if self.dq else -1

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.ms


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null, true, false = None, True, False
    test_cases = [
        {
            "class": MyCircularDeque,
            "cls_init_args": [3],
            "class_methods": [
                "insertLast",
                "insertLast",
                "insertFront",
                "insertFront",
                "getRear",
                "isFull",
                "deleteLast",
                "insertFront",
                "getFront",
            ],
            "args": [[1], [2], [3], [4], [], [], [], [4], []],
            "expected": [true, true, true, false, 2, true, true, true, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
