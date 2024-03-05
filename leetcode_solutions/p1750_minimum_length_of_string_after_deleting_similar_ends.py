class Solution:
    def minimumLength(self, s: str) -> int:
        li, ri = 0, len(s) - 1
        while li < ri and s[li] == s[ri]:
            ch = s[li]
            while li <= ri and s[li] == ch:
                li += 1
            while li <= ri and s[ri] == ch:
                ri -= 1
        return ri - li + 1


class Solution2:
    def minimumLength(self, s: str) -> int:
        li, ri = 0, len(s) - 1
        while True:
            if li == ri:
                return 1
            elif s[li] == s[ri]:
                ch = s[li]
                while li < ri and s[li] == ch:
                    li += 1
                if li == ri:
                    return 0
                while s[ri] == ch:
                    ri -= 1
            else:
                return ri - li + 1


def test_minimum_length():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minimumLength(s="ca") == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.minimumLength(s="cabaabac") == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.minimumLength(s="aabccabba") == 3
    print("OK")


if __name__ == "__main__":
    test_minimum_length()
