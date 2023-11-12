from heapq import heappop, heappush
from math import inf
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {i: [] for i in range(n)}
        for fr, to, wt in edges:
            self.graph[fr].append((to, wt))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        costs = [inf] * len(self.graph)
        costs[node1] = 0

        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            for to, wt in self.graph[node]:
                new_cost = cost + wt
                if costs[to] > new_cost:
                    heappush(heap, (new_cost, to))
                    costs[to] = new_cost
        return -1


class Graph2:

    def __init__(self, n: int, edges: List[List[int]]):

        self.gr = [[inf] * n for _ in range(n)]
        self.n = n

        for i in range(n):
            self.gr[i][i] = 0

        for fr, to, cost in edges:
            self.gr[fr][to] = cost

        for mid in range(n):
            for fr in range(n):
                first = self.gr[fr][mid]
                for to in range(n):
                    curr = first + self.gr[mid][to]
                    if self.gr[fr][to] > curr:
                        self.gr[fr][to] = curr

    def addEdge(self, edge: List[int]) -> None:
        st, end, cost = edge
        for fr in range(self.n):
            first = self.gr[fr][st]
            for to in range(self.n):
                new_cost = first + self.gr[end][to] + cost
                if self.gr[fr][to] > new_cost:
                    self.gr[fr][to] = new_cost

    def shortestPath(self, node1: int, node2: int) -> int:
        ret = self.gr[node1][node2]
        return -1 if ret == inf else ret


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
def generaltest(commands, arguments):
    graph = Graph(*arguments[0])
    out = [None]
    for com, args in zip(commands[1:], arguments[1:]):
        method = graph.shortestPath if com == 'shortestPath' else graph.addEdge
        out.append(method(*args))

    return out


def test():

    print('Test 1 ... ', end='')
    commands = ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
    arguments = [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
    output = [None, 6, -1, None, 6]
    assert generaltest(commands, arguments) == output
    print('ok')

    print('Test 2 ... ', end='')
    commands = ["Graph", "shortestPath", "addEdge", "addEdge", "addEdge", "shortestPath", "shortestPath",
                "shortestPath", "addEdge", "shortestPath", "addEdge", "shortestPath", "shortestPath", "addEdge",
                "addEdge", "shortestPath", "addEdge", "addEdge", "addEdge", "addEdge", "addEdge", "shortestPath",
                "shortestPath", "shortestPath", "shortestPath", "shortestPath", "shortestPath", "shortestPath",
                "shortestPath", "shortestPath", "shortestPath", "shortestPath", "shortestPath", "shortestPath",
                "shortestPath", "shortestPath"]
    arguments = [[4, []], [2, 2], [[0, 3, 745857]], [[1, 3, 432074]], [[0, 2, 103840]], [0, 2], [0, 1], [1, 0],
                 [[2, 0, 100674]], [0, 2], [[1, 2, 977334]], [2, 1], [0, 0], [[0, 1, 686587]], [[3, 1, 65074]], [2, 0],
                 [[2, 3, 871421]], [[3, 0, 19073]], [[1, 0, 751462]], [[2, 1, 12018]], [[3, 2, 989255]], [1, 3], [2, 0],
                 [3, 1], [3, 2], [2, 3], [2, 2], [3, 3], [2, 1], [3, 0], [3, 3], [1, 0], [0, 3], [1, 2], [3, 0], [2, 2]]
    output = [None, 0, None, None, None, 103840, -1, -1, None, 103840, None, -1, 0, None, None, 100674, None, None,
              None, None, None, 432074, 100674, 65074, 122913, 444092, 0, 0, 12018, 19073, 0, 451147, 547932, 554987,
              19073, 0]
    assert generaltest(commands, arguments) == output
    print('ok')


if __name__ == '__main__':
    test()
