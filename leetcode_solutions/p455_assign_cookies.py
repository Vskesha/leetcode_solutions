from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = j = 0
        lg = len(g)
        ls = len(s)

        while j < ls:
            if s[j] >= g[i]:
                i += 1
                if i == lg:
                    return lg
            j += 1

        return i


class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i, j, lg, ls = 0, 0, len(g), len(s)
        while j < ls and i < lg:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i


class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        ls = len(s)
        for i, gr in enumerate(g):
            while j < ls and s[j] < gr:
                j += 1
            if j == ls:
                return i
            else:
                j += 1
        return len(g)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findContentChildren(g=[1, 2, 3], s=[1, 1]) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.findContentChildren(g=[1, 2], s=[1, 2, 3]) == 2
    print("OK")


if __name__ == "__main__":
    test()
