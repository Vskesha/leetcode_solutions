class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]


def main():
    sol = Solution()
    print('True ===', sol.repeatedSubstringPattern("abab"))
    print('False ===', sol.repeatedSubstringPattern("aba"))
    print('True ===', sol.repeatedSubstringPattern("abcabcabcabc"))


if __name__ == '__main__':
    main()
