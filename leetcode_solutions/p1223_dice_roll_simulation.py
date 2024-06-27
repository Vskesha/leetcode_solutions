import unittest
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7

        def dp(n, d, t):
            if not n:
                return 1
            ans = 0
            for dc in range(6):
                if dc == d and t == rollMax[dc]:
                    continue
                combs = dp(n - 1, dc, t + 1 if dc == d else 1)
                ans += combs
                ans %= mod

            return ans

        return dp(n, -1, -1)


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 + [1]]
        for i in range(n):
            dp.append(
                [
                    dp[i][-1]
                    - (
                        dp[i - rollMax[j]][-1] - dp[i - rollMax[j]][j]
                        if i >= rollMax[j]
                        else 0
                    )
                    for j in range(6)
                ]
            )
            dp[-1].append(sum(dp[-1]) % (10**9 + 7))
        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_die_simulator_1(self):
        print("Test dieSimulator 1... ", end="")
        self.assertEqual(self.sol.dieSimulator(n=2, rollMax=[1, 1, 2, 2, 3, 3]), 34)
        print("OK")

    def test_die_simulator_2(self):
        print("Test dieSimulator 2... ", end="")
        self.assertEqual(self.sol.dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]), 30)
        print("OK")

    def test_die_simulator_3(self):
        print("Test dieSimulator 3... ", end="")
        self.assertEqual(self.sol.dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]), 181)
        print("OK")


if __name__ == "__main__":
    unittest.main()
