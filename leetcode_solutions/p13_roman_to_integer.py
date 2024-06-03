import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = 2000
        ans = 0
        for ch in s:
            n = table[ch]
            if prev < n:
                ans -= prev * 2
            ans += n
            prev = n
        return ans


class Solution2:
    def romanToInt(self, s: str) -> int:
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = ans = 0
        for i in range(len(s) - 1, -1, -1):
            ans += -trans[s[i]] if trans[s[i]] < prev else trans[s[i]]
            prev = trans[s[i]]
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_roman_to_int1(self):
        print("Test romanToInt 1 ... ", end="")
        self.assertEqual(self.sol.romanToInt(s="III"), 3)
        print("OK")

    def test_roman_to_int2(self):
        print("Test romanToInt 2 ... ", end="")
        self.assertEqual(self.sol.romanToInt(s="LVIII"), 58)
        print("OK")

    def test_roman_to_int3(self):
        print("Test romanToInt 3 ... ", end="")
        self.assertEqual(self.sol.romanToInt(s="MCMXCIV"), 1994)
        print("OK")


if __name__ == "__main__":
    unittest.main()
