from itertools import pairwise


class Solution:
    def modifyString(self, s: str) -> str:
        res, ls = list(s), len(s)

        for i in range(ls):
            if res[i] == '?':
                res[i] = {'a', 'b', 'c'}.difference({res[i - 1] if i else '?', res[i + 1] if i < ls - 1 else '?'}).pop()

        return ''.join(res)


class Solution2:
    def modifyString(self, s: str) -> str:
        rp = 'abc'
        prev = '?'
        nxt = s[0]
        res = []
        for i in range(1, len(s)):
            ch = nxt
            nxt = s[i]
            if ch == '?':
                for r in rp:
                    if r != prev and r != nxt:
                        ch = r
                        break
            res.append(ch)
            prev = ch
        if s[-1] == '?':
            if not res or res[-1] == 'b':
                res.append('a')
            else:
                res.append('b')
        else:
            res.append(s[-1])

        return ''.join(res)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    for a, b in pairwise(sol.modifyString(s="?zs")):
        assert a != b
    print('OK')

    print('Test 2... ', end='')
    for a, b in pairwise(sol.modifyString(s="ubv?w")):
        assert a != b
    print('OK')


if __name__ == '__main__':
    test()
