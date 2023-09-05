from bisect import bisect_right


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for _ in range(length)]
        for i in range(length):
            self.arr[i].append((0, 0))
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.arr[index]
        idx = bisect_right(snaps, snap_id, key=lambda x: x[0]) - 1
        return snaps[idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
