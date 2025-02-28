import unittest
from collections import deque
from string import ascii_uppercase


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        chars = {ch: (-1, -1) for ch in ascii_uppercase}
        ans = di = 0

        for i, ch in enumerate(s):
            ppi, pi = chars[ch]
            di += i + ppi - 2 * pi
            ans += di
            chars[ch] = (pi, i)

        return ans


class Solution1:
    def uniqueLetterString(self, s: str) -> int:
        chars = {ch: deque([-1, -1], maxlen=2) for ch in ascii_uppercase}
        ans = di = 0

        for i, ch in enumerate(s):
            di += i + chars[ch][-2] - 2 * chars[ch][-1]
            ans += di
            chars[ch].append(i)

        return ans


class Solution2:
    def uniqueLetterString(self, s: str) -> int:
        prev = {ch: -1 for ch in ascii_uppercase}
        pprev = prev.copy()
        ans = di = 0

        for i, ch in enumerate(s):
            di += i + pprev[ch] - 2 * prev[ch]
            ans += di
            pprev[ch] = prev[ch]
            prev[ch] = i

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_unique_letter_string_1(self):
        print("Test uniqueLetterString 1... ", end="")
        self.assertEqual(10, self.sol.uniqueLetterString(s="ABC"))
        print("OK")

    def test_unique_letter_string_2(self):
        print("Test uniqueLetterString 2... ", end="")
        self.assertEqual(8, self.sol.uniqueLetterString(s="ABA"))
        print("OK")

    def test_unique_letter_string_3(self):
        print("Test uniqueLetterString 3... ", end="")
        self.assertEqual(92, self.sol.uniqueLetterString(s="LEETCODE"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
