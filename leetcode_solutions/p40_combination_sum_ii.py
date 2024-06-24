import unittest
from bisect import bisect_right
from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cands = sorted([val, cnt] for val, cnt in Counter(candidates).items())
        lc = len(cands)
        comb = []
        result = []

        def dfs(i, left):
            if not left:
                result.append(comb.copy())
                return
            if i == lc:
                return
            for j in range(i, lc):
                val, cnt = cands[j]
                if val > left:
                    break
                cands[j][1] = cnt - 1
                comb.append(val)
                dfs(j + 1 if cnt == 1 else j, left - val)
                comb.pop()
                cands[j][1] = cnt

        dfs(0, target)
        return result


class Solution3:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lc = len(candidates)

        def dfs(i, left, comb, result):
            if not left:
                result.add(tuple(comb))
                return

            if i == lc:
                return

            for j in range(i, bisect_right(candidates, left)):
                comb.append(candidates[j])
                dfs(j + 1, left - candidates[j], comb, result)
                comb.pop()

        result = set()
        dfs(0, target, [], result)

        return [list(t) for t in result]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def same_combinations(combs1: list, combs2: list) -> bool:
        return set(tuple(comb) for comb in combs1) == set(
            tuple(comb) for comb in combs2
        )

    def test_combination_sum_2_1(self):
        print("Test combinationSum2 1... ", end="")
        self.assertTrue(
            self.same_combinations(
                self.sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8),
                [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            )
        )
        print("OK")

    def test_combination_sum_2_2(self):
        print("Test combinationSum2 2... ", end="")
        self.assertTrue(
            self.same_combinations(
                self.sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5),
                [[1, 2, 2], [5]],
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
