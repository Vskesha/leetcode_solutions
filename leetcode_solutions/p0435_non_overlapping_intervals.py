class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0], reverse=True)

        ans = 0

        next_start = intervals[0][1]

        for start, end in intervals:
            if end > next_start:
                ans += 1
            else:
                next_start = start

        return ans


def main():
    sol = Solution()
    print(
        "1 ===",
        sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]),
    )
    print(
        "2 ===", sol.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]])
    )
    print("0 ===", sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))


if __name__ == "__main__":
    main()
