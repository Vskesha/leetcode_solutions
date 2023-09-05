def longest_palindrome_subsequence(s: str) -> int:
    l = len(s)+1
    pr = [0] * l
    for i in range(1, l):
        cu = [0]
        for j in range(1, l):
            cu.append(pr[j-1] + 1 if s[i-1] == s[-j] else max(cu[-1], pr[j]))
        pr = cu
    return pr[-1]


def longest_palindrome(s: str) -> str:
    l = len(s) + 1
    p = ['' for _ in range(l)]
    for i in range(1, l):
        c = ['']
        for j in range(1, l):
            c.append(p[j-1]+s[i-1] if s[i-1] == s[-j] else max(c[-1], p[j], key=len))
        p = c
    return c[-1]


if __name__ == '__main__':
    print(longest_palindrome_subsequence('bbbab'))
    print(longest_palindrome_subsequence('cbbd'))
    print(longest_palindrome_subsequence('cbabd'))
    print(longest_palindrome('bbbab'))
    print(longest_palindrome('cbbd'))
    print(longest_palindrome('cbabd'))
