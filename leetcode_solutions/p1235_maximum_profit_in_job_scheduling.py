from typing import List
import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_start, _, current_profit = jobs[i]
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]

            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.jobScheduling(
            startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
        )
        == 120
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.jobScheduling(
            startTime=[1, 2, 3, 4, 6],
            endTime=[3, 5, 10, 6, 9],
            profit=[20, 20, 100, 70, 60],
        )
        == 150
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]) == 6
    )
    print("OK")


if __name__ == "__main__":
    test()
