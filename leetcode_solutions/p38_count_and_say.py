from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            ans = ''.join(f'{len(list(gr))}{el}' for el, gr in groupby(ans))
        return ans


class Solution1:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            aux = [0, ans[0]]
            for d in ans:
                if d == aux[-1]:
                    aux[-2] += 1
                else:
                    aux.extend([1, d])
            ans = ''.join(map(str, aux))
        return ans


class Solution2:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            res = []
            counter = 0
            char = ans[0]
            for c in ans:
                if c == char:
                    counter += 1
                else:
                    res.append(f'{counter}{char}')
                    counter = 1
                    char = c
            res.append(f'{counter}{char}')
            ans = ''.join(res)
        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.countAndSay(n=1) == '1'
    print('OK')

    print('Test 2... ', end='')
    assert sol.countAndSay(n=4) == '1211'
    print('OK')


if __name__ == '__main__':
    test()
