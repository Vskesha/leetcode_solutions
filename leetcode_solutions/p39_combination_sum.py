from typing import List


class Solution:
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
                    ans.append(comb + candidates[i:i + 1])

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


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.combinationSum(candidates=[2], target=1) == []
    print('ok')


if __name__ == '__main__':
    test()
