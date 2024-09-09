import unittest
from collections import deque, defaultdict
from functools import cache
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        dirs = [
            (dx, dy)
            for dx in (-2, -1, 1, 2)
            for dy in (-2, -1, 1, 2)
            if abs(dx) + abs(dy) == 3
        ]
        memo = defaultdict(dict)

        def get_moves(kpos, tpos):
            if tpos in memo[kpos]:
                return memo[kpos][tpos]
            bfs = deque([kpos])
            visited = {kpos}
            moves = 0
            while bfs:
                for _ in range(len(bfs)):
                    pos = bfs.popleft()
                    if pos == tpos:
                        memo[kpos][tpos] = memo[tpos][kpos] = moves
                        return memo[kpos][tpos]
                    for dx, dy in dirs:
                        nx, ny = pos[0] + dx, pos[1] + dy
                        if 0 <= nx < 50 and 0 <= ny < 50:
                            npos = (nx, ny)
                            if npos not in visited:
                                visited.add(npos)
                                bfs.append(npos)
                moves += 1
            return inf

        @cache
        def dp(mask: int, kpos: tuple, alice: bool):
            if mask == tmask:
                return 0

            it = (
                get_moves(kpos, pos) + dp(mask | (1 << i), pos, not alice)
                for i, pos in enumerate(positions)
                if not (mask & (1 << i))
            )
            return max(it) if alice else min(it)

        positions = list(map(tuple, positions))
        tmask = (1 << len(positions)) - 1
        return dp(0, (kx, ky), True)


class Solution2:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        sz = 50
        diff = (-2, -1, 1, 2)
        dirs = [(dx, dy) for dx in diff for dy in diff if abs(dx) + abs(dy) == 3]
        memo = defaultdict(dict)

        def get_moves(kpos, tpos):
            if tpos in memo[kpos]:
                return memo[kpos][tpos]
            bfs = deque([kpos])
            visited = {kpos}
            moves = 0
            while bfs:
                for _ in range(len(bfs)):
                    pos = bfs.popleft()
                    if pos == tpos:
                        memo[kpos][tpos] = memo[tpos][kpos] = moves
                        return memo[kpos][tpos]
                    for dx, dy in dirs:
                        nx, ny = pos[0] + dx, pos[1] + dy
                        if 0 <= nx < sz and 0 <= ny < sz:
                            npos = (nx, ny)
                            if npos not in visited:
                                visited.add(npos)
                                bfs.append(npos)
                moves += 1
            return inf

        @cache
        def dp(mask: int, kpos: tuple, alice: bool):
            if mask == tmask:
                return 0

            ans, func = (0, max) if alice else (inf, min)

            for i, pos in enumerate(positions):
                if not (mask & (1 << i)):
                    curr_moves = get_moves(kpos, pos) + dp(
                        mask | (1 << i), pos, not alice
                    )
                    ans = func(ans, curr_moves)

            return ans

        positions = list(map(tuple, positions))
        tmask = (1 << len(positions)) - 1
        return dp(0, (kx, ky), True)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxMoves"] * 3,
            "kwargs": [
                dict(kx=1, ky=1, positions=[[0, 0]]),
                dict(kx=0, ky=2, positions=[[1, 1], [2, 2], [3, 3]]),
                dict(kx=0, ky=0, positions=[[1, 2], [2, 4]]),
            ],
            "expected": [4, 8, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
