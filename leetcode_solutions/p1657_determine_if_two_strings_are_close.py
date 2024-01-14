from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (
            len(word1) == len(word2)
            and set(word1) == set(word2)
            and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        )


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.closeStrings(word1="abc", word2="bca") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.closeStrings(word1="a", word2="aa") is False
    print("OK")

    print("Test 3... ", end="")
    assert sol.closeStrings(word1="cabbba", word2="abbccc") is True
    print("OK")


if __name__ == "__main__":
    test()
