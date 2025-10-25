from itertools import pairwise


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        prev = s[0]
        streak = 0
        ans = 0

        for ch in s:
            if prev == ch:
                streak += 1
            else:
                ans = (ans + streak * (streak + 1) // 2) % mod
                streak = 1
            prev = ch
        ans = (ans + streak * (streak + 1) // 2) % mod

        return ans


class Solution1:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        prev = s[0]
        streak = 0
        ans = 0

        for ch in s:
            streak = streak + 1 if ch == prev else 1
            ans = (ans + streak) % mod
            prev = ch

        return ans


class Solution2:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        streak = ans = 1

        for i in range(1, len(s)):
            streak = streak + 1 if s[i] == s[i - 1] else 1
            ans = (ans + streak) % mod

        return ans


class Solution3:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        streak = ans = 1

        for a, b in pairwise(s):
            streak = streak + 1 if a == b else 1
            ans = (ans + streak) % mod

        return ans


class Solution4:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        streak, ans = 1, 0

        for a, b in pairwise(s):
            if a == b:
                streak += 1
            else:
                ans = (ans + streak * (streak + 1) // 2) % mod
                streak = 1

        ans = (ans + streak * (streak + 1) // 2) % mod
        return ans


def test():
    sol = Solution()

    print("Test 1 ...", end="")
    assert sol.countHomogenous(s="abbcccaa") == 13
    print("ok")

    print("Test 2 ...", end="")
    assert sol.countHomogenous(s="xy") == 2
    print("ok")

    print("Test 3 ...", end="")
    assert sol.countHomogenous(s="zzzzz") == 15
    print("ok")


if __name__ == "__main__":
    test()
