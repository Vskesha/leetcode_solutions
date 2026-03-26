import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(
            word.capitalize() if len(word) > 2 else word.lower()
            for word in title.split()
        )


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["capitalizeTitle"] * 3,
            "kwargs": [
                dict(title="capiTalIze tHe titLe"),
                dict(title="First leTTeR of EACH Word"),
                dict(title="i lOve leetcode"),
            ],
            "expected": [
                "Capitalize The Title",
                "First Letter of Each Word",
                "i Love Leetcode",
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
