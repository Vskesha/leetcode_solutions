import unittest


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"

        neg = (numerator < 0) ^ (denominator < 0)
        num, den = abs(numerator), abs(denominator)
        ip, rem = divmod(num, den)

        ans = ("-" if neg else "") + str(ip)
        if not rem:
            return ans

        ap, seen = [], {}
        while rem:
            if rem in seen:
                ap[seen[rem]] = "(" + ap[seen[rem]]
                ap.append(")")
                break
            seen[rem] = len(ap)
            val, rem = divmod(rem * 10, den)
            ap.append(str(val))

        return ans + "." + "".join(ap)


class Solution2:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"

        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"

        num = abs(numerator)
        den = abs(denominator)

        res += str(num // den)

        if not num % den:
            return res

        res += "."
        rem = num % den
        mp = {}

        while rem and rem not in mp:
            mp[rem] = len(res)
            res += str(rem * 10 // den)
            rem = rem * 10 % den

        if rem in mp:
            res = f"{res[:mp[rem]]}({res[mp[rem]:]})"

        return res


class Solution3:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        num = abs(numerator)
        den = abs(denominator)

        z = num // den
        res.append(str(z))

        rem = num % den
        if rem:
            res.append(".")
        else:
            return "".join(res)

        mp = {}
        brackets_idx = 0

        while rem:
            if rem in mp:
                brackets_idx = mp[rem]
                break
            else:
                mp[rem] = len(res)
                rem *= 10
                res.append(str(rem // den))
                rem %= den

        if brackets_idx:
            res.insert(brackets_idx, "(")
            res.append(")")

        return "".join(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_fraction_to_decimal_1(self):
        print("Test fractionToDecimal 1... ", end="")
        self.assertEqual(
            self.sol.fractionToDecimal(numerator=1, denominator=2), "0.5"
        )
        print("OK")

    def test_fraction_to_decimal_2(self):
        print("Test fractionToDecimal 2... ", end="")
        self.assertEqual(
            self.sol.fractionToDecimal(numerator=2, denominator=1), "2"
        )
        print("OK")

    def test_fraction_to_decimal_3(self):
        print("Test fractionToDecimal 3... ", end="")
        self.assertEqual(
            self.sol.fractionToDecimal(numerator=4, denominator=333), "0.(012)"
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
