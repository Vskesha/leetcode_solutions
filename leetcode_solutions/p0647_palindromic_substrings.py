class Solution:
    def countSubstrings(self, s: str) -> int:
        ls = len(s)
        ans = 0
        for i in range(ls):
            for li, ri in zip(range(i, -1, -1), range(i, ls)):
                if s[li] == s[ri]:
                    ans += 1
                else:
                    break
            for li, ri in zip(range(i, -1, -1), range(i + 1, ls)):
                if s[li] == s[ri]:
                    ans += 1
                else:
                    break
        return ans


class Solution2:
    def countSubstrings(self, s: str) -> int:
        ls = len(s)
        ans = 0
        for i in range(ls):
            l, r = i, i
            while l >= 0 and r < ls and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < ls and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.countSubstrings(s="abc") == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.countSubstrings(s="aaa") == 6
    print("OK")


if __name__ == "__main__":
    test()
