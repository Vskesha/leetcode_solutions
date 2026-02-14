import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class TreeNode:
    def __init__(
        self, lbound, rbound, left=None, right=None, max_gap=0, height=0
    ):
        self.lbound = lbound
        self.rbound = rbound
        self.left = left
        self.right = right
        self.max_gap = max_gap
        self.height = height

    def add_obstacle(self, x: int) -> None:

        if not self.left:
            self.left = TreeNode(
                lbound=self.lbound, rbound=x, max_gap=x - self.lbound
            )
            self.right = TreeNode(
                lbound=x, rbound=self.rbound, max_gap=self.rbound - x
            )
        else:
            if self.left.rbound > x:
                self.left.add_obstacle(x)
            else:
                self.right.add_obstacle(x)

            height_diff = self.right.height - self.left.height
            if height_diff > 1:
                self.left_turn()
            elif height_diff < -1:
                self.right_turn()

        self.height = max(self.left.height, self.right.height) + 1
        self.max_gap = max(self.left.max_gap, self.right.max_gap)

    def check_if_fits(self, x: int, size: int) -> bool:
        if not self.left:
            return (x - self.lbound) >= size
        elif self.left.rbound >= x:
            return self.left.check_if_fits(x, size)
        elif self.left.max_gap >= size:
            return True
        else:
            return self.right.check_if_fits(x, size)

    def left_turn(self):

        if self.right.left.height > self.right.right.height:
            self.right.right_turn()

        lf, rg = self.left, self.right.left
        self.left = TreeNode(
            lbound=lf.lbound,
            rbound=rg.rbound,
            left=lf,
            right=rg,
            max_gap=max(lf.max_gap, rg.max_gap),
            height=max(lf.height, rg.height) + 1,
        )
        self.right = self.right.right
        self.max_gap = max(self.left.max_gap, self.right.max_gap)
        self.height = max(self.left.height, self.right.height) + 1

    def right_turn(self):

        if self.left.right.height > self.left.left.height:
            self.left.left_turn()

        lf, rg = self.left.right, self.right
        self.right = TreeNode(
            lbound=lf.lbound,
            rbound=rg.rbound,
            left=lf,
            right=rg,
            max_gap=max(lf.max_gap, rg.max_gap),
            height=max(lf.height, rg.height) + 1,
        )
        self.left = self.left.left
        self.max_gap = max(self.left.max_gap, self.right.max_gap)
        self.height = max(self.left.height, self.right.height) + 1


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        tree = TreeNode(lbound=0, rbound=float("inf"), max_gap=float("inf"))
        ans = []

        for query in queries:
            if query[0] == 1:
                tree.add_obstacle(query[1])
            else:
                ans.append(tree.check_if_fits(query[1], query[2]))

        return ans


class Solution2:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        barriers = SortedList()  # Sorted list to maintain barrier positions
        barriers.add(0)  # Add initial barrier at position 0

        # Process the add-barrier queries to populate the barriers list
        for query in queries:
            if query[0] == 1:
                it = query[1]
                barriers.add(it)

        holes = SortedList()  # Sorted list to maintain hole sizes
        holes.add(float("inf"))  # Initialize with an infinitely large hole
        hole2start = {float("inf"): barriers[-1]}

        # Calculate initial hole sizes based on the barriers
        for pos in range(len(barriers) - 1):
            start = barriers[pos]
            end = barriers[pos + 1]
            size = end - start
            if size:
                pos = holes.bisect_left(size)
                hole_size = holes[pos]
                if hole2start[hole_size] > start:
                    if hole_size > size:
                        holes.add(size)
                    hole2start[size] = start

        barriers.add(float("inf"))  # Add an infinite barrier at the end

        result = []
        # Process the queries in reverse order
        for query in reversed(queries):
            if query[0] == 1:  # If it's an add-barrier query
                it = query[1]
                pos = barriers.bisect_left(it)
                left = barriers[pos - 1]
                right = barriers[pos + 1]
                size = right - left

                hole_pos = holes.bisect_left(size)
                if hole2start[holes[hole_pos]] > left:
                    while (
                        hole_pos > 0 and hole2start[holes[hole_pos - 1]] > left
                    ):
                        del hole2start[holes[hole_pos - 1]]
                        del holes[hole_pos - 1]
                        hole_pos -= 1

                    hole2start[size] = left
                    if holes[hole_pos] != size:
                        holes.add(size)

                barriers.remove(it)
            else:  # If it's a check-hole query
                _, start, size = query
                hole_pos = holes.bisect_left(size)
                hole = holes[hole_pos]
                result.append(hole2start[hole] <= start - size)

        # Reverse the result to match the original query order
        result.reverse()

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    false = False
    true = True
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getResults"] * 3,
            "kwargs": [
                dict(queries=[[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]),
                dict(
                    queries=[[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
                ),
                dict(
                    queries=[
                        [1, 2],
                        [1, 30],
                        [2, 123, 118],
                        [1, 28],
                        [1, 46],
                        [1, 11],
                        [1, 23],
                        [2, 35, 96],
                        [1, 37],
                        [1, 130],
                        [2, 13, 108],
                        [1, 128],
                        [2, 149, 48],
                        [2, 133, 39],
                        [1, 13],
                        [2, 90, 79],
                        [1, 102],
                        [1, 105],
                        [1, 7],
                        [1, 144],
                        [2, 83, 80],
                        [1, 50],
                        [1, 142],
                        [1, 55],
                        [2, 109, 46],
                        [2, 12, 21],
                        [2, 85, 118],
                        [1, 79],
                        [1, 17],
                        [1, 62],
                        [2, 116, 75],
                        [2, 53, 9],
                        [1, 77],
                        [1, 135],
                        [2, 123, 116],
                        [1, 51],
                        [2, 147, 90],
                        [2, 88, 26],
                        [1, 14],
                        [2, 43, 115],
                        [1, 136],
                        [1, 4],
                        [1, 15],
                        [2, 124, 134],
                        [2, 138, 29],
                        [2, 37, 28],
                        [2, 51, 90],
                        [1, 74],
                        [2, 16, 28],
                        [2, 31, 7],
                    ]
                ),
            ],
            "expected": [
                [false, true, true],
                [true, true, false],
                [
                    false,
                    false,
                    false,
                    true,
                    true,
                    false,
                    false,
                    true,
                    false,
                    false,
                    false,
                    true,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                ],
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
