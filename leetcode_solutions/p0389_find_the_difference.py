from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        for ch in t:
            if count[ch]:
                count[ch] -= 1
            else:
                return ch


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        for ch in s:
            count[ch] -= 1
        ans = ""
        for ch, q in count.items():
            if q:
                return ch


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.findTheDifference(s="abcd", t="abcde") == "e"
    print("ok\nTest 2 ... ", end="")
    assert sol.findTheDifference(s="", t="y") == "y"
    print("ok")


if __name__ == "__main__":
    test()
