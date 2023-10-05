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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def test():
    mf = MedianFinder()
    null = None
    methods = {'addNum': mf.addNum, 'findMedian': mf.findMedian}
    input_methods = ["addNum", "addNum", "findMedian", "addNum", "findMedian"]
    input_args = [[1], [2], [], [3], []]
    output = [null, null, 1.5, null, 2.0]
    for i in range(len(input_methods)):
        print(f'Test {i + 1} ... ', end='')
        assert methods[input_methods[i]](*input_args[i]) == output[i]
        print('ok')


if __name__ == '__main__':
    test()
