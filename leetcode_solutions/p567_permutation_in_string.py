import unittest
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ws = len(s1) - 1
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:ws])

        for c1, c2 in zip(s2, s2[ws:]):
            cnt2[c2] += 1
            if cnt1 == cnt2:
                return True
            cnt2[c1] -= 1

        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_check_inclusion_1(self):
        print("Test checkInclusion 1... ", end="")
        self.assertTrue(self.sol.checkInclusion(s1="ab", s2="eidbaooo"))
        print("OK")

    def test_check_inclusion_2(self):
        print("Test checkInclusion 2... ", end="")
        self.assertFalse(self.sol.checkInclusion(s1="ab", s2="eidboaoo"))
        print("OK")


if __name__ == '__main__':
    unittest.main()
