def is_match(s: str, p: str) -> bool:

    n=len(s)
    m=len(p)
    dp=[[False]*(m+1) for _ in range(n+1)]
    dp[0][0]=True
    for i in range(1, m+1):
        if p[i-1]=="*":
            dp[0][i] = dp[0][i-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == p[j-1] or p[j-1]=="?":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[-1][-1]


def is_match1(s: str, p: str) -> bool:
    i, j, last_matched, asterisk = 0, 0, 0, -1
    
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            last_matched = i
            asterisk = j
            j += 1
        elif asterisk != -1:
            j = asterisk + 1
            i = last_matched + 1
            last_matched += 1
        else:
            return False
        
    while j < len(p) and p[j] == '*':
            j += 1
        
    return j == len(p)


def is_match2(s: str, p: str) -> bool:
    def match(s, p):
        i = len(s) - 1
        j = len(p) - 1
        asterisks = p.count('*')

        if j - asterisks > i:
            return False

        if not s:
            return True

        if not p:
            return False

        while i >= 0 and j >= 0:
            if p[j] == '*':
                break
            elif p[j] == '?' or p[j] == s[i]:
                i -= 1
                j -= 1
            else:
                return False

        if p[j] == '*':
            return match(s[:i+1], p[:j]) or match(s[:i], p[:j+1])

        return match(s[:i+1], p[:j+1])

    while '**' in p:
        p = p.replace('**', '*')

    return match(s, p)

if __name__ == '__main__':
    print('False ===', is_match(s = "aa", p = "a"))
    print('True ====', is_match(s = "aa", p = "*"))
    print('False ===', is_match(s = "cb", p = "?a"))
    print('True ====', is_match(s = "adceb", p = "*a*b"))
    print('True ====', 
          is_match(s = "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab", 
                   p = "*aabb***aa**a******aa*"))
    print('False ===',
          is_match(s = "abaabaaaabbabbaaabaabababbaabaabbabaaaaabababbababaabbabaabbbbaabbbbbbbabaaabbaaaaabbaabbbaaaaabbbabb",
                   p = "ab*aaba**abbaaaa**b*b****aa***a*b**ba*a**ba*baaa*b*ab*"))