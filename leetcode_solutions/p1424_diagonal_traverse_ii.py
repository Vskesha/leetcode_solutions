from collections import defaultdict, deque
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return [
            a[2]
            for a in sorted(
                (i + j, j, n)
                for i, row in enumerate(nums)
                for j, n in enumerate(row)
            )
        ]


class Solution1:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        aux = []
        for i, row in enumerate(nums):
            for j, n in enumerate(row):
                aux.append((i + j, j, n))
        aux.sort()
        return [a[2] for a in aux]


# solution only for small test cases
class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = 0
        ln = len(nums)
        rows = set(range(ln))
        ans = []
        while rows:
            for i in range(min(d, ln - 1), -1, -1):
                j = d - i
                if j < len(nums[i]):
                    ans.append(nums[i][j])
                else:
                    rows.discard(i)
            d += 1
        return ans


# bfs solution
class Solution3:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        bfs = deque()
        bfs.append((0, 0))

        while bfs:
            i, j = bfs.popleft()
            ans.append(nums[i][j])
            if not j and i < len(nums) - 1:
                bfs.append((i + 1, j))
            if j < len(nums[i]) - 1:
                bfs.append((i, j + 1))

        return ans


class Solution4:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                diag[i + j].append(nums[i][j])
        mx = max(diag) + 1
        ans = []
        for i in range(mx):
            ans.extend(diag[i])
        return ans


class Solution5:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                diag[i + j].append(nums[i][j])

        ans, i = [], 0
        while i in diag:
            ans.extend(diag[i])
            i += 1
        return ans


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        4,
        2,
        7,
        5,
        3,
        8,
        6,
        9,
    ]
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.findDiagonalOrder(
        nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    ) == [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
    print("OK")


if __name__ == "__main__":
    test()
