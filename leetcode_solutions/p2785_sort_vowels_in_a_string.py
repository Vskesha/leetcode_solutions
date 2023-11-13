from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        ids = []
        chars = []

        for i, ch in enumerate(s):
            if ch in vowels:
                ids.append(i)
                chars.append(ch)

        res = list(s)
        chars.sort()

        for i, ch in zip(ids, chars):
            res[i] = ch

        return ''.join(res)


class Solution1:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        ids = [i for i in range(len(s)) if s[i] in vowels]
        sids = sorted(ids, key=lambda x: s[x])
        res = list(s)
        for fr, to in zip(sids, ids):
            res[to] = s[fr]
        return ''.join(res)


class Solution2:
    def sortVowels(self, s: str) -> str:
        vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        ids = []
        for i, ch in enumerate(s):
            if ch in vowels:
                ids.append(i)
                vowels[ch] += 1

        def get_vows(vowels):
            for ch in sorted(vowels.keys()):
                for _ in range(vowels[ch]):
                    yield ch

        vow_iter = get_vows(vowels)
        res = list(s)
        for i in ids:
            res[i] = next(vow_iter)
        return ''.join(res)


class Solution3:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        vows = Counter()
        ids = []
        for i, ch in enumerate(s):
            if ch in vowels:
                ids.append(i)
                vows[ch] += 1

        i = 0
        res = list(s)

        for ch in sorted(vows.keys()):
            for _ in range(vows[ch]):
                res[ids[i]] = ch
                i += 1

        return ''.join(res)


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.sortVowels(s="lEetcOde") == "lEOtcede"
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.sortVowels(s="lYmpH") == "lYmpH"
    print('OK')


if __name__ == '__main__':
    test()
