class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, edge):
        root1 = self.find(edge[1])
        root2 = self.find(edge[2])

        if root1 == root2:
            return 1

        self.n -= 1
        self.parent[root2] = root1
        return 0

    def connected(self, edge):
        return self.find(edge[1]) == self.find(edge[2])

    def connected_all(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)

        ans = 0
        for edge in edges:
            if edge[0] == 3:
                ans += alice.union(edge)
                bob.union(edge)

        for edge in edges:
            if edge[0] == 1:
                ans += alice.union(edge)
            elif edge[0] == 2:
                ans += bob.union(edge)

        return ans if alice.connected_all() and bob.connected_all() else -1


def main():
    sol = Solution()
    print('2 ===',
          sol.maxNumEdgesToRemove(n=4,
                                  edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3],
                                         [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
    print('0 ===',
          sol.maxNumEdgesToRemove(n=4,
                                  edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))
    print('-1 ===',
          sol.maxNumEdgesToRemove(n=4,
                                  edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]))


if __name__ == '__main__':
    main()
