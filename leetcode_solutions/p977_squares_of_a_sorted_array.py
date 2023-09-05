from bisect import bisect_left


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        r = bisect_left(nums, 0)
        l = r - 1
        ans = []
        snums = [n ** 2 for n in nums]
        while l >= 0 and r < ln:
            if snums[r] < snums[l]:
                ans.append(snums[r])
                r += 1
            else:
                ans.append(snums[l])
                l -= 1

        ans.extend(snums[r:] if l < 0 else snums[:l + 1][::-1])
        return ans


def main():
    sol = Solution()
    print(' [0, 1, 9, 16, 100]\n', sol.sortedSquares(nums=[-4, -1, 0, 3, 10]))
    print(' [4, 9, 9, 49, 121]\n', sol.sortedSquares(nums=[-7, -3, 2, 3, 11]))


if __name__ == '__main__':
    main()
