from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        lc = len(candidates)

        def combs(i, target, comb):
            if target == 0:
                res.append(comb.copy())
            for j in range(i, lc):
                val = candidates[j]
                if val > target:
                    break
                comb.append(val)
                combs(j, target - val, comb)
                comb.pop()

        combs(0, target, [])

        return res


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        lc = len(candidates)

        def cmb(comb, sm, last):
            for i in range(last, lc):
                nsm = sm + candidates[i]
                if nsm < target:
                    comb.append(candidates[i])
                    cmb(comb, nsm, i)
                    comb.pop()
                elif nsm == target:
                    ans.append(comb + candidates[i : i + 1])

        cmb([], 0, 0)
        return ans


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def cmb(comb, sm, last):
            if sm > target:
                return
            if sm == target:
                ans.append(comb.copy())
                return
            for c in candidates:
                if c >= last:
                    comb.append(c)
                    cmb(comb, sm + c, c)
                    comb.pop()

        cmb([], 0, 0)
        return ans


def test_combination_sum():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.combinationSum(candidates=[2, 3, 5], target=8) == [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ]
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.combinationSum(candidates=[2], target=1) == []
    print("OK")


if __name__ == "__main__":
    test_combination_sum()
