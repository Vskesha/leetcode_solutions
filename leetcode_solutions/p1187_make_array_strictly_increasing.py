import unittest
from bisect import bisect_right
from collections import defaultdict
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        l1 = len(arr1)
        l2 = len(arr2)
        dp = {-1: 0}

        for i in range(l1):
            new_dp = defaultdict(lambda: float("inf"))
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect_right(arr2, prev)
                if idx < l2:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp

        return min(dp.values()) if dp else -1


class Solution2:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        l1 = len(arr1)
        l2 = len(arr2)
        arr2.sort()

        @lru_cache(None)
        def dp(idx, prev):
            if idx == l1:
                return 0

            i2 = bisect_right(arr2, prev)

            if arr1[idx] <= prev:
                return dp(idx + 1, arr2[i2]) + 1 if i2 < l2 else 10000

            without_change = dp(idx + 1, arr1[idx])
            with_change = (
                dp(idx + 1, arr2[i2]) + 1
                if i2 < l2 and arr2[i2] < arr1[idx]
                else 10000
            )
            return min(without_change, with_change)

        ans = dp(0, -1)
        return ans if ans < 10000 else -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_make_array_increasing_1(self):
        print("Test makeArrayIncreasing 1... ", end="")
        self.assertEqual(
            self.sol.makeArrayIncreasing(
                arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]
            ),
            1,
        )
        print("OK")

    def test_make_array_increasing_2(self):
        print("Test makeArrayIncreasing 2... ", end="")
        self.assertEqual(
            self.sol.makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]),
            2,
        )
        print("OK")

    def test_make_array_increasing_3(self):
        print("Test makeArrayIncreasing 3... ", end="")
        self.assertEqual(
            self.sol.makeArrayIncreasing(
                arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]
            ),
            -1,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
