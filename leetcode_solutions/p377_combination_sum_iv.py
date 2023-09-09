from collections import deque
from functools import lru_cache
from typing import List


# the best iterative 2 loop solution
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]


# iterative dp solution (using deque)
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = max(nums)
        dp = deque([0] * (m - 1) + [1], maxlen=m)

        for _ in range(target):
            dp.append(sum(dp[-n] for n in nums))

        return dp[-1]



# iterative dp solution (using list)
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * max(nums) + [1]

        for _ in range(target):
            dp.append(sum(dp[-n] for n in nums))

        return dp[-1]


# recursive dp solution (while loop)
class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dp(t):
            res, i = 0, 0
            while i < ln and nums[i] < t:
                res += dp(t - nums[i])
                i += 1
            if i < ln and nums[i] == t:
                res += 1
            return res

        nums.sort()
        ln = len(nums)
        return dp(target)


# recursive dp solution (for loop)
class Solution4:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dp(t):
            res = 0
            for n in nums:
                if n < t:
                    res += dp(t - n)
                elif n == t:
                    res += 1
                else:
                    break

            return res

        nums.sort()
        return dp(target)


# recursive dp solution
class Solution5:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dp(t):
            if t < 0:
                return 0
            if t == 0:
                return 1

            return sum(dp(t - n) for n in nums)

        return dp(target)


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.combinationSum4(nums=[1, 2, 3], target=4) == 7
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.combinationSum4(nums=[9], target=3) == 0
    print('ok')


if __name__ == '__main__':
    test()
