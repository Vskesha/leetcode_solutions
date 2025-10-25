import unittest

from leetcode_solutions._test_meta import TestMeta


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


class CustomStack2:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": CustomStack,
            "cls_init_args": [3],
            "class_methods": [
                "push",
                "push",
                "pop",
                "push",
                "push",
                "push",
                "increment",
                "increment",
                "pop",
                "pop",
                "pop",
                "pop",
            ],
            "args": [
                [1],
                [2],
                [],
                [2],
                [3],
                [4],
                [5, 100],
                [2, 100],
                [],
                [],
                [],
                [],
            ],
            "expected": [
                null,
                null,
                2,
                null,
                null,
                null,
                null,
                null,
                103,
                202,
                201,
                -1,
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
