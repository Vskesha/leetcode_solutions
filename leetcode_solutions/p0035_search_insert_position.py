from bisect import bisect_left
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


def test_search_insert():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    print("OK")


if __name__ == "__main__":
    test_search_insert()
