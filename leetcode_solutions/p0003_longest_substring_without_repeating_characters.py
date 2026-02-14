import unittest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        st = 0
        ans = 0

        for i, ch in enumerate(s):
            while ch in chars:
                chars.remove(s[st])
                st += 1
            ans = max(ans, i - st + 1)
            chars.add(ch)

        return ans


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = defaultdict(int)
        begin = end = maxlen = 0
        while end < len(s):
            char = s[end]
            chars[char] += 1
            while chars[char] > 1:
                chars[s[begin]] -= 1
                begin += 1
            end += 1
            lenght = end - begin
            if maxlen < lenght:
                maxlen = lenght
        return maxlen


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # make map for the letters
        alphabet = {}
        # make ans var
        ans = 0
        # make start ptr will be where non repeating substring starts
        start = 0

        # enumerate input
        for index, letter in enumerate(s):
            # if curr char in map
            if letter in alphabet:
                # get val of char in map (that char index) + 1
                # and store in sums var so sums is next index
                sums = alphabet[letter] + 1

                # if sums var > start
                if sums > start:
                    # update start, because start will be be where ans begins
                    start = sums

            # make num var set to index - start + 1
            # getting len here
            num = index - start + 1

            # if num(aka the len) > ans
            if num > ans:
                # update ans
                ans = num

            # put letter in map with index as val
            alphabet[letter] = index

        # return ans
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_length_of_longest_substring_1(self):
        print("Test lengthOfLongestSubstring 1... ", end="")
        self.assertEqual(self.sol.lengthOfLongestSubstring(s="abcabcbb"), 3)
        print("OK")

    def test_length_of_longest_substring_2(self):
        print("Test lengthOfLongestSubstring 2... ", end="")
        self.assertEqual(self.sol.lengthOfLongestSubstring(s="bbbbb"), 1)
        print("OK")

    def test_length_of_longest_substring_3(self):
        print("Test lengthOfLongestSubstring 3... ", end="")
        self.assertEqual(self.sol.lengthOfLongestSubstring(s="pwwkew"), 3)
        print("OK")


if __name__ == "__main__":
    unittest.main()
