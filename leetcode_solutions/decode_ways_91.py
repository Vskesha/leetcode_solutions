class Solution:
    def numDecodings(self, s: str) -> int:
        ls = len(s)
        dp = [1] * (ls + 1)
        if s[0] == '0':
            return 0

        for i in range(1, ls):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif 10 < int(s[i-1]+s[i]) < 27:
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[-1]
    
    
if __name__ == '__main__':
    sol = Solution()
    print('2 ===', sol.numDecodings(s = "12"))
    print('3 ===', sol.numDecodings(s = "226"))
    print('0 ===', sol.numDecodings(s = "06"))
    