import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        dp = sorted(zip(difficulty, profit))
        dpi = ans = maxpr = 0

        for w in sorted(worker):
            while dpi < len(dp) and dp[dpi][0] <= w:
                maxpr = max(maxpr, dp[dpi][1])
                dpi += 1
            ans += maxpr
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_profit_assignment_1(self):
        print("Test maxProfitAssignment 1... ", end="")
        self.assertEqual(
            self.sol.maxProfitAssignment(
                difficulty=[2, 4, 6, 8, 10],
                profit=[10, 20, 30, 40, 50],
                worker=[4, 5, 6, 7],
            ),
            100,
        )
        print("OK")

    def test_max_profit_assignment_2(self):
        print("Test maxProfitAssignment 2... ", end="")
        self.assertEqual(
            self.sol.maxProfitAssignment(
                difficulty=[85, 47, 57],
                profit=[24, 66, 99],
                worker=[40, 25, 25],
            ),
            0,
        )
        print("OK")

    def test_max_profit_assignment_3(self):
        self.assertEqual(
            self.sol.maxProfitAssignment(
                difficulty=[68, 35, 52, 47, 86],
                profit=[67, 17, 1, 81, 3],
                worker=[92, 10, 85, 84, 82],
            ),
            324,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
