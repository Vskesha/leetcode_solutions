import unittest
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for n in arr:
            if n % 2:
                if odds == 2:
                    return True
                odds += 1
            else:
                odds = 0
        return False


class Solution2:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = [x % 2 for x in arr]
        return any(
            odds[i] and odds[i + 1] and odds[i + 2] for i in range(len(odds) - 2)
        )


class Solution3:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        win = arr[0] % 2 + arr[1] % 2

        for i in range(2, len(arr)):
            win += arr[i] % 2
            if win == 3:
                return True
            win -= arr[i - 2] % 2

        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_three_consecutive_odds_1(self):
        print("Test threeConsecutiveOdds 1... ", end="")
        self.assertFalse(self.sol.threeConsecutiveOdds(arr=[2, 6, 4, 1]))
        print("OK")

    def test_three_consecutive_odds_2(self):
        print("Test threeConsecutiveOdds 2... ", end="")
        self.assertTrue(
            self.sol.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
