import unittest
from itertools import groupby


class Solution:
    def maxOperations(self, s: str) -> int:
        ans = ones = 0
        for k, gr in groupby(s):
            if k == "1":
                ones += len(list(gr))
            else:
                ans += ones
        return ans


class Solution2:
    def maxOperations(self, s: str) -> int:
        groups, curr = [], 0
        for k, gr in groupby(s):
            if k == "1":
                curr = len(list(gr))
            elif curr:
                groups.append(curr)
        return sum(i * n for i, n in enumerate(reversed(groups), 1))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maxOperations_1(self):
        print("Test maxOperations 1... ", end="")
        self.assertEqual(4, self.sol.maxOperations(s="1001101"))
        print("OK")

    def test_maxOperations_2(self):
        print("Test maxOperations 2... ", end="")
        self.assertEqual(0, self.sol.maxOperations(s="00111"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
