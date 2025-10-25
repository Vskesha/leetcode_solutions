import unittest
from functools import reduce
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


class Solution2:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()


class Solution3:
    def findCenter(self, edges: List[List[int]]) -> int:
        return reduce(lambda x, y: x & y, map(set, edges)).pop()


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_find_center_1(self):
        print("Test findCenter 1 ... ", end="")
        self.assertEqual(
            self.sol.findCenter(edges=[[1, 2], [2, 3], [4, 2]]), 2
        )
        print("OK")

    def test_find_center_2(self):
        print("Test findCenter 2 ... ", end="")
        self.assertEqual(
            self.sol.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]), 1
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
