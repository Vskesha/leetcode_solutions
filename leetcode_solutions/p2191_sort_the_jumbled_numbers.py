import unittest
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(n: int) -> int:
            if not n:
                return mapping[0]
            m, p = 0, 1
            while n:
                m += mapping[n % 10] * p
                p *= 10
                n //= 10
            return m

        return sorted(nums, key=mapped)


class Solution2:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(n: int) -> int:
            if not n:
                return mapping[0]
            m, p = 0, 1
            while n:
                n, d = divmod(n, 10)
                m += mapping[d] * p
                p *= 10
            return m

        return sorted(nums, key=mapped)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_sortJumbled_1(self):
        print("Test sortJumbled 1... ", end="")
        self.assertListEqual(
            [338, 38, 991],
            self.sol.sortJumbled(
                mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]
            ),
        )
        print("OK")

    def test_sortJumbled_2(self):
        print("Test sortJumbled 2... ", end="")
        self.assertListEqual(
            [123, 456, 789],
            self.sol.sortJumbled(
                mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
