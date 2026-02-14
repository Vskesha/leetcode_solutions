from bisect import bisect_left, bisect_right
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        la = len(arr)
        if la < 4:
            return arr[la // 2]
        la4 = len(arr) // 4 or 1

        for i in range(0, la, la4):
            if bisect_right(arr, arr[i]) - bisect_left(arr, arr[i]) > la4:
                return arr[i]


class Solution1:
    def findSpecialInteger(self, arr: List[int]) -> int:
        la = len(arr) / 4
        for n, q in Counter(arr).items():
            if q > la:
                return n


class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        la = len(arr) // 4
        cnt = Counter()
        for n in arr:
            cnt[n] += 1
            if cnt[n] > la:
                return n


class Solution3:
    def findSpecialInteger(self, arr: List[int]) -> int:
        la = len(arr) / 4
        pi, prev = 0, arr[0]
        for i, n in enumerate(arr):
            if n != prev:
                if i - pi > la:
                    return prev
                pi, prev = i, n
        return arr[-1]


class Solution4:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]
        return -1


class Solution5:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = len(arr) // 4
        for i, n in enumerate(arr):
            if n == arr[i + d]:
                return n
        return -1


class Solution6:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cs = [arr[n * k // 4] for k in range(1, 4)]
        t = n / 4

        for c in cs:
            li = bisect_left(arr, c)
            ri = bisect_right(arr, c)
            if ri - li > t:
                return c

        return -1


def test_find_special_integer():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.findSpecialInteger(arr=[1, 1]) == 1
    print("OK")


if __name__ == "__main__":
    test_find_special_integer()
