from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        zero_groups = []
        curr_group = 1
        for n in nums:
            if n:
                zero_groups.append(curr_group)
                curr_group = 1
            else:
                curr_group += 1
        zero_groups.append(curr_group)

        if not goal:
            return sum(map(lambda x: x * (x - 1) // 2, zero_groups))

        ans = 0
        lz = len(zero_groups)
        for l, r in zip(range(lz), range(goal, lz)):
            ans += zero_groups[l] * zero_groups[r]
        return ans


def test_num_subarray_with_sum():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0) == 15
    print("OK")


if __name__ == "__main__":
    test_num_subarray_with_sum()
