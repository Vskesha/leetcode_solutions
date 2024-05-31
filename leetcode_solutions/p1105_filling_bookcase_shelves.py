from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        lb = len(books)
        inf = float("inf")
        dp = [inf] * lb
        dp.append(0)

        for i in range(lb - 1, -1, -1):
            w, h = 0, 0
            for j in range(i, lb):
                w += books[j][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j][1])
                dp[i] = min(dp[i], h + dp[j + 1])

        return dp[0]


def test_min_height_shelves():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.minHeightShelves(
            books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4
        )
        == 6
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.minHeightShelves(books=[[1, 3], [2, 4], [3, 2]], shelfWidth=6) == 4
    print("OK")


if __name__ == "__main__":
    test_min_height_shelves()
