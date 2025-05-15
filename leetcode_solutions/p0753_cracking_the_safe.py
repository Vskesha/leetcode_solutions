import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        ans = []

        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n - 1))
        ans = "".join(ans) + "0" * (n - 1)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["crackSafe"] * 6,
            "kwargs": [
                dict(n=1, k=2),
                dict(n=2, k=2),
                dict(n=3, k=3),
                dict(n=5, k=2),
                dict(n=3, k=5),
                dict(n=2, k=7),
            ],
            "expected": [
                "10",
                "01100",
                "00222121112201202101102001000",
                "000011111011010111001010011000100000",
                "0044434333442342432332422322244134124143133123142132122141131121114403402401404303302301304203202201204103102101104003002001000",
                "06655645446353433625242322615141312116050403020100",
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
