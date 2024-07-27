import unittest
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            rec1[0] >= rec2[2]
            or rec1[2] <= rec2[0]
            or rec1[1] >= rec2[3]
            or rec1[3] <= rec2[1]
        )


class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            rec1[0] >= rec2[2]
            or rec2[0] >= rec1[2]
            or rec1[1] >= rec2[3]
            or rec2[1] >= rec1[3]
        )


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_isRectangleOverlap_1(self):
        print("Test isRectangleOverlap 1... ", end="")
        self.assertTrue(
            self.sol.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3])
        )
        print("OK")

    def test_isRectangleOverlap_2(self):
        print("Test isRectangleOverlap 2... ", end="")
        self.assertFalse(
            self.sol.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1])
        )
        print("OK")

    def test_isRectangleOverlap_3(self):
        print("Test isRectangleOverlap 3... ", end="")
        self.assertFalse(
            self.sol.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[2, 2, 3, 3])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
