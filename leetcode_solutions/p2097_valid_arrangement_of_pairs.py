import unittest
from collections import defaultdict
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        out = defaultdict(int)

        for fr, to in pairs:
            adj[fr].append(to)
            out[fr] += 1
            out[to] -= 1

        start = [k for k, v in out.items() if v > 0]
        gst = start[0] if start else pairs[0][0]

        def gen(st, end):
            ans = [st]
            while len(adj[st]) == 1:
                st = adj[st].pop()
                ans.append(st)
                if st == end:
                    return ans
            if not adj[st]:
                return ans
            tail = []
            while adj[st]:
                neib = adj[st].pop()
                seq = gen(neib, st)
                if seq[-1] == st:
                    ans.extend(seq)
                else:
                    tail = seq
            ans.extend(tail)
            return ans

        seq = gen(gst, None)
        ans = list(map(list, pairwise(seq)))
        return ans


class Solution2:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        income = defaultdict(int)

        for fr, to in pairs:
            adj[to].append(fr)
            income[fr] -= 1
            income[to] += 1

        ends = [k for k, v in income.items() if v > 0]
        end = ends[0] if ends else pairs[0][0]

        def arange(end):
            if not adj[end]:
                return [end]
            ans = arange(adj[end].pop())
            while adj[end]:
                cycle = arange(adj[end].pop())
                ans.extend(cycle)
            ans.append(end)
            return ans

        return list(map(list, pairwise(arange(end))))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["validArrangement"] * 3,
            "kwargs": [
                dict(pairs=[[5, 1], [4, 5], [11, 9], [9, 4]]),
                dict(pairs=[[1, 3], [3, 2], [2, 1]]),
                dict(pairs=[[1, 2], [1, 3], [2, 1]]),
            ],
            "expected": [
                [[11, 9], [9, 4], [4, 5], [5, 1]],
                [[1, 3], [3, 2], [2, 1]],
                [[1, 2], [2, 1], [1, 3]],
            ],
            "assert_methods": ["assertValidArangements"],
        },
    ]

    def assertValidArangements(
        self, actual: List[List[int]], expected: List[List[int]]
    ):
        self.assertEqual(len(actual), len(expected))
        self.assertSetEqual(set(map(tuple, actual)), set(map(tuple, expected)))
        for a, b in pairwise(expected):
            self.assertEqual(a[1], b[0])
        for a, b in pairwise(actual):
            self.assertEqual(a[1], b[0])


if __name__ == "__main__":
    unittest.main()
