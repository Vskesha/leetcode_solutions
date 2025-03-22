import unittest
from collections import defaultdict, deque
from heapq import heappushpop
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


class Solution3:
    def findMinHeightTrees(self, n, edges):
        def dfs1(node, par):
            adj[node].discard(par)
            for nbr in adj[node]:
                dfs1(nbr, node)
                height[node] = max(height[node], height[nbr] + 1)
            max_distance[node] = max(max_distance[node], height[node])

        def dfs2(node, ph):
            temp = [(ph, -1)]
            max_distance[node] = max(max_distance[node], height[node])
            for nbr in adj[node]:
                temp.append((height[nbr] + 1, nbr))
            temp.sort()

            for nbr in adj[node]:
                before_node = height[node]
                before_nbr = height[nbr]

                if temp[-1][1] == nbr:
                    height[node] = temp[-2][0]
                    par_hei = temp[-2][0] + 1
                else:
                    par_hei = temp[-1][0] + 1

                height[nbr] = max(height[nbr], par_hei)
                dfs2(nbr, par_hei)
                height[node] = before_node
                height[nbr] = before_nbr

        adj = [set() for _ in range(n)]
        height = [0] * n
        max_distance = [0] * n
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        dfs1(0, n)
        dfs2(0, 0)

        mn = min(max_distance)
        answer = [i for i in range(n) if max_distance[i] == mn]
        return answer


class Solution4:
    def findMinHeightTrees(self, n, edges):
        def dfs1(node, par):
            adj[node].discard(par)
            for nbr in adj[node]:
                dfs1(nbr, node)
                height[node] = max(height[node], height[nbr] + 1)

        def dfs2(node, ph):
            temp = [(0, -1), (ph, -1)]
            for nbr in adj[node]:
                heappushpop(temp, (height[nbr] + 1, nbr))

            for nbr in adj[node]:
                par_hei = (temp[0][0] if temp[1][1] == nbr else temp[1][0]) + 1
                max_distance[nbr] = max(max_distance[nbr], par_hei)
                dfs2(nbr, par_hei)

        adj = [set() for _ in range(n)]
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        height = [0] * n
        dfs1(0, n)

        max_distance = height.copy()
        dfs2(0, 0)

        mn = min(max_distance)
        answer = [i for i in range(n) if max_distance[i] == mn]
        return answer


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameRoots(self, roots1: List[int], roots2: List[int]):
        assert sorted(roots1) == sorted(roots2)

    def test_findMinHeightTrees_1(self):
        print("Test findMinHeightTrees 1...", end="")
        self.assertSameRoots(
            [1], self.sol.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]])
        )
        print("OK")

    def test_findMinHeightTrees_2(self):
        print("Test findMinHeightTrees 2...", end="")
        self.assertSameRoots(
            [3, 4],
            self.sol.findMinHeightTrees(
                n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
            ),
        )
        print("OK")

    def test_findMinHeightTrees_3(self):
        print("Test findMinHeightTrees 3...", end="")
        self.assertSameRoots(
            [1, 2],
            self.sol.findMinHeightTrees(
                n=7, edges=[[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
            ),
        )
        print("OK")

    def test_findMinHeightTrees_4(self):
        print("Test findMinHeightTrees 4...", end="")
        self.assertSameRoots(
            [2, 3],
            self.sol.findMinHeightTrees(
                n=10,
                edges=[
                    [0, 9],
                    [1, 2],
                    [2, 3],
                    [2, 5],
                    [6, 5],
                    [9, 3],
                    [4, 3],
                    [7, 3],
                    [7, 8],
                ],
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
