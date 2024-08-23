import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            for x in range(9, 4, -1):
                if x % k == 0:
                    return str(x)

        if k == 1 or k == 3 or k == 9:
            return "9" * n

        elif k == 2 or k == 4 or k == 8:
            x = 6 if k == 8 else k  # x = int(log2(k)) * 2
            if n <= x:
                return "8" * n
            st = "8" * (x // 2)
            return st + "9" * (n - x) + st

        elif k == 5:
            return "5" + "9" * (n - 2) + "5"

        elif k == 6:
            if n == 2:
                return "66"
            st = "9" * ((n - 3) // 2)
            return "8" + st + ("8" if n % 2 else "77") + st + "8"

        else:
            rem9 = {0: 0, 1: 2, 2: 1, 3: 5, 4: 3, 5: 4}
            rem10 = {0: 1, 1: 3, 2: 2, 3: 6, 4: 4, 5: 5}
            nn = (n - 1) // 2
            nines = "9" * nn
            mod1 = rem9[nn % 6] * (rem10[(nn + 2 - n % 2) % 6] + 1) % 7
            x = 11 - n % 2 * 10
            for i in range(9, 2, -1):
                mod2 = i * x * rem10[nn % 6] % 7
                if (mod1 + mod2) % 7 == 0:
                    return nines + str(i * x) + nines


class Solution2:
    def largestPalindrome(self, n: int, k: int) -> str:

        if k == 1 or k == 3 or k == 9:
            return "9" * n
        elif k == 2:
            if n > 2:
                return "8" + "9" * (n - 2) + "8"
            else:
                return "8" * n
        elif k == 4:
            if n > 4:
                return "88" + "9" * (n - 4) + "88"
            else:
                return "8" * n
        elif k == 5:
            if n > 2:
                return "5" + "9" * (n - 2) + "5"
            else:
                return "5" * n
        elif k == 6:
            if n == 1:
                return "6"
            elif n == 2:
                return "66"
            elif n % 2:
                return "8" + "9" * ((n - 3) // 2) + "8" + "9" * ((n - 3) // 2) + "8"
            else:
                return "8" + "9" * ((n - 4) // 2) + "77" + "9" * ((n - 4) // 2) + "8"
        elif k == 8:
            if n > 6:
                return "888" + "9" * (n - 6) + "888"
            else:
                return "8" * n
        else:
            rem9 = {0: 0, 1: 2, 2: 1, 3: 5, 4: 3, 5: 4}
            rem10 = {0: 1, 1: 3, 2: 2, 3: 6, 4: 4, 5: 5}
            if n == 1:
                return "7"
            elif n == 2:
                return "77"
            elif n % 2:
                nn = (n - 1) // 2
                nines = "9" * nn
                mod1 = rem9[nn % 6]
                mod2 = mod1 * rem10[(nn + 1) % 6] % 7
                for i in range(9, 0, -1):
                    mod3 = i * rem10[nn % 6]
                    if (mod1 + mod2 + mod3) % 7 == 0:
                        return nines + str(i) + nines
            else:
                nn = (n - 2) // 2
                nines = "9" * nn
                mod1 = rem9[nn % 6]
                mod2 = mod1 * rem10[(nn + 2) % 6] % 7
                for i in range(9, 0, -1):
                    mod3 = i * 11 * rem10[nn % 6]
                    if (mod1 + mod2 + mod3) % 7 == 0:
                        return nines + str(i * 11) + nines


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestPalindrome"] * 3,
            "kwargs": [
                dict(n=3, k=5),
                dict(n=1, k=4),
                dict(n=5, k=6),
            ],
            "expected": ["595", "8", "89898"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
