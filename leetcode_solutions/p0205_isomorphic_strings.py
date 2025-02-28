import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        seen = set()

        for a, b in zip(s, t):
            if a in mp:
                if mp[a] != b:
                    return False
            elif b in seen:
                return False
            else:
                mp[a] = b
                seen.add(b)

        return True


class Solution0:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = set()
        mp = {}

        for a, b in zip(s, t):
            if a not in mp:
                if b in seen:
                    return False
                mp[a] = b
                seen.add(b)
            if mp[a] != b:
                return False

        return True


class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        seen = set()

        for a, b in zip(s, t):
            if a in mp:
                if b != mp[a]:
                    return False
            elif b in seen:
                return False
            else:
                mp[a] = b
                seen.add(b)

        return True


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a not in mp:
                if b not in mp.values():
                    mp[a] = b
                else:
                    return False
            elif mp[a] != b:
                return False
        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_isomorphic_1(self):
        print("Test isIsomorphic 1... ", end="")
        self.assertTrue(self.sol.isIsomorphic(s="egg", t="add"))
        print("OK")

    def test_is_isomorphic_2(self):
        print("Test isIsomorphic 2... ", end="")
        self.assertFalse(self.sol.isIsomorphic(s="foo", t="bar"))
        print("OK")

    def test_is_isomorphic_3(self):
        print("Test isIsomorphic 3... ", end="")
        self.assertTrue(self.sol.isIsomorphic(s="paper", t="title"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
