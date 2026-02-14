import unittest

from sortedcontainers import SortedDict, SortedList

from leetcode_solutions._test_meta import TestMeta


class MyCalendarTwo:

    def __init__(self):
        self.sl1 = SortedList()
        self.sl2 = SortedList()

    def book(self, start: int, end: int) -> bool:
        sti = self.sl1.bisect_right(start)
        eni = self.sl1.bisect_left(end)
        if sti % 2 == 0 and sti == eni:
            self.insert(start, self.sl1)
            self.insert(end, self.sl1)
            return True

        occupied = [start if sti % 2 else self.sl1[sti]]
        for i in range(sti + (sti + 1) % 2, eni):
            occupied.append(self.sl1[i])
        if len(occupied) % 2:
            occupied.append(end)

        for i in range(0, len(occupied), 2):
            sti = self.sl2.bisect_right(occupied[i])
            if sti % 2 or sti != self.sl2.bisect_left(occupied[i + 1]):
                return False

        self.insert(start, self.sl1)
        for num in occupied:
            self.insert(num, self.sl1)
            self.insert(num, self.sl2)
        self.insert(end, self.sl1)
        return True

    def insert(self, num: int, sl: SortedList) -> None:
        if num in sl:
            sl.remove(num)
        else:
            sl.add(num)


class MyCalendarTwo2:

    def __init__(self):
        self.cc = 2
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.sd[start] = self.sd.get(start, 0) + 1
        self.sd[end] = self.sd.get(end, 0) - 1
        concurr = 0
        for k, v in self.sd.items():
            if k >= end:
                break
            concurr += v
            if concurr > self.cc:
                self.sd[start] -= 1
                self.sd[end] += 1
                if not self.sd[start]:
                    del self.sd[start]
                if not self.sd[end]:
                    del self.sd[end]
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    true = True
    false = False
    test_cases = [
        {
            "class": MyCalendarTwo,
            "class_methods": ["book"] * 6,
            "args": [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
            "expected": [true, true, true, false, true, true],
        },
        {
            "class": MyCalendarTwo,
            "class_methods": ["book"] * 40,
            "args": [
                [33, 44],
                [85, 95],
                [20, 37],
                [91, 100],
                [89, 100],
                [77, 87],
                [80, 95],
                [42, 61],
                [40, 50],
                [85, 99],
                [74, 91],
                [70, 82],
                [5, 17],
                [77, 89],
                [16, 26],
                [21, 31],
                [30, 43],
                [96, 100],
                [27, 39],
                [44, 55],
                [15, 34],
                [85, 99],
                [74, 93],
                [84, 94],
                [82, 94],
                [46, 65],
                [31, 49],
                [58, 73],
                [86, 99],
                [73, 84],
                [68, 80],
                [5, 18],
                [75, 87],
                [88, 100],
                [25, 41],
                [66, 79],
                [28, 41],
                [60, 70],
                [62, 73],
                [16, 33],
            ],
            "expected": [
                true,
                true,
                true,
                true,
                false,
                true,
                false,
                true,
                false,
                false,
                false,
                true,
                true,
                false,
                true,
                false,
                false,
                true,
                false,
                true,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                true,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
