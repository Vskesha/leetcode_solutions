import unittest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_count = sum(1 for c in s[:k] if c in vowels)
        tmp = max_count
        for a, b in zip(s, s[k:]):
            if a in vowels:
                tmp -= 1
            if b in vowels:
                tmp += 1
            if tmp == k:
                return k
            if max_count < tmp:
                max_count = tmp
        return max_count


class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        is_vowels = [c in vowels for c in s]
        max_count = count = sum(map(int, is_vowels[:k]))
        for i in range(len(s) - k):
            if not is_vowels[i] and is_vowels[i + k]:
                count += 1
                if max_count < count:
                    if count == k:
                        return k
                    max_count = count
            elif is_vowels[i] and not is_vowels[i + k]:
                count -= 1
        return max_count


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_vowels_1(self):
        print("Test maxVowels 1... ", end="")
        self.assertEqual(self.sol.maxVowels(s="abciiidef", k=3), 3)
        print("OK")

    def test_max_vowels_2(self):
        print("Test maxVowels 2... ", end="")
        self.assertEqual(self.sol.maxVowels(s="aeiou", k=2), 2)
        print("OK")

    def test_max_vowels_3(self):
        print("Test maxVowels 3... ", end="")
        self.assertEqual(self.sol.maxVowels(s="leetcode", k=3), 2)
        print("OK")


if __name__ == "__main__":
    unittest.main()
