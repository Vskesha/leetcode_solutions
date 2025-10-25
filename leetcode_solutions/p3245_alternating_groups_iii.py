import unittest
from collections import Counter
from itertools import pairwise
from typing import List

from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        self.ends = SortedList()
        self.groups = Counter()
        self.colors = []
        self.lc = 0

    def numberOfAlternatingGroups(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        self.colors = colors
        self.lc = len(colors)

        self.ends = SortedList(
            i for i in range(self.lc - 1) if colors[i] == colors[i + 1]
        )
        if colors[0] == colors[-1]:
            self.ends.add(self.lc - 1)

        self.groups = Counter(cv - pv for pv, cv in pairwise(self.ends))
        if self.ends:
            self.groups[self.ends[0] + self.lc - self.ends[-1]] += 1

        ans = []
        for q in queries:
            if q[0] == 1:
                ans.append(self.get_count(q[1]))
            else:
                self.change_color(q[1], q[2])

        return ans

    def get_count(self, size) -> int:
        if not self.groups:
            return self.lc
        cnt = 0
        for grlen, amount in self.groups.items():
            if grlen >= size:
                cnt += (grlen - size + 1) * amount
        return cnt

    def change_color(self, idx: int, color: int) -> None:
        if self.colors[idx] == color:
            return

        self.colors[idx] = color

        if not self.ends:
            self.ends.add(idx)
            self.ends.add((idx - 1) % self.lc)
            self.groups[1] = 1
            self.groups[self.lc - 1] = 1
            return

        le = len(self.ends)
        end_idx = self.ends.bisect_left(idx) % le
        end_of_group = self.ends[end_idx]
        start_of_group = (self.ends[end_idx - 1] + 1) % self.lc
        len_of_group = (end_of_group - start_of_group) % self.lc + 1

        end_of_prev_group = self.ends[(end_idx - 1) % le]
        end_of_pprev_group = self.ends[(end_idx - 2) % le]
        end_of_next_group = self.ends[(end_idx + 1) % le]
        len_of_prev_group = (
            end_of_prev_group - end_of_pprev_group - 1
        ) % self.lc + 1
        len_of_next_group = (
            end_of_next_group - end_of_group - 1
        ) % self.lc + 1

        # 4 cases to consider
        if end_of_group == start_of_group:  # == idx
            if le == 2:
                self.ends.clear()
                self.groups.clear()
            else:
                self.groups[len_of_prev_group] -= 1
                self.groups[len_of_next_group] -= 1
                self.groups[1] -= 1
                self.groups[len_of_prev_group + len_of_next_group + 1] += 1
                self.ends.remove(end_of_group)
                self.ends.remove(end_of_prev_group)

        elif idx == end_of_group:
            if le > 1:
                self.groups[len_of_group] -= 1
                self.groups[len_of_group - 1] += 1
                self.groups[len_of_next_group] -= 1
                self.groups[len_of_next_group + 1] += 1
            self.ends.remove(idx)
            self.ends.add((idx - 1) % self.lc)

        elif idx == start_of_group:
            if le > 1:
                self.groups[len_of_group] -= 1
                self.groups[len_of_group - 1] += 1
                self.groups[len_of_prev_group] -= 1
                self.groups[len_of_prev_group + 1] += 1
            self.ends.remove(end_of_prev_group)
            self.ends.add(start_of_group)

        else:
            self.groups[len_of_group] -= 1
            self.groups[1] += 1
            self.groups[(idx - start_of_group) % self.lc] += 1
            self.groups[(end_of_group - idx) % self.lc] += 1
            self.ends.add(idx)
            self.ends.add((idx - 1) % self.lc)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numberOfAlternatingGroups_1(self):
        print("Test numberOfAlternatingGroups 1... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[0, 1, 1, 0, 1], queries=[[2, 1, 0], [1, 4]]
            ),
            [2],
        )
        print("OK")

    def test_numberOfAlternatingGroups_2(self):
        print("Test numberOfAlternatingGroups 2... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[0, 0, 1, 0, 1, 1], queries=[[1, 3], [2, 3, 0], [1, 5]]
            ),
            [2, 0],
        )
        print("OK")

    def test_numberOfAlternatingGroups_3(self):
        print("Test numberOfAlternatingGroups 3... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[0, 0, 0, 1],
                queries=[[2, 1, 1], [1, 3], [2, 1, 1], [2, 0, 1]],
            ),
            [4],
        )
        print("OK")

    def test_numberOfAlternatingGroups_4(self):
        print("Test numberOfAlternatingGroups 4... ", end="")
        self.assertListEqual(
            self.sol.numberOfAlternatingGroups(
                colors=[0, 1, 0, 0, 1],
                queries=[[2, 0, 1], [2, 2, 0], [1, 3], [1, 3]],
            ),
            [0, 0],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
