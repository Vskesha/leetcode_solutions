import unittest
from itertools import product
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        lt = len(tops)
        for x in (tops[0], bottoms[0]):
            if all(x == tops[i] or x == bottoms[i] for i in range(lt)):
                return lt - max(tops.count(x), bottoms.count(x))
        return -1


class Solution2:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        lt = len(tops)
        top = tops[0]
        bot = bottoms[0]
        ttc = tbc = btc = bbc = 0

        for i in range(lt):
            if tops[i] != top:
                if bottoms[i] == top:
                    ttc += 1
                else:
                    ttc = lt
                    break

        for i in range(lt):
            if bottoms[i] != top:
                if tops[i] == top:
                    tbc += 1
                else:
                    tbc = lt
                    break

        ans = min(ttc, tbc)
        if ans < lt:
            return ans

        for i in range(lt):
            if bottoms[i] != bot:
                if tops[i] == bot:
                    bbc += 1
                else:
                    bbc = lt
                    break

        for i in range(lt):
            if tops[i] != bot:
                if bottoms[i] == bot:
                    btc += 1
                else:
                    btc = lt
                    break

        ans = min(btc, bbc)
        if ans < lt:
            return ans

        return -1


class Solution3:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = lt = len(tops)

        for top, bot in product([tops[0], bottoms[0]], repeat=2):
            ct = cb = 0
            for t, b in zip(tops, bottoms):
                if ct < lt and t != top:
                    if b == top:
                        ct += 1
                    elif cb < lt:
                        ct = lt
                    else:
                        ct = lt
                        break
                if b != bot and cb < lt:
                    if t == bot:
                        cb += 1
                    elif ct < lt:
                        cb = lt
                    else:
                        cb = lt
                        break
            ans = min(ans, ct, cb)

        return ans if ans < lt else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minDominoRotations"] * 2,
            "kwargs": [
                dict(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]),
                dict(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]),
            ],
            "expected": [2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
