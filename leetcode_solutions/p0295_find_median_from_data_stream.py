import unittest
from bisect import insort
from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []
        self.even = True

    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        self.even = not self.even

    def findMedian(self) -> float:
        if self.even:
            return (self.large[0] - self.small[0]) / 2
        return self.large[0]


class MedianFinder2:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        insort(self.arr, num)

    def findMedian(self) -> float:
        la = len(self.arr)
        i = la // 2
        if la % 2:
            return self.arr[i]
        else:
            return (self.arr[i] + self.arr[i - 1]) / 2


class MedianFinder3:

    def __init__(self):
        self.lh = []
        self.rh = []

    def addNum(self, num: int) -> None:
        if self.lh and -self.lh[0] > num:
            if len(self.lh) == len(self.rh):
                heappush(self.rh, -heappushpop(self.lh, -num))
            else:
                heappush(self.lh, -num)
        else:
            if len(self.lh) == len(self.rh):
                heappush(self.rh, num)
            else:
                heappush(self.lh, -heappushpop(self.rh, num))

    def findMedian(self) -> float:
        if len(self.lh) == len(self.rh):
            return (self.rh[0] - self.lh[0]) / 2
        return self.rh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def add_test(i):
    def test_case(self):
        print(f"Test MedianFinder {i}... ", end="")
        self.assertEqual(
            self.expected[i], getattr(self.mf, self.commands[i])(*self.args[i])
        )
        print("OK")

    return test_case


class MetaTest(type):
    def __init__(self, *args, **kwargs):
        for i in range(1, len(self.commands)):
            setattr(self, f"test_median_finder_{i}", add_test(i))
        super().__init__(*args, **kwargs)


class TestMedianFinder(unittest.TestCase, metaclass=MetaTest):
    commands = [
        "MedianFinder",
        "addNum",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
    ]
    args = [[], [1], [2], [], [3], []]
    expected = [None, None, None, 1.5, None, 2.0]
    mf = MedianFinder()


if __name__ == "__main__":
    unittest.main()
