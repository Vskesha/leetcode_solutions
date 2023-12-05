from functools import lru_cache
from string import ascii_uppercase


class Solution:
    def minimumDistance(self, word: str) -> int:
        coords = {c: divmod(i, 6) for i, c in enumerate(ascii_uppercase)}
        lw = len(word)

        @lru_cache(None)
        def min_dist(l, r, i):
            if i == lw:
                return 0
            y, x = coords[word[i]]
            ld = abs(l[0] - y) + abs(l[1] - x) if l else 0
            rd = abs(r[0] - y) + abs(r[1] - x) if r else 0
            i += 1
            return min(min_dist((y, x), r, i) + ld, min_dist(l, (y, x), i) + rd)

        return min_dist(None, None, 0)


class Solution2:
    def minimumDistance(self, word: str) -> int:
        al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        coords = {c: divmod(i, 6) for i, c in enumerate(al)}
        lw = len(word)

        @lru_cache(None)
        def min_dist(l, r, i):
            if i == lw:
                return 0
            y, x = coords[word[i]]
            ld = abs(l[0] - y) + abs(l[1] - x) if l else 0
            rd = abs(r[0] - y) + abs(r[1] - x) if r else 0
            i += 1
            return min(min_dist((y, x), r, i) + ld, min_dist(l, (y, x), i) + rd)

        return min_dist(None, None, 0)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.minimumDistance(word="CAKE") == 3
    print('OK')

    print('Test 2... ', end='')
    assert sol.minimumDistance(word="HAPPY") == 6
    print('OK')


if __name__ == '__main__':
    test()
