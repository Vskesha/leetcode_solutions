import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        oc = image[sr][sc]
        if oc == color:
            return image

        m, n = len(image), len(image[0])
        image[sr][sc] = color
        que = deque([(sr, sc)])

        while que:
            r, c = que.popleft()
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == oc:
                    que.append((nr, nc))
                    image[nr][nc] = color

        return image


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["floodFill"] * 2,
            "kwargs": [
                dict(
                    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                    sr=1,
                    sc=1,
                    color=2,
                ),
                dict(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0),
            ],
            "expected": [
                [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
                [[0, 0, 0], [0, 0, 0]],
            ],
            "assert_methods": ["assertSameImages"] * 2,
        },
    ]

    def assertSameImages(
        self, image1: List[List[int]], image2: List[List[int]]
    ):
        self.assertEqual(len(image1), len(image2))
        for row1, row2 in zip(image1, image2):
            self.assertListEqual(row1, row2)


if __name__ == "__main__":
    unittest.main()
