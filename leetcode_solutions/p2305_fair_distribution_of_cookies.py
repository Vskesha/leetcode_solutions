import unittest
from statistics import mean
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(p):
            nonlocal best
            if p == len(cookies):
                best = min(best, max(split))
                return
            if len(split) < k:
                split.append(cookies[p])
                dfs(p + 1)
                split.pop()
            seen = set()
            for i in range(len(split)):
                if split[i] + cookies[p] < best and split[i] not in seen:
                    seen.add(split[i])
                    split[i] += cookies[p]
                    dfs(p + 1)
                    split[i] -= cookies[p]

        split = []
        best = float("inf")
        dfs(0)
        return best


class Solution1:
    def __init__(self):
        self.unfairness = float("inf")

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(bag):
            if bag == lc:
                self.unfairness = min(self.unfairness, max(ch))
            val = cookies[bag]
            for i in range(k):
                if ch[i] + val >= self.unfairness or ch[i] > m:
                    continue
                ch[i] += val
                backtrack(bag + 1)
                ch[i] -= val

        ch = [0] * k
        m = mean(cookies)
        lc = len(cookies)
        backtrack(0)

        return self.unfairness


class Solution2:
    def __init__(self):
        self.ans = float("inf")

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        cookies.sort(reverse=True)
        curr_distribution = [0] * k

        def distribution(curr_bag, zero_count):
            if curr_bag == n:
                self.ans = min(self.ans, max(curr_distribution))
                return
            if n - curr_bag < zero_count:
                return
            value = cookies[curr_bag]
            for i in range(k):
                new_zero_count = zero_count - (curr_distribution[i] == 0)
                curr_distribution[i] += value
                if curr_distribution[i] < self.ans:
                    distribution(curr_bag + 1, new_zero_count)
                curr_distribution[i] -= value

        distribution(0, k)
        return self.ans


class Solution3:
    def __init__(self):
        self.ans = float("inf")

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)

        def distribution(curr_bag, curr_distribution):
            if curr_bag == n:
                self.ans = min(self.ans, max(curr_distribution))
                return
            val = cookies[curr_bag]
            for i in range(k):
                curr_distribution[i] += val
                distribution(curr_bag + 1, curr_distribution)
                curr_distribution[i] -= val

        distribution(0, [0] * k)
        return self.ans  # noqa


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_distribute_cookies_1(self):
        print("Test distributeCookies 1 ... ", end="")
        self.assertEqual(
            self.sol.distributeCookies(cookies=[8, 15, 10, 20, 8], k=2), 31
        )
        print("OK")

    def test_distribute_cookies_2(self):
        print("Test distributeCookies 2 ... ", end="")
        self.assertEqual(
            self.sol.distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3), 7
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
