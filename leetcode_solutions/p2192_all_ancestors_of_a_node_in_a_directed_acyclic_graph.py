import unittest
from collections import deque
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        income = [0] * n
        graph = [[] for _ in range(n)]
        ans = [set() for _ in range(n)]

        for fr, to in edges:
            graph[fr].append(to)
            income[to] += 1

        q = deque(i for i in range(n) if not income[i])
        while q:
            curr = q.popleft()
            for neib in graph[curr]:
                ans[neib].update(ans[curr])
                ans[neib].add(curr)
                income[neib] -= 1
                if not income[neib]:
                    q.append(neib)

        return list(map(sorted, ans))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def same_ancestors(self, ancs1, ancs2):
        for a1, a2 in zip(ancs1, ancs2):
            self.assertListEqual(a1, a2)

    def test_get_ancestors_1(self):
        print("Test getAncestors 1... ", end="")
        self.same_ancestors(
            self.sol.getAncestors(
                n=8,
                edges=[
                    [0, 3],
                    [0, 4],
                    [1, 3],
                    [2, 4],
                    [2, 7],
                    [3, 5],
                    [3, 6],
                    [3, 7],
                    [4, 6],
                ],
            ),
            [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
        )
        print("OK")

    def test_get_ancestors_2(self):
        print("Test getAncestors 2... ", end="")
        self.same_ancestors(
            self.sol.getAncestors(
                n=5,
                edges=[
                    [0, 1],
                    [0, 2],
                    [0, 3],
                    [0, 4],
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [2, 3],
                    [2, 4],
                    [3, 4],
                ],
            ),
            [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
