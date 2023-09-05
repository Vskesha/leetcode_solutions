class Solution:

    def stoneGameII(self, piles: list[int]) -> int:

        n = len(piles)
        dpt = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        def dp(i, m, alice):
            
            if i == n:
                return 0
            
            if dpt[alice][i][m] != -1:
                return dpt[alice][i][m]
            
            res = 0 if alice else 1000000
            curr_sum = 0
            
            for x in range(1, min(2 * m, n - i) + 1):
                if alice:
                    curr_sum += piles[i + x - 1]
                    res = max(res, curr_sum + dp(i+x, max(x, m), 0))
                else:
                    res = min(res, dp(i+x, max(x, m), 1))
            
            dpt[alice][i][m] = res
            
            return res
        
        return dp(0, 1, 1)
        

if __name__ == '__main__':
    sol = Solution()
    print('10 ===', sol.stoneGameII([2,7,9,4,4]))
    print('104 ===', sol.stoneGameII([1,2,3,4,5,100]))
    print('17 ===', sol.stoneGameII([1,5,7,9,9]))
    print('112766 ===', sol.stoneGameII([3111,4303,2722,2183,6351,5227,8964,7167,9286,6626,2347,1465,5201,7240,5463,8523,8163,9391,8616,5063,7837,7050,1246,9579,7744,6932,7704,9841,6163,4829,7324,6006,4689,8781,621]))
    