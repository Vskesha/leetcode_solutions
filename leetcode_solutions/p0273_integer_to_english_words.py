import unittest


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        places = [
            "",
            "Thousand",
            "Million",
            "Billion",
            "Trillion",
            "Quadrillion",
            "Quintillion",
            "Sextillion",
            "Septillion",
            "Octillion",
            "Nonillion",
            "Decillion",
        ]
        duos = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        def to_words(hto: int) -> str:
            res = []
            h, t, o = hto // 100, hto // 10 % 10, hto % 10

            if h:
                res.append(ones[h])
                res.append("Hundred")
            if t == 1:
                res.append(duos[o])
            else:
                res.append(tens[t])
                res.append(ones[o])

            return " ".join(res)

        parts, i = [], 0
        while num:
            num, hto = divmod(num, 1000)
            words = to_words(hto)
            if hto:
                words += " " + places[i]
            parts.append(words)
            i += 1

        ans = " ".join(reversed(parts))
        return " ".join(ans.split())


class Solution2:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        lt20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = [
            "",
            "Thousand",
            "Million",
            "Billion",
            "Trillion",
            "Quadrillion",
            "Quintillion",
            "Sextillion",
            "Septillion",
            "Octillion",
            "Nonillion",
            "Decillion",
        ]

        def to_words(num: int) -> str:
            if num == 0:
                return ""
            elif num < 20:
                return lt20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + to_words(num % 10)
            else:
                return lt20[num // 100] + " Hundred " + to_words(num % 100)

        ans, i = "", 0
        while num:
            num, hto = divmod(num, 1000)
            if hto:
                ans = to_words(hto) + thousands[i] + " " + ans
            i += 1

        return ans.strip()


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numberToWords_1(self):
        print("Test numberToWords 1... ", end="")
        self.assertEqual(
            self.sol.numberToWords(num=123), "One Hundred Twenty Three"
        )
        print("OK")

    def test_numberToWords_2(self):
        print("Test numberToWords 2... ", end="")
        self.assertEqual(
            self.sol.numberToWords(num=12345),
            "Twelve Thousand Three Hundred Forty Five",
        )
        print("OK")

    def test_numberToWords_3(self):
        print("Test numberToWords 3... ", end="")
        self.assertEqual(
            self.sol.numberToWords(num=1234567),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
