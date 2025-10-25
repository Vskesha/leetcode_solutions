from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter()
        for a, b in zip(s, t):
            cnt[a] += 1
            cnt[b] -= 1
        for a, v in cnt.items():
            if v:
                return False
        return True


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.isAnagram(s="anagram", t="nagaram") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.isAnagram(s="rat", t="car") is False
    print("OK")


if __name__ == "__main__":
    test()
