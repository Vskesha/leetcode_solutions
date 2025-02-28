from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)

        i = ln - 1
        while i and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.sort()
            return

        sorter = Sorter()
        sorter.quick_sort(nums, i, ln - 1)
        pi = i - 1
        prev = nums[pi]
        while nums[i] <= prev:
            i += 1
        nums[pi], nums[i] = nums[i], nums[pi]


class Sorter:
    def quick_sort(self, nums: List[int], l: int, r: int):
        if l < r:
            pivot = self.partition(nums, l, r)
            self.quick_sort(nums, l, pivot - 1)
            self.quick_sort(nums, pivot + 1, r)

    @staticmethod
    def partition(nums: List[int], l: int, r: int) -> int:
        pivot = nums[l]
        st = l + 1
        for i in range(l + 1, r + 1):
            if nums[i] < pivot:
                nums[st], nums[i] = nums[i], nums[st]
                st += 1
        nums[l], nums[st - 1] = nums[st - 1], nums[l]
        return st - 1


def test_next_permutation():
    sol = Solution()

    print("Test 1... ", end="")
    nums = [1, 2, 3]
    out = [1, 3, 2]
    sol.nextPermutation(nums)
    assert nums == out
    print("OK")

    print("Test 2... ", end="")
    nums = [3, 2, 1]
    out = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == out
    print("OK")

    print("Test 3... ", end="")
    nums = [1, 1, 5]
    out = [1, 5, 1]
    sol.nextPermutation(nums)
    assert nums == out
    print("OK")


if __name__ == "__main__":
    test_next_permutation()
