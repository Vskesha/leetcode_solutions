import unittest
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return [
            ch
            for ch, q in reduce(
                lambda x, y: x & y, map(Counter, words)
            ).items()
            for _ in range(q)
        ]


class Solution1:
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


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_common_chars1(self):
        print("Test commonChars 1... ", end="")
        self.assertListEqual(
            sorted(self.sol.commonChars(words=["bella", "label", "roller"])),
            sorted(["e", "l", "l"]),
        )
        print("OK")

    def test_common_chars2(self):
        print("Test commonChars 2... ", end="")
        self.assertListEqual(
            sorted(self.sol.commonChars(words=["cool", "lock", "cook"])),
            sorted(["o", "c"]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
