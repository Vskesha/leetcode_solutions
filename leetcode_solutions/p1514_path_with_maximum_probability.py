import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [{} for _ in range(n)]
        for edge, probability in zip(edges, succProb):
            fr, to = edge
            graph[fr][to] = probability
            graph[to][fr] = probability

        visited = set()
        priority = [(-1, start_node)]

        while priority:
            probability, curr = heappop(priority)
            visited.add(curr)
            if curr == end_node:
                return -probability
            for neib, pr in graph[curr].items():
                if neib not in visited:
                    heappush(priority, (pr * probability, neib))
        return 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_max_probability_1(self):
        print("Test maxProbability 1... ", end="")
        self.assertAlmostEqual(
            self.sol.maxProbability(
                n=3,
                edges=[[0, 1], [1, 2], [0, 2]],
                succProb=[0.5, 0.5, 0.2],
                start_node=0,
                end_node=2,
            ),
            0.25,
        )
        print("OK")

    def test_max_probability_2(self):
        print("Test maxProbability 2... ", end="")
        self.assertAlmostEqual(
            self.sol.maxProbability(
                n=3,
                edges=[[0, 1], [1, 2], [0, 2]],
                succProb=[0.5, 0.5, 0.3],
                start_node=0,
                end_node=2,
            ),
            0.30,
        )
        print("OK")

    def test_max_probability_3(self):
        print("Test maxProbability 3... ", end="")
        self.assertAlmostEqual(
            self.sol.maxProbability(
                n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=2
            ),
            0,
        )
        print("OK")

    def test_max_probability_4(self):
        print("Test maxProbability 4... ", end="")
        self.assertAlmostEqual(
            self.sol.maxProbability(
                n=10,
                edges=[[0, 3], [1, 7], [1, 2], [0, 9]],
                succProb=[0.31, 0.9, 0.86, 0.36],
                start_node=2,
                end_node=3,
            ),
            0,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
