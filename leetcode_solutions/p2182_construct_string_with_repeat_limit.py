import unittest
from collections import Counter
from heapq import heappush, heappop

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = []
        cnt = Counter(s)
        ans = []

        for ch, am in cnt.items():
            heappush(heap, [-ord(ch), am])

        while heap:
            ac, am = heappop(heap)
            if am > repeatLimit:
                ans.append(chr(-ac) * repeatLimit)
                if heap:
                    ans.append(chr(-heap[0][0]))
                    heap[0][1] -= 1
                    if not heap[0][1]:
                        heappop(heap)
                else:
                    break
                heappush(heap, [ac, am - repeatLimit])
            else:
                ans.append(chr(-ac) * am)

        res = "".join(ans)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["repeatLimitedString"] * 2,
            "kwargs": [
                dict(s="cczazcc", repeatLimit=3),
                dict(s="aababab", repeatLimit=2),
            ],
            "expected": ["zzcccac", "bbabaa"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
