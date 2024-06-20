import unittest
from itertools import pairwise
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {ch: i for i, ch in enumerate(order)}

        def bigger(word1, word2) -> bool:
            for c1, c2 in zip(word1, word2):
                if idx[c1] < idx[c2]:
                    return False
                elif idx[c1] > idx[c2]:
                    return True
            return len(word1) > len(word2)

        for w1, w2 in pairwise(words):
            if bigger(w1, w2):
                return False

        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_alien_sorted_1(self):
        print("Test isAlienSorted 1... ", end="")
        self.assertTrue(
            self.sol.isAlienSorted(
                words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
            )
        )
        print("OK")

    def test_is_alien_sorted_2(self):
        print("Test isAlienSorted 2... ", end="")
        self.assertFalse(
            self.sol.isAlienSorted(
                words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"
            )
        )
        print("OK")

    def test_is_alien_sorted_3(self):
        print("Test isAlienSorted 3... ", end="")
        self.assertFalse(
            self.sol.isAlienSorted(
                words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
