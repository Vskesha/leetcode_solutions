import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        ch = 0
        lb = len(blocks)
        for i in range(k - 1):
            if blocks[i] == "W":
                ch += 1

        for i, j in zip(range(k - 1, lb), range(lb)):
            if blocks[i] == "W":
                ch += 1
            ans = min(ans, ch)
            if blocks[j] == "W":
                ch -= 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumRecolors"] * 2,
            "kwargs": [
                dict(blocks="WBBWWBBWBW", k=7),
                dict(blocks="WBWBBBW", k=2),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
