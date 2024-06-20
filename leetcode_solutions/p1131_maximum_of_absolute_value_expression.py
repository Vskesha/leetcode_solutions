import unittest
from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        a1, a2, a3, a4 = [], [], [], []

        for i, (n1, n2) in enumerate(zip(arr1, arr2)):
            a1.append(i + n1 + n2)
            a2.append(i + n1 - n2)
            a3.append(i - n1 + n2)
            a4.append(i - n1 - n2)

        return max(max(a) - min(a) for a in (a1, a2, a3, a4))


class Solution2:  # Time Limit Exceeded
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0

        for i in range(1, len(arr1)):
            for j in range(i):
                ans = max(ans, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + i - j)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_abs_val_expr_1(self):
        print("Test maxAbsValExpr 1... ", end="")
        self.assertEqual(
            self.sol.maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]), 13
        )
        print("OK")

    def test_max_abs_val_expr_2(self):
        print("Test maxAbsValExpr 2... ", end="")
        self.assertEqual(
            self.sol.maxAbsValExpr(arr1=[1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]),
            20,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
