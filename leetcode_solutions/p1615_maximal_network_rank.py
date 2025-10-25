class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        connected = [[0] * n for _ in range(n)]
        counts = [0] * n

        for fr, to in roads:
            counts[fr] += 1
            counts[to] += 1
            connected[fr][to] = 1
            connected[to][fr] = 1

        mc, mis = 0, []
        for i, c in enumerate(counts):
            if mc < c:
                mc = c
                mis = [i]
            elif mc == c:
                mis.append(i)

        ans = 0
        for mi in mis:
            for j, c in enumerate(counts):
                if j != mi:
                    ans = max(ans, mc + c - connected[mi][j])

        return ans


def main():
    sol = Solution()
    print(
        "4 ===",
        sol.maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]),
    )
    print(
        "5 ===",
        sol.maximalNetworkRank(
            n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        ),
    )
    print(
        "5 ===",
        sol.maximalNetworkRank(
            n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        ),
    )


if __name__ == "__main__":
    main()
