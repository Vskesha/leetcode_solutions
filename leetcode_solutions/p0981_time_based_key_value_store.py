from bisect import bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        lst = self.data[key]
        i = bisect_right(lst, timestamp, key=lambda x: x[0])
        return lst[i - 1][1] if i else ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)