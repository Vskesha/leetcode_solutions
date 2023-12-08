from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0, i1, i2 = 0, 0, len(nums) - 1

        while i1 <= i2:
            if nums[i1] == 0:
                nums[i0], nums[i1] = nums[i1], nums[i0]
                i1 += 1
                i0 += 1
            elif nums[i1] == 2:
                nums[i2], nums[i1] = nums[i1], nums[i2]
                i2 -= 1
            else:
                i1 += 1


class Solution2:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


def test():
    sol = Solution()

    print('Test 1... ', end='')
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
    print('OK')

    print('Test 2... ', end='')
    nums = [2, 0, 1]
    sol.sortColors(nums)
    assert nums == [0, 1, 2]
    print('OK')


if __name__ == '__main__':
    test()
