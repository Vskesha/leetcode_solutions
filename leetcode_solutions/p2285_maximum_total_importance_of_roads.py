import unittest
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        imp = [0] * n
        for a, b in roads:
            imp[a] += 1
            imp[b] += 1
        imp.sort()

        return sum(i * m for i, m in enumerate(imp, 1))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximum_importance_1(self):
        print("Test maximumImportance 1... ", end="")
        self.assertEqual(
            self.sol.maximumImportance(
                n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
            ),
            43,
        )
        print("OK")

    def test_maximum_importance_2(self):
        print("Test maximumImportance 2... ", end="")
        self.assertEqual(
            self.sol.maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]),
            20,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
