from bisect import bisect_left
from typing import List


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        r = bisect_left(nums, 0)
        l = r - 1
        ans = []
        snums = [n**2 for n in nums]
        while l >= 0 and r < ln:
            if snums[r] < snums[l]:
                ans.append(snums[r])
                r += 1
            else:
                ans.append(snums[l])
                l -= 1

        ans.extend(snums[r:] if l < 0 else snums[: l + 1][::-1])
        return ans


class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: pow(x, 2), nums))


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num**2 for num in nums)


def main():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sortedSquares(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    print("OK")

    print("Test 2... ", end="")
    assert sol.sortedSquares(nums=[-7, -3, 2, 3, 11])
    print("OK")


if __name__ == "__main__":
    main()
