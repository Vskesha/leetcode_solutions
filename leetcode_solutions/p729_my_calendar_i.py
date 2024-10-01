import unittest

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()

    def book(self, start: int, end: int) -> bool:
        curr_interval = (start, end)
        i = self.intervals.bisect_right(curr_interval)
        if i > 0 and self.intervals[i - 1][1] > start:
            return False
        if i < len(self.intervals) and self.intervals[i][0] < end:
            return False
        self.intervals.add(curr_interval)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": MyCalendar,
            "class_methods": ["book", "book", "book"],
            "args": [[10, 20], [15, 25], [20, 30]],
            "expected": [True, False, True],
        },
    ]


if __name__ == '__main__':
    unittest.main()
