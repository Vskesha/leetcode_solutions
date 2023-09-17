from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        ans = float('inf')
        lg = len(graph)
        vis_all = (1 << lg) - 1

        for n in range(lg):
            visited = [{} for _ in range(lg)]
            bfs = deque()
            vis = 1 << n
            bfs.append((0, n, vis))
            visited[n] = {vis: 0}
            while bfs:
                moves, curr, vis = bfs.popleft()
                if vis == vis_all:
                    ans = min(ans, moves)
                    break
                for neib in graph[curr]:
                    new_vis = vis | (1 << neib)
                    prev = visited[neib].get(new_vis, float('inf'))
                    if moves + 1 < prev:
                        bfs.append((moves + 1, neib, new_vis))
                        visited[neib][new_vis] = moves + 1
        return ans


class Solution2:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        ans = float('inf')
        lg = len(graph)

        for n in range(lg):
            visited = [{} for _ in range(lg)]
            bfs = deque()
            vis = frozenset({n})
            bfs.append((0, n, vis))
            visited[n] = {vis: 0}
            while bfs:
                moves, curr, vis = bfs.popleft()
                if len(vis) == lg:
                    ans = min(ans, moves)
                    break
                for neib in graph[curr]:
                    new_vis = vis.union({neib})
                    prev = visited[neib].get(new_vis, float('inf'))
                    if moves + 1 < prev:
                        bfs.append((moves + 1, neib, new_vis))
                        visited[neib][new_vis] = moves + 1
        return ans


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]]) == 4
    print('ok\nTest 2 ... ', end='')
    assert sol.shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
    print('ok')


if __name__ == '__main__':
    test()
