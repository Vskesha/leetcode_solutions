import unittest
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        cols = [0] * len(mat[0])

        for row in mat:
            st = []
            for j, val in enumerate(row):
                if not val:
                    cols[j] = 0
                    st.clear()
                    continue
                cols[j] += 1
                cnt = 1
                while st and st[-1][0] >= cols[j]:
                    h, w = st.pop()
                    cnt += w
                st.append((cols[j], cnt))
                for h, w in st:
                    ans += h * w
        return ans


class Solution1:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        cols = [0] * len(mat[0])

        for row in mat:
            for j, val in enumerate(row):
                if not val:
                    cols[j] = 0
                    continue
                val = cols[j] = cols[j] + 1
                while j >= 0 and cols[j]:
                    val = min(val, cols[j])
                    ans += val
                    j -= 1

        return ans
class Solution2:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0

        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                if j:
                    mat[i][j] = cell = mat[i][j - 1] + cell
                ans += cell
                for k in range(i - 1, -1, -1):
                    if mat[k][j]:
                        cell = min(cell, mat[k][j])
                        ans += cell
                    else:
                        break

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_num_submat_1(self):
        print("Test numSubmat 1 ... ", end="")
        self.assertEqual(self.sol.numSubmat(mat=[[1, 0, 1], [1, 1, 0], [1, 1, 0]]), 13)
        print("OK")

    def test_num_submat_2(self):
        print("Test numSubmat 2 ... ", end="")
        self.assertEqual(
            self.sol.numSubmat(mat=[[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]), 24
        )
        print("OK")

    def test_num_submat_3(self):
        print("Test numSubmat 3 ... ", end="")
        self.assertEqual(
            self.sol.numSubmat(
                mat=[
                    [1, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 1],
                    [0, 1, 1, 1, 1, 0, 0],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1, 1],
                ]
            ),
            96,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
