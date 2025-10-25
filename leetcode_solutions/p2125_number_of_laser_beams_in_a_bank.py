from itertools import pairwise
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for r in bank:
            q = r.count("1")
            if q:
                ans += q * prev
                prev = q
        return ans


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [r.count("1") for r in bank if "1" in r]
        ans = 0
        for a, b in pairwise(bank):
            ans += a * b
        return ans


class Solution2:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [r for r in bank if "1" in r]
        ans = 0
        for a, b in pairwise(bank):
            ans += a.count("1") * b.count("1")
        return ans


class Solution3:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        a = []
        for i in bank:
            c = i.count("1")
            if c != 0:
                a.append(c)
        for j in range(len(a) - 1):
            ans += a[j] * a[j + 1]
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.numberOfBeams(bank=["011001", "000000", "010100", "001000"]) == 8
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.numberOfBeams(bank=["000", "111", "000"]) == 0
    print("OK")


if __name__ == "__main__":
    test()
