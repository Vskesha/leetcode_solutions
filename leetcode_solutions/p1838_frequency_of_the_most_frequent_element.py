from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, st, summ = 1, 0, 0

        for i in range(len(nums)):
            summ += nums[i]
            while nums[i] * (i - st + 1) > k + summ:
                summ -= nums[st]
                st += 1
            ans = max(ans, i - st + 1)

        return ans


class Solution2:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, st, summ, curr = 1, 0, 0, nums[0]

        for i in range(1, len(nums)):
            summ += curr
            curr = nums[i]
            while curr * (i - st) - summ > k:
                summ -= nums[st]
                st += 1
            ans = max(ans, i - st + 1)

        return ans


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.maxFrequency(nums=[1, 2, 4], k=5) == 3
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.maxFrequency(nums=[1, 4, 8, 13], k=5) == 2
    print("OK")


if __name__ == "__main__":
    test()
