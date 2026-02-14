import unittest
from collections import Counter
from functools import cache
from itertools import accumulate

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        ln = len(num)
        digits = sorted(map(int, num), reverse=True)
        sumd = sum(digits)
        if sumd & 1:
            return 0
        freq = Counter(digits)
        mf = max(freq.values())

        fact = [1] * (mf + 1)
        for i in range(2, mf + 1):
            fact[i] = fact[i - 1] * i % mod

        @cache
        def dp(even, odd, ev_rem, od_rem) -> int:
            if even == odd == 0:
                return 1
            d = digits[ln - even - odd]
            res = 0
            if odd and od_rem >= d:
                res = dp(even, odd - 1, ev_rem, od_rem - d) * odd
            if even and ev_rem >= d:
                res = (
                    res + dp(even - 1, odd, ev_rem - d, od_rem) * even
                ) % mod
            return res

        ans = dp(ln // 2, (ln + 1) // 2, sumd // 2, sumd // 2)

        for fr in freq.values():
            ans = ans * pow(fact[fr], mod - 2, mod) % mod

        return ans


# Time Limit Exceeded
class Solution2:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        ts = sum(map(int, num))
        if ts % 2:
            return 0
        ts2 = ts // 2
        cnt = Counter(map(int, num))
        ln = len(num)
        ln2 = ln // 2
        ln1 = ln - ln2

        fact = [1] * (ln1 + 1)
        for i in range(2, ln1 + 1):
            fact[i] = fact[i - 1] * i % mod

        max_group = max(cnt.values())
        max_group = min(max_group, ln1)
        ifact = [1] * (max_group + 1)
        for i in range(2, max_group + 1):
            ifact[i] = pow(fact[i], mod - 2, mod)

        @cache
        def dp(state: tuple, taken: int, left: int, cur_sum: int) -> int:
            digit = len(state)
            needed = ln2 - taken

            if cur_sum + digit * needed > ts2:
                return 0

            if not needed:
                if cur_sum != ts2:
                    return 0
                while len(state) < 10:
                    state += (0,)
                res1, res2 = fact[ln1], fact[ln2]
                for d in range(10):
                    gr2 = state[d]
                    gr1 = cnt[d] - gr2
                    res1 = res1 * ifact[gr1] % mod
                    res2 = res2 * ifact[gr2] % mod
                res = res1 * res2 % mod
                return res

            if not cnt[digit]:
                while not cnt[len(state)]:
                    state = state + (0,)
                return dp(state, taken, left, cur_sum)

            left -= cnt[digit]
            min_to_take = max(0, needed - left)
            max_to_take = min(needed, cnt[digit])
            res = 0
            for k in range(min_to_take, max_to_take + 1):
                res += dp(state + (k,), taken + k, left, cur_sum + digit * k)
            return res

        ans = dp(tuple(), 0, ln, 0)
        return ans


class Solution3:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        ln = len(num)
        digits = sorted(map(int, num), reverse=True)
        acc = list(accumulate(digits, initial=0))
        sumd = acc[-1]
        sumd2 = sumd // 2
        if sumd & 1:
            return 0
        freq = Counter(digits)
        mf = max(freq.values())

        fact = [1] * (mf + 1)
        for i in range(2, mf + 1):
            fact[i] = fact[i - 1] * i % mod

        @cache
        def dp(even, odd, ev_rem) -> int:
            if even == odd == 0:
                return 1
            i = ln - even - odd
            d = digits[i]
            res = 0
            od_rem = sumd - acc[i] - ev_rem
            if even and ev_rem >= d:
                res = dp(even - 1, odd, ev_rem - d) * even
            if odd and od_rem >= d:
                res = (res + dp(even, odd - 1, ev_rem) * odd) % mod
            return res

        ans = dp(ln // 2, (ln + 1) // 2, sumd2)

        for fr in freq.values():
            ans = ans * pow(fact[fr], mod - 2, mod) % mod

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countBalancedPermutations"] * 5,
            "kwargs": [
                dict(num="298089"),
                dict(num="11"),
                dict(num="123"),
                dict(num="112"),
                dict(num="12345"),
            ],
            "expected": [18, 1, 2, 1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
