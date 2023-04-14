from collections import Counter
import test


def find_substring(s: str, words: list[str]) -> list[int]:
    l = len(words[0])
    c = len(words)
    result = []
    for i in range(len(s) - c * l + 1):
        wds = Counter(words)
        for j in range(c):
            start = i + j * l
            word = s[start:start + l]
            if word in wds and wds[word] > 0:
                wds[word] -= 1
            else:
                break
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    test.assert_equals(find_substring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]), [])
    test.assert_equals(find_substring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]), [6, 9, 12])
    test.assert_equals(find_substring(s="barfoothefoobarman", words=["foo", "bar"]), [0, 9])
