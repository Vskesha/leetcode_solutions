class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        foccs = {s[i]: i for i in range(len(s) - 1, -1, -1)}
        return max(i - foccs[ch] - 1 for i, ch in enumerate(s))


class Solution2:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occ = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in first_occ:
                ans = max(ans, i - first_occ[ch] - 1)
            else:
                first_occ[ch] = i
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxLengthBetweenEqualCharacters(s="aa") == 0
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxLengthBetweenEqualCharacters(s="abca") == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.maxLengthBetweenEqualCharacters(s="cbzxy") == -1
    print("OK")


if __name__ == "__main__":
    test()
