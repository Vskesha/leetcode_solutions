from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        return 0


def test_sum_of_powers():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sumOfPower(nums=[1, 2, 3], k=3) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.sumOfPower(nums=[2, 3, 3], k=5) == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.sumOfPower(nums=[1, 2, 3], k=7) == 0
    print("OK")


if __name__ == "__main__":
    test_sum_of_powers()
