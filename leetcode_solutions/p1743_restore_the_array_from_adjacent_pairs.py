from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        tail = None
        for n in graph:
            if len(graph[n]) == 1:
                tail = n
                break

        ans = [tail]
        curr = graph[tail][0]
        while True:
            ans.append(curr)
            neibs = graph[curr]
            if len(neibs) == 1:
                break
            curr = neibs[0] if neibs[1] == ans[-2] else neibs[1]

        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3]
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.restoreArray(adjacentPairs=[[100000, -100000]]) == [100000, -100000]
    print('ok')


if __name__ == '__main__':
    test()
