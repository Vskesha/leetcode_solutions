from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st = bisect_left(nums, target)
        if st == len(nums) or nums[st] != target:
            return [-1, -1]
        en = bisect_right(nums, target, lo=st) - 1
        return [st, en]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l1, r1 = 0, len(nums)

        while l1 < r1:
            mid = (l1 + r1) // 2
            if nums[mid] >= target:
                r1 = mid
            else:
                l1 = mid + 1

        if l1 == len(nums) or nums[l1] != target:
            return [-1, -1]

        l2, r2 = l1, len(nums)

        while l2 < r2:
            mid = (l2 + r2) // 2
            if nums[mid] > target:
                r2 = mid
            else:
                l2 = mid + 1

        return [l1, l2 - 1]


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    print("ok")

    print("Test 3 ... ", end="")
    assert sol.searchRange(nums=[], target=0) == [-1, -1]
    print("ok")

    print("Test 4 ... ", end="")
    assert sol.searchRange(nums=[1], target=1) == [0, 0]
    print("ok")


if __name__ == "__main__":
    test()
