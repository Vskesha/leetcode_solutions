class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        res = [1] * ln
        prefix = suffix = 1

        for i in range(ln):
            res[i] *= prefix
            prefix *= nums[i]
            res[-i-1] *= suffix
            suffix *= nums[-i-1]

        return res


def main():
    sol = Solution()
    assert [24, 12, 8, 6] == sol.productExceptSelf(nums=[1, 2, 3, 4])
    print('Test 1 ... ok')
    assert [0, 0, 9, 0, 0] == sol.productExceptSelf(nums=[-1, 1, 0, -3, 3])
    print('Test 2 ... ok')


if __name__ == '__main__':
    main()
