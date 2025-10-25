import string
import unittest
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        words.add(beginWord)

        prefix = defaultdict(set)
        suffix = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                prefix[w[:i]].add(w)
                suffix[w[i + 1 :]].add(w)

        que = deque([beginWord])
        words.remove(beginWord)
        dist = 1
        while que:
            dist += 1
            for _ in range(len(que)):
                cw = que.popleft()
                for i in range(len(cw)):
                    for nw in prefix[cw[:i]] & suffix[cw[i + 1 :]]:
                        if nw in words:
                            if nw == endWord:
                                return dist
                            que.append(nw)
                            words.remove(nw)
        return 0


class Solution0:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        prefix = defaultdict(set)
        suffix = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                prefix[w[:i]].add(w)
                suffix[w[i + 1 :]].add(w)

        que = deque([beginWord])
        visited = {beginWord}
        dist = 1
        while que:
            dist += 1
            for _ in range(len(que)):
                cw = que.popleft()
                for i in range(len(cw)):
                    for nw in prefix[cw[:i]] & suffix[cw[i + 1 :]]:
                        if nw not in visited:
                            if nw == endWord:
                                return dist
                            que.append(nw)
                            visited.add(nw)
        return 0


class Solution1:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
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
                    post = w[i + 1 :]
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


class Solution2:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        def differs_one_letter(w1: str, w2: str) -> bool:
            # return len(w1) == len(w2) and sum(a != b for a, b in zip(w1, w2)) == 1
            if len(w1) != len(w2):
                return False
            diff = False
            for a, b in zip(w1, w2):
                if a != b:
                    if diff:
                        return False
                    diff = True
            return diff

        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        lw = len(wordList)
        for i in range(1, lw):
            for j in range(i):
                w1, w2 = wordList[i], wordList[j]
                if differs_one_letter(w1, w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)

        queue = deque(w for w in wordList if differs_one_letter(w, beginWord))
        visited = set(queue)
        dist = 2

        while queue:
            for _ in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return dist
                for neib in graph[w]:
                    if neib not in visited:
                        queue.append(neib)
                        visited.add(neib)
            dist += 1

        return 0


class Solution3:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        def differs_one_letter(w1: str, w2: str) -> bool:
            diff = False
            for a, b in zip(w1, w2):
                if a != b:
                    if diff:
                        return False
                    diff = True
            return diff

        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        lw = len(wordList)
        for i in range(1, lw):
            for j in range(i):
                if differs_one_letter(wordList[i], wordList[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        queue = deque(
            i
            for i, w in enumerate(wordList)
            if differs_one_letter(w, beginWord)
        )
        visited = set(queue)
        dist = 2

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if wordList[i] == endWord:
                    return dist
                for neib in graph[i]:
                    if neib not in visited:
                        queue.append(neib)
                        visited.add(neib)
            dist += 1

        return 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_ladderLength_1(self):
        print("Test ladderLength 1... ", end="")
        self.assertEqual(
            5,
            self.sol.ladderLength(
                beginWord="hit",
                endWord="cog",
                wordList=["hot", "dot", "dog", "lot", "log", "cog"],
            ),
        )
        print("OK")

    def test_ladderLength_2(self):
        print("Test ladderLength 2... ", end="")
        self.assertEqual(
            0,
            self.sol.ladderLength(
                beginWord="hit",
                endWord="cog",
                wordList=["hot", "dot", "dog", "lot", "log"],
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
