from heapq import heappop, heappush
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans, rh, cm, lb, inf = [], [], 0, len(buildings) - 1, float('inf')

        for i, (l, r, h) in enumerate(buildings):

            if h > cm:
                cm = h
                if ans and ans[-1][0] == l:
                    ans[-1][1] = h
                else:
                    ans.append([l, h])
            heappush(rh, (r, h))

            nxt = buildings[i + 1][0] if i < lb else inf
            while rh and rh[0][0] < nxt:
                re, he = heappop(rh)
                if he == cm:
                    cm = max(b for _, b in rh) if rh else 0
                if ans[-1][0] == re:
                    ans[-1][1] = cm
                elif ans[-1][1] != cm:
                    ans.append([re, cm])

        return ans


class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans, rh, cm, lb = [], [], 0, len(buildings) - 1

        for i, (l, r, h) in enumerate(buildings):
            if h > cm:
                cm = h
                if ans and ans[-1][0] == l:
                    ans[-1][1] = h
                else:
                    ans.append([l, h])
            heappush(rh, (r, h))

            while rh and (i == lb or rh[0][0] < buildings[i + 1][0]):
                re, he = heappop(rh)
                if he == cm:
                    cm = max(b for _, b in rh) if rh else 0
                if ans[-1][0] == re:
                    ans[-1][1] = cm
                elif ans[-1][1] != cm:
                    ans.append([re, cm])

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    for a, b in zip(sol.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]),
                    [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]):
        assert a == b
    print('OK')

    print('Test 2... ', end='')
    for a, b in zip(sol.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]),
                    [[0, 3], [5, 0]]):
        assert a == b
    print('OK')

    print('Test 3... ', end='')
    for a, b in zip(sol.getSkyline(buildings=[[1, 2, 1], [1, 2, 2], [1, 2, 3]]),
                    [[1, 3], [2, 0]]):
        assert a == b
    print('OK')


if __name__ == '__main__':
    test()
