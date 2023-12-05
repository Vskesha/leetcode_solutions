from heapq import heappush, heappushpop
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        la = len(arr)
        lm = la // 20
        minh, maxh = [], []
        ans = 0

        for i in range(lm):
            heappush(minh, -arr[i])
            heappush(maxh, arr[i])
            ans += arr[i]

        for i in range(lm, la):
            heappushpop(minh, -arr[i])
            heappushpop(maxh, arr[i])
            ans += arr[i]

        return (ans - sum(maxh) + sum(minh)) / (la - 2 * lm)


class Solution2:
    def trimMean(self, arr: List[int]) -> float:
        lm = len(arr) // 20
        arr.sort()
        return sum(arr[lm:-lm]) / 18 / lm


class Solution3:
    def trimMean(self, arr: List[int]) -> float:
        lm = len(arr) // 20
        a = sorted(arr)[lm:-lm]
        return sum(a) / len(a)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert round(sol.trimMean(arr=[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]), 5) == 2.0
    print('OK')

    print('Test 2... ', end='')
    assert round(sol.trimMean(arr=[6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]), 5) == 4.0
    print('OK')

    print('Test 3... ', end='')
    assert round(sol.trimMean(
        arr=[6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4,
             3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]), 5) == 4.77778
    print('OK')


if __name__ == '__main__':
    test()
