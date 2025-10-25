import unittest
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        ln = len(nums)
        for i in range(ln - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, ln - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                trg = target - nums[i] - nums[j]
                li = j + 1
                ri = ln - 1
                while li < ri:
                    sm = nums[li] + nums[ri]
                    if sm > trg:
                        ri -= 1
                    elif sm < trg:
                        li += 1
                    else:
                        result.append([nums[i], nums[j], nums[li], nums[ri]])
                        li += 1
                        while li < ln and nums[li] == nums[li - 1]:
                            li += 1
        return result


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        quads = []

        for i in range(ln - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, ln - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                nt = target - nums[i] - nums[j]
                l, r = j + 1, ln - 1
                while l < r:
                    sm = nums[l] + nums[r]
                    if sm == nt:
                        quads.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sm > nt:
                        r -= 1
                    else:
                        l += 1
        return quads


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def same_combinations(
        self, a: List[List[int]], b: List[List[int]]
    ) -> bool:
        return set(map(tuple, [sorted(x) for x in a])) == set(
            map(tuple, [sorted(x) for x in b])
        )

    def test_four_sum_1(self):
        print("Test fourSum 1... ", end="")
        self.assertTrue(
            self.same_combinations(
                self.sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0),
                [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            )
        )
        print("OK")

    def test_four_sum_2(self):
        print("Test fourSum 2... ", end="")
        self.assertTrue(
            self.same_combinations(
                self.sol.fourSum(nums=[2, 2, 2, 2, 2], target=8),
                [[2, 2, 2, 2]],
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
