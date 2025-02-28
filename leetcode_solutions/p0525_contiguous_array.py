from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        diffs = {0: -1}
        ans = 0
        for i, n in enumerate(nums):
            diff += n * 2 - 1
            if diff in diffs:
                ans = max(ans, i - diffs[diff])
            else:
                diffs[diff] = i
        return ans


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        totalsum, hashmap = 0, {0: -1}
        res, diff = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                totalsum -= 1
            else:
                totalsum += 1
            try:
                diff = i - hashmap[totalsum]
                if diff > res:
                    res = diff
            except:
                hashmap[totalsum] = i
        return res


def test_find_max_length():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findMaxLength(nums=[0, 1]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.findMaxLength(nums=[0, 1, 0]) == 2
    print("OK")


if __name__ == "__main__":
    test_find_max_length()
