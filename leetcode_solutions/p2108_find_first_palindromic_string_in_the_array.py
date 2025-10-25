from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


class Solution2:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"])
        == "ada"
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.firstPalindrome(words=["notapalindrome", "racecar"]) == "racecar"
    )
    print("OK")

    print("Test 3... ", end="")
    assert sol.firstPalindrome(words=["def", "ghi"]) == ""
    print("OK")


if __name__ == "__main__":
    test()
