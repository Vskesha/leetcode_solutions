import unittest
from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            st1, en1 = firstList[i]
            st2, en2 = secondList[j]
            st = max(st1, st2)
            en = min(en1, en2)
            if st <= en:
                result.append([st, en])
            if en1 > en2:
                j += 1
            else:
                i += 1
        return result


class Solution2:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        lf, ls = len(firstList), len(secondList)
        res = []

        while i < lf and j < ls:
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]

            st = max(s1, s2)
            if e1 < e2:
                i += 1
                if e1 >= st:
                    res.append([st, e1])
            else:
                j += 1
                if e2 >= st:
                    res.append([st, e2])

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def same_intervals(
        self, first: List[List[int]], second: List[List[int]]
    ) -> bool:
        return all(map(lambda x, y: x == y, first, second))

    def test_interval_intersection_1(self):
        print("Test intervalIntersection 1 ... ", end="")
        self.assertTrue(
            self.same_intervals(
                self.sol.intervalIntersection(
                    firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                    secondList=[[1, 5], [8, 12], [15, 24], [25, 26]],
                ),
                [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
            ),
        )
        print("OK")

    def test_interval_intersection_2(self):
        print("Test intervalIntersection 2 ... ", end="")
        self.assertTrue(
            self.same_intervals(
                self.sol.intervalIntersection(
                    firstList=[[1, 3], [5, 9]], secondList=[]
                ),
                [],
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
