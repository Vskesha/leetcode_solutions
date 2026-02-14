class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ln = len(nums)

        if nums[0] <= nums[-1]:
            left, right = 0, ln - 1
        else:
            al, ar, val = 0, ln - 1, nums[0]
            while al < ar:
                mid = (al + ar) // 2
                if nums[mid] < val:
                    ar = mid
                else:
                    al = mid + 1
            left, right = (al, ln - 1) if target < val else (0, ar - 1)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] == target else -1


def main():
    sol = Solution()
    print("4 ===", sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print("-1 ===", sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print("-1 ===", sol.search(nums=[1], target=0))


if __name__ == "__main__":
    main()
