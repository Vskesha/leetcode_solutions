import test
from itertools import product


def letter_combinations(digits: str) -> list[str]:
    number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return [''.join(x) for x in product(*(number_map[c] for c in digits))] if digits else []


if __name__ == '__main__':
    test.assert_equals(letter_combinations('23'), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    test.assert_equals(letter_combinations(''), [])
    test.assert_equals(letter_combinations('2'), ["a", "b", "c"])
