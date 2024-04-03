class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = set()
        mp = {}

        for a, b in zip(s, t):
            if a not in mp:
                if b in seen:
                    return False
                mp[a] = b
                seen.add(b)
            if mp[a] != b:
                return False

        return True


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a not in mp:
                if b not in mp.values():
                    mp[a] = b
                else:
                    return False
            elif mp[a] != b:
                return False
        return True


def test_isIsomorphic():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.isIsomorphic(s="egg", t="add") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.isIsomorphic(s="foo", t="bar") is False
    print("OK")

    print("Test 3... ", end="")
    assert sol.isIsomorphic(s="paper", t="title") is True
    print("OK")


if __name__ == "__main__":
    test_isIsomorphic()
