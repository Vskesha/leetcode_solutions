class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)

        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // m][mid % m] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // m][left % m] == target


class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        m, n = len(matrix[0]), len(matrix)

        vl, vr = 0, n - 1
        while vl < vr:
            mid = (vl + vr + 1) // 2
            if matrix[mid][0] <= target:
                vl = mid
            else:
                vr = mid - 1

        hl, hr = 0, m - 1
        while hl < hr:
            mid = (hl + hr) // 2
            if matrix[vl][mid] >= target:
                hr = mid
            else:
                hl = mid + 1

        return matrix[vl][hl] == target


def main():
    sol = Solution()
    print(
        "True ===",
        sol.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
        ),
    )
    print(
        "False ===",
        sol.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            target=13,
        ),
    )


if __name__ == "__main__":
    main()
