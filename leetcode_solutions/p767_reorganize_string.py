from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:

        ls = len(s)
        counter = Counter(s)
        most_com = counter.most_common()
        hf = (ls + 1) // 2
        if most_com[0][1] > hf:
            return ''
        aux = ''.join(c * n for c, n in most_com)
        aux1 = aux[:hf]
        aux2 = aux[hf:]
        res = ''
        for i in range(len(aux2)):
            res += aux1[i] + aux2[i]
        if len(aux1) > len(aux2):
            res += aux1[-1]
        return res


class Solution2:
    def reorganizeString(self, s: str) -> str:

        def take(seq: list[tuple[int]]):
            for ch, n in seq:
                for _ in range(n):
                    yield ch

        ls = len(s)
        counter = Counter(s)
        most_com = counter.most_common()

        if most_com[0][1] > (ls + 1) // 2:
            return ''

        res = [''] * ls
        taker = take(most_com)
        for i in range(0, ls, 2):
            res[i] = next(taker)
        for i in range(1, ls, 2):
            res[i] = next(taker)
        return ''.join(res)


def main():
    sol = Solution()
    print('aba ===', sol.reorganizeString(s='aab'))
    print(' ===', sol.reorganizeString(s='aaab'))


if __name__ == '__main__':
    main()
