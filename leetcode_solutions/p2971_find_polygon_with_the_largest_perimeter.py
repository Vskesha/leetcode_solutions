from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        tot = sum(nums)
        for i, n in enumerate(nums):
            tot -= n
            if n < tot:
                return tot + n
        return -1


class Solution2:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        tot = sum(nums)
        ln = len(nums)

        for i in range(ln - 2):
            tot -= nums[i]
            if nums[i] < tot:
                return nums[i] + tot

        return -1


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.largestPerimeter(nums=[5, 5, 5]) == 15
    print("OK")

    print("Test 2... ", end="")
    assert sol.largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3]) == 12
    print("OK")

    print("Test 3... ", end="")
    assert sol.largestPerimeter(nums=[5, 5, 50]) == -1
    print("OK")


if __name__ == "__main__":
    test()
