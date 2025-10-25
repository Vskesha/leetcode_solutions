from typing import List


class Solution:
    def sumOfDistancesInTree(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        graph = {i: [] for i in range(n)}
        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)

        count = [1] * n
        res = [0] * n

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)

        return res


def test_sum_of_distances_in_tree():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sumOfDistancesInTree(
        n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    ) == [8, 12, 6, 10, 10, 10]
    print("OK")

    print("Test 2... ", end="")
    assert sol.sumOfDistancesInTree(n=1, edges=[]) == [0]
    print("OK")

    print("Test 3... ", end="")
    assert sol.sumOfDistancesInTree(n=2, edges=[[1, 0]]) == [1, 1]
    print("OK")


if __name__ == "__main__":
    test_sum_of_distances_in_tree()
