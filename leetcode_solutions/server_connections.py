from collections import defaultdict


def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:
    disc = [-1] * n
    low = [-1] * n
    criticalConnections = []
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(vertex, parent=-1, time=0):
        low[vertex] = disc[vertex] = time
        for neighbour in graph[vertex]:
            if (disc[neighbour] == -1):
                dfs(neighbour, vertex, time + 1)
                if (low[neighbour] > disc[vertex]):
                    criticalConnections.append([vertex, neighbour])
                low[vertex] = min(low[vertex], low[neighbour])
            elif (parent != neighbour):
                low[vertex] = min(low[vertex], disc[neighbour])
        return

    dfs(connections[0][0])

    return criticalConnections


if __name__ == '__main__':
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(criticalConnections(4, connections))
    connections = [[0, 1]]
    print(criticalConnections(2, connections))
