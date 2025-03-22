from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)

        for fr, to, pr in flights:
            graph[fr].append((to, pr))

        heap = []
        heap.append((0, 0, src))
        visited = [float("inf")] * n

        while heap:
            tc, st, fr = heappop(heap)
            if fr == dst:
                return tc
            if st > k or st >= visited[fr]:
                continue
            visited[fr] = st
            st += 1
            for to, pr in graph[fr]:
                heappush(heap, (tc + pr, st, to))
        return -1


class Solution2:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        inf = float("inf")
        graph = defaultdict(list)

        for fr, to, pr in flights:
            graph[fr].append((to, pr))

        dist = [inf] * n
        dist[src] = 0

        q = deque()
        q.append((src, 0))

        for _ in range(k + 1):
            for _ in range(len(q)):
                fr, tc = q.popleft()
                for to, pr in graph[fr]:
                    ntc = tc + pr
                    if ntc < dist[to]:
                        dist[to] = ntc
                        q.append((to, ntc))

        return -1 if dist[dst] == inf else dist[dst]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.findCheapestPrice(
            n=4,
            flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            src=0,
            dst=3,
            k=1,
        )
        == 700
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
        )
        == 200
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
        )
        == 500
    )
    print("OK")

    print("Test 4... ", end="")
    assert (
        sol.findCheapestPrice(
            n=11,
            flights=[
                [0, 3, 3],
                [3, 4, 3],
                [4, 1, 3],
                [0, 5, 1],
                [5, 1, 100],
                [0, 6, 2],
                [6, 1, 100],
                [0, 7, 1],
                [7, 8, 1],
                [8, 9, 1],
                [9, 1, 1],
                [1, 10, 1],
                [10, 2, 1],
                [1, 2, 100],
            ],
            src=0,
            dst=2,
            k=4,
        )
        == 11
    )
    print("OK")


if __name__ == "__main__":
    test()
