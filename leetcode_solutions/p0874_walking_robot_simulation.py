import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        di = 0
        x = y = 0
        ans = 0
        obstacles = set(map(tuple, obstacles))
        for com in commands:
            if com == -2:
                di = (di - 1) % 4
            elif com == -1:
                di = (di + 1) % 4
            else:
                for _ in range(com):
                    nx, ny = x + dirs[di], y + dirs[di + 1]
                    if (nx, ny) not in obstacles:
                        x = nx
                        y = ny
                        ans = max(ans, x**2 + y**2)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["robotSim"] * 3,
            "kwargs": [
                dict(commands=[4, -1, 3], obstacles=[]),
                dict(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]),
                dict(commands=[6, -1, -1, 6], obstacles=[]),
            ],
            "expected": [25, 65, 36],
        },
    ]


if __name__ == "__main__":
    unittest.main()
