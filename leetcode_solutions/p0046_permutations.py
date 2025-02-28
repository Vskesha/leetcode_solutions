import unittest
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        taken = [False] * ln
        curr = []
        res = []

        def perm():
            if len(curr) == ln:
                res.append(curr.copy())

            for i in range(ln):
                if not taken[i]:
                    curr.append(nums[i])
                    taken[i] = True
                    perm()
                    curr.pop()
                    taken[i] = False

        perm()
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums, len(nums))))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def same_permutations(self, p1, p2):
        return set(map(tuple, p1)) == set(map(tuple, p2))

    def test_permute_1(self):
        print("Test permute 1... ", end="")
        self.assertTrue(
            self.same_permutations(
                self.sol.permute(nums=[1, 2, 3]),
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            )
        )
        print("OK")

    def test_permute_2(self):
        print("Test permute 2... ", end="")
        self.assertTrue(
            self.same_permutations(
                self.sol.permute(nums=[0, 1]),
                [[0, 1], [1, 0]],
            )
        )
        print("OK")

    def test_permute_3(self):
        print("Test permute 3... ", end="")
        self.assertTrue(
            self.same_permutations(
                self.sol.permute(nums=[1]),
                [[1]],
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
