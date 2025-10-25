class Solution:
    def champagneTower(
        self, poured: int, query_row: int, query_glass: int
    ) -> float:
        row = [poured]

        for i in range(1, query_row + 1):
            new = [0] * (i + 1)
            for j, fl in enumerate(row):
                if fl < 1:
                    continue
                fl = (fl - 1) / 2
                new[j] += fl
                new[j + 1] += fl
            row = new

        return min(row[query_glass], 1)


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.champagneTower(poured=1, query_row=1, query_glass=1) == 0.0
    print("ok\nTest 2 ... ", end="")
    assert sol.champagneTower(poured=2, query_row=1, query_glass=1) == 0.50000
    print("ok\nTest 3 ... ", end="")
    assert (
        sol.champagneTower(poured=100000009, query_row=33, query_glass=17)
        == 1.0
    )
    print("ok")


if __name__ == "__main__":
    test()
