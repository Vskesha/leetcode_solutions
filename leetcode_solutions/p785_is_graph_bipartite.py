from collections import deque


class Solution:
    def isBipartite(self, graph):
        color = [0] * len(graph)

        for node in range(len(graph)):
            if not color[node]:
                deq = deque([node])
                color[node] = 1
                while deq:
                    curr = deq.popleft()
                    for neib in graph[curr]:
                        if not color[neib]:
                            deq.append(neib)
                            color[neib] = -color[curr]
                        elif color[neib] == color[curr]:
                            return False

        return True


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    print('ok\nTest 2 ... ', end='')
    assert sol.isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    print('ok')


if __name__ == '__main__':
    test()
