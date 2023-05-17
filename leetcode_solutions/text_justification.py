def full_justify(words, maxWidth):
    ans = []
    line = []
    len_line = maxWidth
    for word in words:
        if len_line + len(word) < maxWidth:
            line.append(' ')
            line.append(word)
            len_line += len(word) + 1
        else:
            if not line:
                pass
            elif len_line == maxWidth:
                ans.append(''.join(line))
            elif len(line) == 1:
                ans.append(line[0] + ' ' * (maxWidth - len_line))
            else:
                gaps = len(line) // 2
                spaces_remains = maxWidth - len_line + gaps
                for i in range(1, len(line), 2):
                    n_spaces = (spaces_remains - 1) // gaps + 1
                    spaces_remains -= n_spaces
                    gaps -= 1
                    line[i] = ' ' * n_spaces
                ans.append(''.join(line))
            line = [word]
            len_line = len(word)
    ans.append(''.join(line) + ' ' * (maxWidth - len_line))
    return ans


if __name__ == '__main__':
    for line in full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16):
        print(f"'{line}'")
    for line in full_justify(["What","must","be","acknowledgment","shall","be"], 16):
        print(f"'{line}'")