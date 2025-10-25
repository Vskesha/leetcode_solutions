import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neibs = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        tb = tuple(v for row in board for v in row)
        end = (1, 2, 3, 4, 5, 0)

        moves = 0
        if tb == end:
            return moves

        bfs = deque([tb])
        seen = {tb}

        while bfs:
            moves += 1
            for _ in range(len(bfs)):
                cb = list(bfs.popleft())
                i = cb.index(0)
                for j in neibs[i]:
                    cb[i], cb[j] = cb[j], cb[i]
                    ctb = tuple(cb)
                    cb[i], cb[j] = cb[j], cb[i]
                    if ctb in seen:
                        continue
                    if ctb == end:
                        return moves
                    bfs.append(ctb)
                    seen.add(ctb)

        return -1


class Solution2:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neibs = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        tb = tuple(v for row in board for v in row)
        end = (1, 2, 3, 4, 5, 0)

        moves = 0
        if tb == end:
            return moves

        i = tb.index(0)
        bfs = deque([(tb, i)])
        seen = {tb}

        while bfs:
            moves += 1
            for _ in range(len(bfs)):
                cb, i = bfs.popleft()
                cb = list(cb)
                for j in neibs[i]:
                    cb[i], cb[j] = cb[j], cb[i]
                    ctb = tuple(cb)
                    cb[i], cb[j] = cb[j], cb[i]
                    if ctb in seen:
                        continue
                    if ctb == end:
                        return moves
                    bfs.append((ctb, j))
                    seen.add(ctb)

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["slidingPuzzle"] * 3,
            "kwargs": [
                dict(board=[[1, 2, 3], [4, 0, 5]]),
                dict(board=[[1, 2, 3], [5, 4, 0]]),
                dict(board=[[4, 1, 2], [5, 0, 3]]),
            ],
            "expected": [1, -1, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()
