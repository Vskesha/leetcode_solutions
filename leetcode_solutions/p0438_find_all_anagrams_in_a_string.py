class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        lp, ls = len(p), len(s)
        if lp > ls:
            return []

        cp = [0] * 26
        for c in p:
            cp[ord(c) - 97] += 1

        cs = [0] * 26
        for i in range(lp - 1):
            cs[ord(s[i]) - 97] += 1

        res = []
        for i, j in zip(range(lp - 1, ls), range(ls)):
            cs[ord(s[i]) - 97] += 1
            if cp == cs:
                res.append(j)
            cs[ord(s[j]) - 97] -= 1

        return res


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.findAnagrams(s="abab", p="ab") == [0, 1, 2]
    print("ok")


if __name__ == "__main__":
    main()
