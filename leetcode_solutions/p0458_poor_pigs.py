from math import ceil, log


class Solution:
    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        return ceil(round(log(buckets, minutesToTest // minutesToDie + 1), 10))


class Solution2:
    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        c = minutesToTest // minutesToDie + 1
        pigs = 0
        while c**pigs < buckets:
            pigs += 1
        return pigs


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.poorPigs(buckets=4, minutesToDie=15, minutesToTest=15) == 2
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.poorPigs(buckets=4, minutesToDie=15, minutesToTest=30) == 2
    print("ok")


if __name__ == "__main__":
    test()
