import unittest
from statistics import mean
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        et = tw = 0

        for arr, t in customers:
            et = max(arr, et) + t
            tw += et - arr

        return tw / len(customers)


class Solution1:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        et, ans = 0, []

        for arr, t in customers:
            et = max(arr, et) + t
            ans.append(et - arr)

        return mean(ans)


class Solution2:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        et = 0
        ans = []

        for arr, t in customers:
            if et > arr:
                et += t
                ans.append(et - arr)
            else:
                et = arr + t
                ans.append(t)
        return mean(ans)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_average_waiting_time_1(self):
        print("Test averageWaitingTime 1... ", end="")
        self.assertAlmostEqual(
            self.sol.averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]),
            5.0,
            places=5,
        )
        print("OK")

    def test_average_waiting_time_2(self):
        print("Test averageWaitingTime 2... ", end="")
        self.assertAlmostEqual(
            self.sol.averageWaitingTime(
                customers=[[5, 2], [5, 4], [10, 3], [20, 1]]
            ),
            3.25,
            places=5,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
