class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 3000
        self.table = [None] * self.size

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:

        idx = self.hash(key)

        if not self.table[idx]:
            self.table[idx] = Node(key, value)
            return

        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                curr.next = Node(key, value)
                return
            curr = curr.next

    def get(self, key: int) -> int:

        idx = self.hash(key)
        curr = self.table[idx]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.table[idx]

        if not curr:
            return

        if curr.key == key:
            self.table[idx] = curr.next
            return

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


class MyHashMap2:

    def __init__(self):
        self.arr = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
