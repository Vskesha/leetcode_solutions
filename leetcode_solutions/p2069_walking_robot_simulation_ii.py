import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Robot:
    dirs = (("East", "North"), ("West", "South"))

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.width = width
        self.height = height
        self.p2 = width + height - 2
        self.p = self.p2 * 2
        self.direction = "East"
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        self.pos = (self.pos + num - 1) % self.p + 1

        if self.pos <= self.p2:
            if self.pos < self.width:
                self.direction = "East"
                self.y = 0
                self.x = self.pos
            else:
                self.direction = "North"
                self.x = self.width - 1
                self.y = self.pos - self.width + 1
        else:
            if self.pos < self.p2 + self.width:
                self.direction = "West"
                self.y = self.height - 1
                self.x = self.width - 1 - (self.pos - self.p2)
            else:
                self.direction = "South"
                self.x = 0
                self.y = self.p - self.pos

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
class TestSolution(TestCaseExtended, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": Robot,
            "cls_init_args": [6, 3],
            "class_methods": [
                "step",
                "step",
                "getPos",
                "getDir",
                "step",
                "step",
                "step",
                "getPos",
                "getDir",
            ],
            "args": [[2], [2], [], [], [2], [1], [4], [], []],
            "expected": [
                null,
                null,
                [4, 0],
                "East",
                null,
                null,
                null,
                [1, 2],
                "West",
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
