from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ln = len(nums)
        freq = [0] * (ln + 1)

        for n in nums:
            freq[min(n, ln)] += 1

        ba = 0
        for k in range(ln, 0, -1):
            ba += freq[k]
            if ba == k:
                return k
            elif ba > k:
                break

        return -1


class Solution2:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ln = len(nums)

        if nums[-1] >= ln:
            return ln

        i = 1
        while i < ln:
            if i > nums[i - 1]:
                return -1
            if nums[i] == nums[i - 1] or nums[i] > i:
                i += 1
            else:
                return i


def test_special_array():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.specialArray(nums=[3, 5]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.specialArray(nums=[0, 0]) == -1
    print("OK")

    print("Test 3... ", end="")
    assert sol.specialArray(nums=[0, 4, 3, 0, 4]) == 3
    print("OK")


if __name__ == "__main__":
    test_special_array()
