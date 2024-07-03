import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = b, max(b, n + a)
        return b


class Solution1:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            dp.append(max(dp[-1], n + dp[-2]))
        return dp[-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i < 0:
                return 0
            return max(dp(i - 1), nums[i] + dp(i - 2))

        return dp(len(nums) - 1)


class Solution3:
    def rob(self, nums: List[int]) -> int:
        nums = iter(nums)
        rb, om = next(nums), 0
        for n in nums:
            rb, om = om + n, max(rb, om)
        return max(rb, om)


class Solution4:
    def rob(self, nums: List[int]) -> int:
        rb, om = nums[0], 0
        for i in range(1, len(nums)):
            rb, om = om + nums[i], max(rb, om)
        return max(rb, om)


class Solution5:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        rb, om = [0] * ln, [0] * ln
        rb[0] = nums[0]

        for i in range(1, ln):
            rb[i] = om[i - 1] + nums[i]
            om[i] = max(rb[i - 1], om[i - 1])

        return max(rb[-1], om[-1])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_rob_1(self):
        print("Test rob 1... ", end="")
        self.assertEqual(self.sol.rob(nums=[1, 2, 3, 1]), 4)
        print("OK")

    def test_rob_2(self):
        print("Test rob 2... ", end="")
        self.assertEqual(self.sol.rob(nums=[2, 7, 9, 3, 1]), 12)
        print("OK")


if __name__ == "__main__":
    unittest.main()
