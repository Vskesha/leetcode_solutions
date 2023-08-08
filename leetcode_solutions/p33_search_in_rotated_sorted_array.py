class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ln = len(nums)

        if nums[0] <= nums[-1]:
            l, r = 0, ln - 1
        else:
            al, ar, val = 0, ln - 1, nums[0]
            while al < ar:
                m = (al + ar) // 2
                if nums[m] < val:
                    ar = m
                else:
                    al = m + 1
            l, r = (al, ln - 1) if target < val else (0, ar - 1)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l if nums[l] == target else -1


def main():
    sol = Solution()
    print('4 ===', sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print('-1 ===', sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print('-1 ===', sol.search(nums=[1], target=0))


if __name__ == '__main__':
    main()
