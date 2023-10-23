from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [1] * ln
        prefix = suffix = 1

        for i in range(ln):
            res[i] *= prefix
            prefix *= nums[i]
            res[-i-1] *= suffix
            suffix *= nums[-i-1]

        return res


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        answer = [1] * ln
        prefix = 1
        for i in range(1, ln):
            prefix *= nums[i - 1]
            answer[i] = prefix
        suffix = 1
        for i in range(ln - 2, -1, -1):
            suffix *= nums[i + 1]
            answer[i] *= suffix
        return answer


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert [24, 12, 8, 6] == sol.productExceptSelf(nums=[1, 2, 3, 4])
    print('ok')

    print('Test 2 ... ', end='')
    assert [0, 0, 9, 0, 0] == sol.productExceptSelf(nums=[-1, 1, 0, -3, 3])
    print('ok')


if __name__ == '__main__':
    main()
