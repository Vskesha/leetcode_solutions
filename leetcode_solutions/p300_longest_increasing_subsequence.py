from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tails = [nums[0]]
        for n in nums:
            if n > tails[-1]:
                tails.append(n)
            else:
                tails[bisect_left(tails, n)] = n
        return len(tails)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
    print("OK")


if __name__ == "__main__":
    test()
