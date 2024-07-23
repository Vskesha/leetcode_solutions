import unittest
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mc = sorted((fr, -k) for k, fr in Counter(nums).items())
        return [-k for fr, k in mc for _ in range(fr)]


class Solution2:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted(nums, key=lambda x: (cnt[x], -x))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_frequencySort_1(self):
        print("Test frequencySort 1... ", end="")
        self.assertListEqual(
            [3, 1, 1, 2, 2, 2], self.sol.frequencySort(nums=[1, 1, 2, 2, 2, 3])
        )
        print("OK")

    def test_frequencySort_2(self):
        print("Test frequencySort 2... ", end="")
        self.assertListEqual(
            [1, 3, 3, 2, 2], self.sol.frequencySort(nums=[2, 3, 1, 3, 2])
        )
        print("OK")

    def test_frequencySort_3(self):
        print("Test frequencySort 3... ", end="")
        self.assertListEqual(
            [5, -1, 4, 4, -6, -6, 1, 1, 1],
            self.sol.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
