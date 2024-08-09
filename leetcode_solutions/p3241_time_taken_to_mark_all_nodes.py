import unittest
from heapq import heappushpop
from typing import List


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        def dfs1(node, parent):
            adj[node].discard(parent)
            for neib in adj[node]:
                dfs1(neib, node)
                height[node] = max(height[node], height[neib] + (neib + 1) % 2 + 1)

        def dfs2(node, htp):
            heap = [(0, -1), (htp, -1)]
            for neib in adj[node]:
                heappushpop(heap, (height[neib] + (neib + 1) % 2 + 1, neib))

            for neib in adj[node]:
                htp = (
                    (heap[0][0] if neib == heap[1][1] else heap[1][0])
                    + (node + 1) % 2
                    + 1
                )
                times[neib] = max(times[neib], htp)
                dfs2(neib, htp)

        n = len(edges) + 1
        adj = [set() for _ in range(n)]
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        height = [0] * n
        dfs1(0, n)

        times = height.copy()
        dfs2(0, 0)

        return times


class Solution2:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        def dfs1(node, parent):
            adj[node].discard(parent)
            for neib in adj[node]:
                dfs1(neib, node)
                height[node] = max(height[node], height[neib] + (neib + 1) % 2 + 1)

        def dfs2(node, htp):
            heap = [(0, -1), (htp, -1)]
            for neib in adj[node]:
                heappushpop(heap, (height[neib] + (neib + 1) % 2 + 1, neib))

            for neib in adj[node]:
                if neib == heap[1][1]:
                    htp = heap[0][0] + (node + 1) % 2 + 1
                    times[neib] = max(times[neib], htp)
                    dfs2(neib, htp)
                else:
                    htp = heap[1][0] + (node + 1) % 2 + 1
                    dfs3(neib, htp)

        def dfs3(node, htp):
            times[node] = htp
            htp += (node + 1) % 2 + 1
            for neib in adj[node]:
                dfs3(neib, htp)

        n = len(edges) + 1
        adj = [set() for _ in range(n)]
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        height = [0] * n
        dfs1(0, n)

        times = height.copy()
        dfs2(0, 0)

        return times


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_timeTaken_1(self):
        print("Test timeTaken 1... ", end="")
        self.assertListEqual([2, 4, 3], self.sol.timeTaken(edges=[[0, 1], [0, 2]]))
        print("OK")

    def test_timeTaken_2(self):
        print("Test timeTaken 2... ", end="")
        self.assertListEqual([1, 2], self.sol.timeTaken(edges=[[0, 1]]))
        print("OK")

    def test_timeTaken_3(self):
        print("Test timeTaken 3... ", end="")
        self.assertListEqual(
            [4, 6, 3, 5, 5], self.sol.timeTaken(edges=[[2, 4], [0, 1], [2, 3], [0, 2]])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
