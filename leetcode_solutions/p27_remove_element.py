from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ln = len(nums)
        l, r = 0, ln - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return r + 1


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for n in nums:
            if n != val:
                nums[k] = n
                k += 1

        return k


def test_remove_element():
    sol = Solution()

    print("Test 1... ", end="")
    nums = [3, 2, 2, 3]
    assert sol.removeElement(nums=nums, val=3) == 2
    nums_v = [2, 2]
    assert set(nums_v) == set(nums[: len(nums_v)])
    print("OK")

    print("Test 2... ", end="")
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert sol.removeElement(nums=nums, val=2) == 5
    nums_v = [0, 1, 4, 0, 3]
    assert set(nums_v) == set(nums[: len(nums_v)])
    print("OK")


if __name__ == "__main__":
    test_remove_element()
