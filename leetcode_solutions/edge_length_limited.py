def distance_limited_paths_exist(n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:

    def max_of_min_distances(node=0):
        pass

    nodes = [dict() for _ in range(n)]
    for nd1, nd2, dist in edgeList:
        nodes[nd1][nd2] = min(nodes[nd1][nd2], dist) if nd2 in nodes[nd1] else dist
        nodes[nd2][nd1] = min(nodes[nd2][nd1], dist) if nd1 in nodes[nd2] else dist
    print(nodes)
    for node in nodes

    answer = [False] * len(queries)
    for i, q in enumerate(queries):
        if q[1] in nodes[q[0]] and nodes[q[0]][q[1]] < q[2]:
            answer[i] = True
    return answer


def distance_limited_paths_exist2(n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:

    def dfs(nd_fr, nd_to, lim, visit):
        if nd_fr == nd_to:
            return True
        visit.add(nd_fr)
        for node, dst in nodes[nd_fr].items():
            if node not in visit and dst < lim and dfs(node, nd_to, lim, visit):
                return True
        return False

    nodes = [dict() for _ in range(n)]
    for nd1, nd2, dist in edgeList:
        nodes[nd1][nd2] = min(nodes[nd1][nd2], dist) if nd2 in nodes[nd1] else dist
        nodes[nd2][nd1] = min(nodes[nd2][nd1], dist) if nd1 in nodes[nd2] else dist
    print(nodes)

    answer = [False] * len(queries)
    for i, q in enumerate(queries):
        if dfs(q[0], q[1], q[2], set()):
            answer[i] = True
    return answer



if __name__ == '__main__':
    print(distance_limited_paths_exist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]))
    print(distance_limited_paths_exist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]))
