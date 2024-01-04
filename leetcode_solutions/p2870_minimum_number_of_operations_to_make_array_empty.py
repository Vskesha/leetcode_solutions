from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for q in cnt.values():
            if q == 1:
                return -1
            else:
                ans += (q - 1) // 3 + 1
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.minOperations(nums=[2, 1, 2, 2, 3, 3]) == -1
    print("OK")


if __name__ == "__main__":
    test()
