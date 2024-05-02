class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch) + 1
        if not i:
            return word
        return word[:i][::-1] + word[i:]


def test_reverse_prefix():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.reversePrefix(word="abcdefd", ch="d") == "dcbaefd"
    print("OK")

    print("Test 2... ", end="")
    assert sol.reversePrefix(word="xyxzxe", ch="z") == "zxyxxe"
    print("OK")

    print("Test 3... ", end="")
    assert sol.reversePrefix(word="abcd", ch="z") == "abcd"
    print("OK")


if __name__ == "__main__":
    test_reverse_prefix()
