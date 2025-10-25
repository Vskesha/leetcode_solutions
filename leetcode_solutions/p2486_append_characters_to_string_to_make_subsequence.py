import unittest


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j, lt = 0, len(t)
        for i, ch in enumerate(s):
            if j == lt:
                return 0
            if ch == t[j]:
                j += 1
        return lt - j


class Solution1:
    def appendCharacters(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        i = j = 0

        while i < ls and j < lt:
            if s[i] == t[j]:
                j += 1
            i += 1

        return lt - j


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_append_characters1(self):
        print("Test appendCharacters 1 ... ", end="")
        self.assertEqual(
            self.sol.appendCharacters(s="coaching", t="coding"), 4
        )
        print("OK")

    def test_append_characters2(self):
        print("Test appendCharacters 2 ... ", end="")
        self.assertEqual(self.sol.appendCharacters(s="abcde", t="a"), 0)
        print("OK")

    def test_append_characters3(self):
        print("Test appendCharacters 3 ... ", end="")
        self.assertEqual(self.sol.appendCharacters(s="z", t="abcde"), 5)
        print("OK")


if __name__ == "__main__":
    unittest.main()
