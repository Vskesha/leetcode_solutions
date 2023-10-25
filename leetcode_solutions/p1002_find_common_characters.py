from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
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


class Solution2:
    def commonChars(self, words: List[str]) -> List[str]:
        counters = [Counter(word) for word in words]
        res = {}
        for ch in counters[0]:
            res[ch] = min(counter[ch] for counter in counters)
        ans = []
        for ch in res:
            if res[ch]:
                ans += [ch] * res[ch]
        return ans


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert ["e", "l", "l"] == sol.commonChars(words=["bella", "label", "roller"])
    print('ok')

    print('Test 2 ... ', end='')
    assert ["c", "o"] == sol.commonChars(words=["cool", "lock", "cook"])
    print('ok')


if __name__ == '__main__':
    main()
