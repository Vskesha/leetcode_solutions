from heapq import heappop, heappush


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = []
        self.last = 0

    def reserve(self) -> int:
        if self.unreserved:
            return heappop(self.unreserved)
        else:
            self.last += 1
            return self.last

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)


class SeatManager2:

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


def test():
    null = None

    funcs = [
        "SeatManager",
        "reserve",
        "reserve",
        "unreserve",
        "reserve",
        "reserve",
        "reserve",
        "reserve",
        "unreserve",
    ]
    args = [[5], [], [], [2], [], [], [], [], [5]]
    outs = [null, 1, 2, null, 2, 3, 4, 5, null]

    sm = SeatManager(*args[0])
    for i in range(1, len(args)):
        print(f"Test {i} ... ", end="")
        func = (
            sm.reserve
            if funcs[i] == "reserve"
            else sm.unreserve if funcs[i] == "unreserve" else None
        )
        assert func(*args[i]) == outs[i]
        print("ok")


if __name__ == "__main__":
    test()
