import unittest
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [
            chr(c) + str(r)
            for c in range(ord(s[0]), ord(s[3]) + 1)
            for r in range(int(s[1]), int(s[4]) + 1)
        ]


class Solution2:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for c in range(ord(s[0]), ord(s[3]) + 1):
            for r in range(int(s[1]), int(s[4]) + 1):
                ans.append(f"{chr(c)}{r}")

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_cells_in_range_1(self):
        print("Test cellsInRange 1... ", end="")
        self.assertListEqual(
            self.sol.cellsInRange(s="K1:L2"), ["K1", "K2", "L1", "L2"]
        )
        print("OK")

    def test_cells_in_range_2(self):
        print("Test cellsInRange 2... ", end="")
        self.assertListEqual(
            self.sol.cellsInRange(s="A1:F1"),
            ["A1", "B1", "C1", "D1", "E1", "F1"],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
