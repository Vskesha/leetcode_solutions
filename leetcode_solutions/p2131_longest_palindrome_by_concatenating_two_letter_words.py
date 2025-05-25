import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        single_double_found = False
        ans = 0
        seen = set()
        for word, num in count.items():
            if word == word[::-1]:
                if num % 2 == 1:
                    single_double_found = True
                ans += 4 * (num // 2)
            else:
                if word[::-1] in count and word[::-1] not in seen:
                    ans += 4 * min(count[word], count[word[::-1]])

                seen.add(word)

        if single_double_found:
            ans += 2

        return ans


class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = {}
        ans = 0

        for w in words:
            if w in seen:
                ans += 4
                if seen[w] == 1:
                    del seen[w]
                else:
                    seen[w] -= 1
            else:
                rw = w[1] + w[0]
                seen[rw] = seen.get(rw, 0) + 1

        ans += 2 * int(any(w[0] == w[1] for w in seen))

        return ans


class Solution3:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = Counter()
        ans = 0

        for word in words:
            if seen[word]:
                ans += 4
                seen[word] -= 1
            else:
                seen[word[::-1]] += 1

        if any(w[0] == w[1] for w in seen if seen[w]):
            ans += 2

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestPalindrome"] * 3,
            "kwargs": [
                dict(words=["lc", "cl", "gg"]),
                dict(words=["ab", "ty", "yt", "lc", "cl", "ab"]),
                dict(words=["cc", "ll", "xx"]),
            ],
            "expected": [6, 8, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
