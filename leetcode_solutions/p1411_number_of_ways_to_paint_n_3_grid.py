import time
from functools import lru_cache, wraps
from itertools import product


def time_taken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


class Solution:
    tuples = {t for t in product(range(3), repeat=3) if t[0] != t[1] and t[1] != t[2]}
    combs = {}
    for t in tuples:
        combs[t] = []
        for tc in tuples:
            if tc[0] != t[0] and tc[1] != t[1] and tc[2] != t[2]:
                combs[t].append(tc)

    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        prev = {t: 1 for t in Solution.tuples}

        for _ in range(1, n):
            prev = {
                tc: sum(prev[tp] for tp in Solution.combs[tc]) % mod
                for tc in Solution.combs
            }

        return sum(prev.values()) % mod


class Solution2:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7

        prev = {
            t: 1 for t in product(range(3), repeat=3) if t[0] != t[1] and t[1] != t[2]
        }

        for _ in range(1, n):
            new = {}
            for tc in prev:
                new[tc] = 0
                for tp in prev:
                    if tp[0] != tc[0] and tp[1] != tc[1] and tp[2] != tc[2]:
                        new[tc] = (new[tc] + prev[tp]) % mod
            prev = new

        return sum(prev.values()) % mod


class Solution3:
    def numOfWays(self, n: int) -> int:
        color = {1, 2, 3}

        @lru_cache(None)
        def dp(row, prev1, prev2, prev3):
            if row == n:
                return 1

            ans = 0

            for i in color:
                for j in color:
                    for k in color:
                        if (
                            i != j
                            and j != k
                            and i != prev1
                            and j != prev2
                            and k != prev3
                        ):
                            ans += dp(row + 1, i, j, k)
            return ans

        return dp(0, "", "", "") % (10**9 + 7)


@time_taken
def test_num_of_ways():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numOfWays(n=1) == 12
    print("OK")

    print("Test 2... ", end="")
    assert sol.numOfWays(n=5000) == 30228214
    print("OK")


if __name__ == "__main__":
    test_num_of_ways()
