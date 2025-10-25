from functools import lru_cache
from typing import List


# iterative dp solution
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max(use, dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


# recursive dp solution
class Solution2:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0, 0)


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]) == 18
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]) == 21
    print("ok")

    print("Test 3 ... ", end="")
    assert sol.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]) == -1
    print("ok")


if __name__ == "__main__":
    test()
