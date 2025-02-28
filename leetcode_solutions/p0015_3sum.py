import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if sum(nums[-3:]) < 0:
            return []
        ln = len(nums)
        ans = []

        for i, ni in enumerate(nums[: ln - 2]):
            if ni > 0:
                break
            if i and ni == nums[i - 1]:
                continue
            l, r = i + 1, ln - 1
            while l < r:
                sm = nums[l] + nums[r] + ni
                if not sm:
                    ans.append([ni, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif sm > 0:
                    r -= 1
                else:
                    l += 1

        return ans


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[l] + nums[r]
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameTriplets(self, result: List[List[int]], expected: List[List[int]]):
        self.assertEqual(len(result), len(expected))
        result = set(tuple(sorted(triplet)) for triplet in result)
        expected = set(tuple(sorted(triplet)) for triplet in expected)
        self.assertSetEqual(result, expected)

    def test_three_sum_1(self):
        print("Test threeSum 1... ", end="")
        self.assertSameTriplets(
            self.sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )
        print("OK")

    def test_three_sum_2(self):
        print("Test threeSum 2... ", end="")
        self.assertSameTriplets(self.sol.threeSum(nums=[0, 1, 1]), [])
        print("OK")

    def test_three_sum_3(self):
        print("Test threeSum 3... ", end="")
        self.assertSameTriplets(self.sol.threeSum(nums=[0, 0, 0]), [[0, 0, 0]])
        print("OK")


if __name__ == "__main__":
    unittest.main()
