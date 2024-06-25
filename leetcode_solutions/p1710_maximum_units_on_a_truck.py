import unittest
from heapq import heapify, heappop
from operator import itemgetter
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        res = 0

        while truckSize and boxTypes:
            b, u = boxTypes.pop()
            if b < truckSize:
                truckSize -= b
                res += b * u
            else:
                return res + truckSize * u

        return res


class Solution2:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=itemgetter(1), reverse=True)
        i = res = 0
        lb = len(boxTypes)

        while i < lb:
            b, u = boxTypes[i]
            if truckSize <= b:
                res += u * truckSize
                return res
            res += b * u
            truckSize -= b
            i += 1

        return res


class Solution3:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ub = [(-u, b) for b, u in boxTypes]
        heapify(ub)
        res = 0

        while truckSize and ub:
            u, b = heappop(ub)
            if b < truckSize:
                res -= b * u
                truckSize -= b
            else:
                return res - truckSize * u

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximum_units_1(self):
        print("Test maximumUnits 1... ", end="")
        self.assertEqual(
            self.sol.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4), 8
        )
        print("OK")

    def test_maximum_units_2(self):
        print("Test maximumUnits 2... ", end="")
        self.assertEqual(
            self.sol.maximumUnits(
                boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10
            ),
            91,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
