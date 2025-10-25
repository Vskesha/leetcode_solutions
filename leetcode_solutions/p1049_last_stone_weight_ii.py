from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        diffs = {0}

        for stone in stones:
            new = set()
            for diff in diffs:
                new.add(abs(diff - stone))
                new.add(diff + stone)
            diffs = new

        return min(diffs)


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1]) == 1
    print("ok\nTest 2 ... ", end="")
    assert sol.lastStoneWeightII(stones=[31, 26, 33, 21, 40]) == 5
    print("ok")


if __name__ == "__main__":
    test()
