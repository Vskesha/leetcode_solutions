from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = [[False] * n for _ in range(m)]
        result = []

        for i in range(m):
            for j in range(n):
                if visited[i][j] or land[i][j] == 0:
                    continue
                eni = i + 1
                enj = j + 1
                while eni < m and land[eni][j]:
                    eni += 1
                while enj < n and land[i][enj]:
                    enj += 1
                for y in range(i, eni):
                    for x in range(j, enj):
                        visited[y][x] = True
                result.append([i, j, eni - 1, enj - 1])

        return result


def test_find_farmland():
    sol = Solution()

    print("Test 1... ", end="")
    for land1, land2 in zip(
        sol.findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]),
        [[0, 0, 0, 0], [1, 1, 2, 2]],
    ):
        assert land1 == land2
    print("OK")

    print("Test 2... ", end="")
    for land1, land2 in zip(
        sol.findFarmland(land=[[1, 1], [1, 1]]), [[0, 0, 1, 1]]
    ):
        assert land1 == land2
    print("OK")

    print("Test 3... ", end="")
    for land1, land2 in zip(sol.findFarmland(land=[[0]]), []):
        assert land1 == land2
    print("OK")


if __name__ == "__main__":
    test_find_farmland()
