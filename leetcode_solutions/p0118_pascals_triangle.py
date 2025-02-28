import unittest
from itertools import pairwise
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for _ in range(numRows - 1):
            ans.append([1] + [a + b for a, b in pairwise(ans[-1])] + [1])

        return ans


class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            row = [1]
            prev = res[-1]
            for j in range(i - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            res.append(row)

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_generate_1(self):
        print("Test generate 1... ", end="")
        self.assertEqual(
            self.sol.generate(numRows=5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )
        print("OK")

    def test_generate_2(self):
        print("Test generate 2... ", end="")
        self.assertEqual(self.sol.generate(numRows=1), [[1]])
        print("OK")


if __name__ == "__main__":
    unittest.main()
