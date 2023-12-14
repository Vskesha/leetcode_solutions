from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wl = set(wordlist)
        lows, vows = {}, {}
        for i, word in enumerate(wordlist):
            w = word.lower()
            if w not in lows:
                lows[w] = word
            w = (w.replace('e', 'a')
                 .replace('i', 'a')
                 .replace('o', 'a')
                 .replace('u', 'a'))
            if w not in vows:
                vows[w] = word

        ans = []
        for word in queries:
            if word in wl:
                ans.append(word)
                continue
            w = word.lower()
            if w in lows:
                ans.append(lows[w])
                continue
            w = (w.replace('e', 'a')
                 .replace('i', 'a')
                 .replace('o', 'a')
                 .replace('u', 'a'))
            if w in vows:
                ans.append(vows[w])
                continue
            ans.append('')

        return ans


class Solution2:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vs = 'aeiou'
        wl = set(wordlist)
        low = [word.lower() for word in wordlist]
        lset = set(low)
        vow = [''.join('*' if c in vs else c for c in w) for w in low]
        vset = set(vow)
        ans = []
        for word in queries:
            if word in wl:
                ans.append(word)
                continue
            w = word.lower()
            if w in lset:
                i = low.index(w)
                ans.append(wordlist[i])
                continue
            w = ''.join('*' if c in vs else c for c in w)
            if w in vset:
                i = vow.index(w)
                ans.append(wordlist[i])
                continue
            ans.append('')

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.spellchecker(
        wordlist=["KiTe", "kite", "hare", "Hare"],
        queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    ) == ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
    print('OK')

    print('Test 2... ', end='')
    assert sol.spellchecker(
        wordlist=["yellow"],
        queries=["YellOw"]
    ) == ["yellow"]
    print('OK')


if __name__ == '__main__':
    test()
