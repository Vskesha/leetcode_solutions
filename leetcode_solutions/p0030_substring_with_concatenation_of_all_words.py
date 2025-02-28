from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lw = len(words[0])
        lws = len(words)
        cnt = Counter(words)
        ans = []

        for i in range(lw):
            splitted = [s[j:j+lw] for j in range(i, len(s), lw)]
            new = Counter(splitted[:lws-1])
            st = 0
            for j in range(lws-1, len(splitted)):
                new[splitted[j]] += 1
                if new == cnt:
                    ans.append(st * lw + i)
                first = splitted[st]
                if new[first] == 1:
                    del new[first]
                else:
                    new[first] -= 1
                st += 1
        return ans


class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lw = len(words[0])
        tl = lw * (len(words) - 1)
        cnt = Counter(words)
        ans = []

        for i in range(lw):
            new = Counter(s[j:j + lw] for j in range(i, i + tl, lw))
            st = i
            for j in range(i + tl, len(s), lw):
                new[s[j:j + lw]] += 1
                if new == cnt:
                    ans.append(st)
                first = s[st:st + lw]
                if new[first] == 1:
                    del new[first]
                else:
                    new[first] -= 1
                st += lw

        return ans


class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lw = len(words[0])
        lws = len(words)
        tl = lw * lws
        cnt = Counter(words)
        ans = []
        for i in range(len(s) - tl + 1):
            new = Counter(s[j:j + lw] for j in range(i, i + tl, lw))
            if new == cnt:
                ans.append(i)
        return ans


class Solution3:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        c = len(words)
        w = Counter(words)
        result = []
        for i in range(len(s) - c * l + 1):
            wds = w.copy()
            for j in range(c):
                start = i + j * l
                word = s[start:start + l]
                if word in wds and wds[word] > 0:
                    wds[word] -= 1
                else:
                    break
            else:
                result.append(i)
        return result


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]) == [0, 9]
    print('OK')

    print('Test 2... ', end='')
    assert sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]) == []
    print('OK')

    print('Test 3... ', end='')
    assert sol.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]) == [6, 9, 12]
    print('OK')


if __name__ == '__main__':
    test()
