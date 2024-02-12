from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.majorityElement(nums=[3, 2, 3]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    print("OK")


if __name__ == "__main__":
    test()
