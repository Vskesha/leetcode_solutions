import unittest


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)


class Solution2:
    def doesAliceWin(self, s: str) -> bool:
        return sum(c in "aeiou" for c in s) != 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_doesAliceWin_1(self):
        print("Test doesAliceWin 1... ", end="")
        self.assertTrue(self.sol.doesAliceWin(s="leetcoder"))
        print("OK")

    def test_doesAliceWin_2(self):
        print("Test doesAliceWin 2... ", end="")
        self.assertFalse(self.sol.doesAliceWin(s="bbcd"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
