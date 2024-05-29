from collections import defaultdict
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        pals = defaultdict(list)
        ls = len(s)

        for i in range(ls):
            for di in range(2):
                l, r = i, i + di
                while l >= 0 and r < ls and s[l] == s[r]:
                    pals[l].append(r + 1)
                    l -= 1
                    r += 1

        def backtrack(st, comb):
            if st == ls:
                self.ans.append(comb.copy())

            for end in pals[st]:
                comb.append(s[st:end])
                backtrack(end, comb)
                comb.pop()

        backtrack(0, [])

        return self.ans


def test_partition():
    sol = Solution()

    print("Test 1... ", end="")
    res = sol.partition(s="aab")
    out = [["a", "a", "b"], ["aa", "b"]]
    assert set(tuple(x) for x in res) == set(tuple(x) for x in out)
    print("OK")

    print("Test 2... ", end="")
    res = sol.partition(s="a")
    out = [["a"]]
    assert set(tuple(x) for x in res) == set(tuple(x) for x in out)
    print("OK")


if __name__ == "__main__":
    test_partition()
