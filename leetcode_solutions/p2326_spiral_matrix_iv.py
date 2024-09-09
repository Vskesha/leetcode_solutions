import unittest
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirs = (0, 1, 0, -1, 0)
        i = j = di = 0
        mat = [[-1] * n for _ in range(m)]

        while head:
            mat[i][j] = head.val
            ni, nj = i + dirs[di], j + dirs[di + 1]
            if ni < 0 or nj < 0 or ni >= m or nj >= n or mat[ni][nj] != -1:
                di = (di + 1) % 4
                i, j = i + dirs[di], j + dirs[di + 1]
            else:
                i, j = ni, nj
            head = head.next

        return mat


class Solution1:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        def get_coordinates(b, r):
            l = t = 0
            while l < r and t < b:
                for j in range(l, r):
                    yield t, j
                for i in range(t, b):
                    yield i, r
                for j in range(r, l, -1):
                    yield b, j
                for i in range(b, t, -1):
                    yield i, l
                l, r, t, b = l + 1, r - 1, t + 1, b - 1
            if t == b:
                for j in range(l, r + 1):
                    yield t, j
            elif r == l:
                for i in range(t, b + 1):
                    yield i, l

        matrix = [[-1] * n for _ in range(m)]
        coords = get_coordinates(m - 1, n - 1)

        while head:
            i, j = next(coords)
            matrix[i][j] = head.val
            head = head.next

        return matrix


class Solution2:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def get_values(head):
            while head:
                yield head.val
                head = head.next

        ans = [[-1] * n for _ in range(m)]
        r, c = 0, -1
        vals = get_values(head)
        m -= 1

        while True:
            if not n:
                break
            for _ in range(n):
                c += 1
                ans[r][c] = next(vals, -1)
            n -= 1

            if not m:
                break
            for _ in range(m):
                r += 1
                ans[r][c] = next(vals, -1)
            m -= 1

            if not n:
                break
            for _ in range(n):
                c -= 1
                ans[r][c] = next(vals, -1)
            n -= 1

            if not m:
                break
            for _ in range(m):
                r -= 1
                ans[r][c] = next(vals, -1)
            m -= 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["spiralMatrix"] * 2,
            "kwargs": [
                dict(
                    m=3,
                    n=5,
                    head=array_to_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]),
                ),
                dict(m=1, n=4, head=array_to_linked_list([0, 1, 2])),
            ],
            "expected": [
                [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]],
                [[0, 1, 2, -1]],
            ],
            "assert_methods": ["assertSpiralMatrixEqual"] * 2,
        },
    ]

    def assertSpiralMatrixEqual(
        self, matrix1: List[List[int]], matrix2: List[List[int]]
    ):
        self.assertEqual(len(matrix1), len(matrix2))
        for row1, row2 in zip(matrix1, matrix2):
            self.assertListEqual(row1, row2)


if __name__ == "__main__":
    unittest.main()
