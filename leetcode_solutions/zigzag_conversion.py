import test


def zigzag_conversion(s: str, n: int) -> str:
    if n < 2:
        return s
    rows = [[] for _ in range(n)]
    i, direction = 0, 1
    for char in s:
        rows[i].append(char)
        i += direction
        if i == 0 or i == n - 1:
            direction *= -1
    return ''.join(''.join(row) for row in rows)


if __name__ == '__main__':
    test.assert_equals(zigzag_conversion("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
    test.assert_equals(zigzag_conversion("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
    test.assert_equals(zigzag_conversion('A', 1), 'A')
    test.assert_equals(zigzag_conversion('AB', 1), 'AB')

