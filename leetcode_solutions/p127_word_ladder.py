import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        bs = {beginWord}
        es = {endWord}
        dis = 1

        while bs:
            words -= bs
            dis += 1
            ns = set()
            for w in bs:
                for i in range(len(w)):
                    pre = w[:i]
                    post = w[i + 1:]
                    for c in string.ascii_lowercase:
                        nw = pre + c + post
                        if nw in words:
                            if nw in es:
                                return dis
                            ns.add(nw)
            bs = ns
            if len(bs) > len(es):
                bs, es = es, bs
        return 0


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    print('ok')

    print('Test 1 ... ', end='')
    assert sol.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]) == 0
    print('ok')


if __name__ == '__main__':
    test()
