from collections import deque
from string import ascii_uppercase


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        chars = {ch: (-1, -1) for ch in ascii_uppercase}
        ans = di = 0

        for i, ch in enumerate(s):
            ppi, pi = chars[ch]
            di += i + ppi - 2 * pi
            ans += di
            chars[ch] = (pi, i)

        return ans


class Solution1:
    def uniqueLetterString(self, s: str) -> int:
        chars = {ch: deque([-1, -1], maxlen=2) for ch in ascii_uppercase}
        ans = di = 0

        for i, ch in enumerate(s):
            di += i + chars[ch][-2] - 2 * chars[ch][-1]
            ans += di
            chars[ch].append(i)

        return ans


class Solution2:
    def uniqueLetterString(self, s: str) -> int:
        prev = {ch: -1 for ch in ascii_uppercase}
        pprev = prev.copy()
        ans = di = 0

        for i, ch in enumerate(s):
            di += i + pprev[ch] - 2 * prev[ch]
            ans += di
            pprev[ch] = prev[ch]
            prev[ch] = i

        return ans


def test_unique_letter_string():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.uniqueLetterString(s="ABC") == 10
    print("OK")

    print("Test 2... ", end="")
    assert sol.uniqueLetterString(s="ABA") == 8
    print("OK")

    print("Test 3... ", end="")
    assert sol.uniqueLetterString(s="LEETCODE") == 92
    print("OK")


if __name__ == "__main__":
    test_unique_letter_string()
