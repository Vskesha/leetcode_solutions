import unittest
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        heap = [(v, i + 1) for i, v in enumerate(nums)]
        heapify(heap)

        for _ in range(left - 1):
            s, i = heappop(heap)
            if i < n:
                heappush(heap, (s + nums[i], i + 1))

        ans = 0
        for _ in range(right - left + 1):
            s, i = heappop(heap)
            ans = (ans + s) % mod
            if i < n:
                heappush(heap, (s + nums[i], i + 1))

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_rangeSum_1(self):
        print("Test rangeSum 1... ", end="")
        self.assertEqual(13, self.sol.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
        print("OK")

    def test_rangeSum_2(self):
        print("Test rangeSum 2... ", end="")
        self.assertEqual(6, self.sol.rangeSum(nums=[1, 2, 3, 4], n=4, left=3, right=4))
        print("OK")

    def test_rangeSum_3(self):
        print("Test rangeSum 3... ", end="")
        self.assertEqual(
            50, self.sol.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=10)
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
