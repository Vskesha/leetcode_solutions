import string
import unittest
from collections import Counter
from heapq import heapify, heappop, heappush

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        cnt = Counter(s)
        heap = [(cnt[ch], ch) for ch in string.ascii_lowercase]
        heapify(heap)

        for _ in range(cnt["?"]):
            q, ch = heappop(heap)
            heappush(heap, (q + 1, ch))

        fin = {ch: q for q, ch in heap}

        for ch in string.ascii_lowercase:
            s = s.replace("?", ch, fin[ch] - cnt[ch])

        return s


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimizeStringValue"] * 2,
            "kwargs": [
                dict(s="???"),
                dict(s="a?a?"),
            ],
            "expected": ["abc", "abac"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_minimize_string_value():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.minimizeStringValue(s="???") == "abc"
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.minimizeStringValue(s="a?a?") == "abac"
#     print("OK")


# if __name__ == "__main__":
#     test_minimize_string_value()
