import re


def is_match(s: str, p: str) -> bool:
    return bool(re.fullmatch(p, s))


if __name__ == '__main__':
    print(is_match('aa', 'a'))
    print(is_match('aa', 'a*'))
    print(is_match('ab', '.*'))
