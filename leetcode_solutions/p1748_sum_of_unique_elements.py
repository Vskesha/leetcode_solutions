from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, q in Counter(nums).items() if q == 1)


def test_sum_of_unique():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.sumOfUnique(nums=[1, 2, 3, 2]) == 4
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.sumOfUnique(nums=[1, 1, 1, 1, 1]) == 0
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.sumOfUnique(nums=[1, 2, 3, 4, 5]) == 15
    print("OK")


if __name__ == "__main__":
    test_sum_of_unique()
