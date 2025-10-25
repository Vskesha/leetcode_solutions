from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(
        self, n: int, relations: List[List[int]], time: List[int]
    ) -> int:
        income = [0] * n
        graph = [[] for _ in range(n)]

        for fr, to in relations:
            income[to - 1] += 1
            graph[fr - 1].append(to - 1)

        hque = []
        for i, k in enumerate(income):
            if not k:
                heappush(hque, (time[i], i))

        while hque:
            t, node = heappop(hque)
            for nxt in graph[node]:
                income[nxt] -= 1
                if not income[nxt]:
                    heappush(hque, (t + time[nxt], nxt))

        return t


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert (
        sol.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]) == 8
    )
    print("ok")

    print("Test 2 ... ", end="")
    assert (
        sol.minimumTime(
            n=5,
            relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]],
            time=[1, 2, 3, 4, 5],
        )
        == 12
    )
    print("ok")


if __name__ == "__main__":
    test()
