class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = ones ^ (num & ~twos)
            twos = twos ^ (num & ~ones)

        return ones


def main():
    sol = Solution()
    print('3 ===', sol.singleNumber([2, 2, 3, 2]))
    print('99 ==', sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))


if __name__ == '__main__':
    main()
