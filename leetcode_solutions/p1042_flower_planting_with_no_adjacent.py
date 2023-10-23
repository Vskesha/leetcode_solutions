from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for fr, to in paths:
            graph[fr - 1].append(to - 1)
            graph[to - 1].append(fr - 1)

        ans = [0] * n

        for i in range(n):
            available = {1, 2, 3, 4}
            for neib in graph[i]:
                available.discard(ans[neib])
            ans[i] = available.pop()
        return ans


def verify(n: int, paths: list[list[int, int]]) -> str:
    sol = Solution()
    res = sol.gardenNoAdj(n, paths)
    for fr, to in paths:
        if res[fr - 1] == res[to - 1]:
            return 'failed'
    return 'ok'


def test():
    print('Test 1 ... ', verify(n=3, paths=[[1, 2], [2, 3], [3, 1]]))

    print('Test 2 ... ', verify(n=4, paths=[[1, 2], [3, 4]]))

    print('Test 3 ... ', verify(n=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))


if __name__ == '__main__':
    test()
