from functools import lru_cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        la = len(arr)
        dp = [0] * la

        mx = arr[0]
        for ei in range(k):
            mx = max(mx, arr[ei])
            dp[ei] = mx * (ei + 1)

        for ei in range(k, la):
            mx = msm = 0
            for la in range(k):
                mx = max(mx, arr[ei - la])
                cs = mx * (la + 1)
                msm = max(msm, cs + dp[ei - la - 1])
            dp[ei] = msm

        return dp[-1]


# recursive dp solution
class Solution2:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(ei: int) -> int:
            if ei < 0:
                return 0
            mx = arr[ei]
            sm = 0
            msm = 0
            for la in range(min(k, ei + 1)):
                mx = max(mx, arr[ei - la])
                sm = mx * (la + 1)
                msm = max(msm, sm + dp(ei - la - 1))
            return msm

        return dp(len(arr) - 1)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3) == 84
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4)
        == 83
    )
    print("OK")

    print("Test 3... ", end="")
    assert sol.maxSumAfterPartitioning(arr=[1], k=1) == 1
    print("OK")


if __name__ == "__main__":
    test()
