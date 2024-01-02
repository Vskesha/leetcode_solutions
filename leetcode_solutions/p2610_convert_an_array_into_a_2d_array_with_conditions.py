from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = [0] * (len(nums) + 1)
        for num in nums:
            if count[num] >= len(ans):
                ans.append([])
            ans[count[num]].append(num)
            count[num] += 1
        return ans


class Solution1:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans, cnt = [], Counter()
        for n in nums:
            if cnt[n] < len(ans):
                ans[cnt[n]].append(n)
            else:
                ans.append([n])
            cnt[n] += 1
        return ans


class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rem = ln = len(nums)
        taken = [False] * ln
        res = []
        while rem:
            row = set()
            for i, n in enumerate(nums):
                if not (taken[i] or n in row):
                    taken[i] = True
                    row.add(n)
            res.append(list(row))
            rem -= len(row)

        return res


class Solution3:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        cnt = Counter(nums)
        res = []
        while ln:
            row = []
            for n in cnt:
                if cnt[n]:
                    row.append(n)
                    cnt[n] -= 1
            res.append(row)
            ln -= len(row)
        return res


class Solution4:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        cnt = Counter(nums)
        rows = max(cnt.values())
        res = [[] for _ in range(rows)]

        for n, q in cnt.items():
            for row in range(q):
                res[row].append(n)

        return res


def test():
    sol = Solution()

    print("Test 1... ", end="")
    for row in sol.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]):
        assert len(set(row)) == len(row)
    print("OK")

    print("Test 2... ", end="")
    for row in sol.findMatrix(nums=[1, 2, 3, 4]):
        assert len(set(row)) == len(row)
    print("OK")


if __name__ == "__main__":
    test()
