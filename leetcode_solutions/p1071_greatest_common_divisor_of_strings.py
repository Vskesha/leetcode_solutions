import unittest
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        lg = gcd(len(str1), len(str2))
        return str1[:lg]


class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        ml = min(l1, l2)

        for cl in range(ml, 0, -1):
            if l1 % cl == 0 and l2 % cl == 0:
                snip = str1[:cl]
                if snip != str2[:cl]:
                    continue
                k1 = l1 // cl
                k2 = l2 // cl
                if str1 == snip * k1 and str2 == snip * k2:
                    return snip

        return ''


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_gcd_of_strings_1(self):
        print("Test gcdOfStrings 1... ", end="")
        self.assertEqual(self.sol.gcdOfStrings(str1="ABCABC", str2="ABC"), "ABC")
        print("OK")

    def test_gcd_of_strings_2(self):
        print("Test gcdOfStrings 2... ", end="")
        self.assertEqual(self.sol.gcdOfStrings(str1="ABABAB", str2="ABAB"), "AB")
        print("OK")

    def test_gcd_of_strings_3(self):
        print("Test gcdOfStrings 3... ", end="")
        self.assertEqual(self.sol.gcdOfStrings(str1="LEET", str2="CODE"), "")
        print("OK")


if __name__ == '__main__':
    unittest.main()
