from bisect import bisect_right, bisect_left
from collections import Counter
from typing import List


class Solution:
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
            l = bisect_left(arr, c)
            r = bisect_right(arr, c)
            if r - l > t:
                return c

        return -1


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
    print('OK')

    print('Test 2... ', end='')
    assert sol.findSpecialInteger(arr=[1, 1]) == 1
    print('OK')


if __name__ == '__main__':
    test()
