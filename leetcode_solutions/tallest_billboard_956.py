class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for d, r in list(dp.items()):
                dp[d + rod] = max(dp.get(d + rod, 0), r + rod)
                if d > rod:
                    dp[d - rod] = max(dp.get(d - rod, 0), r)
                else:
                    dp[rod - d] = max(dp.get(rod - d, 0), r - d + rod)
        return dp[0]


def main():
    sol = Solution()
    print('6 ===', sol.tallestBillboard(rods=[1, 2, 3, 6]))
    print('10 ===', sol.tallestBillboard(rods=[1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
