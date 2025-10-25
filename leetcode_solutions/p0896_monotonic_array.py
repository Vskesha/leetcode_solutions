from typing import List


class Solution2:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = nums[-1] > nums[0]

        for i in range(1, len(nums)):
            if is_increasing and nums[i] < nums[i - 1]:
                return False
            elif not is_increasing and nums[i] > nums[i - 1]:
                return False
        return True


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        bigger = nums[-1] > nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif (nums[i] < nums[i - 1]) is bigger:
                return False
        return True


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.isMonotonic(nums=[1, 2, 2, 3]) is True
    print("ok\nTest 2 ... ", end="")
    assert sol.isMonotonic(nums=[6, 5, 4, 4]) is True
    print("ok\nTest 3 ... ", end="")
    assert sol.isMonotonic(nums=[1, 3, 2]) is False
    print("ok")


if __name__ == "__main__":
    test()
