def gp(n, o, c, s):
    if n == o == c:
        return [s]
    r = []
    if o < n:
        r.extend(gp(n, o+1, c, s+"("))
    if c < o:
        r.extend(gp(n, o, c+1, s+")"))
    return r


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return gp(n, 0, 0, "")


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(4))
    print(sol.generateParenthesis(5))

