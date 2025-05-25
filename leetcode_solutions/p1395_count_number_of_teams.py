import unittest
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # BITree
        lr = len(rating)
        rmax = max(rating)
        lbit = [0] * (rmax + 1)
        rbit = [0] * (rmax + 1)

        def get_sum(r, bit):
            sm = 0
            while r > 0:
                sm += bit[r]
                r -= r & (-r)
            return sm

        def update(r, d, bit):
            while r <= rmax:
                bit[r] += d
                r += r & (-r)

        for r in rating:
            update(r, 1, rbit)

        teams = 0
        for i, r in enumerate(rating):
            update(r, -1, rbit)
            sl = get_sum(r, lbit)
            sr = get_sum(r, rbit)
            update(r, 1, lbit)
            bl = i - sl
            br = lr - sr - i - 1
            teams += sl * br + bl * sr

        return teams


class Solution1:
    def numTeams(self, rating: List[int]) -> int:
        lr = len(rating)
        smaller = [0] * lr
        bigger = [0] * lr
        ans = 0
        for i in range(1, lr):
            for j in range(i):
                if rating[j] < rating[i]:
                    ans += smaller[j]
                    smaller[i] += 1
                elif rating[j] > rating[i]:
                    ans += bigger[j]
                    bigger[i] += 1
        return ans


class Solution2:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        lower_left = [0] * n
        higher_right = [0] * n
        lower_right = [0] * n
        higher_left = [0] * n

        for i in range(1, n):
            for j in range(i):
                if rating[j] < rating[i]:
                    higher_right[j] += 1
                    lower_left[i] += 1
                else:
                    lower_right[j] += 1
                    higher_left[i] += 1

        ans = 0
        for i in range(n):
            ans += lower_left[i] * higher_right[i]
            ans += higher_left[i] * lower_right[i]

        return ans


class Solution3:
    def numTeams(self, rating: List[int]) -> int:
        @cache
        def increasing(i, size=1):
            if size == 3:
                return 1
            teams = 0
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    teams += increasing(j, size + 1)
            return teams

        @cache
        def decreasing(i, size=1):
            if size == 3:
                return 1
            teams = 0
            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    teams += decreasing(j, size + 1)
            return teams

        n = len(rating)
        teams = 0

        for i in range(n):
            teams += increasing(i)
            teams += decreasing(i)

        return teams


class Solution4:
    def numTeams(self, rating: List[int]) -> int:
        smaller = defaultdict(list)
        bigger = defaultdict(list)
        lr = len(rating)

        for i in range(lr):
            for j in range(i):
                if rating[i] > rating[j]:
                    smaller[i].append(j)
                else:
                    bigger[i].append(j)

        ans = 0
        for i in range(lr):
            for j in smaller[i]:
                ans += len(smaller[j])
            for j in bigger[i]:
                ans += len(bigger[j])

        return ans


from sortedcontainers import SortedList


class Solution5:
    def numTeams(self, rating: List[int]) -> int:
        lr = len(rating) - 1
        sl = SortedList()
        low = {r: i for i, r in enumerate(sorted(rating))}
        res = 0

        for idx, r in enumerate(rating):
            i = sl.bisect(r)
            sl.add(r)
            j = low[r] - i
            res += i * (lr - idx - 2 * j) + j * idx

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numTeams(self):
        print("Test numTeams 1... ", end="")
        self.assertEqual(3, self.sol.numTeams(rating=[2, 5, 3, 4, 1]))
        print("OK")

    def test_numTeams_2(self):
        print("Test numTeams 2... ", end="")
        self.assertEqual(0, self.sol.numTeams(rating=[2, 1, 3]))
        print("OK")

    def test_numTeams_3(self):
        print("Test numTeams 3... ", end="")
        self.assertEqual(4, self.sol.numTeams(rating=[1, 2, 3, 4]))
        print("OK")

    def test_numTeams_4(self):
        print("Test numTeams 4... ", end="")
        self.assertEqual(1, self.sol.numTeams(rating=[3, 7, 5, 6]))
        print("OK")


if __name__ == "__main__":
    unittest.main()
