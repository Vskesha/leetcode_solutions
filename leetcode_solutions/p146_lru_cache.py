import unittest
from collections import OrderedDict


# Solution using OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key)
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)


# Solution using dictionary and double-linked list
class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self) -> None:
        prev = self.prev
        next = self.next
        prev.next = next
        next.prev = prev

    def insert_after(self, other) -> None:
        after_start = other.next
        after_start.prev = self
        self.next = after_start
        other.next = self
        self.prev = other


class LRUCache2:
    def __init__(self, capacity: int):
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        node.remove()
        node.insert_after(self.start)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            node.remove()
        else:
            node = ListNode(key, value)
        node.insert_after(self.start)
        self.d[key] = node
        if len(self.d) > self.capacity:
            last = self.end.prev
            last.remove()
            key = last.key
            del self.d[key]


class TestLRUCache(unittest.TestCase):

    def test_put_get_methods(self):
        print("Testing LRUCache... ")
        null = None
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        expected = [null, null, null, 1, null, -1, null, -1, 3, 4]
        cache = LRUCache(*args[0])
        for i in range(1, len(args)):
            print(f"    Test {i}... ", end="")
            self.assertEqual(getattr(cache, commands[i])(*args[i]), expected[i])
            print("OK")


if __name__ == "__main__":
    unittest.main()
