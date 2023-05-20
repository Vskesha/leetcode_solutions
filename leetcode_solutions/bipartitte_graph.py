from collections import deque


def is_graph_bipartite1(graph: list[list[int]]) -> bool:
    visited = [None] * len(graph)
    
    def dfs(node, flag):
        visited[node] = flag
        ans = True
        for n in graph[node]:
            if visited[n] is None:
                visited[n] = not flag
                ans = dfs(n, (not flag))
            elif visited[n] == flag:
                return False
        return ans
        
    for node in range(len(graph)):
        if visited[node] is None and not dfs(node, False):
            return False
    return True
    


def is_graph_bipartite(graph: list[list[int]]) -> bool:
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


def is_graph_bipartite2(graph: list[list[int]]) -> bool:
    set_1 = set()
    set_2 = set()

    def traverse(node, curr_set):
        curr_set.add(node)
        other_set = set_1 if curr_set is set_2 else set_2
        for nd in graph[node]:
            if nd not in other_set:
                traverse(nd, other_set)

    for node in range(len(graph)):
        if node not in set_1 and node not in set_2:
            traverse(node, set_1)
            
    return not set_1.intersection(set_2)


if __name__ == '__main__':
    print('False ===', is_graph_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print('True ===', is_graph_bipartite([[1,3],[0,2],[1,3],[0,2]]))
    