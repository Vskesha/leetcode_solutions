from functools import reduce
from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for length in range(1, len(nums) + 1):
            for comb in combinations(nums, length):
                ans += reduce(lambda x, y: x ^ y, comb)
        return ans


class Solution2:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res * (1 << (len(nums) - 1))


def test_subset_xor_sum():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.subsetXORSum(nums=[1, 3]) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.subsetXORSum(nums=[5, 1, 6]) == 28
    print("OK")

    print("Test 3... ", end="")
    assert sol.subsetXORSum(nums=[3, 4, 5, 6, 7, 8]) == 480
    print("OK")


if __name__ == "__main__":
    test_subset_xor_sum()
