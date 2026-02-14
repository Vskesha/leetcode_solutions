from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        arr.sort()
        dp = {}

        for num in arr:
            ans, li = 1, 0
            while True:
                left = arr[li]
                ri = bisect_left(arr, num // left)
                if li >= ri:
                    break
                right = arr[ri]
                if left * right == num:
                    ans += 2 * dp[left] * dp[right] % mod
                li += 1
            if left**2 == num:
                ans += pow(dp[left], 2, mod)
            ans %= mod
            dp[num] = ans

        return sum(dp.values()) % mod


class Solution1:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        arr.sort()

        @lru_cache(None)
        def dp(n) -> int:
            ans = 1
            li = 0
            while True:
                ri = bisect_left(arr, n // arr[li])
                if li >= ri:
                    break
                if arr[li] * arr[ri] == n:
                    ans += 2 * dp(arr[li]) * dp(arr[ri]) % mod
                li += 1

            if arr[li] ** 2 == n:
                ans += dp(arr[li]) ** 2 % mod

            ans %= mod
            return ans

        res = 0
        for num in arr:
            res = (res + dp(num)) % mod

        return res


class Solution2:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        arr.sort()
        aux = {}

        def dp(n) -> int:
            if n in aux:
                return aux[n]
            ans = 1
            li = 0
            while True:
                ri = bisect_left(arr, n // arr[li])
                if li >= ri:
                    break
                if arr[li] * arr[ri] == n:
                    ans += 2 * dp(arr[li]) * dp(arr[ri]) % mod
                li += 1

            if arr[li] ** 2 == n:
                ans += dp(arr[li]) ** 2 % mod

            ans %= mod
            aux[n] = ans
            return ans

        res = 0
        for num in arr:
            res = (res + dp(num)) % mod

        return res


def test():
    sol = Solution()

    print("Test 1 ...", end="")
    assert sol.numFactoredBinaryTrees(arr=[2, 4]) == 3
    print("ok")

    print("Test 2 ...", end="")
    assert sol.numFactoredBinaryTrees(arr=[2, 4, 5, 10]) == 7
    print("ok")


if __name__ == "__main__":
    test()
