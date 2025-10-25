from functools import lru_cache
from typing import Any, Tuple


# recursive solution
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        nums.append(float("inf"))
        ln = len(nums)

        @lru_cache(None)
        def dp(i: int) -> tuple[int | Any, int]:

            length_i = 1
            count_i = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    length_j, count_j = dp(j)
                    if length_j + 1 > length_i:
                        length_i = length_j + 1
                        count_i = 0
                    if length_j + 1 == length_i:
                        count_i += count_j

            return length_i, count_i

        ans = dp(ln - 1)[1]
        nums.pop()
        return ans


# iterative solution
class Solution2:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        nums.append(float("inf"))
        ln = len(nums)
        length = [1] * ln
        count = [1] * ln

        for i in range(ln):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        nums.pop()
        return count[-1]


def main():
    sol = Solution()
    print("2 ===", sol.findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
    print("5 ===", sol.findNumberOfLIS(nums=[2, 2, 2, 2, 2]))


if __name__ == "__main__":
    main()
