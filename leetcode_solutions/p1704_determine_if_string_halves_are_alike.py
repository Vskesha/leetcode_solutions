class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        l, r = 0, len(s) - 1
        lc = rc = 0
        while l < r:
            if s[l] in vowels:
                lc += 1
            if s[r] in vowels:
                rc += 1
            l += 1
            r -= 1

        return lc == rc


class Solution1:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        ls = len(s)
        hls = ls // 2
        lc = 0
        for i in range(hls):
            if s[i] in vowels:
                lc += 1
        rc = 0
        for i in range(hls, ls):
            if s[i] in vowels:
                rc += 1

        return lc == rc


class Solution2:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aieou"
        s = s.lower()

        ls = len(s)
        hls = ls // 2

        lc = 0
        for i in range(hls):
            if s[i] in vowels:
                lc += 1
        for i in range(hls, ls):
            if s[i] in vowels:
                lc -= 1

        return lc == 0


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.halvesAreAlike(s="book") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.halvesAreAlike(s="textbook") is False
    print("OK")


if __name__ == "__main__":
    test()
