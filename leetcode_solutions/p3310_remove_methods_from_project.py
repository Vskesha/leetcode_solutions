import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for fr, to in invocations:
            graph[fr].append(to)

        q = deque([k])
        suspicious = {k}
        while q:
            curr = q.popleft()
            for neib in graph[curr]:
                if neib not in suspicious:
                    suspicious.add(neib)
                    q.append(neib)

        for fr, to in invocations:
            if fr not in suspicious and to in suspicious:
                return list(range(n))

        return [x for x in range(n) if x not in suspicious]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["remainingMethods"] * 3,
            "kwargs": [
                dict(n=4, k=1, invocations=[[1, 2], [0, 1], [3, 2]]),
                dict(n=5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]]),
                dict(n=3, k=2, invocations=[[1, 2], [0, 1], [2, 0]]),
            ],
            "expected": [
                [0, 1, 2, 3],
                [3, 4],
                [],
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
