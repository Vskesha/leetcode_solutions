from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        lw = len(words)
        wds = "".join(words)

        if len(wds) % lw:
            return False
        for n in Counter(wds).values():
            if n % lw:
                return False
        return True


class Solution2:
    def makeEqual(self, words: List[str]) -> bool:
        return all(
            c % len(words) == 0 for c in Counter(chain(*words)).values()
        )


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.makeEqual(words=["abc", "aabc", "bc"]) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.makeEqual(words=["ab", "a"]) is False
    print("OK")


if __name__ == "__main__":
    test()
