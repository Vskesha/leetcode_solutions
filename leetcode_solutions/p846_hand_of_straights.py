import unittest
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        cnt = Counter(hand)
        sorted_keys = sorted(cnt.keys())
        i, ls = 0, len(sorted_keys)

        while i < ls:
            key = sorted_keys[i]
            if cnt[key]:
                for n in range(key, key + groupSize):
                    if cnt[n]:
                        cnt[n] -= 1
                    else:
                        return False
            else:
                i += 1

        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_n_straight_hand1(self):
        print("Test isNStraightHand 1 ... ", end="")
        self.assertTrue(
            self.sol.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
        )
        print("OK")

    def test_is_n_straight_hand2(self):
        print("Test isNStraightHand 2 ... ", end="")
        self.assertFalse(self.sol.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
        print("OK")

    def test_is_n_straight_hand3(self):
        print("Test isNStraightHand 3 ... ", end="")
        self.assertTrue(self.sol.isNStraightHand(hand=[1, 1, 2, 2, 3, 3], groupSize=3))
        print("OK")


if __name__ == "__main__":
    unittest.main()
