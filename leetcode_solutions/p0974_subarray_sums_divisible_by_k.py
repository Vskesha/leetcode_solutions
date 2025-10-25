import unittest
from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = [0] * k
        mods[0] = 1
        rem = 0

        for n in nums:
            rem = (rem + n) % k
            mods[rem] += 1

        return sum(i * (i - 1) // 2 for i in mods)


class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt, rem, ans = Counter([0]), 0, 0

        for n in nums:
            rem = (rem + n) % k
            ans += cnt[rem]
            cnt[rem] += 1

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_subarrays_div_by_k1(self):
        print("Test subarraysDivByK 1 ... ", end="")
        self.assertEqual(
            self.sol.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5), 7
        )
        print("OK")

    def test_subarrays_div_by_k2(self):
        print("Test subarraysDivByK 2 ... ", end="")
        self.assertEqual(self.sol.subarraysDivByK(nums=[5], k=9), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()
