from heapq import nlargest, nsmallest
from operator import mul
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return mul(*nlargest(2, nums)) - mul(*nsmallest(2, nums))


class Solution1:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


class Solution2:
    def maxProductDifference(self, nums: List[int]) -> int:
        s, ss, sb, b = sorted(nums[:4])
        for i in range(4, len(nums)):
            n = nums[i]
            if n > b:
                b, sb = n, b
            elif n > sb:
                sb = n
            elif n < s:
                s, ss = n, s
            elif n < ss:
                ss = n
        return b * sb - s * ss


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxProductDifference(nums=[5, 6, 2, 7, 4]) == 34
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8]) == 64
    print("OK")


if __name__ == "__main__":
    test()
