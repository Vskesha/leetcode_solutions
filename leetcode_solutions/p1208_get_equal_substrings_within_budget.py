class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        diffs = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        st = tc = ans = 0

        for end, diff in enumerate(diffs):
            tc += diff
            while tc > maxCost:
                tc -= diffs[st]
                st += 1
            ans = max(ans, end - st + 1)

        return ans


class Solution2:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diffs = []
        st = tc = ans = 0

        for end in range(n):
            diff = abs(ord(s[end]) - ord(t[end]))
            diffs.append(diff)
            tc += diff
            while tc > maxCost:
                tc -= diffs[st]
                st += 1
            ans = max(ans, end - st + 1)

        return ans


def test_equal_substring():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.equalSubstring(s="abcd", t="bcdf", maxCost=3) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.equalSubstring(s="abcd", t="cdef", maxCost=3) == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.equalSubstring(s="abcd", t="acde", maxCost=0) == 1
    print("OK")


if __name__ == "__main__":
    test_equal_substring()
