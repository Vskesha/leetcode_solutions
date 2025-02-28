from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        m = {chr(97 + i): m[i] for i in range(26)}
        return len({''.join(m[ch] for ch in word) for word in words})


class Solution2:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(m[ord(ch) - 97] for ch in word) for word in words})


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]) == 2
    print('OK')

    print('Test 2... ', end='')
    assert sol.uniqueMorseRepresentations(words=["a"]) == 1
    print('OK')


if __name__ == '__main__':
    test()
