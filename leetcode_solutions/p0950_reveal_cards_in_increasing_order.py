import unittest
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        indexes = deque(range(len(deck)))
        indexes.appendleft(indexes.pop())

        for n in sorted(deck):
            indexes.append(indexes.popleft())
            deck[indexes.popleft()] = n

        return deck


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_deck_revealed_increasing_1(self):
        print("Test deckRevealedIncreasing 1... ", end="")
        self.assertEqual(
            self.sol.deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]),
            [2, 13, 3, 11, 5, 17, 7],
        )
        print("OK")

    def test_deck_revealed_increasing_2(self):
        print("Test deckRevealedIncreasing 2... ", end="")
        self.assertEqual(
            self.sol.deckRevealedIncreasing(deck=[1, 1000]),
            [1, 1000],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
