from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)

        res = []
        for i in range(1, n + 1):
            avail = {1, 2, 3, 4}
            for neib in graph[i]:
                if neib < i:
                    avail.discard(res[neib - 1])
            res.append(avail.pop())

        return res


class Solution1:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)
        av, res = {1, 2, 3, 4}, [0] * n
        for i in range(n):
            res[i] = av.difference({res[k - 1] for k in graph[i + 1]}).pop()
        return res


class Solution2:
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


def verify(n, paths):
    sol = Solution()
    res = sol.gardenNoAdj(n, paths)
    for a, b in paths:
        if res[a - 1] == res[b - 1]:
            return False
    return True


def test():
    print('Test 1... ', end='')
    assert verify(n=3, paths=[[1, 2], [2, 3], [3, 1]])
    print('OK')

    print('Test 2... ', end='')
    assert verify(n=4, paths=[[1, 2], [3, 4]])
    print('OK')


if __name__ == '__main__':
    test()
