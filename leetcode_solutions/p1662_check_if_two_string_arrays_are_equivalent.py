from itertools import chain, zip_longest
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a, b in zip_longest(chain(*word1), chain(*word2)):
            if a != b:
                return False
        return True


class Solution2:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a, b in zip_longest("".join(word1), "".join(word2)):
            if a != b:
                return False
        return True


class Solution3:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = i1 = i2 = 0
        lw1 = len(word1)
        lw2 = len(word2)

        while w1 < lw1 and w2 < lw2:
            if word1[w1][i1] != word2[w2][i2]:
                return False
            i1 += 1
            i2 += 1
            if i1 == len(word1[w1]):
                i1 = 0
                w1 += 1
            if i2 == len(word2[w2]):
                i2 = 0
                w2 += 1

        return w1 == lw1 and w2 == lw2 and not (i1 or i2)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]) is True
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]) is False
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.arrayStringsAreEqual(
            word1=["abc", "d", "defg"], word2=["abcddefg"]
        )
        is True
    )
    print("OK")


if __name__ == "__main__":
    test()
