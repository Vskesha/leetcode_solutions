import unittest
from collections import OrderedDict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        indices = OrderedDict()
        st = -1
        ans = 0
        for i, n in enumerate(nums):
            indices[n] = i
            indices.move_to_end(n)
            if len(indices) < k:
                continue
            if len(indices) > k:
                st = indices.popitem(last=False)[1]
            ans += indices[next(iter(indices))] - st
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_subarraysWithKDistinct_1(self):
        print("Test subarraysWithKDistinct 1... ", end="")
        self.assertEqual(
            7,
            self.sol.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2),
        )
        print("OK")

    def test_subarraysWithKDistinct_2(self):
        print("Test subarraysWithKDistinct 2... ", end="")
        self.assertEqual(
            3,
            self.sol.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
