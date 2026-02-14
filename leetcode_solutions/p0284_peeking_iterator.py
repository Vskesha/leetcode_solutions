from collections import deque
from typing import List


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums: List[int]):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.i = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.i += 1
        return self.nums[self.i - 1]


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.q = deque()
        while iterator.hasNext():
            self.q.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration
        without advancing the iterator.
        :rtype: int
        """
        return self.q[0]

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)


class PeekingIterator2:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.nxt = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration
        without advancing the iterator.
        :rtype: int
        """
        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        ret = self.nxt
        self.nxt = self.it.next() if self.it.hasNext() else None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


def test():
    null, false = None, False
    commands = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
    args = [[[1, 2, 3]], [], [], [], [], []]
    outputs = [null, 1, 2, 2, 3, false]

    pi = PeekingIterator(Iterator(*args[0]))
    for i in range(1, len(commands)):
        print(f"Test {i}... ", end="")
        res = getattr(pi, commands[i])(*args[i])
        assert res == outputs[i]
        print("OK")


if __name__ == "__main__":
    test()
