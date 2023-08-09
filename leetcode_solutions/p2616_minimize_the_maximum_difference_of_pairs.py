# binary search and greedy solution
class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        if not p:
            return 0
        nums.sort()
        ln = len(nums)
        diffs = [nums[i] - nums[i - 1] for i in range(1, ln)]

        def has_p_pairs(diff) -> bool:
            i = 0
            pairs = 0
            while i < ln - 1:
                if diffs[i] <= diff:
                    pairs += 1
                    if pairs == p:
                        return True
                    i += 1
                i += 1
            return False

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            middle = (left + right) // 2
            if has_p_pairs(middle):
                right = middle
            else:
                left = middle + 1
        return left


def main():
    sol = Solution()
    print('1 ===', sol.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
    print('0 ===', sol.minimizeMax(nums=[4, 2, 1, 2], p=1))


if __name__ == '__main__':
    main()
