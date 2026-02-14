import unittest
from heapq import heappop, heappush

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        left = [[a, "a"], [b, "b"], [c, "c"]]
        left.sort()
        res = []

        while left[1][0]:
            if left[2][0] > left[1][0]:
                res.append(left[2][1])
                left[2][0] -= 1
            res.append(left[2][1])
            left[2][0] -= 1
            res.append(left[1][1])
            left[1][0] -= 1
            left.sort()

        res.extend([left[2][1]] * min(2, left[2][0]))
        return "".join(res)


class Solution2:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for ch in "abc":
            if locals()[ch]:
                heappush(heap, (-locals()[ch], ch))
        res = []

        while heap:
            q1, c1 = heappop(heap)
            if len(res) > 1 and res[-2] == res[-1] == c1:
                if not heap:
                    break
                q2, c2 = heappop(heap)
                res.append(c2)
                q2 += 1
                if q2:
                    heappush(heap, (q2, c2))
            else:
                res.append(c1)
                q1 += 1
            if q1:
                heappush(heap, (q1, c1))

        return "".join(res)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestDiverseString"] * 2,
            "kwargs": [
                dict(a=1, b=1, c=7),
                dict(a=7, b=1, c=0),
            ],
            "expected": [
                "ccaccbcc",
                "aabaa",
            ],
            "assert_methods": ["assertDiverseString"] * 2,
        },
    ]

    def assertDiverseString(self, result: str, expected: str) -> None:
        self.assertEqual(len(result), len(expected))
        for i in range(2, len(expected)):
            self.assertFalse(result[i] == result[i - 1] == result[i - 2])
            self.assertFalse(expected[i] == expected[i - 1] == expected[i - 2])


if __name__ == "__main__":
    unittest.main()
