from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = Counter(stones)
        return sum(cnt[j] for j in jewels)


def test_num_jewels_in_stones():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.numJewelsInStones(jewels="z", stones="ZZ") == 0
    print("OK")


if __name__ == "__main__":
    test_num_jewels_in_stones()
