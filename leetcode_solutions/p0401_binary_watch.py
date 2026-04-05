import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    ans.append(f"{hour}:{minute:02}")

        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["readBinaryWatch"] * 2,
            "kwargs": [
                dict(turnedOn=1),
                dict(turnedOn=9),
            ],
            "expected": [
                [
                    "0:01",
                    "0:02",
                    "0:04",
                    "0:08",
                    "0:16",
                    "0:32",
                    "1:00",
                    "2:00",
                    "4:00",
                    "8:00",
                ],
                [],
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
