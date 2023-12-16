from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        for i in range(1, len(tiles) + 1):
            for p in permutations(tiles, i):
                res.add(p)

        return len(res)


class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)

        result = set()

        for length in range(1, n + 1):
            for perm in permutations(tiles, length):
                result.add(''.join(perm))

        return len(result)


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.numTilePossibilities(tiles="AAB") == 8
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.numTilePossibilities(tiles="AAABBC") == 188
    print('OK')

    print('Test 3 ... ', end='')
    assert sol.numTilePossibilities(tiles="V") == 1
    print('OK')


if __name__ == '__main__':
    test()
