from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())


class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        counter = 0
        for char in set(s):
            diff = s.count(char) - t.count(char)
            counter += diff if diff > 0 else 0
        return counter


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        cnts = Counter(s)
        cntt = Counter(t)
        chars = set(s) | set(t)
        ans = 0

        for ch in chars:
            if cnts[ch] > cntt[ch]:
                ans += cnts[ch] - cntt[ch]

        return abs(ans)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minSteps(s="bab", t="aba") == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.minSteps(s="leetcode", t="practice") == 5
    print("OK")

    print("Test 3... ", end="")
    assert sol.minSteps(s="anagram", t="mangaar") == 0
    print("OK")


if __name__ == "__main__":
    test()
