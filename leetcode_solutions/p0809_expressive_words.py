import unittest
from itertools import groupby
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ls = [list(g) for _, g in groupby(s)]

        def is_strechy(w1) -> bool:
            lw1 = [list(g) for _, g in groupby(w1)]

            if len(lw1) != len(ls):
                return False

            for a, b in zip(lw1, ls):
                if (a[0] != b[0]) or (len(a) > len(b)) or (len(a) == 1 and len(b) == 2):
                    return False

            return True

        return sum(map(is_strechy, words))


class Solution2:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_strechy(w1, w2) -> bool:
            lw1 = [list(g) for _, g in groupby(w1)]
            lw2 = [list(g) for _, g in groupby(w2)]

            if len(lw1) != len(lw2):
                return False

            for a, b in zip(lw1, lw2):
                if (a[0] != b[0]) or (len(a) > len(b)) or (len(a) == 1 and len(b) == 2):
                    return False

            return True

        return sum(1 for w in words if is_strechy(w, s))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_expressive_words_1(self):
        print("Test expressiveWords 1... ", end="")
        self.assertEqual(
            self.sol.expressiveWords(s="heeellooo", words=["hello", "hi", "helo"]), 1
        )
        print("OK")

    def test_expressive_words_2(self):
        print("Test expressiveWords 2... ", end="")
        self.assertEqual(
            self.sol.expressiveWords(s="zzzzzyyyyy", words=["zzyy", "zy", "zyy"]), 3
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
