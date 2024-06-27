import unittest
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        ln = len(nums)

        for i, n in enumerate(nums):
            while 0 <= n < ln and nums[n] != n:
                nums[n], n = n, nums[n]

        for i, n in enumerate(nums):
            if n != i:
                return i

        return ln


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ln = len(nums)
        is_one = False

        for i, n in enumerate(nums):
            if n == 1:
                is_one = True
            elif n < 1 or n > ln:
                nums[i] = 1

        if not is_one:
            return 1

        for i, n in enumerate(nums):
            j = abs(n) - 1
            nums[j] = -abs(nums[j])

        for i, n in enumerate(nums):
            if n > 0:
                return i + 1

        return ln + 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_first_missing_positive_1(self):
        print("Test firstMissingPositive 1... ", end="")
        self.assertEqual(self.sol.firstMissingPositive(nums=[1, 2, 0]), 3)
        print("OK")

    def test_first_missing_positive_2(self):
        print("Test firstMissingPositive 2... ", end="")
        self.assertEqual(self.sol.firstMissingPositive(nums=[3, 4, -1, 1]), 2)
        print("OK")

    def test_first_missing_positive_3(self):
        print("Test firstMissingPositive 3... ", end="")
        self.assertEqual(self.sol.firstMissingPositive(nums=[7, 8, 9, 11, 12]), 1)
        print("OK")


if __name__ == '__main__':
    unittest.main()
