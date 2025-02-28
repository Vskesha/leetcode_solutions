from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        nums.sort()
        ans = [[n] for n in nums]

        for i in range(ln):
            for j in range(i):
                if not nums[i] % nums[j]:
                    curr = ans[j] + [nums[i]]
                    ans[i] = max(ans[i], curr, key=len)

        return max(ans, key=len)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.largestDivisibleSubset(nums=[1, 2, 3]) == [1, 2]
    print('OK')

    print('Test 2... ', end='')
    assert sol.largestDivisibleSubset(nums=[1, 2, 4, 8]) == [1, 2, 4, 8]
    print('OK')


if __name__ == '__main__':
    test()
