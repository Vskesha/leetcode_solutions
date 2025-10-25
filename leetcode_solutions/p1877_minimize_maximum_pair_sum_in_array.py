from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[~i] for i in range(len(nums) // 2))


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.minPairSum(nums=[3, 5, 2, 3]) == 7
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.minPairSum(nums=[3, 5, 4, 2, 4, 6]) == 8
    print("OK")


if __name__ == "__main__":
    test()
