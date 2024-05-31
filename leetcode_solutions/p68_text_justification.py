from typing import List


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        start = 0
        left = maxWidth + 1

        for end, word in enumerate(words):
            if left > len(word):
                left -= len(word) + 1
            else:
                gaps = end - start - 1
                if not gaps:
                    ans.append(words[start] + " " * left)
                else:
                    spaces = " " * (left // gaps + 1)
                    line = spaces.join(words[start:end])
                    line = line.replace(spaces, spaces + " ", left % gaps)
                    ans.append(line)
                left = maxWidth - len(word)
                start = end
        ans.append(" ".join(words[start:]) + " " * left)
        return ans


class Solution1:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        words = iter(words)
        line = next(words)
        left = maxWidth - len(line)
        gaps = 0

        for word in words:
            if left > len(word):
                left -= len(word) + 1
                line += " " + word
                gaps += 1
            else:
                if not gaps:
                    line += " " * left
                else:
                    spaces = " " * (left // gaps + 1)
                    line = line.replace(" ", spaces)
                    line = line.replace(spaces, spaces + " ", left % gaps)
                ans.append(line)
                line = word
                left = maxWidth - len(word)
                gaps = 0
        line += " " * left
        ans.append(line)
        return ans


class Solution2:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        words.append(" " * 100)
        res = []
        loc = 0
        while loc < len(words) - 1:
            s = words[loc]
            loc += 1
            while len(s + words[loc]) + 1 <= maxWidth:
                s += " " + words[loc]
                loc += 1
            res.append(s)

        for i in range(len(res) - 1):
            space = maxWidth - len(res[i])
            total = len(res[i].split(" ")) - 1
            if total != 0:
                amount = space // total + 1
                res[i] = res[i].replace(" ", " " * (amount))
                res[i] = res[i].replace(
                    " " * (amount), " " * (amount + 1), space % total
                )
            else:
                res[i] += " " * space
        res[-1] += " " * (maxWidth - len(res[-1]))
        return res


class Solution3:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        row = []
        chars = 0
        ans = []

        for word in words:
            if chars + len(row) + len(word) <= maxWidth:
                row.append(word)
                chars += len(word)
            else:
                if len(row) == 1:
                    ans.append(row[0].ljust(maxWidth, " "))
                else:
                    d, m = divmod(maxWidth - chars, len(row) - 1)
                    s = (" " * d).join(row)
                    s = s.replace(" " * d, " " * (d + 1), m)
                    ans.append(s)
                row = [word]
                chars = len(word)

        ans.append(" ".join(row).ljust(maxWidth, " "))

        return ans


def test_full_justify():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    ) == ["This    is    an", "example  of text", "justification.  "]
    print("OK")

    print("Test 2... ", end="")
    assert sol.fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    ) == ["What   must   be", "acknowledgment  ", "shall be        "]
    print("OK")

    print("Test 3... ", end="")
    assert sol.fullJustify(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
    print("OK")


if __name__ == "__main__":
    test_full_justify()
