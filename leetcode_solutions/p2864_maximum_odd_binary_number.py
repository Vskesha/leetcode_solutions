import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        return "1" * (c["1"] - 1) + "0" * c["0"] + "1"


class Solution2:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * (zeros) + "1"


class Solution3:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(sorted(s, reverse=True))[1:] + "1"


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumOddBinaryNumber"] * 2,
            "kwargs": [
                dict(s="010"),
                dict(s="0101"),
            ],
            "expected": ["001", "1001"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.maximumOddBinaryNumber(s="010") == "001"
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.maximumOddBinaryNumber(s="0101") == "1001"
#     print("OK")


# if __name__ == "__main__":
#     test()
