def shortest_palindrome(s: str) -> str:
    r = s[::-1]
    for i in range(len(s)):
        if s.startswith(r[i:]):
            return r[:i] + s
    return ''


if __name__ == '__main__':
    print(shortest_palindrome("aacecaaa"))
    print(shortest_palindrome('abcd'))
