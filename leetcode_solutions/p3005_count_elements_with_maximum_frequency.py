from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        vals = Counter(nums).values()
        mx = max(vals)
        return sum(x for x in vals if x == mx)


def test_max_frequency_elements():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxFrequencyElements(nums=[1, 2, 3, 4, 5]) == 5
    print("OK")


if __name__ == "__main__":
    test_max_frequency_elements()
