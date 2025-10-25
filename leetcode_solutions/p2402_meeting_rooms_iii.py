from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = list(range(n))
        taken = []
        cnt = [0] * n

        meetings.sort(key=lambda x: x[0])
        for start, end in meetings:
            while taken and taken[0][0] <= start:
                _, room = heappop(taken)
                heappush(free, room)
            if free:
                room = heappop(free)
            else:
                free_at, room = heappop(taken)
                end += free_at - start
            cnt[room] += 1
            heappush(taken, (end, room))

        return cnt.index(max(cnt))


class Solution2:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        cnt = [0] * n
        meetings = sorted(meetings, key=lambda x: x[0])
        for start, end in meetings:
            for i in range(n):
                if rooms[i] <= start:
                    cnt[i] += 1
                    rooms[i] = end
                    break
            else:
                i = rooms.index(min(rooms))
                cnt[i] += 1
                rooms[i] += end - start
        return cnt.index(max(cnt))


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.mostBooked(
            n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        )
        == 1
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.mostBooked(
            n=4, meetings=[[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]
        )
        == 0
    )
    print("OK")


if __name__ == "__main__":
    test()
