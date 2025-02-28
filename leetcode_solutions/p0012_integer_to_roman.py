import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        maps = [
            {"0": "", "1": "M", "2": "MM", "3": "MMM"},
            {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD",
             "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM"},
            {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL",
             "5": "L", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC"},
            {"0": "", "1": "I", "2": "II", "3": "III", "4": "IV",
             "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX"}
        ]

        return "".join(maps[i][c] for i, c in enumerate(str(num).zfill(4)))


class Solution1:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
            2000: "MM",
            3000: "MMM",
        }

        return "".join(roman_map[num // d % 10 * d] for d in (1000, 100, 10, 1))


class Solution2:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
            2000: "MM",
            3000: "MMM",
        }
        res = ""
        val = f"{num:0>4}"
        for i, ch in enumerate(val):
            po = 3 - i
            num = int(ch) * (10**po)
            rch = roman_map[num]
            res += rch
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_int_to_roman_1(self):
        print("Test intToRoman 1 ... ", end="")
        self.assertEqual(self.sol.intToRoman(num=3749), "MMMDCCXLIX")
        print("OK")

    def test_int_to_roman_2(self):
        print("Test intToRoman 2 ... ", end="")
        self.assertEqual(self.sol.intToRoman(num=58), "LVIII")
        print("OK")

    def test_int_to_roman_3(self):
        print("Test intToRoman 3 ... ", end="")
        self.assertEqual(self.sol.intToRoman(num=1994), "MCMXCIV")
        print("OK")


if __name__ == "__main__":
    unittest.main()
