from bisect import bisect_left


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        ln = len(nums)
        left, right = 0, ln - 1

        while left <= right:
            if right - left < 10:
                for i in range(left, right + 1):
                    if nums[i] == target:
                        return True
                return False
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] > nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < nums[left]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                while left < ln and nums[left] == nums[middle]:
                    left += 1
                while right >= 0 and nums[right] == nums[middle]:
                    right -= 1

        return False


class Solution2:
    def search(self, nums: list[int], target: int) -> bool:
        ln = len(nums)
        if ln == 1:
            return nums[0] == target

        piv = 1
        while piv < ln - 1 and nums[piv] >= nums[piv - 1]:
            piv += 1

        if target > nums[0]:
            l, r = 1, piv
        elif target < nums[0]:
            l, r = piv, ln - 1
        else:
            return True

        idx = bisect_left(nums, target, lo=l, hi=r)
        return nums[idx] == target


def main():
    sol = Solution()
    print('True ===', sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
    print('False ===', sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
    print('False ===', sol.search(nums=[1, 1], target=0))


if __name__ == '__main__':
    main()
