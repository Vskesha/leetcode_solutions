from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        @lru_cache(None)
        def dp(st) -> bool:
            if st == len(s):
                return True

            for word in wordDict:
                l = len(word)
                if word == s[st:st + l] and dp(st + l):
                    return True

            return False

        return dp(0)


def main():
    sol = Solution()
    print('True ===', sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print('True ===', sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print('False ==', sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))


if __name__ == '__main__':
    main()
