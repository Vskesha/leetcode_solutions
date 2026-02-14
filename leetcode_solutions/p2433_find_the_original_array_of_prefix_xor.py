from itertools import pairwise
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [a ^ b for a, b in pairwise([0] + pref)]


class Solution1:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [a ^ b for a, b in pairwise(pref)]


class Solution2:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = pref[:1]
        for a, b in pairwise(pref):
            arr.append(a ^ b)
        return arr
