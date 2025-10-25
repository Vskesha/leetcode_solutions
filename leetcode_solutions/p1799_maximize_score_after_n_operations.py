import unittest
from functools import lru_cache
from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2

        @lru_cache(None)
        def dp(i, mask):
            if i == 2 * n:
                return []
            if not (mask >> i) & 1:
                return dp(i + 1, mask)
            ans, tot = [], 0
            mask -= 1 << i
            for j in range(i + 1, 2 * n):
                if (mask >> j) & 1:
                    gcds = sorted(
                        dp(i + 1, mask - (1 << j)) + [gcd(nums[i], nums[j])]
                    )
                    score = sum(((i + 1) * gcds[i]) for i in range(len(gcds)))
                    if score > tot:
                        ans = gcds
                        tot = score
            return ans

        gcds = sorted(dp(0, (1 << (2 * n)) - 1))
        return sum(((i + 1) * gcds[i]) for i in range(n))


class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        def backtrack(state, pairs_picked) -> int:
            if pairs_picked == max_pairs:
                return 0

            if memo[state] != -1:
                return memo[state]

            max_score = 0
            for i in range(n - 1):
                if (state >> i) & 1:
                    continue
                for j in range(i + 1, n):
                    if (state >> j) & 1:
                        continue
                    new_state = state | (1 << i) | (1 << j)
                    curr_score = (pairs_picked + 1) * gcd(nums[i], nums[j])
                    rem_score = backtrack(new_state, pairs_picked + 1)
                    max_score = max(max_score, curr_score + rem_score)
            memo[state] = max_score
            return max_score

        n = len(nums)
        max_pairs = n // 2
        memo = [-1] * (2**n)
        return backtrack(0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_score_1(self):
        print("Test maxScore 1 ... ", end="")
        self.assertEqual(self.sol.maxScore(nums=[1, 2]), 1)
        print("OK")

    def test_max_score_2(self):
        print("Test maxScore 2 ... ", end="")
        self.assertEqual(self.sol.maxScore(nums=[3, 4, 6, 8]), 11)
        print("OK")

    def test_max_score_3(self):
        print("Test maxScore 3 ... ", end="")
        self.assertEqual(self.sol.maxScore(nums=[1, 2, 3, 4, 5, 6]), 14)
        print("OK")


if __name__ == "__main__":
    unittest.main()
