from typing import List


class DisjointSet:
    def __init__(self, n):
        self.anc = list(range(n))

    def find(self, node):
        if self.anc[node] == node:
            return node
        self.anc[node] = self.find(self.anc[node])
        return self.anc[node]

    def union(self, edge):
        root1 = self.find(edge[0])
        root2 = self.find(edge[1])
        if root1 != root2:
            self.anc[root2] = root1

    def are_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ds = DisjointSet(n)

        for i, query in enumerate(queries):
            query.append(i)

        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])

        idx = 0
        le = len(edgeList)
        ans = [False] * len(queries)

        for fr, to, lim, i in queries:
            while idx < le and edgeList[idx][2] < lim:
                ds.union(edgeList[idx])
                idx += 1
            ans[i] = ds.are_connected(fr, to)

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                         queries=[[0, 1, 2], [0, 2, 5]]) == [False, True]
    print('OK')

    print('Test 2... ', end='')
    assert sol.distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                         queries=[[0, 4, 14], [1, 4, 13]]) == [True, False]
    print('OK')


if __name__ == '__main__':
    test()
