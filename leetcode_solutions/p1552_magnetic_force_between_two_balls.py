import unittest
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lp = len(position)

        def can_place(dist) -> bool:
            st = position[0]
            i = 1
            for j in range(m - 1):
                st += dist
                while position[i] < st:
                    i += 1
                    if i == lp:
                        return False
                st = position[i]
            return True

        l, r = 0, (max(position) - min(position)) // (m - 1)

        while l < r:
            mid = (l + r + 1) // 2
            if can_place(mid):
                l = mid
            else:
                r = mid - 1

        return r


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_distance_1(self):
        print("Test maxDistance 1 ... ", end="")
        self.assertEqual(self.sol.maxDistance(position=[1, 2, 3, 4, 7], m=3), 3)
        print("OK")

    def test_max_distance_2(self):
        print("Test maxDistance 2 ... ", end="")
        self.assertEqual(
            self.sol.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2), 999999999
        )
        print("OK")

    def test_max_distance_3(self):
        print("Test maxDistance 3 ... ", end="")
        self.assertEqual(self.sol.maxDistance(position=[79, 74, 57, 22], m=4), 5)
        print("OK")


if __name__ == "__main__":
    unittest.main()
