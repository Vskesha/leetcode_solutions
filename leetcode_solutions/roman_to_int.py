def romanToInt(s: str) -> int:
    rimap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 2000
    for c in s:
        curr = rimap[c]
        if prev < curr:
            result -= prev * 2
        result += curr
        prev = curr
    return result


if __name__ == '__main__':
    print(romanToInt('MXCIV'))
