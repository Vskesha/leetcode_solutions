from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        root = list(range(n))

        def find(node):
            if node == root[node]:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                root[root2] = root1

        for n1, n2 in edges:
            union(n1, n2)

        return find(source) == find(destination)


def test_valid_path():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.validPath(
            n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2
        )
        is True
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.validPath(
            n=6,
            edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            source=0,
            destination=5,
        )
        is False
    )
    print("OK")


if __name__ == "__main__":
    test_valid_path()
