from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for pair, val in zip(equations, values):
            a, b = pair
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def eq(fr, to) -> float:

            if not (fr in graph and to in graph):
                return -1.0

            bfs = deque()
            bfs.append((fr, 1.0))
            visited = {fr}

            while bfs:
                curr, val = bfs.popleft()
                if curr == to:
                    return val
                for neib, rel in graph[curr]:
                    if neib not in visited:
                        visited.add(neib)
                        bfs.append((neib, val * rel))
            return -1.0

        return [eq(fr, to) for fr, to in queries]


class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def equat(node1: str, node2: str) -> float:
            bfs = deque()
            bfs.append((node1, 1))
            visited = set()
            visited.add(node1)
            while bfs:
                curr, eq = bfs.popleft()
                if curr == node2:
                    return eq
                for neib, val in nodes[curr]:
                    if neib not in visited:
                        bfs.append((neib, eq * val))
                        visited.add(neib)
            return -1

        nodes = defaultdict(list)
        for equation, value in zip(equations, values):
            node1, node2 = equation
            nodes[node1].append((node2, value))
            nodes[node2].append((node1, 1 / value))

        return [equat(n1, n2) if n1 in nodes and n2 in nodes else -1 for n1, n2 in queries]


class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def equat(node1_: str, node2_: str) -> float:
            bfs = deque()
            bfs.append((node1_, 1))
            visited = set()
            visited.add(node1_)
            while bfs:
                curr, eq = bfs.popleft()
                if curr == node2_:
                    return eq
                for neib, val in nodes[curr]:
                    if neib not in visited:
                        bfs.append((neib, eq * val))
                        visited.add(neib)
            return -1

        nodes = defaultdict(list)
        for equation, value in zip(equations, values):
            node1, node2 = equation
            nodes[node1].append((node2, value))
            nodes[node2].append((node1, 1 / value))

        return [equat(n1, n2) if n1 in nodes and n2 in nodes else -1 for n1, n2 in queries]


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000, 0.50000,
                                                                                                      -1.00000, 1.00000,
                                                                                                      -1.00000]
    print('OK')

    print('Test 2... ', end='')
    assert sol.calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000, 5.00000,
                                                                                              0.20000]
    print('OK')

    print('Test 3... ', end='')
    assert sol.calcEquation(equations=[["a", "b"]], values=[0.5],
                            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [0.50000, 2.00000, -1.00000,
                                                                                          -1.00000]
    print('OK')


if __name__ == '__main__':
    test()
