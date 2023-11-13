from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(ch * q for ch, q in Counter(s).most_common())


class Solution2:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        return ''.join(sorted(s, key=lambda x: (cnt[x], x), reverse=True))


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.frequencySort("tree") in ("eert", 'eetr')
    print('OK')

    print('Test 2... ', end='')
    assert sol.frequencySort("cccaaa") in ("aaaccc", "cccaaa")
    print('OK')


if __name__ == '__main__':
    test()
