class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.sep = n - 1
        self.weight = 0

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2, weight, *args):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.root[root2] = root1
            self.sep -= 1
            self.weight += weight

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def all_connected(self):
        return not self.sep


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:
        le = len(edges)
        for i in range(le):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        mi = 0
        while uf.sep:
            uf.union(*edges[mi])
            mi += 1
        while mi < le and edges[mi][2] == edges[mi - 1][2]:
            mi += 1

        min_weight = uf.weight

        cr, pcr = [], []
        for i in range(mi):
            uf = UnionFind(n)

            for j in range(i):
                uf.union(*edges[j])
            for j in range(i + 1, mi):
                uf.union(*edges[j])

            if uf.sep or uf.weight > min_weight:
                cr.append(edges[i][3])
                continue

            uf = UnionFind(n)
            uf.union(*edges[i])
            for j in range(mi):
                uf.union(*edges[j])

            if uf.weight == min_weight:
                pcr.append(edges[i][3])

        return [cr, pcr]


class Solution2:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:

        def dp(i, used, uf, mi):
            if uf.weight > self.min_weight:
                return

            if uf.all_connected():
                self.combs.append(set(used))

            if i == mi:
                return

            n1, n2, wt, j = edges[i]
            if not uf.connected(n1, n2):
                pr, ps, pw = uf.root.copy(), uf.sep, uf.weight
                uf.union(*edges[i])
                used.append(j)
                dp(i + 1, used, uf, mi)
                used.pop()
                uf.root, uf.sep, uf.weight = pr, ps, pw
            dp(i + 1, used, uf, mi)

        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        ufm = UnionFind(n)
        mi = 0
        while ufm.sep:
            ufm.union(*edges[mi])
            mi += 1
        self.min_weight = ufm.weight
        while mi < len(edges) and edges[mi][2] == edges[mi - 1][2]:
            mi += 1
        uf = UnionFind(n)
        # self.ans = [[], []]
        self.combs = []
        dp(0, [], uf, mi)

        critical = self.combs[0].intersection(*self.combs)
        non_critical = set().union(*self.combs) - critical

        return [list(critical), list(non_critical)]


def main():
    sol = Solution()
    print(
        " [[0, 1], [2, 3, 4, 5]]\n",
        sol.findCriticalAndPseudoCriticalEdges(
            n=5,
            edges=[
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
        ),
    )
    print(
        " [[], [0, 1, 2, 3]]\n",
        sol.findCriticalAndPseudoCriticalEdges(
            n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
        ),
    )
    print(
        " [[58, 13, 45, 55, 61, 89, 16, 57], [28, 32, 39, 10, 37, 51, 54, 70, 75, 76, 85, 15, 23, 25]]\n",
        sol.findCriticalAndPseudoCriticalEdges(
            n=14,
            edges=[
                [0, 1, 13],
                [0, 2, 6],
                [2, 3, 13],
                [3, 4, 4],
                [0, 5, 11],
                [4, 6, 14],
                [4, 7, 8],
                [2, 8, 6],
                [4, 9, 6],
                [7, 10, 4],
                [5, 11, 3],
                [6, 12, 7],
                [12, 13, 9],
                [7, 13, 2],
                [5, 13, 10],
                [0, 6, 4],
                [2, 7, 3],
                [0, 7, 8],
                [1, 12, 9],
                [10, 12, 11],
                [1, 2, 7],
                [1, 3, 10],
                [3, 10, 6],
                [6, 10, 4],
                [4, 8, 5],
                [1, 13, 4],
                [11, 13, 8],
                [2, 12, 10],
                [5, 8, 1],
                [3, 7, 6],
                [7, 12, 12],
                [1, 7, 9],
                [5, 9, 1],
                [2, 13, 10],
                [10, 11, 4],
                [3, 5, 10],
                [6, 11, 14],
                [5, 12, 3],
                [0, 8, 13],
                [8, 9, 1],
                [3, 6, 8],
                [0, 3, 4],
                [2, 9, 6],
                [0, 11, 4],
                [2, 5, 14],
                [4, 11, 2],
                [7, 11, 11],
                [1, 11, 6],
                [2, 10, 12],
                [0, 13, 4],
                [3, 9, 9],
                [4, 12, 3],
                [6, 7, 10],
                [6, 8, 13],
                [9, 11, 3],
                [1, 6, 2],
                [2, 4, 12],
                [0, 10, 3],
                [3, 12, 1],
                [3, 8, 12],
                [1, 8, 6],
                [8, 13, 2],
                [10, 13, 12],
                [9, 13, 11],
                [2, 11, 14],
                [5, 10, 9],
                [5, 6, 10],
                [2, 6, 9],
                [4, 10, 7],
                [3, 13, 10],
                [4, 13, 3],
                [3, 11, 9],
                [7, 9, 14],
                [6, 9, 5],
                [1, 5, 12],
                [4, 5, 3],
                [11, 12, 3],
                [0, 4, 8],
                [5, 7, 8],
                [9, 12, 13],
                [8, 12, 12],
                [1, 10, 6],
                [1, 9, 9],
                [7, 8, 9],
                [9, 10, 13],
                [8, 11, 3],
                [6, 13, 7],
                [0, 12, 10],
                [1, 4, 8],
                [8, 10, 2],
            ],
        ),
    )


if __name__ == "__main__":
    main()
