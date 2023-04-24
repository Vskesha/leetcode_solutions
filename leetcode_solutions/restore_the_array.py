def numberOfArrays(s: str, k: int) -> int:
    l = len(s)
    ml = len(str(k))
    dp = [1] + [0] * l
    for i in range(1, l + 1):
        for w in range(1, min(i, ml) + 1):
            if s[i - w] != '0' and (w < ml or int(s[i - w:i]) <= k):
                dp[i] += dp[i - w]
                dp[i] %= 1000000007
    return dp[l]


if __name__ == '__main__':
    print('1 ====', numberOfArrays(s="1000", k=10000))
    print('0 ====', numberOfArrays(s="1000", k=10))
    print('8 ====', numberOfArrays(s="1317", k=2000))
    print('34 ===', numberOfArrays(s="1234567890", k=90))