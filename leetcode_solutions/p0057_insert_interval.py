from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        st, end = newInterval
        if end < intervals[0][0]:
            return [newInterval] + intervals
        if st > intervals[-1][1]:
            return intervals + [newInterval]

        li = bisect_right(intervals, st, key=lambda x: x[1] + 1)
        ri = bisect_left(intervals, end, key=lambda x: x[0] - 1)
        if li == ri:
            return intervals[:li] + [newInterval] + intervals[ri:]
        st = min(st, intervals[li][0])
        end = max(end, intervals[ri - 1][1])
        return intervals[:li] + [[st, end]] + intervals[ri:]
