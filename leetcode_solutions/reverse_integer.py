import test


def reverse_integer(x: int) -> int:
    s = str(x)
    if s[0].isnumeric():
        x = int(s[::-1])
    else:
        x = int(s[0] + s[1:][::-1])
    if abs(x) > 2 ** 31 - 1:
        return 0
    return x


if __name__ == '__main__':
    test.assert_equals(reverse_integer(123), 321)
    test.assert_equals(reverse_integer(-123), -321)
    test.assert_equals(reverse_integer(120), 21)
