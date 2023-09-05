from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        res = Counter(words[0])

        for i in range(1, len(words)):

            curr = Counter(words[i])

            keys = list(res.keys())
            for c in keys:
                if c in curr:
                    res[c] = min(res[c], curr[c])
                else:
                    del res[c]

        ans = []
        for c in res:
            ans += [c] * res[c]

        return ans


def main():
    sol = Solution()
    print(' ["e", "l", "l"]\n', sol.commonChars(words=["bella", "label", "roller"]))
    print(' ["c", "o"]\n', sol.commonChars(words=["cool", "lock", "cook"]))


if __name__ == '__main__':
    main()
