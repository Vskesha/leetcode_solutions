import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = "$".join(words)
        res = []
        for w in words:
            if s.count(w) > 1:
                res.append(w)
        return res


class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    ans.append(w1)
                    break
        return ans


class Solution3:
    def stringMatching(self, words: List[str]) -> List[str]:

        def get_z(word):
            lw = len(word)
            z = [0] * lw
            li = ri = 0

            for i in range(1, lw):
                if i > ri:
                    li = ri = i
                    while ri < lw and word[ri] == word[ri - li]:
                        ri += 1
                    z[i] = ri - li
                    ri -= 1
                elif i + z[i - li] > ri:
                    li = i
                    ri += 1
                    while ri < lw and word[ri] == word[ri - li]:
                        ri += 1
                    z[i] = ri - li
                    ri -= 1
                else:
                    z[i] = z[i - li]

            return z

        word = "$" + "$".join(words)
        ans = []

        for pat in words:
            lp = len(pat)
            if sum(v >= lp for v in get_z(pat + word)) > 1:
                ans.append(pat)

        return ans


class Solution4:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        wordsall = "$".join(words).join(["#", "?"])
        for pattern in words:
            lp = len(pattern)
            word = pattern + wordsall
            lw = len(word)
            z = [0] * lw
            li = ri = 0
            seen = False

            for i in range(1, lw - lp):
                if i <= ri and i + z[i - li] <= ri:
                    z[i] = z[i - li]
                else:
                    li = i
                    ri = i if i > ri else ri + 1
                    while word[ri] == word[ri - li]:
                        ri += 1
                    z[i] = ri - li
                    ri -= 1

                if z[i] >= lp:
                    if seen:
                        ans.append(pattern)
                        break
                    else:
                        seen = True
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["stringMatching"] * 3,
            "kwargs": [
                dict(words=["mass", "as", "hero", "superhero"]),
                dict(words=["leetcode", "et", "code"]),
                dict(words=["blue", "green", "bu"]),
            ],
            "expected": [["as", "hero"], ["et", "code"], []],
        },
    ]


if __name__ == "__main__":
    unittest.main()
