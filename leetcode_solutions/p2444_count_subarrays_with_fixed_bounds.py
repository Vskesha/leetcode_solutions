from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def get_count_from_subarr(st, end) -> int:
            ans = 0
            min_idx = max_idx = begin = st - 1
            for i in range(st, end):
                if nums[i] == minK:
                    min_idx = i
                    begin = min(min_idx, max_idx)
                if nums[i] == maxK:
                    max_idx = i
                    begin = min(min_idx, max_idx)
                ans += begin - st + 1
            return ans

        ln = len(nums)
        i = 0
        ans = 0
        while i < ln:
            while i < ln and (nums[i] < minK or nums[i] > maxK):
                i += 1
            st = i
            while i < ln and minK <= nums[i] <= maxK:
                i += 1
            ans += get_count_from_subarr(st, i)

        return ans


def test_count_subarrays():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1) == 10
    print("OK")


if __name__ == "__main__":
    test_count_subarrays()
