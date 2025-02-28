import unittest
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.root = list(range(n))
        self.groups = n

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.groups -= 1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(s1: str, s2: str) -> bool:
            diffs = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diffs += 1
                    if diffs > 2:
                        return False
            return True

        ls = len(strs)
        ds = DisjointSet(ls)

        for i in range(1, ls):
            for j in range(i):
                if are_similar(strs[i], strs[j]):
                    ds.union(i, j)

        return ds.groups


class Solution2:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(s1: str, s2: str) -> bool:
            diffs = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diffs += 1
                    if diffs > 2:
                        return False
            return True

        def dfs(el):
            visited[el] = False
            for node in similar[el]:
                if visited[node]:
                    dfs(node)

        ls = len(strs)
        similar = [[] for _ in range(ls)]
        for i in range(ls):
            for j in range(i + 1, ls):
                if are_similar(strs[i], strs[j]):
                    similar[i].append(j)
                    similar[j].append(i)

        groups = 0
        visited = [True] * ls
        for i in range(ls):
            if visited[i]:
                dfs(i)
                groups += 1

        return groups


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_num_similar_groups_1(self):
        print("Test numSimilarGroups 1... ", end="")
        self.assertEqual(
            self.sol.numSimilarGroups(strs=["tars", "rats", "arts", "star"]), 2
        )
        print("OK")

    def test_num_similar_groups_2(self):
        print("Test numSimilarGroups 2... ", end="")
        self.assertEqual(self.sol.numSimilarGroups(strs=["omv", "ovm"]), 1)
        print("OK")

    def test_num_similar_groups_3(self):
        print("Test numSimilarGroups 3... ", end="")
        self.assertEqual(
            self.sol.numSimilarGroups(
                strs=[
                    "kccomwcgcs",
                    "socgcmcwkc",
                    "sgckwcmcoc",
                    "coswcmcgkc",
                    "cowkccmsgc",
                    "cosgmccwkc",
                    "sgmkwcccoc",
                    "coswmccgkc",
                    "kowcccmsgc",
                    "kgcomwcccs",
                ]
            ),
            5,
        )
        print("OK")

    def test_num_similar_groups_4(self):
        print("Test numSimilarGroups 4... ", end="")
        self.assertEqual(
            self.sol.numSimilarGroups(
                strs=[
                    "qihcochwmglyiggvsqqfgjjxu",
                    "gcgqxiysqfqugmjgwclhjhovi",
                    "gjhoggxvcqlcsyifmqgqujwhi",
                    "wqoijxciuqlyghcvjhgsqfmgg",
                    "qshcoghwmglygqgviiqfjcjxu",
                    "jgcxqfqhuyimjglgihvcqsgow",
                    "qshcoghwmggylqgviiqfjcjxu",
                    "wcoijxqiuqlyghcvjhgsqgmgf",
                    "qshcoghwmglyiqgvigqfjcjxu",
                    "qgsjggjuiyihlqcxfovchqmwg",
                    "wcoijxjiuqlyghcvqhgsqgmgf",
                    "sijgumvhqwqioclcggxgyhfjq",
                    "lhogcgfqqihjuqsyicxgwmvgj",
                    "ijhoggxvcqlcsygfmqgqujwhi",
                    "qshcojhwmglyiqgvigqfgcjxu",
                    "wcoijxqiuqlyghcvjhgsqfmgg",
                    "qshcojhwmglyiggviqqfgcjxu",
                    "lhogcgqqfihjuqsyicxgwmvgj",
                    "xscjjyfiuglqigmgqwqghcvho",
                    "lhggcgfqqihjuqsyicxgwmvoj",
                    "lhgocgfqqihjuqsyicxgwmvgj",
                    "qihcojhwmglyiggvsqqfgcjxu",
                    "ojjycmqshgglwicfqguxvihgq",
                    "sijvumghqwqioclcggxgyhfjq",
                    "gglhhifwvqgqcoyumcgjjisqx",
                ]
            ),
            11,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
