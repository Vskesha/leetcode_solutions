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
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:
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
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:

        def get_coordinates(bottom, right):
            left = top = 0
            while left < right and top < bottom:
                for j in range(left, right):
                    yield top, j
                for i in range(top, bottom):
                    yield i, right
                for j in range(right, left, -1):
                    yield bottom, j
                for i in range(bottom, top, -1):
                    yield i, left
                left, right, top, bottom = (
                    left + 1,
                    right - 1,
                    top + 1,
                    bottom - 1,
                )
            if top == bottom:
                for j in range(left, right + 1):
                    yield top, j
            elif right == left:
                for i in range(top, bottom + 1):
                    yield i, left

        matrix = [[-1] * n for _ in range(m)]
        coords = get_coordinates(m - 1, n - 1)

        while head:
            i, j = next(coords)
            matrix[i][j] = head.val
            head = head.next

        return matrix


class Solution2:
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:
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
                    head=array_to_linked_list(
                        [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
                    ),
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
