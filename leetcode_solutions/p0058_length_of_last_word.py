class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        s = s.strip()
        for ch in reversed(s):
            if ch == " ":
                return ans
            ans += 1
        return len(s)


def test_length_of_last_word():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.lengthOfLastWord(s="Hello World") == 5
    print("OK")

    print("Test 2... ", end="")
    assert sol.lengthOfLastWord(s="   fly me   to   the moon  ") == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.lengthOfLastWord(s="luffy is still joyboy") == 6
    print("OK")


if __name__ == "__main__":
    test_length_of_last_word()
