from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


def equal(lst1, lst2):
    for a, b in zip(lst1, lst2):
        if b == "_":
            break
        if a != b:
            return False
    return True


def test():
    _ = "_"
    sol = Solution()

    print("Test 1... ", end="")
    nums = [1, 1, 2]
    assert sol.removeDuplicates(nums) == 2
    assert equal(nums, [1, 2, _])
    print("OK")

    print("Test 2... ", end="")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert sol.removeDuplicates(nums) == 5
    assert equal(
        nums,
        [
            0,
            1,
            2,
            3,
            4,
            _,
            _,
            _,
        ],
    )
    print("OK")


if __name__ == "__main__":
    test()
