from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        ans = 0

        for j in range(len(mat[0])):
            q = False
            for i in range(len(mat)):
                if mat[i][j]:
                    if q:
                        q = False
                        break
                    elif rows[i] == 1:
                        q = True
                    else:
                        q = False
                        break
            if q:
                ans += 1

        return ans


class Solution1:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        ans = 0

        for j in range(len(mat[0])):
            q = 0
            for i in range(len(mat)):
                if mat[i][j]:
                    if q:
                        q = 0
                        break
                    elif rows[i] == 1:
                        q = 1
                    else:
                        q = 0
                        break
            ans += q

        return ans


class Solution2:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat[0]), len(mat)
        rows = [sum(row) for row in mat]
        ans = 0

        for j in range(m):
            q = False
            idx = -1
            for i in range(n):
                if mat[i][j]:
                    if q:
                        q = False
                        break
                    else:
                        q = True
                        idx = i
            if q and rows[idx] == 1:
                ans += 1

        return ans


class Solution3:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat[0]), len(mat)
        rows = [sum(row) for row in mat]
        ans = 0

        for j in range(m):
            q = False
            idx = -1
            for i in range(n):
                if mat[i][j]:
                    if q:
                        break
                    else:
                        q = True
                        idx = i
            else:
                if q and rows[idx] == 1:
                    ans += 1

        return ans


class Solution4:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat[0]), len(mat)
        rows = [sum(row) for row in mat]
        cols = [sum(mat[i][j] for i in range(n)) for j in range(m)]
        ans = 0

        for i, row in enumerate(mat):
            for j, el in enumerate(row):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    ans += 1
        return ans


class Solution5:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat[0]), len(mat)
        ans = 0
        rows, cols = [0] * n, [0] * m

        for i in range(n):
            for j in range(m):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]

        for i in range(n):
            for j in range(m):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    ans += 1

        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    print("OK")


if __name__ == "__main__":
    test()
