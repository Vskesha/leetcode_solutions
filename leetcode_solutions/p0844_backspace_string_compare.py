from itertools import zip_longest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nxt(st, i):
            skip = 0
            i -= 1
            while i >= 0:
                if st[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break
                i -= 1
            return i

        i = len(s)
        j = len(t)

        while True:
            i = nxt(s, i)
            j = nxt(t, j)

            if i < 0 or j < 0:
                break

            if s[i] != t[j]:
                return False

        return i == j


class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)
        j = len(t)

        while True:
            i -= 1
            j -= 1

            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break
                i -= 1

            skip = 0
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break
                j -= 1

            if i < 0 or j < 0:
                break

            if s[i] != t[j]:
                return False

        return i == j


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def chars(st: str):
            skip = 0
            for ch in reversed(st):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch

        return all(a == b for a, b in zip_longest(chars(s), chars(t)))


class Solution3:
    def backspaceCompare(self, s: str, t: str) -> bool:

        ls = []
        lt = []

        for ch in s:
            if ch == '#':
                if ls:
                    ls.pop()
            else:
                ls.append(ch)

        for ch in t:
            if ch == '#':
                if lt:
                    lt.pop()
            else:
                lt.append(ch)

        return ls == lt


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.backspaceCompare(s="ab#c", t="ad#c") is True
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.backspaceCompare(s="ab##", t="c#d#") is True
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.backspaceCompare(s="a#c", t="b") is False
    print('ok')


if __name__ == '__main__':
    test()
