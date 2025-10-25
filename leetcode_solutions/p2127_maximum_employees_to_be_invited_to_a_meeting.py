import unittest
from collections import deque
from typing import List

from _test_meta import TestMeta


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        inc = [0] * n
        tails = [1] * n
        for i, f in enumerate(favorite):
            inc[f] += 1

        q = deque(i for i, v in enumerate(inc) if v == 0)
        while q:
            curr = q.popleft()
            neib = favorite[curr]
            tails[neib] = max(tails[neib], tails[curr] + 1)
            inc[neib] -= 1
            if not inc[neib]:
                q.append(neib)

        ans = tl = 0
        for i in range(n):
            if inc[i]:
                cycle = []
                while inc[i]:
                    inc[i] -= 1
                    cycle.append(i)
                    i = favorite[i]
                ans = max(ans, len(cycle))
                if len(cycle) == 2:
                    tl += tails[cycle[0]] + tails[cycle[1]]

        ans = max(ans, tl)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumInvitations"] * 3,
            "kwargs": [
                dict(favorite=[2, 2, 1, 2]),
                dict(favorite=[1, 2, 0]),
                dict(favorite=[3, 0, 1, 4, 1]),
            ],
            "expected": [3, 3, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
