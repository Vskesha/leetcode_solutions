import unittest
from collections import deque
from typing import List

from _test_meta import TestMeta


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        n = numCourses
        graph = [[] for _ in range(n)]
        income = [0] * n
        for a, b in prerequisites:
            graph[a].append(b)
            income[b] += 1

        q = deque(i for i in range(n) if not income[i])
        aux = [set() for _ in range(n)]
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                aux[nxt].update(aux[cur])
                aux[nxt].add(cur)
                income[nxt] -= 1
                if not income[nxt]:
                    q.append(nxt)

        ans = []
        for a, b in queries:
            ans.append(a in aux[b])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    true, false = True, False
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkIfPrerequisite"] * 3,
            "kwargs": [
                dict(numCourses=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]),
                dict(numCourses=2, prerequisites=[], queries=[[1, 0], [0, 1]]),
                dict(
                    numCourses=3,
                    prerequisites=[[1, 2], [1, 0], [2, 0]],
                    queries=[[1, 0], [1, 2]],
                ),
            ],
            "expected": [[false, true], [false, false], [true, true]],
        },
    ]


if __name__ == "__main__":
    unittest.main()
