import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = sorted((n, i) for i, n in enumerate(nums))
        li, r = 0, len(nums) - 1

        while li < r:
            sm = idx[li][0] + idx[r][0]
            if sm == target:
                return [idx[li][1], idx[r][1]]
            elif sm > target:
                r -= 1
            else:
                li += 1


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in hm:
                return [hm[c], i]
            hm[n] = i


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_two_sum_1(self) -> None:
        print("Test twoSum 1... ", end="")
        self.assertEqual(
            self.sol.twoSum(nums=[2, 7, 11, 15], target=9), [0, 1]
        )
        print("OK")

    def test_two_sum_2(self) -> None:
        print("Test twoSum 2... ", end="")
        self.assertEqual(self.sol.twoSum(nums=[3, 2, 4], target=6), [1, 2])
        print("OK")

    def test_two_sum_3(self) -> None:
        print("Test twoSum 3... ", end="")
        self.assertEqual(self.sol.twoSum(nums=[3, 3], target=6), [0, 1])
        print("OK")


if __name__ == "__main__":
    unittest.main()
