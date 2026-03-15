import unittest

from leetcode_solutions._test_meta import TestMeta


class Fancy:
    mod = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv_mul = pow(self.mul, -1, self.mod)
        self.seq.append(((val - self.add) * inv_mul) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.mod
        self.add = self.add * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": Fancy,
            "class_methods": [
                "append",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "getIndex",
                "getIndex",
            ],
            "args": [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]],
            "expected": [
                null,
                null,
                null,
                null,
                10,
                null,
                null,
                null,
                26,
                34,
                20,
            ],
        }
    ]


if __name__ == "__main__":
    unittest.main()
