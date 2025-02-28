from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.missingNumber(nums=[3, 0, 1]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.missingNumber(nums=[0, 1]) == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("OK")


if __name__ == "__main__":
    test()
