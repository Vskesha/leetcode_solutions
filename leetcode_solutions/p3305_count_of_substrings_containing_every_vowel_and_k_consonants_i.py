import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        ans, st, prc = 0, 0, -1

        for i, ch in enumerate(word):
            if ch in cnt:
                cnt[ch] += 1
            elif k:
                k -= 1
            else:
                while word[st] in cnt:
                    cnt[word[st]] -= 1
                    st += 1
                prc = st
                st += 1

            if not k and all(cnt.values()):
                while cnt.get(word[st], 0) > 1:
                    cnt[word[st]] -= 1
                    st += 1
                ans += st - prc

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countOfSubstrings"] * 4,
            "kwargs": [
                dict(word="aeioqq", k=1),
                dict(word="aeiou", k=0),
                dict(word="ieaouqqieaouqq", k=1),
                dict(word="auaroiuerg", k=3),
            ],
            "expected": [0, 1, 3, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
