import unittest
from bisect import bisect_left
from collections import Counter
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        p = [(nums[i], nums[~i]) for i in range(len(nums) // 2)]
        ds = Counter(abs(a - b) for a, b in p)
        md = sorted(max(a, b, k - a, k - b) for a, b in p)
        return len(p) + min(bisect_left(md, d) - v for d, v in ds.items())


class Solution2:
    def minChanges(self, nums: List[int], k: int) -> int:
        p = [
            (max(nums[i], nums[~i]), min(nums[i], nums[~i]))
            for i in range(len(nums) // 2)
        ]
        ds = Counter(a - b for a, b in p)
        md = sorted(max(a, k - b) for a, b in p)
        return len(p) + min(bisect_left(md, d) - v for d, v in ds.items())


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minChanges_1(self):
        print("Test minChanges 1... ", end="")
        self.assertEqual(2, self.sol.minChanges(nums=[1, 0, 1, 2, 4, 3], k=4))
        print("OK")

    def test_minChanges_2(self):
        print("Test minChanges 2... ", end="")
        self.assertEqual(
            2, self.sol.minChanges(nums=[0, 1, 2, 3, 3, 6, 5, 4], k=6)
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
