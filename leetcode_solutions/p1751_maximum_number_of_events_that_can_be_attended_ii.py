from bisect import bisect_left
from functools import lru_cache


# iterative solution
class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        events_starts = [x[0] for x in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for idx in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                _, end, val = events[idx]
                next_idx = bisect_left(events_starts, end + 1)
                with_curr = val + dp[next_idx][j - 1]
                without_curr = dp[idx + 1][j]
                dp[idx][j] = max(without_curr, with_curr)

        return dp[0][k]


# recursive solution
class Solution2:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        events_starts = [x[0] for x in events]

        @lru_cache(None)
        def dfs(curr_idx, remain) -> int:
            if not remain or curr_idx == n:
                return 0

            without_curr = dfs(curr_idx + 1, remain)

            next_idx = bisect_left(events_starts, events[curr_idx][1] + 1)
            with_curr = dfs(next_idx, remain - 1) + events[curr_idx][2]
            return max(without_curr, with_curr)

        return dfs(0, k)


def main():
    sol = Solution()
    print("7 ===", sol.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
    print(
        "10 ==", sol.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2)
    )
    print(
        "9 ===",
        sol.maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3),
    )


if __name__ == "__main__":
    main()
