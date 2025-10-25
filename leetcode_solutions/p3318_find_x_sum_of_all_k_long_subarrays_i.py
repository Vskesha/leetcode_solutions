import unittest
from collections import Counter
from itertools import accumulate
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        xlist, others = SortedList(), SortedList()
        freq = Counter()
        xsum = 0
        ans = [0] * (len(nums) - k + 1)

        def add(val) -> int:
            fr = freq[val]
            if not fr:
                return 0
            p = (fr, val)
            if xlist and p > xlist[0]:
                xlist.add(p)
                return fr * val
            else:
                others.add(p)
                return 0

        def remove(val) -> int:
            fr = freq[val]
            if not fr:
                return 0
            p = (fr, val)
            if p in xlist:
                xlist.remove(p)
                return fr * val
            else:
                others.remove(p)
                return 0

        for ri, val in enumerate(nums):
            xsum -= remove(val)
            freq[val] += 1
            xsum += add(val)

            li = ri - k + 1
            if li < 0:
                continue

            while len(xlist) > x:
                p = xlist[0]
                xlist.remove(p)
                others.add(p)
                xsum -= p[0] * p[1]

            while others and len(xlist) < x:
                p = others[-1]
                others.remove(p)
                xlist.add(p)
                xsum += p[0] * p[1]

            ans[li] = xsum
            val = nums[li]
            xsum -= remove(val)
            freq[val] -= 1
            xsum += add(val)

        return ans


class Solution2:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ln = len(nums)
        sn = set(nums)
        ans = []
        if len(sn) <= x:
            acc = list(accumulate(nums, initial=0))
            for i, j in zip(range(k, ln + 1), range(ln)):
                ans.append(acc[i] - acc[j])
            return ans

        frd = Counter(nums[: k - 1])
        frl = SortedList((-frd[n], -n) for n in sn)
        xsum = sum(fr * n for fr, n in frl[:x])

        for i, j in zip(range(k - 1, ln), range(ln)):

            n = nums[i]
            fr = frd[n]
            frd[n] += 1
            pi = frl.index((-fr, -n))
            frl.pop(pi)
            frl.add((-fr - 1, -n))
            ci = frl.index((-fr - 1, -n))
            if pi < x:
                xsum += n
            elif ci < x:
                xsum += n * (fr + 1) - frl[x][0] * frl[x][1]

            ans.append(xsum)

            n = nums[j]
            fr = frd[n]
            frd[n] -= 1
            pi = frl.index((-fr, -n))
            frl.pop(pi)
            frl.add((-fr + 1, -n))
            ci = frl.index((-fr + 1, -n))
            if ci < x:
                xsum -= n
            elif pi < x:
                xsum += frl[x - 1][0] * frl[x - 1][1] - n * fr

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findXSum"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2),
                dict(nums=[3, 8, 7, 8, 7, 5], k=2, x=2),
            ],
            "expected": [
                [6, 10, 12],
                [11, 15, 15, 15, 12],
            ],
            "assert_methods": ["assertListEqual"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
