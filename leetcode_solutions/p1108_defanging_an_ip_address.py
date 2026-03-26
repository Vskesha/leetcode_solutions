import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["defangIPaddr"] * 2,
            "kwargs": [
                dict(address="1.1.1.1"),
                dict(address="255.100.50.0"),
            ],
            "expected": ["1[.]1[.]1[.]1", "255[.]100[.]50[.]0"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
