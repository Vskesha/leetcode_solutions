from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefixes = Counter()
        prefixes[0] = 1
        shifts = {ch: i for i, ch in enumerate("abcdefghij")}
        mask = 0
        res = 0

        for ch in word:
            mask ^= 1 << shifts[ch]
            res += prefixes[mask]
            prefixes[mask] += 1

            for i in range(10):
                res += prefixes[mask ^ (1 << i)]

        return res


def test_wonderful_substrings():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.wonderfulSubstrings(word="aba") == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.wonderfulSubstrings(word="aabb") == 9
    print("OK")

    print("Test 3... ", end="")
    assert sol.wonderfulSubstrings(word="he") == 2
    print("OK")


if __name__ == "__main__":
    test_wonderful_substrings()
