from itertools import groupby, zip_longest


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        for a, b in zip_longest(groupby(name), groupby(typed)):
            if a is None or b is None:
                return False

            if a[0] != b[0]:
                return False

            if len(list(a[1])) > len(list(b[1])):
                return False

        return True


class Solution1:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ln, lt = len(name), len(typed)
        i = j = 0

        while i < ln and j < lt:
            a = name[i]
            b = typed[j]
            if a != b:
                return False
            si = i
            while i < ln and name[i] == a:
                i += 1
            sj = j
            while j < lt and typed[j] == b:
                j += 1
            if i - si > j - sj:
                return False
        return i == ln and j == lt


class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ln, lt = len(name), len(typed)
        if name[0] != typed[0]:
            return False
        i = j = 1

        while i < ln and j < lt:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        if i != ln:
            return False
        a = name[-1]
        while j < lt:
            if typed[j] != a:
                return False
            j += 1
        return True


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.isLongPressedName(name="alex", typed="aaleex") is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.isLongPressedName(name="saeed", typed="ssaaedd") is False
    print("OK")


if __name__ == "__main__":
    test()
