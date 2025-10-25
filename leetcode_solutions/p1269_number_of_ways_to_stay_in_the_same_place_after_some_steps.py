from functools import lru_cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(i, rem):
            if i < 0 or i >= arrLen or rem < i:
                return 0
            if rem == i:
                return 1
            return (
                dp(i, rem - 1) + dp(i - 1, rem - 1) + dp(i + 1, rem - 1)
            ) % mod

        return dp(0, steps)


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.numWays(steps=3, arrLen=2) == 4
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.numWays(steps=2, arrLen=4) == 2
    print("ok")

    print("Test 3 ... ", end="")
    assert sol.numWays(steps=4, arrLen=2) == 8
    print("ok")


if __name__ == "__main__":
    test()
