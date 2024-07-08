import unittest
from functools import cache
from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ln = len(nums)

        @cache
        def k_sum_closest(k, i, t):
            if k == 1:
                return min(nums[i:], key=lambda x: abs(x - t))

            if k == ln - i:
                return sum(nums[i:])

            ans = sum(nums[-k:])
            if ans <= t:
                return ans

            ans = sum(nums[i : i + k])
            if ans >= t:
                return ans

            for j in range(i, ln - k + 1):
                if j > i and nums[j] == nums[i]:
                    continue
                curr = nums[j] + k_sum_closest(k - 1, j + 1, t - nums[j])
                if abs(t - curr) < abs(t - ans):
                    if t - curr == 0:
                        return curr
                    ans = curr

            return ans

        return k_sum_closest(3, 0, target)


class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_first_3, sum_last_3 = sum(nums[:3]), sum(nums[-3:])
        if sum_first_3 >= target:
            return sum_first_3
        if sum_last_3 <= target:
            return sum_last_3

        best_diff = inf
        best_sum = target
        ln = len(nums)

        for i in range(ln - 2):
            min_sum = sum(nums[i : i + 3])
            if min_sum >= target:
                if min_sum - target < best_diff:
                    return min_sum
                break

            max_sum = sum(nums[-2:]) + nums[i]
            if max_sum <= target:
                diff = target - max_sum
                if not diff:
                    return max_sum
                if diff < best_diff:
                    best_diff = diff
                    best_sum = max_sum
                continue

            l, r = i + 1, ln - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                diff = sm - target
                if not diff:
                    return sm
                elif abs(diff) < best_diff:
                    best_diff = abs(diff)
                    best_sum = sm
                if diff > 0:
                    r -= 1
                else:
                    l += 1

        return best_sum


class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dif = target - sum(nums[:3])
        ln = len(nums)
        for i in range(ln - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            trg = target - nums[i]
            li = i + 1
            ri = ln - 1
            while li < ri:
                dif = trg - nums[li] - nums[ri]
                if abs(min_dif) > abs(dif):
                    min_dif = dif
                if not dif:  # dif == 0
                    return target
                elif dif > 0:  # dif > 0
                    li += 1
                else:  # dif < 0
                    ri -= 1
        return target - min_dif


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_three_sum_closest_1(self):
        print("Test threeSumClosest 1... ", end="")
        self.assertEqual(self.sol.threeSumClosest(nums=[-1, 2, 1, -4], target=1), 2)
        print("OK")

    def test_three_sum_closest_2(self):
        print("Test threeSumClosest 2... ", end="")
        self.assertEqual(self.sol.threeSumClosest(nums=[0, 0, 0], target=1), 0)
        print("OK")

    def test_three_sum_closest_3(self):
        print("Test threeSumClosest 3... ", end="")
        self.assertEqual(self.sol.threeSumClosest(nums=[-2, -1, 1, 4], target=0), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()
