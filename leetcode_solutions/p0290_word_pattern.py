class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapch = {}
        mapword = {}
        splitted = s.split()

        if len(splitted) != len(pattern):
            return False

        for ch, word in zip(pattern, splitted):

            if ch in mapch:
                if mapch[ch] != word:
                    return False
            else:
                mapch[ch] = word

            if word in mapword:
                if mapword[word] != ch:
                    return False
            else:
                mapword[word] = ch

        return True


class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        spl = s.split()
        if len(spl) != len(pattern):
            return False
        for c, word in zip(pattern, spl):
            if c not in m:
                if word not in m.values():
                    m[c] = word
                else:
                    return False
            elif m[c] != word:
                return False
        return True


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.wordPattern(pattern="abba", s="dog cat cat dog") is True
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.wordPattern(pattern="abba", s="dog cat cat fish") is False
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.wordPattern(pattern="aaaa", s="dog cat cat dog") is False
    print("OK")


if __name__ == "__main__":
    test()
