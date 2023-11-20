from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        lg = len(garbage)

        g = 0
        for i in range(lg - 1, 0, -1):
            if 'G' in garbage[i]:
                break
            else:
                g += travel[i - 1]

        m = 0
        for i in range(lg - 1, 0, -1):
            if 'M' in garbage[i]:
                break
            else:
                m += travel[i - 1]

        p = 0
        for i in range(lg - 1, 0, -1):
            if 'P' in garbage[i]:
                break
            else:
                p += travel[i - 1]

        return sum(len(s) for s in garbage) + 3 * sum(travel) - g - m - p


class Solution2:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        tr = {'G': 0, 'M': 0, 'P': 0}
        stops = len(garbage[0])
        curr = 0

        for i in range(len(travel)):
            curr += travel[i]
            for ch in garbage[i + 1]:
                tr[ch] = curr
                stops += 1

        return sum(tr.values()) + stops


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]) == 21
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10]) == 37
    print('OK')


if __name__ == '__main__':
    test()
