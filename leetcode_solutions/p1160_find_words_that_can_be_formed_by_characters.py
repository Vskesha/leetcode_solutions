from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        counter = Counter(chars)

        for word in words:
            for ch in word:
                if ch not in counter or word.count(ch) > counter[ch]:
                    break
            else:
                ans += len(word)

        return ans


class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0
        for word in words:
            for ch, n in Counter(word).items():
                if chars[ch] < n:
                    break
            else:
                ans += len(word)
        return ans


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10
    print('ok')


if __name__ == '__main__':
    main()
