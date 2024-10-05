import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        seen = False
        for word in message:
            if word in banned:
                if seen:
                    return True
                else:
                    seen = True
        return False


class Solution2:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        cnt = 0
        for word in message:
            if word in banned:
                cnt += 1
                if cnt == 2:
                    return True
        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reportSpam"] * 2,
            "kwargs": [
                dict(
                    message=["hello", "world", "leetcode"],
                    bannedWords=["world", "hello"],
                ),
                dict(
                    message=["hello", "programming", "fun"],
                    bannedWords=["world", "programming", "leetcode"],
                ),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
