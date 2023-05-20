from collections import defaultdict, deque


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    
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
        
    ans = []
    for n1, n2 in queries:
        if n1 in nodes and n2 in nodes:
            ans.append(equat(n1, n2))
        else:
            ans.append(-1)
    
    return ans


if __name__ == '__main__':
    print('[6.00000,0.50000,-1.00000,1.00000,-1.00000] ===', calc_equation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print('[3.75000,0.40000,5.00000,0.20000] ===', calc_equation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print('[0.50000,2.00000,-1.00000,-1.00000] ===', calc_equation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
    print('[0.11111,1.00000] ===', calc_equation(equations=[["a","aa"]], values=[9.0], queries=[["aa","a"],["aa","aa"]]))
    