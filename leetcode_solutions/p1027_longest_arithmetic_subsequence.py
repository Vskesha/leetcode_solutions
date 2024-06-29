import unittest
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for r in range(1, len(nums)):
            for l in range(r):
                d = nums[r] - nums[l]
                dp[(r, d)] = dp.get((l, d), 1) + 1
        return max(dp.values())


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_longest_arith_seq_length_1(self):
        print("Test longestArithSeqLength 1 ... ", end="")
        self.assertEqual(self.sol.longestArithSeqLength(nums=[3, 6, 9, 12]), 4)
        print("OK")

    def test_longest_arith_seq_length_2(self):
        print("Test longestArithSeqLength 2 ... ", end="")
        self.assertEqual(self.sol.longestArithSeqLength(nums=[9, 4, 7, 2, 10]), 3)
        print("OK")

    def test_longest_arith_seq_length_3(self):
        print("Test longestArithSeqLength 3 ... ", end="")
        self.assertEqual(
            self.sol.longestArithSeqLength(nums=[20, 1, 15, 3, 10, 5, 8]), 4
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
