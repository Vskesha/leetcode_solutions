from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums


class Solution2:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        res = []
        for a, b in zip(even, odd):
            res.append(a)
            res.append(b)
        return res


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.sortArrayByParityII(nums=[4, 2, 5, 7]) == [4, 5, 2, 7]
    print('OK')

    print('Test 2... ', end='')
    assert sol.sortArrayByParityII(nums=[2, 3]) == [2, 3]
    print('OK')


if __name__ == '__main__':
    test()
