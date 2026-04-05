import re
import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        coupons = []
        categories = {"electronics", "grocery", "pharmacy", "restaurant"}
        for cod, bline, active in zip(code, businessLine, isActive):
            if (
                active
                and re.fullmatch(r"[A-Za-z0-9_]+", cod)
                and bline in categories
            ):
                coupons.append((bline, cod))

        return [c for _, c in sorted(coupons)]


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    true, false = True, False
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["validateCoupons"] * 2,
            "kwargs": [
                dict(
                    code=["SAVE20", "", "PHARMA5", "SAVE@20"],
                    businessLine=[
                        "restaurant",
                        "grocery",
                        "pharmacy",
                        "restaurant",
                    ],
                    isActive=[true, true, true, true],
                ),
                dict(
                    code=["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
                    businessLine=["grocery", "electronics", "invalid"],
                    isActive=[false, true, true],
                ),
            ],
            "expected": [["PHARMA5", "SAVE20"], ["ELECTRONICS_50"]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
