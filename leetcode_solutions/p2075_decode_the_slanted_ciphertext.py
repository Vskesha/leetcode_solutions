import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        le = len(encodedText)
        lr = le // rows

        res = []
        for j in range(lr):
            for i in range(min(rows, lr - j)):
                res.append(encodedText[i * lr + j + i])

        return "".join(res).rstrip()


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["decodeCiphertext"] * 3,
            "kwargs": [
                dict(encodedText="ch   ie   pr", rows=3),
                dict(encodedText="iveo    eed   l te   olc", rows=4),
                dict(encodedText="coding", rows=1),
            ],
            "expected": ["cipher", "i love leetcode", "coding"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
