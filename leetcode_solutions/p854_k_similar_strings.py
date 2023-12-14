from collections import defaultdict, deque
from functools import cache


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        ls = len(s1)
        bfs = deque()
        bfs.append((s1, 0))
        visited = {s1}
        while bfs:
            s, dist = bfs.popleft()
            if s == s2:
                return dist
            i = dist
            while i < ls and s[i] == s2[i]:
                i += 1
            tf = s2[i]
            for j in range(i + 1, ls):
                if tf == s[j] != s2[j]:
                    ns = s[:i] + tf + s[i + 1:j] + s[i] + s[j + 1:]
                    if ns not in visited:
                        visited.add(ns)
                        bfs.append((ns, dist + 1))


class Solution2:
    def kSimilarity(self, s1: str, s2: str) -> int:
        ls = len(s1)
        idx = tuple(i for i in range(ls) if s1[i] != s2[i])
        chi = defaultdict(list)
        for i in idx:
            chi[s1[i]].append(i)

        @cache
        def dfs(ids: tuple[int]) -> int:
            if not ids:
                return 0
            bfs = deque([(i,) for i in ids])
            cycles = set()
            while not cycles and bfs:
                for _ in range(len(bfs)):
                    path = bfs.popleft()
                    tf = s2[path[-1]]
                    for i in chi[tf]:
                        if i == path[0]:
                            im = path.index(min(path))
                            cycles.add(path[im:] + path[:im])
                        elif i in ids:
                            bfs.append(path + (i,))

            return max(dfs(tuple(i for i in ids if i not in c)) for c in cycles) + 1 if cycles else 0

        return len(idx) - dfs(idx)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.kSimilarity(s1="ab", s2="ba") == 1
    print('OK')

    print('Test 2... ', end='')
    assert sol.kSimilarity(s1="abc", s2="bca") == 2
    print('OK')

    print('Test 3... ', end='')
    assert sol.kSimilarity(s1="abcd", s2="badc") == 2
    print('OK')

    print('Test 4... ', end='')
    assert sol.kSimilarity(s1="abfcd", s2="bdfac") == 3
    print('OK')

    print('Test 5... ', end='')
    assert sol.kSimilarity(s1="aabbccddee", s2="cdacbeebad") == 6
    print('OK')

    print('Test 6... ', end='')
    assert sol.kSimilarity(s1="abcdefabcdefabcdef", s2="bcbecadfbeaafefcdd") == 11
    print('OK')

    print('Test 7... ', end='')
    assert sol.kSimilarity(s1="baabaaabaabbbbbbbaba", s2="abbabbbabbabaaababab") == 9
    print('OK')


if __name__ == '__main__':
    test()
