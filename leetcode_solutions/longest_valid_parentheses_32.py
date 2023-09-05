class Solution:

    # solution using stack
    def longestValidParentheses(self, s: str) -> int:
        max_valid = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_valid = max(max_valid, i - stack[-1])
                else:
                    stack.append(i)

        return max_valid

    # brute force solution
    def longestValidParentheses1(self, s: str) -> int:
        n = len(s)

        def is_valid(string):
            op = 0
            for c in string:
                if c == '(':
                    op += 1
                else:
                    op -= 1
                if op < 0:
                    return False
            return not op

        for substring_len in range(n, -1, -1):
            for start in range(n - substring_len + 1):
                ss = s[start:start + substring_len]
                if is_valid(ss):
                    return substring_len

    # dp solution
    def longestValidParentheses2(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2
                    if i > 1:
                        dp[i] += dp[i-2]
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i-dp[i-1]-2]
            ans = max(ans, dp[i])
        return ans


def main():
    sol = Solution()
    print('2 ===', sol.longestValidParentheses("(()"))
    print('4 ===', sol.longestValidParentheses(")()())"))
    print('0 ===', sol.longestValidParentheses(''))
    print('8 ===', sol.longestValidParentheses('()(()()))('))


if __name__ == '__main__':
    main()
