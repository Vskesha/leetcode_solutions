from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        total = sum(nums)
        ln = len(nums)
        prefix = 0

        for i, n in enumerate(nums):
            left = n * i - prefix
            prefix += n
            right = total - prefix - n * (ln - i - 1)
            ans.append(left + right)
        return ans


class Solution2:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans = [0] * ln
        prefix = suffix = 0
        for i in range(1, ln):
            j = ~i
            prefix += (nums[i] - nums[i - 1]) * i
            suffix += (nums[j + 1] - nums[j]) * i
            ans[i] += prefix
            ans[j] += suffix
        return ans


class Solution3:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans = [0] * ln
        prefix = suffix = 0

        for i in range(1, ln):
            j = ~i
            prefix += nums[i - 1]
            ans[i] += nums[i] * i - prefix
            suffix += nums[j + 1]
            ans[j] += suffix - nums[j] * i

        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.getSumAbsoluteDifferences(nums=[2, 3, 5]) == [4, 3, 5]
    print("OK")

    print("Test 2... ", end="")
    assert sol.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]) == [
        24,
        15,
        13,
        15,
        21,
    ]
    print("OK")


if __name__ == "__main__":
    test()
