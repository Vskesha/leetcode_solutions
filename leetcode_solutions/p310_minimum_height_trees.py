from collections import deque, defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)

        income = [len(graph[i]) for i in range(n)]
        bfs = deque(i for i in range(n) if income[i] == 1)

        while n > 2:
            for _ in range(len(bfs)):
                leaf = bfs.popleft()
                for neib in graph[leaf]:
                    income[neib] -= 1
                    if income[neib] == 1:
                        bfs.append(neib)
                n -= 1
        return list(bfs)


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(n)}
        for fr, to in edges:
            graph[fr].add(to)
            graph[to].add(fr)

        while n > 2:
            leaves = [i for i in graph if len(graph[i]) == 1]
            for leaf in leaves:
                neib = graph[leaf].pop()
                graph[neib].remove(leaf)
                del graph[leaf]
                n -= 1
        return list(graph.keys())


def test_find_min_height_trees():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
    print("OK")

    print("Test 2... ", end="")
    assert sol.findMinHeightTrees(
        n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    ) == [3, 4]
    print("OK")

    print("Test 3... ", end="")
    assert sol.findMinHeightTrees(
        n=7, edges=[[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    ) == [1, 2]
    print("OK")

    print("Test 4... ", end="")
    assert sol.findMinHeightTrees(
        n=10,
        edges=[[0, 9], [1, 2], [2, 3], [2, 5], [6, 5], [9, 3], [4, 3], [7, 3], [7, 8]],
    ) == [2, 3]
    print("OK")


if __name__ == "__main__":
    test_find_min_height_trees()
