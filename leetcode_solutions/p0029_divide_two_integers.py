import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if dividend < 0:
            is_negative = not is_negative
            dividend = -dividend
        if divisor < 0:
            is_negative = not is_negative
            divisor = -divisor
        pows = 1

        while divisor < dividend:
            divisor <<= 1
            pows <<= 1

        ans = 0
        while pows:
            if divisor <= dividend:
                dividend -= divisor
                ans += pows
            divisor >>= 1
            pows >>= 1

        if is_negative:
            ans = -ans

        max_val = pow(2, 31)
        if ans == max_val:
            return max_val - 1

        return ans


class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        divs = [divisor]
        pows = [1]
        ans = 0

        while divs[-1] < dividend:
            new_div = divs[-1] + divs[-1]
            new_pow = pows[-1] + pows[-1]
            divs.append(new_div)
            pows.append(new_pow)

        for i in range(len(divs) - 1, -1, -1):
            if divs[i] <= dividend:
                dividend -= divs[i]
                ans += pows[i]

        return -ans if is_negative else ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["divide"] * 2,
            "kwargs": [
                dict(dividend=10, divisor=3),
                dict(dividend=7, divisor=-3),
            ],
            "expected": [3, -2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
