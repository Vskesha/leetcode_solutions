from functools import lru_cache
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        @lru_cache(None)
        def dp(left, right, k):
            if k == 1:  # <-- 1.
                mid = houses[(left + right) // 2]
                return sum(
                    abs(houses[i] - mid) for i in range(left, right + 1)
                )

            return min(
                dp(left, i, 1) + dp(i + 1, right, k - 1)
                for i in range(left, right - k + 2)
            )  # <-- 2.

        return dp(0, len(houses) - 1, k)


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.minDistance(houses=[1, 4, 8, 10, 20], k=3) == 5
    print("ok\nTest 2 ... ", end="")
    assert sol.minDistance(houses=[2, 3, 5, 12, 18], k=2) == 9
    print("ok")


if __name__ == "__main__":
    test()
