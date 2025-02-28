import unittest
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        rem = Counter(s1)
        st = 0

        for i, ch in enumerate(s2):
            rem[ch] -= 1
            if rem[ch] == 0:
                del rem[ch]
                if not rem:
                    return True
            elif rem[ch] == -1:
                while rem[ch] == -1:
                    rem[s2[st]] += 1
                    st += 1
                del rem[ch]

        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ws = len(s1) - 1
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:ws])

        for c1, c2 in zip(s2, s2[ws:]):
            cnt2[c2] += 1
            if cnt1 == cnt2:
                return True
            cnt2[c1] -= 1

        return False


class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1, ls2 = len(s1), len(s2)
        if ls1 > ls2:
            return False
        diff = Counter(s1)
        for ch in s2[: ls1 - 1]:
            diff[ch] -= 1
            if not diff[ch]:
                del diff[ch]

        for sch, ech in zip(s2, s2[ls1 - 1 :]):
            diff[ech] -= 1
            if not diff[ech]:
                del diff[ech]
            if not diff:
                return True
            diff[sch] += 1
            if not diff[sch]:
                del diff[sch]

        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_check_inclusion_1(self):
        print("Test checkInclusion 1... ", end="")
        self.assertTrue(self.sol.checkInclusion(s1="ab", s2="eidbaooo"))
        print("OK")

    def test_check_inclusion_2(self):
        print("Test checkInclusion 2... ", end="")
        self.assertFalse(self.sol.checkInclusion(s1="ab", s2="eidboaoo"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
