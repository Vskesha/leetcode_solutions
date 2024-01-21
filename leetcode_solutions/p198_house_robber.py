from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = iter(nums)
        rb, om = next(nums), 0
        for n in nums:
            rb, om = om + n, max(rb, om)
        return max(rb, om)


class Solution1:
    def rob(self, nums: List[int]) -> int:
        rb, om = nums[0], 0
        for i in range(1, len(nums)):
            rb, om = om + nums[i], max(rb, om)
        return max(rb, om)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        rb, om = [0] * ln, [0] * ln
        rb[0] = nums[0]

        for i in range(1, ln):
            rb[i] = om[i - 1] + nums[i]
            om[i] = max(rb[i - 1], om[i - 1])

        return max(rb[-1], om[-1])


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.rob(nums=[1, 2, 3, 1]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.rob(nums=[2, 7, 9, 3, 1]) == 12
    print("OK")


if __name__ == "__main__":
    test()
