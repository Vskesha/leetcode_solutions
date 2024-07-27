import unittest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {c: i for i, c in enumerate(s)}

        result = []
        st = 0
        end = last_occurence[s[0]]
        for i, c in enumerate(s):
            if i > end:
                result.append(i - st)
                st = i
            end = max(end, last_occurence[c])
        result.append(len(s) - st)

        return result


class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {ch: i for i, ch in enumerate(s)}
        lo, prev = 0, -1
        ans = []
        for i, ch in enumerate(s):
            lo = max(lo, last_occ[ch])
            if i == lo:
                ans.append(i - prev)
                prev = i
        return ans


class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, 0
        i = 0
        ans = []
        while i < len(s):
            end = max(end, s.rindex(s[i]))
            if i == end:
                end += 1
                ans.append(end - start)
                start = end
            i += 1
        return ans


class Solution3:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}
        for i, ch in enumerate(s):
            last_occ[ch] = i

        lo = 0
        prev = 0
        ans = []
        for i, ch in enumerate(s):
            if i > lo:
                ans.append(i - prev)
                prev = i
            lo = max(lo, last_occ[ch])
        ans.append(len(s) - prev)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_partitionLabels_1(self):
        print("Test partitionLabels 1... ", end="")
        self.assertListEqual(
            [9, 7, 8], self.sol.partitionLabels(s="ababcbacadefegdehijhklij")
        )
        print("OK")

    def test_partitionLabels_2(self):
        print("Test partitionLabels 2... ", end="")
        self.assertListEqual([10], self.sol.partitionLabels(s="eccbbbbdec"))
        print("OK")


if __name__ == "__main__":
    unittest.main()
