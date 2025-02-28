import unittest
from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped, flips = deque(), 0

        for i, num in enumerate(nums):
            if flipped and flipped[0] == i - k:
                flipped.popleft()
            if len(flipped) % 2 == num:
                if i + k > len(nums):
                    return -1
                flips += 1
                flipped.append(i)

        return flips


class Solution1:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        window = deque()
        flipped = flips = 0

        for i, num in enumerate(nums):
            if i >= k:
                flipped ^= window.popleft()

            if flipped == num:
                if i + k > len(nums):
                    return -1
                flipped ^= 1
                flips += 1
                window.append(1)
            else:
                window.append(0)

        return flips


class Solution2:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = flipCount = 0

        for i in range(len(nums)):
            if i >= k and flipped[i - k]:
                validFlipsFromPastWindow -= 1

            if validFlipsFromPastWindow % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1

        return flipCount


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_k_bit_flips_1(self):
        print("Test minKBitFlips 1... ", end="")
        self.assertEqual(self.sol.minKBitFlips(nums=[0, 1, 0], k=1), 2)
        print("OK")

    def test_min_k_bit_flips_2(self):
        print("Test minKBitFlips 2... ", end="")
        self.assertEqual(self.sol.minKBitFlips(nums=[1, 1, 0], k=2), -1)
        print("OK")

    def test_min_k_bit_flips_3(self):
        print("Test minKBitFlips 3... ", end="")
        self.assertEqual(self.sol.minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3), 3)
        print("OK")


if __name__ == "__main__":
    unittest.main()
