from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(node):
            if node == root[node]:
                return node
            root[node] = find(root[node])
            return root[node]

        n = len(isConnected)
        root = list(range(n))
        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    root1 = find(i)
                    root2 = find(j)
                    if root1 != root2:
                        root[root2] = root1
                        n -= 1
        return n


class DisjointSet:
    def __init__(self, n):
        self.root = list(range(n))
        self.gr = n

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.gr -= 1


class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    ds.union(i, j)

        return ds.gr


class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]

        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    root1 = find(i)
                    root2 = find(j)
                    if root1 != root2:
                        parents[root2] = root1

        answer = 0
        for i in range(n):
            if parents[i] == i:
                answer += 1

        return answer


class Solution3:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)

        provinces = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces


def test_find_circle_num():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    )
    print("OK")


if __name__ == "__main__":
    test_find_circle_num()
