from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for fr, to in connections:
            graph[fr].append((to, True))
            graph[to].append((fr, False))

        bfs = deque([0])
        visited = {0}
        res = 0

        while bfs:
            curr = bfs.popleft()

            for neib, reverse in graph[curr]:
                if neib not in visited:
                    bfs.append(neib)
                    visited.add(neib)
                    res += reverse
        return res


def test_min_reorder():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert (
        sol.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    )
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.minReorder(n=3, connections=[[1, 0], [2, 0]]) == 0
    print("OK")


if __name__ == "__main__":
    test_min_reorder()
