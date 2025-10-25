import unittest
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(1 for a, b in zip(secret, guess) if a == b)
        cows = sum((Counter(secret) & Counter(guess)).values()) - bulls
        return f"{bulls}A{cows}B"


class Solution2:
    def getHint(self, secret: str, guess: str) -> str:
        bullnumber = 0

        nonbullsecret = Counter()
        nonbullguess = Counter()

        for a, b in zip(secret, guess):
            if a == b:
                bullnumber += 1
            else:
                nonbullsecret[a] += 1
                nonbullguess[b] += 1

        nonbullnumber = 0
        for ch in nonbullguess:
            nonbullnumber += min(nonbullguess[ch], nonbullsecret[ch])

        return f"{bullnumber}A{nonbullnumber}B"


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_get_hint_1(self):
        print("Test getHint 1... ", end="")
        self.assertEqual(self.sol.getHint(secret="1807", guess="7810"), "1A3B")
        print("OK")

    def test_get_hint_2(self):
        print("Test getHint 2... ", end="")
        self.assertEqual(self.sol.getHint(secret="1123", guess="0111"), "1A1B")
        print("OK")


if __name__ == "__main__":
    unittest.main()
