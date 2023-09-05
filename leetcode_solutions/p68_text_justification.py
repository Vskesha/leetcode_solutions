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
                    ans.append(words[start] + ' ' * left)
                else:
                    spaces = ' ' * (left // gaps + 1)
                    line = spaces.join(words[start:end])
                    line = line.replace(spaces, spaces + ' ', left % gaps)
                    ans.append(line)
                left = maxWidth - len(word)
                start = end
        ans.append(' '.join(words[start:]) + ' ' * left)
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
                line += ' ' + word
                gaps += 1
            else:
                if not gaps:
                    line += ' ' * left
                else:
                    spaces = ' ' * (left // gaps + 1)
                    line = line.replace(' ', spaces)
                    line = line.replace(spaces, spaces + ' ', left % gaps)
                ans.append(line)
                line = word
                left = maxWidth - len(word)
                gaps = 0
        line += ' ' * left
        ans.append(line)
        return ans


class Solution2:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        words.append(' ' * 100)
        res = []
        loc = 0
        while loc < len(words) - 1:
            s = words[loc]
            loc += 1
            while len(s + words[loc]) + 1 <= maxWidth:
                s += (' ' + words[loc])
                loc += 1
            res.append(s)

        for i in range(len(res) - 1):
            space = maxWidth - len(res[i])
            total = len(res[i].split(' ')) - 1
            if total != 0:
                amount = (space // total + 1)
                res[i] = res[i].replace(' ', ' ' * (amount))
                res[i] = res[i].replace(' ' * (amount), ' ' * (amount + 1), space % total)
            else:
                res[i] += (' ' * space)
        res[-1] += (' ' * (maxWidth - len(res[-1])))
        return res


def main():
    sol = Solution()
    print(' ["This    is    an", '
          '"example  of text", '
          '"justification.  "]\n',
          sol.fullJustify(words=["This", "is", "an", "example", "of",
                                 "text", "justification."],
                          maxWidth=16))
    print(' ["What   must   be", '
          '"acknowledgment  ", '
          '"shall be        "]\n',
          sol.fullJustify(words=["What", "must", "be",
                                  "acknowledgment", "shall", "be"],
                          maxWidth=16))
    print(' ["Science  is  what we", '
          '"understand      well", '
          '"enough to explain to", '
          '"a  computer.  Art is", '
          '"everything  else  we", '
          '"do                  "]\n',
          sol.fullJustify(words=["Science", "is", "what", "we",
                                 "understand", "well", "enough", "to",
                                 "explain", "to", "a", "computer.", "Art",
                                 "is", "everything", "else", "we", "do"],
                          maxWidth=20))


if __name__ == '__main__':
    main()
