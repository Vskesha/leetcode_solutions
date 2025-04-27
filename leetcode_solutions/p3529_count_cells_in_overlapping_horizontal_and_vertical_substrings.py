import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        lg = m * n

        hstring = "".join(ch for row in grid for ch in row)
        vstring = "".join(ch for col in zip(*grid) for ch in col)

        lp = len(pattern)
        hconcat = pattern + "$" + hstring
        vconcat = pattern + "$" + vstring

        zh = self.get_z_arr(hconcat)[lp + 1 :]
        zv = self.get_z_arr(vconcat)[lp + 1 :]

        hseen = set()
        i = 0
        while i < lg:
            if zh[i] == lp:
                bound = i + lp
                while i < bound:
                    hseen.add((i // n, i % n))
                    if zh[i] == lp:
                        bound = i + lp
                    i += 1
            else:
                i += 1

        vseen = set()
        i = 0
        while i < lg:
            if zv[i] == lp:
                bound = i + lp
                while i < bound:
                    vseen.add((i % m, i // m))
                    if zv[i] == lp:
                        bound = i + lp
                    i += 1
            else:
                i += 1

        return len(hseen.intersection(vseen))

    def get_z_arr(self, string):
        l, r, k = 0, 0, 0
        n = len(string)
        z = [0] * n

        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1

        return z


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countCells"] * 3,
            "kwargs": [
                dict(
                    grid=[
                        ["a", "a", "c", "c"],
                        ["b", "b", "b", "c"],
                        ["a", "a", "b", "a"],
                        ["c", "a", "a", "c"],
                        ["a", "a", "c", "c"],
                    ],
                    pattern="abaca",
                ),
                dict(
                    grid=[
                        ["c", "a", "a", "a"],
                        ["a", "a", "b", "a"],
                        ["b", "b", "a", "a"],
                        ["a", "a", "b", "a"],
                    ],
                    pattern="aba",
                ),
                dict(grid=[["a"]], pattern="a"),
            ],
            "expected": [1, 4, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
