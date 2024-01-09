from collections import defaultdict


class Solution1:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        map = {}

        for i in range(n):
            temp = nums[i]
            if temp not in map:
                map[temp] = []
            map[temp].append(i)

        total_sum = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                a = 2 * nums[i] - nums[j]
                if a in map:
                    for k in map[a]:
                        if k < i:
                            dp[i][j] += dp[k][i] + 1
                        else:
                            break
                total_sum += dp[i][j]

        return total_sum


class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)

        total_sum = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                a = 2 * nums[i] - nums[j]
                if a in mp:
                    for k in mp[a]:
                        if k < i:
                            dp[i][j] += dp[k][i] + 1
                        else:
                            break
                total_sum += dp[i][j]

        return total_sum


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]) == 7
    print("OK")

    print("Test 2... ", end="")
    assert sol.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]) == 16
    print("OK")


if __name__ == "__main__":
    test()
